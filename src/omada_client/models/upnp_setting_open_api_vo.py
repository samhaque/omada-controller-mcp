from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpnpSettingOpenApiVO")


@_attrs_define
class UpnpSettingOpenApiVO:
    """
    Attributes:
        enable (bool): Whether to enable UPnP
        wan_port_ids (list[str] | Unset): This field represents WAN Port ID, WAN Port ID can be obtained from "Get
            internet basic info" interface.
        network_ids (list[str] | Unset): This field represents LAN Network ID. LAN Network ID can be obtained from "Get
            all "single"/"multi" interface lan network" interface.
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
    """

    enable: bool
    wan_port_ids: list[str] | Unset = UNSET
    network_ids: list[str] | Unset = UNSET
    support_by_ds_lite_and_map_e: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        wan_port_ids: list[str] | Unset = UNSET
        if not isinstance(self.wan_port_ids, Unset):
            wan_port_ids = self.wan_port_ids

        network_ids: list[str] | Unset = UNSET
        if not isinstance(self.network_ids, Unset):
            network_ids = self.network_ids

        support_by_ds_lite_and_map_e = self.support_by_ds_lite_and_map_e

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if wan_port_ids is not UNSET:
            field_dict["wanPortIds"] = wan_port_ids
        if network_ids is not UNSET:
            field_dict["networkIds"] = network_ids
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        wan_port_ids = cast(list[str], d.pop("wanPortIds", UNSET))

        network_ids = cast(list[str], d.pop("networkIds", UNSET))

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        upnp_setting_open_api_vo = cls(
            enable=enable,
            wan_port_ids=wan_port_ids,
            network_ids=network_ids,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
        )

        upnp_setting_open_api_vo.additional_properties = d
        return upnp_setting_open_api_vo

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
