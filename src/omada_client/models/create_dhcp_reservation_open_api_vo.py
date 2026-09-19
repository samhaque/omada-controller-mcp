from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dhcp_options import CustomDHCPOptions


T = TypeVar("T", bound="CreateDhcpReservationOpenApiVO")


@_attrs_define
class CreateDhcpReservationOpenApiVO:
    """
    Attributes:
        net_id (str): This field represents LAN Network ID. LAN Network can be created using 'Create LAN network'
            interface, and LAN Network ID can be obtained from 'Get LAN network list' interface
        mac (str): Device MAC address, format: AA-BB-CC-11-22-33
        status (bool): DHCP reservation enable status
        ip (str | Unset): Reserved IP address
        options (list[CustomDHCPOptions] | Unset): Advanced DHCP options
        description (str | Unset): Description of DHCP reservation. Description should contain 1 to 128 characters
        confirm_conflict (bool | Unset): True when creating an entry with IP and IP-MAC Binding conflicts confirmed
        server_type (str | Unset): Dhcp Server Device Type
        server_mac (str | Unset): Dhcp Server Device Mac
        server_stack_id (str | Unset): Dhcp Server Stack ID
    """

    net_id: str
    mac: str
    status: bool
    ip: str | Unset = UNSET
    options: list[CustomDHCPOptions] | Unset = UNSET
    description: str | Unset = UNSET
    confirm_conflict: bool | Unset = UNSET
    server_type: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        net_id = self.net_id

        mac = self.mac

        status = self.status

        ip = self.ip

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        description = self.description

        confirm_conflict = self.confirm_conflict

        server_type = self.server_type

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "netId": net_id,
                "mac": mac,
                "status": status,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if options is not UNSET:
            field_dict["options"] = options
        if description is not UNSET:
            field_dict["description"] = description
        if confirm_conflict is not UNSET:
            field_dict["confirmConflict"] = confirm_conflict
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if server_mac is not UNSET:
            field_dict["serverMac"] = server_mac
        if server_stack_id is not UNSET:
            field_dict["serverStackId"] = server_stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_dhcp_options import CustomDHCPOptions

        d = dict(src_dict)
        net_id = d.pop("netId")

        mac = d.pop("mac")

        status = d.pop("status")

        ip = d.pop("ip", UNSET)

        _options = d.pop("options", UNSET)
        options: list[CustomDHCPOptions] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CustomDHCPOptions.from_dict(options_item_data)

                options.append(options_item)

        description = d.pop("description", UNSET)

        confirm_conflict = d.pop("confirmConflict", UNSET)

        server_type = d.pop("serverType", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        create_dhcp_reservation_open_api_vo = cls(
            net_id=net_id,
            mac=mac,
            status=status,
            ip=ip,
            options=options,
            description=description,
            confirm_conflict=confirm_conflict,
            server_type=server_type,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
        )

        create_dhcp_reservation_open_api_vo.additional_properties = d
        return create_dhcp_reservation_open_api_vo

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
