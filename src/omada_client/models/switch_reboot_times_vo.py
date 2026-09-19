from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_reboot_vo import NameRebootVO


T = TypeVar("T", bound="SwitchRebootTimesVO")


@_attrs_define
class SwitchRebootTimesVO:
    """Switch reboot times

    Attributes:
        total_switch_times (int | Unset): Switch total reboot times
        first_switch (NameRebootVO | Unset):
        second_switch (NameRebootVO | Unset):
        third_switch (NameRebootVO | Unset):
        fourth_switch (NameRebootVO | Unset):
        fifth_switch (NameRebootVO | Unset):
        other_switch (NameRebootVO | Unset):
    """

    total_switch_times: int | Unset = UNSET
    first_switch: NameRebootVO | Unset = UNSET
    second_switch: NameRebootVO | Unset = UNSET
    third_switch: NameRebootVO | Unset = UNSET
    fourth_switch: NameRebootVO | Unset = UNSET
    fifth_switch: NameRebootVO | Unset = UNSET
    other_switch: NameRebootVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_switch_times = self.total_switch_times

        first_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_switch, Unset):
            first_switch = self.first_switch.to_dict()

        second_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.second_switch, Unset):
            second_switch = self.second_switch.to_dict()

        third_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.third_switch, Unset):
            third_switch = self.third_switch.to_dict()

        fourth_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fourth_switch, Unset):
            fourth_switch = self.fourth_switch.to_dict()

        fifth_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fifth_switch, Unset):
            fifth_switch = self.fifth_switch.to_dict()

        other_switch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_switch, Unset):
            other_switch = self.other_switch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_switch_times is not UNSET:
            field_dict["totalSwitchTimes"] = total_switch_times
        if first_switch is not UNSET:
            field_dict["firstSwitch"] = first_switch
        if second_switch is not UNSET:
            field_dict["secondSwitch"] = second_switch
        if third_switch is not UNSET:
            field_dict["thirdSwitch"] = third_switch
        if fourth_switch is not UNSET:
            field_dict["fourthSwitch"] = fourth_switch
        if fifth_switch is not UNSET:
            field_dict["fifthSwitch"] = fifth_switch
        if other_switch is not UNSET:
            field_dict["otherSwitch"] = other_switch

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.name_reboot_vo import NameRebootVO

        d = dict(src_dict)
        total_switch_times = d.pop("totalSwitchTimes", UNSET)

        _first_switch = d.pop("firstSwitch", UNSET)
        first_switch: NameRebootVO | Unset
        if isinstance(_first_switch, Unset):
            first_switch = UNSET
        else:
            first_switch = NameRebootVO.from_dict(_first_switch)

        _second_switch = d.pop("secondSwitch", UNSET)
        second_switch: NameRebootVO | Unset
        if isinstance(_second_switch, Unset):
            second_switch = UNSET
        else:
            second_switch = NameRebootVO.from_dict(_second_switch)

        _third_switch = d.pop("thirdSwitch", UNSET)
        third_switch: NameRebootVO | Unset
        if isinstance(_third_switch, Unset):
            third_switch = UNSET
        else:
            third_switch = NameRebootVO.from_dict(_third_switch)

        _fourth_switch = d.pop("fourthSwitch", UNSET)
        fourth_switch: NameRebootVO | Unset
        if isinstance(_fourth_switch, Unset):
            fourth_switch = UNSET
        else:
            fourth_switch = NameRebootVO.from_dict(_fourth_switch)

        _fifth_switch = d.pop("fifthSwitch", UNSET)
        fifth_switch: NameRebootVO | Unset
        if isinstance(_fifth_switch, Unset):
            fifth_switch = UNSET
        else:
            fifth_switch = NameRebootVO.from_dict(_fifth_switch)

        _other_switch = d.pop("otherSwitch", UNSET)
        other_switch: NameRebootVO | Unset
        if isinstance(_other_switch, Unset):
            other_switch = UNSET
        else:
            other_switch = NameRebootVO.from_dict(_other_switch)

        switch_reboot_times_vo = cls(
            total_switch_times=total_switch_times,
            first_switch=first_switch,
            second_switch=second_switch,
            third_switch=third_switch,
            fourth_switch=fourth_switch,
            fifth_switch=fifth_switch,
            other_switch=other_switch,
        )

        switch_reboot_times_vo.additional_properties = d
        return switch_reboot_times_vo

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
