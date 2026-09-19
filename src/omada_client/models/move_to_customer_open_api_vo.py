from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveToCustomerOpenApiVO")


@_attrs_define
class MoveToCustomerOpenApiVO:
    """
    Attributes:
        customer (str): Target customer id.
        site (str): Target site id.
        device_macs (list[str] | Unset): Mac adress of the device.
        device_mac (str | Unset): Mac adress of the device. If [deviceMac] is not empty, it takes effect with a higher
            priority than [deviceMacs].
    """

    customer: str
    site: str
    device_macs: list[str] | Unset = UNSET
    device_mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer = self.customer

        site = self.site

        device_macs: list[str] | Unset = UNSET
        if not isinstance(self.device_macs, Unset):
            device_macs = self.device_macs

        device_mac = self.device_mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer": customer,
                "site": site,
            }
        )
        if device_macs is not UNSET:
            field_dict["deviceMacs"] = device_macs
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        customer = d.pop("customer")

        site = d.pop("site")

        device_macs = cast(list[str], d.pop("deviceMacs", UNSET))

        device_mac = d.pop("deviceMac", UNSET)

        move_to_customer_open_api_vo = cls(
            customer=customer,
            site=site,
            device_macs=device_macs,
            device_mac=device_mac,
        )

        move_to_customer_open_api_vo.additional_properties = d
        return move_to_customer_open_api_vo

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
