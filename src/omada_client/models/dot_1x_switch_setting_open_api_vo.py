from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dot1XSwitchSettingOpenApiVO")


@_attrs_define
class Dot1XSwitchSettingOpenApiVO:
    """Enabled switch ports, optional when update switch 802.1x setting

    Attributes:
        mac (str): MAC address of the switch
        dot_1_x_ports (list[int] | Unset): Switch 802.1x enabled ports
        mab_ports (list[int] | Unset): Switch MAB enabled ports
        account_vrf_id (str | Unset): Account VRF ID
        auth_vrf_id (str | Unset): Auth VRF ID
    """

    mac: str
    dot_1_x_ports: list[int] | Unset = UNSET
    mab_ports: list[int] | Unset = UNSET
    account_vrf_id: str | Unset = UNSET
    auth_vrf_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        dot_1_x_ports: list[int] | Unset = UNSET
        if not isinstance(self.dot_1_x_ports, Unset):
            dot_1_x_ports = self.dot_1_x_ports

        mab_ports: list[int] | Unset = UNSET
        if not isinstance(self.mab_ports, Unset):
            mab_ports = self.mab_ports

        account_vrf_id = self.account_vrf_id

        auth_vrf_id = self.auth_vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
            }
        )
        if dot_1_x_ports is not UNSET:
            field_dict["dot1xPorts"] = dot_1_x_ports
        if mab_ports is not UNSET:
            field_dict["mabPorts"] = mab_ports
        if account_vrf_id is not UNSET:
            field_dict["accountVrfId"] = account_vrf_id
        if auth_vrf_id is not UNSET:
            field_dict["authVrfId"] = auth_vrf_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        dot_1_x_ports = cast(list[int], d.pop("dot1xPorts", UNSET))

        mab_ports = cast(list[int], d.pop("mabPorts", UNSET))

        account_vrf_id = d.pop("accountVrfId", UNSET)

        auth_vrf_id = d.pop("authVrfId", UNSET)

        dot_1x_switch_setting_open_api_vo = cls(
            mac=mac,
            dot_1_x_ports=dot_1_x_ports,
            mab_ports=mab_ports,
            account_vrf_id=account_vrf_id,
            auth_vrf_id=auth_vrf_id,
        )

        dot_1x_switch_setting_open_api_vo.additional_properties = d
        return dot_1x_switch_setting_open_api_vo

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
