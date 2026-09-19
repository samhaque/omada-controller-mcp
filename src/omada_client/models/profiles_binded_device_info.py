from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfilesBindedDeviceInfo")


@_attrs_define
class ProfilesBindedDeviceInfo:
    """
    Attributes:
        id (str | Unset):
        device_name (str | Unset): Device name.
        device_mac (str | Unset): Device MAC.
        model (str | Unset): Device model name
        model_version (str | Unset): Device model version
        type_ (str | Unset): Device type
        profile_names (list[str] | Unset): Profile names binded to the device.
    """

    id: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    profile_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        device_name = self.device_name

        device_mac = self.device_mac

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        profile_names: list[str] | Unset = UNSET
        if not isinstance(self.profile_names, Unset):
            profile_names = self.profile_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if profile_names is not UNSET:
            field_dict["profileNames"] = profile_names

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        profile_names = cast(list[str], d.pop("profileNames", UNSET))

        profiles_binded_device_info = cls(
            id=id,
            device_name=device_name,
            device_mac=device_mac,
            model=model,
            model_version=model_version,
            type_=type_,
            profile_names=profile_names,
        )

        profiles_binded_device_info.additional_properties = d
        return profiles_binded_device_info

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
