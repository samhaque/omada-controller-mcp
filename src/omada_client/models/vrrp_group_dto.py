from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VrrpGroupDTO")


@_attrs_define
class VrrpGroupDTO:
    """Vrrp node member's vrrp group information

    Attributes:
        vrrp_id (int | Unset):
        vrrp_name (str | Unset):
        is_master (bool | Unset):
    """

    vrrp_id: int | Unset = UNSET
    vrrp_name: str | Unset = UNSET
    is_master: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vrrp_id = self.vrrp_id

        vrrp_name = self.vrrp_name

        is_master = self.is_master

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vrrp_id is not UNSET:
            field_dict["vrrpId"] = vrrp_id
        if vrrp_name is not UNSET:
            field_dict["vrrpName"] = vrrp_name
        if is_master is not UNSET:
            field_dict["isMaster"] = is_master

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vrrp_id = d.pop("vrrpId", UNSET)

        vrrp_name = d.pop("vrrpName", UNSET)

        is_master = d.pop("isMaster", UNSET)

        vrrp_group_dto = cls(
            vrrp_id=vrrp_id,
            vrrp_name=vrrp_name,
            is_master=is_master,
        )

        vrrp_group_dto.additional_properties = d
        return vrrp_group_dto

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
