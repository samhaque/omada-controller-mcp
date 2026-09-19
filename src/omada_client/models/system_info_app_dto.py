from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemInfoAppDTO")


@_attrs_define
class SystemInfoAppDTO:
    """
    Attributes:
        system_description (str | Unset): OLT device system description.
        device_name (str | Unset): Device name should contain 1-32 bits numbers, Upper and lower letters, -@_:/. .
        device_location (str | Unset): Device location should contain 1-32 bits numbers, Upper and lower letters, -@_:/.
            .
        contact_information (str | Unset): Contact information should contain 1-32 bits numbers, Upper and lower
            letters, -@_:/. .
        mac (str | Unset): Mac address
        serial_number (str | Unset): SerialNumber of ONU should contain 12, 13, or 16 characters, in the format
            <XXXXXXXXXXXX> ,<XXXX-XXXXXXXX>,<XXXXXXXXXXXXXXXX>
        hardware_version (str | Unset): Hardware version
        firmware_version (str | Unset): Firmware version
        boot_loader_version (str | Unset): Boot loader version
        system_time (str | Unset): System time
        running_time (int | Unset): Uptime, unit (s).
        jumbo_frame_status (int | Unset): Whether Jumbo Frame is enabled, jumboFrameStatus should be a value as follows:
            1:ENABLE;0:DISABLE.
        sntp_status (int | Unset): Whether to obtain time from the NTP server, sntpStatus should be a value as
            follows:1:ENABLE;0:DISABLE.
        igmp_snooping_status (int | Unset): Whether IGMP Snooping is enabled, igmpSnoopingStatus should be a value as
            follows: 1:ENABLE;0:DISABLE.
        snmp_status (int | Unset): Whether SNMP is enabled, snmpStatus should be a value as follows: 1:ENABLE;0:DISABLE.
        spanning_tree_status (int | Unset): Whether Spanning Tree is enabled, spanningTreeStatus should be a value as
            follows: 1:ENABLE;0:DISABLE.
        dhcp_relay_status (int | Unset): Whether DHCP Relaying is enabled, dhcpRelayStatus should be a value as follows:
            1:ENABLE;0:DISABLE.
        http_server_status (int | Unset): Whether the HTTP Server function is enabled, httpServerStatus should be a
            value as follows: 1:ENABLE;0:DISABLE.
        telnet_status (int | Unset): Whether Telnet is enabled, telnetStatus should be a value as follows:
            1:ENABLE;0:DISABLE.
        ssh_status (int | Unset): Whether SSH is enabled, sshStatus should be a value as follows: 1:ENABLE;0:DISABLE.
    """

    system_description: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_location: str | Unset = UNSET
    contact_information: str | Unset = UNSET
    mac: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    hardware_version: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    boot_loader_version: str | Unset = UNSET
    system_time: str | Unset = UNSET
    running_time: int | Unset = UNSET
    jumbo_frame_status: int | Unset = UNSET
    sntp_status: int | Unset = UNSET
    igmp_snooping_status: int | Unset = UNSET
    snmp_status: int | Unset = UNSET
    spanning_tree_status: int | Unset = UNSET
    dhcp_relay_status: int | Unset = UNSET
    http_server_status: int | Unset = UNSET
    telnet_status: int | Unset = UNSET
    ssh_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_description = self.system_description

        device_name = self.device_name

        device_location = self.device_location

        contact_information = self.contact_information

        mac = self.mac

        serial_number = self.serial_number

        hardware_version = self.hardware_version

        firmware_version = self.firmware_version

        boot_loader_version = self.boot_loader_version

        system_time = self.system_time

        running_time = self.running_time

        jumbo_frame_status = self.jumbo_frame_status

        sntp_status = self.sntp_status

        igmp_snooping_status = self.igmp_snooping_status

        snmp_status = self.snmp_status

        spanning_tree_status = self.spanning_tree_status

        dhcp_relay_status = self.dhcp_relay_status

        http_server_status = self.http_server_status

        telnet_status = self.telnet_status

        ssh_status = self.ssh_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system_description is not UNSET:
            field_dict["systemDescription"] = system_description
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_location is not UNSET:
            field_dict["deviceLocation"] = device_location
        if contact_information is not UNSET:
            field_dict["contactInformation"] = contact_information
        if mac is not UNSET:
            field_dict["mac"] = mac
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if hardware_version is not UNSET:
            field_dict["hardwareVersion"] = hardware_version
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if boot_loader_version is not UNSET:
            field_dict["bootLoaderVersion"] = boot_loader_version
        if system_time is not UNSET:
            field_dict["systemTime"] = system_time
        if running_time is not UNSET:
            field_dict["runningTime"] = running_time
        if jumbo_frame_status is not UNSET:
            field_dict["jumboFrameStatus"] = jumbo_frame_status
        if sntp_status is not UNSET:
            field_dict["sntpStatus"] = sntp_status
        if igmp_snooping_status is not UNSET:
            field_dict["igmpSnoopingStatus"] = igmp_snooping_status
        if snmp_status is not UNSET:
            field_dict["snmpStatus"] = snmp_status
        if spanning_tree_status is not UNSET:
            field_dict["spanningTreeStatus"] = spanning_tree_status
        if dhcp_relay_status is not UNSET:
            field_dict["dhcpRelayStatus"] = dhcp_relay_status
        if http_server_status is not UNSET:
            field_dict["httpServerStatus"] = http_server_status
        if telnet_status is not UNSET:
            field_dict["telnetStatus"] = telnet_status
        if ssh_status is not UNSET:
            field_dict["sshStatus"] = ssh_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        system_description = d.pop("systemDescription", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_location = d.pop("deviceLocation", UNSET)

        contact_information = d.pop("contactInformation", UNSET)

        mac = d.pop("mac", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        hardware_version = d.pop("hardwareVersion", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        boot_loader_version = d.pop("bootLoaderVersion", UNSET)

        system_time = d.pop("systemTime", UNSET)

        running_time = d.pop("runningTime", UNSET)

        jumbo_frame_status = d.pop("jumboFrameStatus", UNSET)

        sntp_status = d.pop("sntpStatus", UNSET)

        igmp_snooping_status = d.pop("igmpSnoopingStatus", UNSET)

        snmp_status = d.pop("snmpStatus", UNSET)

        spanning_tree_status = d.pop("spanningTreeStatus", UNSET)

        dhcp_relay_status = d.pop("dhcpRelayStatus", UNSET)

        http_server_status = d.pop("httpServerStatus", UNSET)

        telnet_status = d.pop("telnetStatus", UNSET)

        ssh_status = d.pop("sshStatus", UNSET)

        system_info_app_dto = cls(
            system_description=system_description,
            device_name=device_name,
            device_location=device_location,
            contact_information=contact_information,
            mac=mac,
            serial_number=serial_number,
            hardware_version=hardware_version,
            firmware_version=firmware_version,
            boot_loader_version=boot_loader_version,
            system_time=system_time,
            running_time=running_time,
            jumbo_frame_status=jumbo_frame_status,
            sntp_status=sntp_status,
            igmp_snooping_status=igmp_snooping_status,
            snmp_status=snmp_status,
            spanning_tree_status=spanning_tree_status,
            dhcp_relay_status=dhcp_relay_status,
            http_server_status=http_server_status,
            telnet_status=telnet_status,
            ssh_status=ssh_status,
        )

        system_info_app_dto.additional_properties = d
        return system_info_app_dto

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
