from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SdWanLinksToHub")


@_attrs_define
class SdWanLinksToHub:
    """A list of hub-spokes of the sdWan group

    Attributes:
        device_mac (str | Unset): The device MAC of the sdWan member.
        type_ (str | Unset): The device type of a SD-WAN candidate device.
        model (str | Unset): The model of a SD-WAN candidate device.
        model_version (str | Unset): The model version of a SD-WAN candidate device.
        linked_to_hub (int | Unset): If a member is a spoke, the link connection to the hub is identified.
        online_status (int | Unset): The device online status of the sdWan member.
    """

    device_mac: str | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    linked_to_hub: int | Unset = UNSET
    online_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        linked_to_hub = self.linked_to_hub

        online_status = self.online_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if linked_to_hub is not UNSET:
            field_dict["linkedToHub"] = linked_to_hub
        if online_status is not UNSET:
            field_dict["onlineStatus"] = online_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac = d.pop("deviceMac", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        linked_to_hub = d.pop("linkedToHub", UNSET)

        online_status = d.pop("onlineStatus", UNSET)

        sd_wan_links_to_hub = cls(
            device_mac=device_mac,
            type_=type_,
            model=model,
            model_version=model_version,
            linked_to_hub=linked_to_hub,
            online_status=online_status,
        )

        sd_wan_links_to_hub.additional_properties = d
        return sd_wan_links_to_hub

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
