from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApDensityInfoOpenApiVO")


@_attrs_define
class ApDensityInfoOpenApiVO:
    """The current detail of low ap density metrics displayed on the WIFI Dashboard page.

    Attributes:
        name (str | Unset): The name of ap.
        mac (str | Unset): The mac of ap.
        model (str | Unset): The model of ap.
        model_version (str | Unset): The modelVersion of ap.
        type_ (str | Unset): The type of ap.
        no_data (bool | Unset): This flag indicates whether data exists.
        no_data_reason (int | Unset): The no data reason of ap.
        neighbor_ap_num (int | Unset): The neighbor ap number of ap.
        neighbor_ap_percent (int | Unset): The neighbor ap percent
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    no_data: bool | Unset = UNSET
    no_data_reason: int | Unset = UNSET
    neighbor_ap_num: int | Unset = UNSET
    neighbor_ap_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        no_data = self.no_data

        no_data_reason = self.no_data_reason

        neighbor_ap_num = self.neighbor_ap_num

        neighbor_ap_percent = self.neighbor_ap_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if no_data is not UNSET:
            field_dict["noData"] = no_data
        if no_data_reason is not UNSET:
            field_dict["noDataReason"] = no_data_reason
        if neighbor_ap_num is not UNSET:
            field_dict["neighborApNum"] = neighbor_ap_num
        if neighbor_ap_percent is not UNSET:
            field_dict["neighborApPercent"] = neighbor_ap_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        no_data = d.pop("noData", UNSET)

        no_data_reason = d.pop("noDataReason", UNSET)

        neighbor_ap_num = d.pop("neighborApNum", UNSET)

        neighbor_ap_percent = d.pop("neighborApPercent", UNSET)

        ap_density_info_open_api_vo = cls(
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            type_=type_,
            no_data=no_data,
            no_data_reason=no_data_reason,
            neighbor_ap_num=neighbor_ap_num,
            neighbor_ap_percent=neighbor_ap_percent,
        )

        ap_density_info_open_api_vo.additional_properties = d
        return ap_density_info_open_api_vo

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
