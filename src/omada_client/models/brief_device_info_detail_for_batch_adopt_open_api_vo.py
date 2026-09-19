from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefDeviceInfoDetailForBatchAdoptOpenApiVO")


@_attrs_define
class BriefDeviceInfoDetailForBatchAdoptOpenApiVO:
    """
    Attributes:
        type_ (str | Unset): device type
        mac (str | Unset): device mac
        name (str | Unset): device name
        model (str | Unset): device model
        license_status (int | Unset): license status. 0 means unactive; 1 means unbind; 2 means expired; 3 means active;
            4 means incompatible
        compatible (int | Unset): device compatible
        in_whitelist (bool | Unset): device inWhitelist
        status_category (int | Unset): device status: connected, pending, and disconnected
        status (int | Unset): device status subcategory: connected， pending， wireless pending
        hw_version (str | Unset): device hardware version
        model_version (str | Unset): device model version
        omadac_id (str | Unset): the omadacId of device
        wireless (bool | Unset): Whether the device is wireless
        es (bool | Unset): Whether it is an ES device or not
        device_series_type (int | Unset): Device type: 0: advanced 1: pro
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    license_status: int | Unset = UNSET
    compatible: int | Unset = UNSET
    in_whitelist: bool | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    hw_version: str | Unset = UNSET
    model_version: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    es: bool | Unset = UNSET
    device_series_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        model = self.model

        license_status = self.license_status

        compatible = self.compatible

        in_whitelist = self.in_whitelist

        status_category = self.status_category

        status = self.status

        hw_version = self.hw_version

        model_version = self.model_version

        omadac_id = self.omadac_id

        wireless = self.wireless

        es = self.es

        device_series_type = self.device_series_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if in_whitelist is not UNSET:
            field_dict["inWhitelist"] = in_whitelist
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if es is not UNSET:
            field_dict["es"] = es
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        compatible = d.pop("compatible", UNSET)

        in_whitelist = d.pop("inWhitelist", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        wireless = d.pop("wireless", UNSET)

        es = d.pop("es", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        brief_device_info_detail_for_batch_adopt_open_api_vo = cls(
            type_=type_,
            mac=mac,
            name=name,
            model=model,
            license_status=license_status,
            compatible=compatible,
            in_whitelist=in_whitelist,
            status_category=status_category,
            status=status,
            hw_version=hw_version,
            model_version=model_version,
            omadac_id=omadac_id,
            wireless=wireless,
            es=es,
            device_series_type=device_series_type,
        )

        brief_device_info_detail_for_batch_adopt_open_api_vo.additional_properties = d
        return brief_device_info_detail_for_batch_adopt_open_api_vo

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
