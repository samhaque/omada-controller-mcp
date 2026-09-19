from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApBtDetailOpenApiVO")


@_attrs_define
class ApBtDetailOpenApiVO:
    """Detailed information about the devices bound to this configuration.

    Attributes:
        mac (str | Unset): Device mac.
        name (str | Unset): Device name.
        type_ (int | Unset): Device type.
        show_model (str | Unset): Device show model.
        firmware_version (str | Unset): Device firmware version.
        status_category (int | Unset): Device status.
        device_type (str | Unset): Device type.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    show_model: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    status_category: int | Unset = UNSET
    device_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        type_ = self.type_

        show_model = self.show_model

        firmware_version = self.firmware_version

        status_category = self.status_category

        device_type = self.device_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        show_model = d.pop("showModel", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        device_type = d.pop("deviceType", UNSET)

        ap_bt_detail_open_api_vo = cls(
            mac=mac,
            name=name,
            type_=type_,
            show_model=show_model,
            firmware_version=firmware_version,
            status_category=status_category,
            device_type=device_type,
        )

        ap_bt_detail_open_api_vo.additional_properties = d
        return ap_bt_detail_open_api_vo

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
