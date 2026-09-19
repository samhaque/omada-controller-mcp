from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApInfoOpenApiVO")


@_attrs_define
class ApInfoOpenApiVO:
    """A list of information for AP devices.

    Attributes:
        name (str | Unset): Default uses the MAC address as the name.
        mac (str | Unset): Mac address
        model (str | Unset): Model, such as EAP225.
        model_version (str | Unset): Model version of device,for example:3.0
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        time (int | Unset): Last active time.
        has_result (bool | Unset): Whether the result exists.
        support2g (bool | Unset): Whether the Ap device support 2g.
        support5g (bool | Unset): Whether the Ap device support 5g.
        support6g (bool | Unset): Whether the Ap device support 6g.
        support_wifi_interf (bool | Unset): Whether the Ap device support wifi interference detection.
        support_non_wifi_interf (bool | Unset): Whether the Ap device support non-wifi interference detection.
        support_channel_util (bool | Unset): Whether the Ap device support channel util detection.
        support_return_band_width (bool | Unset): Whether the Ap device support get band width by interference
            detection.
        actual_channel_2_g (str | Unset): Actual 2.4G channel of the device.
        band_width_2_g (str | Unset): 2.4G bandWidth of the device.
        actual_channel_5_g (str | Unset): Actual 5G channel of the device.
        band_width_5_g (str | Unset): 5G bandWidth of the device.
        actual_channel_6_g (str | Unset): Actual 6G channel of the device.
        band_width_6_g (str | Unset): 6G bandWidth of the device.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    time: int | Unset = UNSET
    has_result: bool | Unset = UNSET
    support2g: bool | Unset = UNSET
    support5g: bool | Unset = UNSET
    support6g: bool | Unset = UNSET
    support_wifi_interf: bool | Unset = UNSET
    support_non_wifi_interf: bool | Unset = UNSET
    support_channel_util: bool | Unset = UNSET
    support_return_band_width: bool | Unset = UNSET
    actual_channel_2_g: str | Unset = UNSET
    band_width_2_g: str | Unset = UNSET
    actual_channel_5_g: str | Unset = UNSET
    band_width_5_g: str | Unset = UNSET
    actual_channel_6_g: str | Unset = UNSET
    band_width_6_g: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        time = self.time

        has_result = self.has_result

        support2g = self.support2g

        support5g = self.support5g

        support6g = self.support6g

        support_wifi_interf = self.support_wifi_interf

        support_non_wifi_interf = self.support_non_wifi_interf

        support_channel_util = self.support_channel_util

        support_return_band_width = self.support_return_band_width

        actual_channel_2_g = self.actual_channel_2_g

        band_width_2_g = self.band_width_2_g

        actual_channel_5_g = self.actual_channel_5_g

        band_width_5_g = self.band_width_5_g

        actual_channel_6_g = self.actual_channel_6_g

        band_width_6_g = self.band_width_6_g

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
        if time is not UNSET:
            field_dict["time"] = time
        if has_result is not UNSET:
            field_dict["hasResult"] = has_result
        if support2g is not UNSET:
            field_dict["support2g"] = support2g
        if support5g is not UNSET:
            field_dict["support5g"] = support5g
        if support6g is not UNSET:
            field_dict["support6g"] = support6g
        if support_wifi_interf is not UNSET:
            field_dict["supportWifiInterf"] = support_wifi_interf
        if support_non_wifi_interf is not UNSET:
            field_dict["supportNonWifiInterf"] = support_non_wifi_interf
        if support_channel_util is not UNSET:
            field_dict["supportChannelUtil"] = support_channel_util
        if support_return_band_width is not UNSET:
            field_dict["supportReturnBandWidth"] = support_return_band_width
        if actual_channel_2_g is not UNSET:
            field_dict["actualChannel2g"] = actual_channel_2_g
        if band_width_2_g is not UNSET:
            field_dict["bandWidth2g"] = band_width_2_g
        if actual_channel_5_g is not UNSET:
            field_dict["actualChannel5g"] = actual_channel_5_g
        if band_width_5_g is not UNSET:
            field_dict["bandWidth5g"] = band_width_5_g
        if actual_channel_6_g is not UNSET:
            field_dict["actualChannel6g"] = actual_channel_6_g
        if band_width_6_g is not UNSET:
            field_dict["bandWidth6g"] = band_width_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        time = d.pop("time", UNSET)

        has_result = d.pop("hasResult", UNSET)

        support2g = d.pop("support2g", UNSET)

        support5g = d.pop("support5g", UNSET)

        support6g = d.pop("support6g", UNSET)

        support_wifi_interf = d.pop("supportWifiInterf", UNSET)

        support_non_wifi_interf = d.pop("supportNonWifiInterf", UNSET)

        support_channel_util = d.pop("supportChannelUtil", UNSET)

        support_return_band_width = d.pop("supportReturnBandWidth", UNSET)

        actual_channel_2_g = d.pop("actualChannel2g", UNSET)

        band_width_2_g = d.pop("bandWidth2g", UNSET)

        actual_channel_5_g = d.pop("actualChannel5g", UNSET)

        band_width_5_g = d.pop("bandWidth5g", UNSET)

        actual_channel_6_g = d.pop("actualChannel6g", UNSET)

        band_width_6_g = d.pop("bandWidth6g", UNSET)

        ap_info_open_api_vo = cls(
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            type_=type_,
            time=time,
            has_result=has_result,
            support2g=support2g,
            support5g=support5g,
            support6g=support6g,
            support_wifi_interf=support_wifi_interf,
            support_non_wifi_interf=support_non_wifi_interf,
            support_channel_util=support_channel_util,
            support_return_band_width=support_return_band_width,
            actual_channel_2_g=actual_channel_2_g,
            band_width_2_g=band_width_2_g,
            actual_channel_5_g=actual_channel_5_g,
            band_width_5_g=band_width_5_g,
            actual_channel_6_g=actual_channel_6_g,
            band_width_6_g=band_width_6_g,
        )

        ap_info_open_api_vo.additional_properties = d
        return ap_info_open_api_vo

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
