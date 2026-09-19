from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="MspDeviceIncidentCountItemOpenApiVO")


@_attrs_define
class MspDeviceIncidentCountItemOpenApiVO:
    """Devices grouped by their owning customer.

    Attributes:
        customer_id (str): Customer ID
        mac (str): Device MAC address for which the incident count is requested.
    """

    customer_id: str
    mac: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        mac = self.mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "mac": mac,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        customer_id = d.pop("customerId")

        mac = d.pop("mac")

        msp_device_incident_count_item_open_api_vo = cls(
            customer_id=customer_id,
            mac=mac,
        )

        msp_device_incident_count_item_open_api_vo.additional_properties = d
        return msp_device_incident_count_item_open_api_vo

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
