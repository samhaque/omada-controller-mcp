from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPMacBindingGeneralSetting")


@_attrs_define
class IPMacBindingGeneralSetting:
    """
    Attributes:
        enable (bool): Enable of the IP MAC binding general setting, If applied, fill in at least one of LAN and WAN.
        lan_ids (list[str] | Unset): LANs of the IP MAC binding general setting. LAN Network can be created using
            'Create LAN network' interface, and LAN Network ID can be obtained from 'Get LAN network list' interface.
        wan_ids (list[str] | Unset): WANs of the IP MAC binding general setting. WAN port ID can be obtained from 'Get
            internet basic info' interface.
        imb_pass (bool | Unset): ImbPass of the IP MAC binding general setting.
        garp (bool | Unset): GARP of the IP MAC binding general setting.
        interval (int | Unset): Interval should be within the range of 1–10000.
    """

    enable: bool
    lan_ids: list[str] | Unset = UNSET
    wan_ids: list[str] | Unset = UNSET
    imb_pass: bool | Unset = UNSET
    garp: bool | Unset = UNSET
    interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        lan_ids: list[str] | Unset = UNSET
        if not isinstance(self.lan_ids, Unset):
            lan_ids = self.lan_ids

        wan_ids: list[str] | Unset = UNSET
        if not isinstance(self.wan_ids, Unset):
            wan_ids = self.wan_ids

        imb_pass = self.imb_pass

        garp = self.garp

        interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if lan_ids is not UNSET:
            field_dict["lanIds"] = lan_ids
        if wan_ids is not UNSET:
            field_dict["wanIds"] = wan_ids
        if imb_pass is not UNSET:
            field_dict["imbPass"] = imb_pass
        if garp is not UNSET:
            field_dict["garp"] = garp
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        lan_ids = cast(list[str], d.pop("lanIds", UNSET))

        wan_ids = cast(list[str], d.pop("wanIds", UNSET))

        imb_pass = d.pop("imbPass", UNSET)

        garp = d.pop("garp", UNSET)

        interval = d.pop("interval", UNSET)

        ip_mac_binding_general_setting = cls(
            enable=enable,
            lan_ids=lan_ids,
            wan_ids=wan_ids,
            imb_pass=imb_pass,
            garp=garp,
            interval=interval,
        )

        ip_mac_binding_general_setting.additional_properties = d
        return ip_mac_binding_general_setting

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
