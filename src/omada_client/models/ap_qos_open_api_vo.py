from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApQosOpenApiVO")


@_attrs_define
class ApQosOpenApiVO:
    """Qos setting of 6 GHz.

    Attributes:
        wmm_enable (bool | Unset): WWM enabled or not.
        no_acknowledgement (bool | Unset): No Acknowledgement enabled or not.
        delivery_enable (bool | Unset): Unscheduled Automatic Power Save Delivery enabled or not.
    """

    wmm_enable: bool | Unset = UNSET
    no_acknowledgement: bool | Unset = UNSET
    delivery_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wmm_enable = self.wmm_enable

        no_acknowledgement = self.no_acknowledgement

        delivery_enable = self.delivery_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wmm_enable is not UNSET:
            field_dict["wmmEnable"] = wmm_enable
        if no_acknowledgement is not UNSET:
            field_dict["noAcknowledgement"] = no_acknowledgement
        if delivery_enable is not UNSET:
            field_dict["deliveryEnable"] = delivery_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wmm_enable = d.pop("wmmEnable", UNSET)

        no_acknowledgement = d.pop("noAcknowledgement", UNSET)

        delivery_enable = d.pop("deliveryEnable", UNSET)

        ap_qos_open_api_vo = cls(
            wmm_enable=wmm_enable,
            no_acknowledgement=no_acknowledgement,
            delivery_enable=delivery_enable,
        )

        ap_qos_open_api_vo.additional_properties = d
        return ap_qos_open_api_vo

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
