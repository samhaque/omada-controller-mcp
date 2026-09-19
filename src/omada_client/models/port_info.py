from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PortInfo")


@_attrs_define
class PortInfo:
    """Port List

    Attributes:
        port (int): Port ID
        name (str): Port name
        profile_id (str): Profile ID
        profile_name (str): Profile Name
        profile_override_enable (bool): Profile Override Enable
        poe_mode (int): PoE mode should be a value as follows: 1: on(802.3at/af); 0: off.
        lag_port (bool): Whether this port exists in a LAG
        status (int): Status should be a value as follows: 0: off; 1: on, only when lagPort is false
    """

    port: int
    name: str
    profile_id: str
    profile_name: str
    profile_override_enable: bool
    poe_mode: int
    lag_port: bool
    status: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        profile_id = self.profile_id

        profile_name = self.profile_name

        profile_override_enable = self.profile_override_enable

        poe_mode = self.poe_mode

        lag_port = self.lag_port

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
                "name": name,
                "profileId": profile_id,
                "profileName": profile_name,
                "profileOverrideEnable": profile_override_enable,
                "poeMode": poe_mode,
                "lagPort": lag_port,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port")

        name = d.pop("name")

        profile_id = d.pop("profileId")

        profile_name = d.pop("profileName")

        profile_override_enable = d.pop("profileOverrideEnable")

        poe_mode = d.pop("poeMode")

        lag_port = d.pop("lagPort")

        status = d.pop("status")

        port_info = cls(
            port=port,
            name=name,
            profile_id=profile_id,
            profile_name=profile_name,
            profile_override_enable=profile_override_enable,
            poe_mode=poe_mode,
            lag_port=lag_port,
            status=status,
        )

        port_info.additional_properties = d
        return port_info

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
