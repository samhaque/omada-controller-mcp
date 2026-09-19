from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_bridge_tdma_config_vo import ApBridgeTdmaConfigVO


T = TypeVar("T", bound="ApBridgeConfig")


@_attrs_define
class ApBridgeConfig:
    """
    Attributes:
        bridge_ssid_name (str | Unset): Bridge SSID name. It should contain 1 to 32 UTF-8 characters.
        bridge_ssid_password (str | Unset): Bridge SSID password. It should contain 8-63 printable ASCII characters.
        hw_switch (int | Unset): Bridge DIP Switch config status. 0: disable, 1: enable.
        tdma_config (ApBridgeTdmaConfigVO | Unset): Bridge TDMA config.
    """

    bridge_ssid_name: str | Unset = UNSET
    bridge_ssid_password: str | Unset = UNSET
    hw_switch: int | Unset = UNSET
    tdma_config: ApBridgeTdmaConfigVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_ssid_name = self.bridge_ssid_name

        bridge_ssid_password = self.bridge_ssid_password

        hw_switch = self.hw_switch

        tdma_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tdma_config, Unset):
            tdma_config = self.tdma_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bridge_ssid_name is not UNSET:
            field_dict["bridgeSsidName"] = bridge_ssid_name
        if bridge_ssid_password is not UNSET:
            field_dict["bridgeSsidPassword"] = bridge_ssid_password
        if hw_switch is not UNSET:
            field_dict["hwSwitch"] = hw_switch
        if tdma_config is not UNSET:
            field_dict["tdmaConfig"] = tdma_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_bridge_tdma_config_vo import (
            ApBridgeTdmaConfigVO,
        )

        d = dict(src_dict)
        bridge_ssid_name = d.pop("bridgeSsidName", UNSET)

        bridge_ssid_password = d.pop("bridgeSsidPassword", UNSET)

        hw_switch = d.pop("hwSwitch", UNSET)

        _tdma_config = d.pop("tdmaConfig", UNSET)
        tdma_config: ApBridgeTdmaConfigVO | Unset
        if isinstance(_tdma_config, Unset):
            tdma_config = UNSET
        else:
            tdma_config = ApBridgeTdmaConfigVO.from_dict(_tdma_config)

        ap_bridge_config = cls(
            bridge_ssid_name=bridge_ssid_name,
            bridge_ssid_password=bridge_ssid_password,
            hw_switch=hw_switch,
            tdma_config=tdma_config,
        )

        ap_bridge_config.additional_properties = d
        return ap_bridge_config

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
