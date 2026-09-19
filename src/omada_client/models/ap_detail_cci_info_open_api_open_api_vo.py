from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApDetailCciInfoOpenApiOpenApiVO")


@_attrs_define
class ApDetailCciInfoOpenApiOpenApiVO:
    """The current detail of low CCI metrics displayed on the WIFI Dashboard page.

    Attributes:
        name (str | Unset): The name of ap.
        mac (str | Unset): The mac of ap.
        model (str | Unset): The model of ap.
        model_version (str | Unset): The modelVersion of ap.
        type_ (str | Unset): The type of ap.
        no_data (bool | Unset): This flag indicates whether data exists.
        no_data_reason (int | Unset): The no data reason of ap.
        channel (int | Unset): The channel of ap.
        channel5g2 (int | Unset): The channel of 5g2 radio of ap.
        total_level (int | Unset): The total CCI level of ap.
        total_level_percent (int | Unset): The total CCI level percent of ap.
        in_site_level (int | Unset): The inSite CCI level of ap.
        in_site_level_percent (int | Unset): The inSite CCI level percent of ap.
        out_site_level (int | Unset): The outSite CCI level of ap.
        out_site_level_percent (int | Unset): The outSite CCI level percent of ap.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    no_data: bool | Unset = UNSET
    no_data_reason: int | Unset = UNSET
    channel: int | Unset = UNSET
    channel5g2: int | Unset = UNSET
    total_level: int | Unset = UNSET
    total_level_percent: int | Unset = UNSET
    in_site_level: int | Unset = UNSET
    in_site_level_percent: int | Unset = UNSET
    out_site_level: int | Unset = UNSET
    out_site_level_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        no_data = self.no_data

        no_data_reason = self.no_data_reason

        channel = self.channel

        channel5g2 = self.channel5g2

        total_level = self.total_level

        total_level_percent = self.total_level_percent

        in_site_level = self.in_site_level

        in_site_level_percent = self.in_site_level_percent

        out_site_level = self.out_site_level

        out_site_level_percent = self.out_site_level_percent

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
        if channel is not UNSET:
            field_dict["channel"] = channel
        if channel5g2 is not UNSET:
            field_dict["channel5g2"] = channel5g2
        if total_level is not UNSET:
            field_dict["totalLevel"] = total_level
        if total_level_percent is not UNSET:
            field_dict["totalLevelPercent"] = total_level_percent
        if in_site_level is not UNSET:
            field_dict["inSiteLevel"] = in_site_level
        if in_site_level_percent is not UNSET:
            field_dict["inSiteLevelPercent"] = in_site_level_percent
        if out_site_level is not UNSET:
            field_dict["outSiteLevel"] = out_site_level
        if out_site_level_percent is not UNSET:
            field_dict["outSiteLevelPercent"] = out_site_level_percent

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

        channel = d.pop("channel", UNSET)

        channel5g2 = d.pop("channel5g2", UNSET)

        total_level = d.pop("totalLevel", UNSET)

        total_level_percent = d.pop("totalLevelPercent", UNSET)

        in_site_level = d.pop("inSiteLevel", UNSET)

        in_site_level_percent = d.pop("inSiteLevelPercent", UNSET)

        out_site_level = d.pop("outSiteLevel", UNSET)

        out_site_level_percent = d.pop("outSiteLevelPercent", UNSET)

        ap_detail_cci_info_open_api_open_api_vo = cls(
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            type_=type_,
            no_data=no_data,
            no_data_reason=no_data_reason,
            channel=channel,
            channel5g2=channel5g2,
            total_level=total_level,
            total_level_percent=total_level_percent,
            in_site_level=in_site_level,
            in_site_level_percent=in_site_level_percent,
            out_site_level=out_site_level,
            out_site_level_percent=out_site_level_percent,
        )

        ap_detail_cci_info_open_api_open_api_vo.additional_properties = d
        return ap_detail_cci_info_open_api_open_api_vo

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
