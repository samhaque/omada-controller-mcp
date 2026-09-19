from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPMacBinding")


@_attrs_define
class IPMacBinding:
    """
    Attributes:
        mac (str): MAC of the IP MAC binding entity.
        ip (str): IP of the IP MAC binding entity.
        status (bool): Status of the IP MAC binding entity.
        interface_type (int): Interface type should be a value as follows: 0: WAN; 1: LAN interface.
        interface_id (str): Interface ID. WAN port ID can be obtained from 'Get internet basic info' interface. LAN
            Network can be created using 'Create LAN network' interface, and LAN Network ID can be obtained from 'Get LAN
            network list' interface.
        description (str | Unset): Description should contain 1 to 64 characters.
        export_to_dhcp_reservation (bool | Unset): Whether to export to the DhcpReservation table. This subsection is
            deprecated.
        support_export (bool | Unset): Whether could export to the DhcpReservation table. This subsection is deprecated.
        enable_export_to_dhcp_reservation (bool | Unset): Whether to enable export to the DhcpReservation table.
    """

    mac: str
    ip: str
    status: bool
    interface_type: int
    interface_id: str
    description: str | Unset = UNSET
    export_to_dhcp_reservation: bool | Unset = UNSET
    support_export: bool | Unset = UNSET
    enable_export_to_dhcp_reservation: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        status = self.status

        interface_type = self.interface_type

        interface_id = self.interface_id

        description = self.description

        export_to_dhcp_reservation = self.export_to_dhcp_reservation

        support_export = self.support_export

        enable_export_to_dhcp_reservation = self.enable_export_to_dhcp_reservation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "ip": ip,
                "status": status,
                "interfaceType": interface_type,
                "interfaceId": interface_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if export_to_dhcp_reservation is not UNSET:
            field_dict["exportToDhcpReservation"] = export_to_dhcp_reservation
        if support_export is not UNSET:
            field_dict["supportExport"] = support_export
        if enable_export_to_dhcp_reservation is not UNSET:
            field_dict["enableExportToDhcpReservation"] = (
                enable_export_to_dhcp_reservation
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        ip = d.pop("ip")

        status = d.pop("status")

        interface_type = d.pop("interfaceType")

        interface_id = d.pop("interfaceId")

        description = d.pop("description", UNSET)

        export_to_dhcp_reservation = d.pop("exportToDhcpReservation", UNSET)

        support_export = d.pop("supportExport", UNSET)

        enable_export_to_dhcp_reservation = d.pop(
            "enableExportToDhcpReservation", UNSET
        )

        ip_mac_binding = cls(
            mac=mac,
            ip=ip,
            status=status,
            interface_type=interface_type,
            interface_id=interface_id,
            description=description,
            export_to_dhcp_reservation=export_to_dhcp_reservation,
            support_export=support_export,
            enable_export_to_dhcp_reservation=enable_export_to_dhcp_reservation,
        )

        ip_mac_binding.additional_properties = d
        return ip_mac_binding

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
