from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apn_profile import ApnProfile


T = TypeVar("T", bound="ApnProfileData")


@_attrs_define
class ApnProfileData:
    """
    Attributes:
        support_dual_sim (int | Unset): Support dual sim card or not
        data (list[ApnProfile] | Unset): Apn profile list
    """

    support_dual_sim: int | Unset = UNSET
    data: list[ApnProfile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_dual_sim = self.support_dual_sim

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support_dual_sim is not UNSET:
            field_dict["supportDualSim"] = support_dual_sim
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.apn_profile import ApnProfile

        d = dict(src_dict)
        support_dual_sim = d.pop("supportDualSim", UNSET)

        _data = d.pop("data", UNSET)
        data: list[ApnProfile] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ApnProfile.from_dict(data_item_data)

                data.append(data_item)

        apn_profile_data = cls(
            support_dual_sim=support_dual_sim,
            data=data,
        )

        apn_profile_data.additional_properties = d
        return apn_profile_data

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
