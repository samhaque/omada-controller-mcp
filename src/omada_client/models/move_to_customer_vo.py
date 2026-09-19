from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="MoveToCustomerVO")


@_attrs_define
class MoveToCustomerVO:
    """
    Attributes:
        device_macs (list[str]): DeviceMacs should contain 1 entry
        customer (str): Target customer ID
        site (str): Target site ID
    """

    device_macs: list[str]
    customer: str
    site: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_macs = self.device_macs

        customer = self.customer

        site = self.site

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceMacs": device_macs,
                "customer": customer,
                "site": site,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_macs = cast(list[str], d.pop("deviceMacs"))

        customer = d.pop("customer")

        site = d.pop("site")

        move_to_customer_vo = cls(
            device_macs=device_macs,
            customer=customer,
            site=site,
        )

        move_to_customer_vo.additional_properties = d
        return move_to_customer_vo

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
