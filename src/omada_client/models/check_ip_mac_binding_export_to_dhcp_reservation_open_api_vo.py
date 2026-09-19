from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckIpMacBindingExportToDhcpReservationOpenApiVO")


@_attrs_define
class CheckIpMacBindingExportToDhcpReservationOpenApiVO:
    """
    Attributes:
        mac (str): MAC of the IP MAC binding entity.
        ip (str): IP of the IP MAC binding entity.
        interface_id (str): Interface ID. WAN port ID can be obtained from 'Get internet basic info' interface. LAN
            Network can be created using 'Create LAN network' interface, and LAN Network ID can be obtained from 'Get LAN
            network list' interface.
        imb_id (str | Unset): IP-MAC binding entry ID.
    """

    mac: str
    ip: str
    interface_id: str
    imb_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        interface_id = self.interface_id

        imb_id = self.imb_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "ip": ip,
                "interfaceId": interface_id,
            }
        )
        if imb_id is not UNSET:
            field_dict["imbId"] = imb_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        ip = d.pop("ip")

        interface_id = d.pop("interfaceId")

        imb_id = d.pop("imbId", UNSET)

        check_ip_mac_binding_export_to_dhcp_reservation_open_api_vo = cls(
            mac=mac,
            ip=ip,
            interface_id=interface_id,
            imb_id=imb_id,
        )

        check_ip_mac_binding_export_to_dhcp_reservation_open_api_vo.additional_properties = d
        return check_ip_mac_binding_export_to_dhcp_reservation_open_api_vo

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
