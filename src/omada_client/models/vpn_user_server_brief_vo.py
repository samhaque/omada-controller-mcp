from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnUserServerBriefVO")


@_attrs_define
class VpnUserServerBriefVO:
    """
    Attributes:
        id (str | Unset): ID of the VPN user.
        name (str | Unset): Name of the VPN user.
        vpn_type (int | Unset): Server Vpn type. 0: L2TP; 1: PPTP; 2: IPSec; 3: OpenVPN; 4: WireGuard; 5: SSL VPN.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    vpn_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vpn_type = self.vpn_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vpn_type is not UNSET:
            field_dict["vpnType"] = vpn_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        vpn_user_server_brief_vo = cls(
            id=id,
            name=name,
            vpn_type=vpn_type,
        )

        vpn_user_server_brief_vo.additional_properties = d
        return vpn_user_server_brief_vo

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
