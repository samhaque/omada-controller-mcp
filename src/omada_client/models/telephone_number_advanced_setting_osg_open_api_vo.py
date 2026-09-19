from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelephoneNumberAdvancedSettingOsgOpenApiVO")


@_attrs_define
class TelephoneNumberAdvancedSettingOsgOpenApiVO:
    """Advanced settings.

    Attributes:
        interface_type (int): InterfaceType should be a value as follows: 0: WAN; 1: LAN; 2: Virtual WAN.
        locale (str | Unset): The country code of telephone number.
        no_answer_time (int | Unset): The no answer time of telephone number.
        t_38_support (bool | Unset): Whether to enable t38 Support.
        interface_id (str | Unset): Interface ID, for example: if interfaceType is LAN network, interfaceId should be
            LAN network ID. LAN Network can be created using 'Create LAN network' interface, and LAN Network ID can be
            obtained from 'Get LAN network list' interface. When parameter [interfaceType] is 0 or 1, parameter
            [interfaceId] should not be empty.
        virtual_wan_id (str | Unset): Virtual WAN ID, can be obtained from 'Query virtual WAN list' interface. When
            parameter [interfaceType] is 2, parameter [virtualWanId] should not be empty.
    """

    interface_type: int
    locale: str | Unset = UNSET
    no_answer_time: int | Unset = UNSET
    t_38_support: bool | Unset = UNSET
    interface_id: str | Unset = UNSET
    virtual_wan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_type = self.interface_type

        locale = self.locale

        no_answer_time = self.no_answer_time

        t_38_support = self.t_38_support

        interface_id = self.interface_id

        virtual_wan_id = self.virtual_wan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaceType": interface_type,
            }
        )
        if locale is not UNSET:
            field_dict["locale"] = locale
        if no_answer_time is not UNSET:
            field_dict["noAnswerTime"] = no_answer_time
        if t_38_support is not UNSET:
            field_dict["t38Support"] = t_38_support
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interface_type = d.pop("interfaceType")

        locale = d.pop("locale", UNSET)

        no_answer_time = d.pop("noAnswerTime", UNSET)

        t_38_support = d.pop("t38Support", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        virtual_wan_id = d.pop("virtualWanId", UNSET)

        telephone_number_advanced_setting_osg_open_api_vo = cls(
            interface_type=interface_type,
            locale=locale,
            no_answer_time=no_answer_time,
            t_38_support=t_38_support,
            interface_id=interface_id,
            virtual_wan_id=virtual_wan_id,
        )

        telephone_number_advanced_setting_osg_open_api_vo.additional_properties = d
        return telephone_number_advanced_setting_osg_open_api_vo

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
