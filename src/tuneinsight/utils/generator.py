from typing import Any, Callable, List
from random import Random

import pandas as pd

class MixedGenerator(Random):

    cols: List[str]
    generators: List[Callable[[],Any]]


    def __init__(self):
        self.cols = []
        self.generators = []

    def addRangeColumn(self,column: str, r: List[float]):
        self.cols.append(column)
        def generator():
            min_val,max_val = r[0],r[1]
            return self.random() * (max_val - min_val) + min_val
        self.generators.append(generator)

    def addCategoricalColumn(self,column: str,categories: List[str]):
        self.cols.append(column)
        def generator():
            return categories[self.randint(0,len(categories) -1)]
        self.generators.append(generator)

    def generate(self,num_rows: int) -> pd.DataFrame:
        data = []
        for _ in range(num_rows):
            tmp = []
            for g in self.generators:
                tmp.append(g())
            data.append(tmp)
        return pd.DataFrame(data=data,columns=self.cols)




class PatientGenerator(MixedGenerator):

    age_ranges: List[List[int]] = [[3,15],[16,45],[45,70],[70,105]]
    age_weights: List[float] = [1,2,3,2]
    gender_choices: List[str] = ["female","male","agender","bigender"]
    gender_weights: List[float] = [0.45,0.45,0.05,0.05]
    district_choices: List[str] = ["Geneva","Vaud","Bern","Fribourg","Neuchatel"]
    district_weights: List[float] = [1,1,1,1,1]
    weight_factor: float = 1
    height_factor: float = 1
    age_height_ranges = [5,10,20,60,80,200]
    age_height_averages = [70,120,150,180,170,160]
    origin_choices: List[str] = ["Swiss","Europe","North America","South America","Africa","Asia","Oceania"]
    origin_weights: List[float] = [20,10,2,3,7,5,1]


    def __init__(self):
        self.age_ranges = [[3,15],[16,45],[45,70],[70,105]]
        self.age_weights = [1,2,3,2]
        self.gender_choices = ["female","male","agender","bigender"]
        self.gender_weights = [0.48,0.48,0.02,0.02]
        self.district_weights = [0.1,0.3,0.3,0.3]

    def get_age_average(self,age: int) -> float:
        for i,k in enumerate(self.age_height_ranges):
            if age < k:
                return self.age_height_averages[i]
        return self.age_height_averages[len(self.age_height_averages) -1]


    def random_district(self) -> str:
        return self.choices(self.district_choices,weights=self.district_weights,k=1)[0]

    def random_gender(self) -> str:
        return self.choices(self.gender_choices,weights=self.gender_weights,k=1)[0]


    def age_to_height(self,age: int) -> float:
        return (self.random() * 0.2 + 0.8 + self.random() * 0.1) * self.get_age_average(age) * self.height_factor


    def height_to_weight(self,height: float) -> float:
        return (self.random() * 0.4 + 0.8) * height * 0.35


    def random_age(self) -> int:
        chosen_range = self.choices(self.age_ranges,weights=self.age_weights,k=1)[0]
        return self.random_age_from_range(chosen_range)


    def random_origin(self,district: str) -> str:
        weights = self.origin_weights.copy()
        if district == "Fribourg":
            weights[0] += 10
        if district == "Vaud":
            weights[0] += 5
        return self.choices(self.origin_choices,weights=weights,k=1)[0]

    def random_age_from_range(self,range_values: List[int]) -> int:
        min_val,max_val = range_values[0],range_values[1]
        return self.randint(min_val,max_val)

    def random_patient(self) -> List[Any]:
        age = self.random_age()
        gender = self.random_gender()
        district = self.random_district()
        origin = self.random_origin(district)
        addFactor = 1
        # gender based discrimination
        if gender != "male" and gender != "female" and age > 70:
            age = int(age * 0.6)
        if gender == "female":
            addFactor = 0.95
        if gender == "male":
            addFactor = 1.05
        height = self.age_to_height(age) * addFactor
        weight = self.height_to_weight(height)
        return [district,origin,gender,age,height,weight]

    @staticmethod
    def columns() -> List[str]:
        return ["district","origin","gender","age","height","weight"]

    def new_dataframe(self,num_rows: int) ->pd.DataFrame:
        data = self.generate(num_rows=num_rows)
        return pd.DataFrame(data=data,columns=self.columns())

    def generate(self,num_rows: int):
        data = []
        for _ in range(num_rows):
            data.append(self.random_patient())
        return data
