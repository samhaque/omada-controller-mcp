from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApAdvancedQosOpenApiVO")


@_attrs_define
class ApAdvancedQosOpenApiVO:
    """
    Attributes:
        support2g (bool | Unset): Whether the device supports 2.4GHz.
        support5g (bool | Unset): Whether the device supports 5GHz.
        support5g2 (bool | Unset): Whether the device supports 5GHz frequency splitting into two parts.
        support6g (bool | Unset): Whether the device supports 6GHz.
        delivery_enable_2_g (bool | Unset): Whether Unscheduled Automatic Power Save Delivery enabled in 2.4GHz.
        delivery_enable_5_g (bool | Unset): Whether Unscheduled Automatic Power Save Delivery enabled in 5GHz. The field
            [deliveryEnable5g] will be filled in when the device supports 5GHz. If the device supports frequency division,
            the field indicates 5GHZ-1.(5GHZ-1 is the second part of the 5GHz band) If the device does not support frequency
            division, the field indicates the entire band of 5GHz.
        delivery_enable_5_g_2 (bool | Unset): Whether Unscheduled Automatic Power Save Delivery enabled in
            5GHz-2.(5GHZ-2 is the second part of the 5GHz band) The field [deliveryEnable5g2] will be filled in when the
            device supports 5GHz and frequency splitting.
        delivery_enable_6_g (bool | Unset): Whether Unscheduled Automatic Power Save Delivery enabled in 6GHz.
    """

    support2g: bool | Unset = UNSET
    support5g: bool | Unset = UNSET
    support5g2: bool | Unset = UNSET
    support6g: bool | Unset = UNSET
    delivery_enable_2_g: bool | Unset = UNSET
    delivery_enable_5_g: bool | Unset = UNSET
    delivery_enable_5_g_2: bool | Unset = UNSET
    delivery_enable_6_g: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support2g = self.support2g

        support5g = self.support5g

        support5g2 = self.support5g2

        support6g = self.support6g

        delivery_enable_2_g = self.delivery_enable_2_g

        delivery_enable_5_g = self.delivery_enable_5_g

        delivery_enable_5_g_2 = self.delivery_enable_5_g_2

        delivery_enable_6_g = self.delivery_enable_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support2g is not UNSET:
            field_dict["support2g"] = support2g
        if support5g is not UNSET:
            field_dict["support5g"] = support5g
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if support6g is not UNSET:
            field_dict["support6g"] = support6g
        if delivery_enable_2_g is not UNSET:
            field_dict["deliveryEnable2g"] = delivery_enable_2_g
        if delivery_enable_5_g is not UNSET:
            field_dict["deliveryEnable5g"] = delivery_enable_5_g
        if delivery_enable_5_g_2 is not UNSET:
            field_dict["deliveryEnable5g2"] = delivery_enable_5_g_2
        if delivery_enable_6_g is not UNSET:
            field_dict["deliveryEnable6g"] = delivery_enable_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support2g = d.pop("support2g", UNSET)

        support5g = d.pop("support5g", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        support6g = d.pop("support6g", UNSET)

        delivery_enable_2_g = d.pop("deliveryEnable2g", UNSET)

        delivery_enable_5_g = d.pop("deliveryEnable5g", UNSET)

        delivery_enable_5_g_2 = d.pop("deliveryEnable5g2", UNSET)

        delivery_enable_6_g = d.pop("deliveryEnable6g", UNSET)

        ap_advanced_qos_open_api_vo = cls(
            support2g=support2g,
            support5g=support5g,
            support5g2=support5g2,
            support6g=support6g,
            delivery_enable_2_g=delivery_enable_2_g,
            delivery_enable_5_g=delivery_enable_5_g,
            delivery_enable_5_g_2=delivery_enable_5_g_2,
            delivery_enable_6_g=delivery_enable_6_g,
        )

        ap_advanced_qos_open_api_vo.additional_properties = d
        return ap_advanced_qos_open_api_vo

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
