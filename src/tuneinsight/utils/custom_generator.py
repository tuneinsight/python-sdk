"""
Soon-to-be-deprecated module to generate mock patients data.

This module will be removed in favour of the utils.datagen module for mock
data generation on a Tune Insight instance.

"""

from typing import List, Any
from random import Random
from datetime import timedelta
import uuid
import math

import pandas as pd
import numpy as np

from tuneinsight.utils import deprecation

deprecation.warn("custom_generator", "utils.datagen classes")


def inv_sigmoid(x, c1, c2):
    return 1.0 / (1.0 + math.exp(c1 * (-x - c2)))


def get_sigmoids(c1, c2, num):
    res = []
    for i in range(num):
        x = (float(i) / float(num)) * 2 - 1
        res.append(inv_sigmoid(x, c1, c2))
    return res


def flatten(l):
    return [item for sublist in l for item in sublist]


def cluster_weights(cluster_size: int):
    half = float(cluster_size) / 2.0 - 0.5

    def get_weight(i):
        dist = abs(half - i)
        if dist < 1:
            return 1
        return 1.0 / (dist * 1.1)

    return [get_weight(i) for i in range(cluster_size)]


def generate_survival_curve(
    num_months: int, death_rate: float, shift: float
) -> List[float]:
    c1 = -10 * death_rate
    c2 = shift
    return get_sigmoids(c1, c2, num_months)


class CustomGenerator(Random):
    df: pd.DataFrame
    snp_weights: List[float]
    snp_choices: List[float]
    locuses: List[str]
    rows: int

    def __init__(self, rows: int = 10):
        Random.__init__(self)
        self.df = pd.DataFrame(index=range(rows))
        self.rows = rows
        self.np_rng = np.random.default_rng()
        self.snp_weights = [15, 5, 1]
        self.snp_choices = [0, 0.5, 1]

    def seed(self, a=None, version=2):
        self.np_rng = np.random.default_rng(a)
        super().seed(a, version)

    def generate_dummies(self, name: str):
        dummies = pd.get_dummies(self.df[name], prefix=name, prefix_sep="_")
        self.df = pd.concat([self.df, dummies], axis=1)

    def generate_genome(
        self, num_snps: int, locus_path: str, locus_column: str, keep: List[str] = None
    ):
        locuses = self._get_sample_locuses(num_snps, locus_path, locus_column, keep)
        for i, locus in enumerate(locuses):
            self.df[locus] = self.choices(
                self.snp_choices, weights=self.snp_weights, k=self.rows
            )
            if i % 25 == 0:
                self.df = self.df.copy()
        self.locuses = locuses

    def normalize_min_max(self, column):
        self.df[column] = (self.df[column] - self.df[column].min()) / (
            self.df[column].max() - self.df[column].min()
        )

    def clip(self, column, lower, upper):
        self.df[column] = self.df[column].clip(lower=lower, upper=upper)

    def add_random_event(self, event: str, start, end):
        delta = end - start

        def random_date():
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = self.randrange(int_delta)
            return start + timedelta(seconds=random_second)

        self.df[event] = self.df.apply(lambda x: random_date(), axis=1)

    def add_covariate(self, name: str, choices: List[float], weights: List[float]):
        self.df[name] = self.choices(choices, weights=weights, k=self.rows)
        self.normalize_min_max(name)

    def encode_category(self, name: str, encoded_name: str, choices: List[Any]):
        mapping = {}
        for i, choice in enumerate(choices):
            mapping[choice] = i

        def encode(x):
            return mapping[x[name]]

        self.df[encoded_name] = self.df.apply(encode, axis=1)
        self.normalize_min_max(encoded_name)

    def add_survival_event(
        self,
        event: str,
        start_event: str,
        num_months: int = 12,
        death_rate: float = 0.9,
        shift: float = 0.0,
        condition=None,
    ):
        if not event in self.df:
            self.df[event] = pd.NaT
        survivals = generate_survival_curve(
            num_months=num_months, death_rate=death_rate, shift=shift
        )

        def survival_func(x):
            if condition is not None:
                if not condition(x):
                    return x[event]
            return self.survival_events(x[start_event], survivals)

        self.df[event] = self.df.apply(survival_func, axis=1)

    def add_phenotype(
        self,
        name: str,
        correlated_snp_indexes: List[int],
        weights: List[float],
        covariates: List[str] = None,
        covariates_weights: List[float] = None,
    ):
        def compute_value(x):
            val = 0.0
            for i, index in enumerate(correlated_snp_indexes):
                val += x[self.locuses[index]] * weights[i]
            for i, cov in enumerate(covariates):
                val += x[cov] * covariates_weights[i]
            return val

        self.df[name] = self.df.apply(compute_value, axis=1)
        self.normalize_min_max(name)

    def apply_snp_correlation(
        self, num_regions: int, condition, correlation_factor: float = 0.9
    ):
        snp_indices, probabilities = self.get_random_snp_clusters(
            num_clusters=num_regions,
            num_vals=len(self.locuses),
            scale=correlation_factor,
        )

        def correlate(x, snp, probability):
            if condition(x) and self.random() < probability:
                return 1
            return x[snp]

        for i, snp_index in enumerate(snp_indices):
            snp = self.locuses[snp_index]
            prob = probabilities[i]
            self.df[snp] = self.df.apply(
                lambda x, y=snp, z=prob: correlate(x, y, z), axis=1
            )

    def add_variable(
        self,
        variable_name: str,
        loc: float = 0.0,
        scale: float = 1.0,
        normalize: bool = True,
    ):
        self.df[variable_name] = self.np_rng.normal(loc, scale, size=self.df.shape[0])
        if normalize:
            self.normalize_min_max(variable_name)

    def add_relation(
        self,
        new_variable: str,
        related_variable: str,
        loc: float = 0.0,
        scale: float = 1.0,
    ):
        vals = self.np_rng.normal(loc, scale, size=self.df.shape[0])

        def apply_func(x):
            return x[related_variable] + vals[x.name]

        self.df[new_variable] = self.df.apply(apply_func, axis=1)

    def apply_variable(
        self, variable_name: str, condition, loc: float = 0.0, scale: float = 1.0
    ):
        vals = self.np_rng.normal(loc, scale, size=self.df.shape[0])

        def apply_func(x):
            if condition(x):
                return vals[x.name]
            return x[variable_name]

        self.df[variable_name] = self.df.apply(apply_func, axis=1)

    def apply_correlation(
        self,
        column: str,
        condition,
        applied_value: float = 1,
        correlation_factor: float = 0.9,
    ):
        def correlate(x):
            if condition(x) and self.random() < correlation_factor:
                return applied_value
            return x[column]

        self.df[column] = self.df.apply(correlate, axis=1)

    def get_random_snp_clusters(self, num_clusters: int, num_vals: int, scale: float):
        allIndices = []
        allWeights = []
        cluster_size = int(math.ceil(float(num_vals) / 500))
        for _ in range(num_clusters):
            random_index = self.randint(0, num_vals - 1 - cluster_size)
            indices = list(range(random_index, random_index + cluster_size))
            weights = cluster_weights(cluster_size=cluster_size)
            allIndices.append(indices)
            allWeights.append(weights)
        allIndices = flatten(allIndices)
        allWeights = flatten(allWeights)
        for i, _ in enumerate(allWeights):
            allWeights[i] *= scale
            allWeights[i] -= self.random() * 0.1 * allWeights[i]
        return allIndices, allWeights

    def apply_choice(self, name: str, choices: List[Any], weights: List[float] = None):
        self.df[name] = self.choices(choices, weights=weights, k=self.rows)

    def survival_events(self, start_time, target_survival):
        endEventTime = start_time
        for prob in target_survival:
            endEventTime += np.timedelta64(1, "M")
            if endEventTime > pd.Timestamp.now():
                return pd.NaT
            t = self.random()
            if t > prob:
                return endEventTime
        return pd.NaT

    def gen_ids(self, id_column: str):
        self.df[id_column] = ""
        self.df[id_column] = self.df.apply(lambda x: self._random_id(), axis=1)

    def _random_id(self):
        return str(uuid.UUID(int=self.getrandbits(128)))

    @staticmethod
    def _get_sample_locuses(
        num: int,
        locus_values_csv_path: str,
        locus_csv_column: str,
        keep: List[str] = None,
    ) -> List[str]:
        tmp = pd.read_csv(locus_values_csv_path)
        others = (
            tmp[(~tmp[locus_csv_column].isin(keep))]
            .sample(n=num - len(keep))
            .sort_index()
        )
        kept = tmp[tmp[locus_csv_column].isin(keep)].sort_index()
        res = pd.concat([others, kept]).sort_index()
        return res[locus_csv_column].to_list()
