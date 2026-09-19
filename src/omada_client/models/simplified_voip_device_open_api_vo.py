from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedVoipDeviceOpenApiVO")


@_attrs_define
class SimplifiedVoipDeviceOpenApiVO:
    """
    Attributes:
        id (str | Unset): Device ID.
        mac (str | Unset): Device MAC.
        name (str | Unset): Device name.
        model (str | Unset): Device model.
        model_version (str | Unset): Model version of device,for example:3.0.
        type_ (str | Unset): Device type: AP or gateway.
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
    """

    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        added_in_advanced = self.added_in_advanced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        simplified_voip_device_open_api_vo = cls(
            id=id,
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            type_=type_,
            added_in_advanced=added_in_advanced,
        )

        simplified_voip_device_open_api_vo.additional_properties = d
        return simplified_voip_device_open_api_vo

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
