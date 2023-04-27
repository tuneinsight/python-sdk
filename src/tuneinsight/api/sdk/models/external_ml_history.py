from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalMlHistory")


@attr.s(auto_attribs=True)
class ExternalMlHistory:
    """Training history of external ML containing the evolution of the metrics during training

    Attributes:
        test_f1_s (List[List[float]]): Test f1s at each round at each local epoch
        train_accs (List[List[float]]): Train accuracies at each round at each local epoch
        train_f1_s (List[List[float]]): Train f1s at each round at each local epoch
        test_accs (List[List[float]]): Test accuracies at each round at each local epoch
        train_losses (List[List[float]]): Train losses at each round at each local epoch
        test_losses (List[List[float]]): Test losses at each round at each local epoch
        end_timestamps (List[List[float]]): Ending timestamps of local training epochs in unix milliseconds timestamps
        start_timestamps (List[List[float]]): Starting timestamps of local training epochs in unix milliseconds
            timestamps
        init_test_f1_s (Union[Unset, List[float]]): Test f1s at each round before local training
        init_timestamps (Union[Unset, List[float]]): Init timestamps of local training in unix milliseconds timestamps
        init_train_accs (Union[Unset, List[float]]): Train accs at each round before local training
        init_train_losses (Union[Unset, List[float]]): Train losses at each round before local training
        init_test_accs (Union[Unset, List[float]]): Test accs at each round before local training
        init_test_losses (Union[Unset, List[float]]): Test losses at each round before local training
        init_train_f1_s (Union[Unset, List[float]]): Train f1s at each round before local training
    """

    test_f1_s: List[List[float]]
    train_accs: List[List[float]]
    train_f1_s: List[List[float]]
    test_accs: List[List[float]]
    train_losses: List[List[float]]
    test_losses: List[List[float]]
    end_timestamps: List[List[float]]
    start_timestamps: List[List[float]]
    init_test_f1_s: Union[Unset, List[float]] = UNSET
    init_timestamps: Union[Unset, List[float]] = UNSET
    init_train_accs: Union[Unset, List[float]] = UNSET
    init_train_losses: Union[Unset, List[float]] = UNSET
    init_test_accs: Union[Unset, List[float]] = UNSET
    init_test_losses: Union[Unset, List[float]] = UNSET
    init_train_f1_s: Union[Unset, List[float]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        test_f1_s = []
        for test_f1_s_item_data in self.test_f1_s:
            test_f1_s_item = test_f1_s_item_data

            test_f1_s.append(test_f1_s_item)

        train_accs = []
        for train_accs_item_data in self.train_accs:
            train_accs_item = train_accs_item_data

            train_accs.append(train_accs_item)

        train_f1_s = []
        for train_f1_s_item_data in self.train_f1_s:
            train_f1_s_item = train_f1_s_item_data

            train_f1_s.append(train_f1_s_item)

        test_accs = []
        for test_accs_item_data in self.test_accs:
            test_accs_item = test_accs_item_data

            test_accs.append(test_accs_item)

        train_losses = []
        for train_losses_item_data in self.train_losses:
            train_losses_item = train_losses_item_data

            train_losses.append(train_losses_item)

        test_losses = []
        for test_losses_item_data in self.test_losses:
            test_losses_item = test_losses_item_data

            test_losses.append(test_losses_item)

        end_timestamps = []
        for end_timestamps_item_data in self.end_timestamps:
            end_timestamps_item = end_timestamps_item_data

            end_timestamps.append(end_timestamps_item)

        start_timestamps = []
        for start_timestamps_item_data in self.start_timestamps:
            start_timestamps_item = start_timestamps_item_data

            start_timestamps.append(start_timestamps_item)

        init_test_f1_s: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_test_f1_s, Unset):
            init_test_f1_s = self.init_test_f1_s

        init_timestamps: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_timestamps, Unset):
            init_timestamps = self.init_timestamps

        init_train_accs: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_train_accs, Unset):
            init_train_accs = self.init_train_accs

        init_train_losses: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_train_losses, Unset):
            init_train_losses = self.init_train_losses

        init_test_accs: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_test_accs, Unset):
            init_test_accs = self.init_test_accs

        init_test_losses: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_test_losses, Unset):
            init_test_losses = self.init_test_losses

        init_train_f1_s: Union[Unset, List[float]] = UNSET
        if not isinstance(self.init_train_f1_s, Unset):
            init_train_f1_s = self.init_train_f1_s

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "testF1s": test_f1_s,
                "trainAccs": train_accs,
                "trainF1s": train_f1_s,
                "testAccs": test_accs,
                "trainLosses": train_losses,
                "testLosses": test_losses,
                "endTimestamps": end_timestamps,
                "startTimestamps": start_timestamps,
            }
        )
        if init_test_f1_s is not UNSET:
            field_dict["initTestF1s"] = init_test_f1_s
        if init_timestamps is not UNSET:
            field_dict["initTimestamps"] = init_timestamps
        if init_train_accs is not UNSET:
            field_dict["initTrainAccs"] = init_train_accs
        if init_train_losses is not UNSET:
            field_dict["initTrainLosses"] = init_train_losses
        if init_test_accs is not UNSET:
            field_dict["initTestAccs"] = init_test_accs
        if init_test_losses is not UNSET:
            field_dict["initTestLosses"] = init_test_losses
        if init_train_f1_s is not UNSET:
            field_dict["initTrainF1s"] = init_train_f1_s

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        test_f1_s = []
        _test_f1_s = d.pop("testF1s")
        for test_f1_s_item_data in _test_f1_s:
            test_f1_s_item = cast(List[float], test_f1_s_item_data)

            test_f1_s.append(test_f1_s_item)

        train_accs = []
        _train_accs = d.pop("trainAccs")
        for train_accs_item_data in _train_accs:
            train_accs_item = cast(List[float], train_accs_item_data)

            train_accs.append(train_accs_item)

        train_f1_s = []
        _train_f1_s = d.pop("trainF1s")
        for train_f1_s_item_data in _train_f1_s:
            train_f1_s_item = cast(List[float], train_f1_s_item_data)

            train_f1_s.append(train_f1_s_item)

        test_accs = []
        _test_accs = d.pop("testAccs")
        for test_accs_item_data in _test_accs:
            test_accs_item = cast(List[float], test_accs_item_data)

            test_accs.append(test_accs_item)

        train_losses = []
        _train_losses = d.pop("trainLosses")
        for train_losses_item_data in _train_losses:
            train_losses_item = cast(List[float], train_losses_item_data)

            train_losses.append(train_losses_item)

        test_losses = []
        _test_losses = d.pop("testLosses")
        for test_losses_item_data in _test_losses:
            test_losses_item = cast(List[float], test_losses_item_data)

            test_losses.append(test_losses_item)

        end_timestamps = []
        _end_timestamps = d.pop("endTimestamps")
        for end_timestamps_item_data in _end_timestamps:
            end_timestamps_item = cast(List[float], end_timestamps_item_data)

            end_timestamps.append(end_timestamps_item)

        start_timestamps = []
        _start_timestamps = d.pop("startTimestamps")
        for start_timestamps_item_data in _start_timestamps:
            start_timestamps_item = cast(List[float], start_timestamps_item_data)

            start_timestamps.append(start_timestamps_item)

        init_test_f1_s = cast(List[float], d.pop("initTestF1s", UNSET))

        init_timestamps = cast(List[float], d.pop("initTimestamps", UNSET))

        init_train_accs = cast(List[float], d.pop("initTrainAccs", UNSET))

        init_train_losses = cast(List[float], d.pop("initTrainLosses", UNSET))

        init_test_accs = cast(List[float], d.pop("initTestAccs", UNSET))

        init_test_losses = cast(List[float], d.pop("initTestLosses", UNSET))

        init_train_f1_s = cast(List[float], d.pop("initTrainF1s", UNSET))

        external_ml_history = cls(
            test_f1_s=test_f1_s,
            train_accs=train_accs,
            train_f1_s=train_f1_s,
            test_accs=test_accs,
            train_losses=train_losses,
            test_losses=test_losses,
            end_timestamps=end_timestamps,
            start_timestamps=start_timestamps,
            init_test_f1_s=init_test_f1_s,
            init_timestamps=init_timestamps,
            init_train_accs=init_train_accs,
            init_train_losses=init_train_losses,
            init_test_accs=init_test_accs,
            init_test_losses=init_test_losses,
            init_train_f1_s=init_train_f1_s,
        )

        external_ml_history.additional_properties = d
        return external_ml_history

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
