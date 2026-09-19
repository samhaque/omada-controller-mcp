from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SdWanGroupBrief")


@_attrs_define
class SdWanGroupBrief:
    """
    Attributes:
        id (str | Unset): The ID of the SD-WAN group
        name (str | Unset): The name of the SD-WAN group
        hub_device_type (str | Unset): The type of the hub device of this SD-WAN group
        hub_model (str | Unset): The model of the hub device of this SD-WAN group
        hub_model_version (str | Unset): The model version of the hub device of this SD-WAN group
        device_num (int | Unset): The number of device in this SD-WAN group
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    hub_device_type: str | Unset = UNSET
    hub_model: str | Unset = UNSET
    hub_model_version: str | Unset = UNSET
    device_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        hub_device_type = self.hub_device_type

        hub_model = self.hub_model

        hub_model_version = self.hub_model_version

        device_num = self.device_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if hub_device_type is not UNSET:
            field_dict["hubDeviceType"] = hub_device_type
        if hub_model is not UNSET:
            field_dict["hubModel"] = hub_model
        if hub_model_version is not UNSET:
            field_dict["hubModelVersion"] = hub_model_version
        if device_num is not UNSET:
            field_dict["deviceNum"] = device_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        hub_device_type = d.pop("hubDeviceType", UNSET)

        hub_model = d.pop("hubModel", UNSET)

        hub_model_version = d.pop("hubModelVersion", UNSET)

        device_num = d.pop("deviceNum", UNSET)

        sd_wan_group_brief = cls(
            id=id,
            name=name,
            hub_device_type=hub_device_type,
            hub_model=hub_model,
            hub_model_version=hub_model_version,
            device_num=device_num,
        )

        sd_wan_group_brief.additional_properties = d
        return sd_wan_group_brief

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
