from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dot1XEapSettingOpenApiVO")


@_attrs_define
class Dot1XEapSettingOpenApiVO:
    """Enabled eap ports

    Attributes:
        mac (str): MAC address of the EAP. Parameter [mac] should not be null when [eaps] is not null.
        dot_1_x_ports (list[str] | Unset): EAP 802.1x enabled ports. Parameter [dot1xPorts] should be a list of port
            names Example: ['ETH1', 'ETH2'].
    """

    mac: str
    dot_1_x_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        dot_1_x_ports: list[str] | Unset = UNSET
        if not isinstance(self.dot_1_x_ports, Unset):
            dot_1_x_ports = self.dot_1_x_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
            }
        )
        if dot_1_x_ports is not UNSET:
            field_dict["dot1xPorts"] = dot_1_x_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        dot_1_x_ports = cast(list[str], d.pop("dot1xPorts", UNSET))

        dot_1x_eap_setting_open_api_vo = cls(
            mac=mac,
            dot_1_x_ports=dot_1_x_ports,
        )

        dot_1x_eap_setting_open_api_vo.additional_properties = d
        return dot_1x_eap_setting_open_api_vo

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
