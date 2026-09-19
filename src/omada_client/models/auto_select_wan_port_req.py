from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoSelectWanPortReq")


@_attrs_define
class AutoSelectWanPortReq:
    """A list of the SD-WAN devices which use auto select.

    Attributes:
        device_mac (str): The MAC of a SD-WAN candidate device.
        site_id (str): Site ID.
        role (int): The role of SD-WAN member, hub: 0 or spoke: 1.
        linked_spokes (list[str] | Unset): A list MAC of linked-spokes of the sdWan group.
    """

    device_mac: str
    site_id: str
    role: int
    linked_spokes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        site_id = self.site_id

        role = self.role

        linked_spokes: list[str] | Unset = UNSET
        if not isinstance(self.linked_spokes, Unset):
            linked_spokes = self.linked_spokes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceMac": device_mac,
                "siteId": site_id,
                "role": role,
            }
        )
        if linked_spokes is not UNSET:
            field_dict["linkedSpokes"] = linked_spokes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac = d.pop("deviceMac")

        site_id = d.pop("siteId")

        role = d.pop("role")

        linked_spokes = cast(list[str], d.pop("linkedSpokes", UNSET))

        auto_select_wan_port_req = cls(
            device_mac=device_mac,
            site_id=site_id,
            role=role,
            linked_spokes=linked_spokes,
        )

        auto_select_wan_port_req.additional_properties = d
        return auto_select_wan_port_req

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
