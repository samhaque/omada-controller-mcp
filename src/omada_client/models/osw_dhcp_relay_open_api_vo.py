from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswDhcpRelayOpenApiVO")


@_attrs_define
class OswDhcpRelayOpenApiVO:
    """Network DHCP relay settings. Only valid when deviceType is 2 and mode is 2

    Attributes:
        addr (str | Unset): Address IP, like 192.168.0.1
        vrf_id (str | Unset): VRF ID
        server_addrs (list[str] | Unset): Server Address IP List, like 192.168.0.1
    """

    addr: str | Unset = UNSET
    vrf_id: str | Unset = UNSET
    server_addrs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        vrf_id = self.vrf_id

        server_addrs: list[str] | Unset = UNSET
        if not isinstance(self.server_addrs, Unset):
            server_addrs = self.server_addrs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if server_addrs is not UNSET:
            field_dict["serverAddrs"] = server_addrs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        addr = d.pop("addr", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        server_addrs = cast(list[str], d.pop("serverAddrs", UNSET))

        osw_dhcp_relay_open_api_vo = cls(
            addr=addr,
            vrf_id=vrf_id,
            server_addrs=server_addrs,
        )

        osw_dhcp_relay_open_api_vo.additional_properties = d
        return osw_dhcp_relay_open_api_vo

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
