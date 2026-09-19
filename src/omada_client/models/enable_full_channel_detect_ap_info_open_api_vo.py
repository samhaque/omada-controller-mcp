from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnableFullChannelDetectApInfoOpenApiVO")


@_attrs_define
class EnableFullChannelDetectApInfoOpenApiVO:
    """
    Attributes:
        mac (str | Unset): Mac address
        name (str | Unset): Default uses the MAC address as the name.
        model (str | Unset): Model, such as EAP225.
        model_version (str | Unset): Model version of device,for example:3.0
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        ip (str | Unset): Ip address,such as 192.168.0.105
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        version (str | Unset): Software version, such as "2.5.0," extracted from DeviceDO.firmwareVersion - "2.5.0 Build
            20190118 Rel. 64821."
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
        uptime_long (int | Unset): Runtime duration, in seconds (s).
        wireless_linked (bool | Unset): Whether the device is wireless linked.
        scan_status (int | Unset): Scan Status of device,status should be a value as follows:  0:Not Scanned, 1:Spectrum
            Scanning, 2:RFScanning, 3:packet capturing, 4:RFPlanning;
        power_mode_list (list[int] | Unset): Indicating the power supply modes for AP devices across frequency bands,
            with array indices corresponding to the frequency bands: 0: 2.4G 1: 5G/5G1 2: 5G2 3: 6G. The corresponding
            values for power supply modes are: 0: Normal operation 1: Power limited 2: Frequency band disabled
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    ip: str | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    version: str | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    uptime_long: int | Unset = UNSET
    wireless_linked: bool | Unset = UNSET
    scan_status: int | Unset = UNSET
    power_mode_list: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        ip = self.ip

        status_category = self.status_category

        status = self.status

        version = self.version

        added_in_advanced = self.added_in_advanced

        uptime_long = self.uptime_long

        wireless_linked = self.wireless_linked

        scan_status = self.scan_status

        power_mode_list: list[int] | Unset = UNSET
        if not isinstance(self.power_mode_list, Unset):
            power_mode_list = self.power_mode_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if uptime_long is not UNSET:
            field_dict["uptimeLong"] = uptime_long
        if wireless_linked is not UNSET:
            field_dict["wirelessLinked"] = wireless_linked
        if scan_status is not UNSET:
            field_dict["scanStatus"] = scan_status
        if power_mode_list is not UNSET:
            field_dict["powerModeList"] = power_mode_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        ip = d.pop("ip", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        version = d.pop("version", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        uptime_long = d.pop("uptimeLong", UNSET)

        wireless_linked = d.pop("wirelessLinked", UNSET)

        scan_status = d.pop("scanStatus", UNSET)

        power_mode_list = cast(list[int], d.pop("powerModeList", UNSET))

        enable_full_channel_detect_ap_info_open_api_vo = cls(
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            type_=type_,
            ip=ip,
            status_category=status_category,
            status=status,
            version=version,
            added_in_advanced=added_in_advanced,
            uptime_long=uptime_long,
            wireless_linked=wireless_linked,
            scan_status=scan_status,
            power_mode_list=power_mode_list,
        )

        enable_full_channel_detect_ap_info_open_api_vo.additional_properties = d
        return enable_full_channel_detect_ap_info_open_api_vo

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
