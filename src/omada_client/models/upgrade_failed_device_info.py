from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO


T = TypeVar("T", bound="UpgradeFailedDeviceInfo")


@_attrs_define
class UpgradeFailedDeviceInfo:
    """
    Attributes:
        model_type_info (ModelTypeInfoOpenApiVO | Unset): Model type information.
        device_name (str | Unset): Name of the device which failed to upgrade.
        mac (str | Unset): Mac address of device which upgrade failed.
        current_version (str | Unset): The current firmware version of the device which upgrade failed.
        site_name (str | Unset): The siteName of the device which upgrade failed.
        type_ (str | Unset): Device type should be a value as follows: gateway, switch, ap.
    """

    model_type_info: ModelTypeInfoOpenApiVO | Unset = UNSET
    device_name: str | Unset = UNSET
    mac: str | Unset = UNSET
    current_version: str | Unset = UNSET
    site_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_type_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_type_info, Unset):
            model_type_info = self.model_type_info.to_dict()

        device_name = self.device_name

        mac = self.mac

        current_version = self.current_version

        site_name = self.site_name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_type_info is not UNSET:
            field_dict["modelTypeInfo"] = model_type_info
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_type_info_open_api_vo import (
            ModelTypeInfoOpenApiVO,
        )

        d = dict(src_dict)
        _model_type_info = d.pop("modelTypeInfo", UNSET)
        model_type_info: ModelTypeInfoOpenApiVO | Unset
        if isinstance(_model_type_info, Unset):
            model_type_info = UNSET
        else:
            model_type_info = ModelTypeInfoOpenApiVO.from_dict(_model_type_info)

        device_name = d.pop("deviceName", UNSET)

        mac = d.pop("mac", UNSET)

        current_version = d.pop("currentVersion", UNSET)

        site_name = d.pop("siteName", UNSET)

        type_ = d.pop("type", UNSET)

        upgrade_failed_device_info = cls(
            model_type_info=model_type_info,
            device_name=device_name,
            mac=mac,
            current_version=current_version,
            site_name=site_name,
            type_=type_,
        )

        upgrade_failed_device_info.additional_properties = d
        return upgrade_failed_device_info

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
