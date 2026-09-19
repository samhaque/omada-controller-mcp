from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="MspDeviceItem")


@_attrs_define
class MspDeviceItem:
    """Devices to query

    Attributes:
        mac (str): Mac of device.
        site_id (str): SiteId of device.
        customer_id (str): CustomerId of device.
    """

    mac: str
    site_id: str
    customer_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        site_id = self.site_id

        customer_id = self.customer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "siteId": site_id,
                "customerId": customer_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        site_id = d.pop("siteId")

        customer_id = d.pop("customerId")

        msp_device_item = cls(
            mac=mac,
            site_id=site_id,
            customer_id=customer_id,
        )

        msp_device_item.additional_properties = d
        return msp_device_item

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
