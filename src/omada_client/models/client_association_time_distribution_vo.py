from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientAssociationTimeDistributionVO")


@_attrs_define
class ClientAssociationTimeDistributionVO:
    """
    Attributes:
        less_than_2_s_num (int | Unset):
        from_2_to_4_s_num (int | Unset):
        from_4_to_6_s_num (int | Unset):
        from_6_to_8_s_num (int | Unset):
        from_8_to_10_s_num (int | Unset):
        more_than_10_s_num (int | Unset):
        fails (int | Unset):
        less_than_10_s_percent (int | Unset):
    """

    less_than_2_s_num: int | Unset = UNSET
    from_2_to_4_s_num: int | Unset = UNSET
    from_4_to_6_s_num: int | Unset = UNSET
    from_6_to_8_s_num: int | Unset = UNSET
    from_8_to_10_s_num: int | Unset = UNSET
    more_than_10_s_num: int | Unset = UNSET
    fails: int | Unset = UNSET
    less_than_10_s_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        less_than_2_s_num = self.less_than_2_s_num

        from_2_to_4_s_num = self.from_2_to_4_s_num

        from_4_to_6_s_num = self.from_4_to_6_s_num

        from_6_to_8_s_num = self.from_6_to_8_s_num

        from_8_to_10_s_num = self.from_8_to_10_s_num

        more_than_10_s_num = self.more_than_10_s_num

        fails = self.fails

        less_than_10_s_percent = self.less_than_10_s_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if less_than_2_s_num is not UNSET:
            field_dict["lessThan2sNum"] = less_than_2_s_num
        if from_2_to_4_s_num is not UNSET:
            field_dict["from2To4sNum"] = from_2_to_4_s_num
        if from_4_to_6_s_num is not UNSET:
            field_dict["from4To6sNum"] = from_4_to_6_s_num
        if from_6_to_8_s_num is not UNSET:
            field_dict["from6To8sNum"] = from_6_to_8_s_num
        if from_8_to_10_s_num is not UNSET:
            field_dict["from8To10sNum"] = from_8_to_10_s_num
        if more_than_10_s_num is not UNSET:
            field_dict["moreThan10sNum"] = more_than_10_s_num
        if fails is not UNSET:
            field_dict["fails"] = fails
        if less_than_10_s_percent is not UNSET:
            field_dict["lessThan10sPercent"] = less_than_10_s_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        less_than_2_s_num = d.pop("lessThan2sNum", UNSET)

        from_2_to_4_s_num = d.pop("from2To4sNum", UNSET)

        from_4_to_6_s_num = d.pop("from4To6sNum", UNSET)

        from_6_to_8_s_num = d.pop("from6To8sNum", UNSET)

        from_8_to_10_s_num = d.pop("from8To10sNum", UNSET)

        more_than_10_s_num = d.pop("moreThan10sNum", UNSET)

        fails = d.pop("fails", UNSET)

        less_than_10_s_percent = d.pop("lessThan10sPercent", UNSET)

        client_association_time_distribution_vo = cls(
            less_than_2_s_num=less_than_2_s_num,
            from_2_to_4_s_num=from_2_to_4_s_num,
            from_4_to_6_s_num=from_4_to_6_s_num,
            from_6_to_8_s_num=from_6_to_8_s_num,
            from_8_to_10_s_num=from_8_to_10_s_num,
            more_than_10_s_num=more_than_10_s_num,
            fails=fails,
            less_than_10_s_percent=less_than_10_s_percent,
        )

        client_association_time_distribution_vo.additional_properties = d
        return client_association_time_distribution_vo

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
