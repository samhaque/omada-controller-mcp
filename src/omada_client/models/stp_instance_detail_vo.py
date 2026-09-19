from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StpInstanceDetailVO")


@_attrs_define
class StpInstanceDetailVO:
    """
    Attributes:
        stp (int): stp, 1: STP / 2: RSTP / 3: MSTP / 4: RPVST / 0: OFF
        id (int | Unset): instance ID
        vlan (int | Unset): instance vlanId
    """

    stp: int
    id: int | Unset = UNSET
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stp = self.stp

        id = self.id

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stp": stp,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stp = d.pop("stp")

        id = d.pop("id", UNSET)

        vlan = d.pop("vlan", UNSET)

        stp_instance_detail_vo = cls(
            stp=stp,
            id=id,
            vlan=vlan,
        )

        stp_instance_detail_vo.additional_properties = d
        return stp_instance_detail_vo

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
