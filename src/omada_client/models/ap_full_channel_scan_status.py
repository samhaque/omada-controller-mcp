from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApFullChannelScanStatus")


@_attrs_define
class ApFullChannelScanStatus:
    """
    Attributes:
        status (int | Unset): Full channel detection status of the AP device. Status should be a value as follows: 0: In
            the unscanned state but the scan result is displayed;1: In the unscanned state, and there is no scan result;3:
            Scanning.
        wifi_interf_status (int | Unset): Wifi interference detection status of the AP device. Status should be a value
            as follows: 0: In the unscanned state but the scan result is displayed;1: In the unscanned state, and there is
            no scan result;3: Scanning.
        interf_status (int | Unset): Interference detection status of the AP device. Status should be a value as
            follows: 0: In the unscanned state but the scan result is displayed;1: In the unscanned state, and there is no
            scan result;3: Scanning.
        channel_load_status (int | Unset): Channel load detection status of the AP device. Status should be a value as
            follows: 0: In the unscanned state but the scan result is displayed;1: In the unscanned state, and there is no
            scan result;3: Scanning.
        last_seen (int | Unset): The last time full channel detection was triggered.
        from_global (bool | Unset): If the status from batch full channel detect
    """

    status: int | Unset = UNSET
    wifi_interf_status: int | Unset = UNSET
    interf_status: int | Unset = UNSET
    channel_load_status: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    from_global: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        wifi_interf_status = self.wifi_interf_status

        interf_status = self.interf_status

        channel_load_status = self.channel_load_status

        last_seen = self.last_seen

        from_global = self.from_global

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if wifi_interf_status is not UNSET:
            field_dict["wifiInterfStatus"] = wifi_interf_status
        if interf_status is not UNSET:
            field_dict["interfStatus"] = interf_status
        if channel_load_status is not UNSET:
            field_dict["channelLoadStatus"] = channel_load_status
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if from_global is not UNSET:
            field_dict["fromGlobal"] = from_global

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        wifi_interf_status = d.pop("wifiInterfStatus", UNSET)

        interf_status = d.pop("interfStatus", UNSET)

        channel_load_status = d.pop("channelLoadStatus", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        from_global = d.pop("fromGlobal", UNSET)

        ap_full_channel_scan_status = cls(
            status=status,
            wifi_interf_status=wifi_interf_status,
            interf_status=interf_status,
            channel_load_status=channel_load_status,
            last_seen=last_seen,
            from_global=from_global,
        )

        ap_full_channel_scan_status.additional_properties = d
        return ap_full_channel_scan_status

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
