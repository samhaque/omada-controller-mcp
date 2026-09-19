from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientAssociationActivities")


@_attrs_define
class ClientAssociationActivities:
    """Clients association activities with time.

    Attributes:
        less_than_1_s_num (int | Unset): Number of clients with association time less than 1 second.
        from_1_to_3_s_num (int | Unset): Number of clients with association time less than 3 seconds and greater than or
            equal to 1 second.
        from_3_to_12_s_num (int | Unset): Number of clients with association time less than 12 seconds and greater than
            or equal to 3 second.
        more_than_12_s_num (int | Unset): Number of clients with association time greater than or equal to 12 second.
        time (int | Unset): Timestamp, unit is second.
    """

    less_than_1_s_num: int | Unset = UNSET
    from_1_to_3_s_num: int | Unset = UNSET
    from_3_to_12_s_num: int | Unset = UNSET
    more_than_12_s_num: int | Unset = UNSET
    time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        less_than_1_s_num = self.less_than_1_s_num

        from_1_to_3_s_num = self.from_1_to_3_s_num

        from_3_to_12_s_num = self.from_3_to_12_s_num

        more_than_12_s_num = self.more_than_12_s_num

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if less_than_1_s_num is not UNSET:
            field_dict["lessThan1sNum"] = less_than_1_s_num
        if from_1_to_3_s_num is not UNSET:
            field_dict["from1To3sNum"] = from_1_to_3_s_num
        if from_3_to_12_s_num is not UNSET:
            field_dict["from3To12sNum"] = from_3_to_12_s_num
        if more_than_12_s_num is not UNSET:
            field_dict["moreThan12sNum"] = more_than_12_s_num
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        less_than_1_s_num = d.pop("lessThan1sNum", UNSET)

        from_1_to_3_s_num = d.pop("from1To3sNum", UNSET)

        from_3_to_12_s_num = d.pop("from3To12sNum", UNSET)

        more_than_12_s_num = d.pop("moreThan12sNum", UNSET)

        time = d.pop("time", UNSET)

        client_association_activities = cls(
            less_than_1_s_num=less_than_1_s_num,
            from_1_to_3_s_num=from_1_to_3_s_num,
            from_3_to_12_s_num=from_3_to_12_s_num,
            more_than_12_s_num=more_than_12_s_num,
            time=time,
        )

        client_association_activities.additional_properties = d
        return client_association_activities

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
