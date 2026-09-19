from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTemplateAdd")


@_attrs_define
class DeviceTemplateAdd:
    """
    Attributes:
        template_name (str | Unset): The name of device template.
        device_type (str | Unset): The type of device.
        model (str | Unset): The model name of device.
        model_version (str | Unset): The model version of device.For example: 1.0
        template_settings (list[int] | Unset): The configurable modules of device. For Access Series/ Aggregation/
            Campus Switches: 1:port; 2:vlanInterface; 3:staticRoute; 6:general; 7:loopbackControl. For Agile Series
            Switches: 1:port; 5:ipSetting; 6:general; 7:loopbackControl. For only Wireless Gateways: 2:radios; 3:wlans;
            5:advanced. For only 4G/5G Gateways: 7:sim_statistics; 8:sms_settings. For all Gateways: 1:port; 4:general;
            9:routing; 10:nat; 11:bandwidth_control; 12:acl; 13:session_limit; 14:gateway_qos; 15:url_filtering;
            16:application_control; 17:ids_ips; 18:firewall; 19:dns; 20:upnp; 21:iptv; 23:advanced_general;
            24:mac_filtering.
    """

    template_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    template_settings: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_name = self.template_name

        device_type = self.device_type

        model = self.model

        model_version = self.model_version

        template_settings: list[int] | Unset = UNSET
        if not isinstance(self.template_settings, Unset):
            template_settings = self.template_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if template_settings is not UNSET:
            field_dict["templateSettings"] = template_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        template_name = d.pop("templateName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        template_settings = cast(list[int], d.pop("templateSettings", UNSET))

        device_template_add = cls(
            template_name=template_name,
            device_type=device_type,
            model=model,
            model_version=model_version,
            template_settings=template_settings,
        )

        device_template_add.additional_properties = d
        return device_template_add

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
