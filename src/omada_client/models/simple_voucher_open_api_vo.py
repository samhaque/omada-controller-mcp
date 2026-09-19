from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleVoucherOpenApiVO")


@_attrs_define
class SimpleVoucherOpenApiVO:
    """Voucher pagination data of the voucher group

    Attributes:
        id (str | Unset): Voucher ID
        code (str | Unset): Voucher code
        status (int | Unset): Voucher status. It should be a value as follows: 0: unused, 1: in use, 2: expired
        traffic_used (int | Unset): Used traffic of the voucher, unit: Byte
        traffic_unused (int | Unset): Unused traffic of the voucher, unit: Byte
        traffic_limit (int | Unset): Traffic limit in MB. It should be within the range of 1–10485760
        traffic_limit_frequency (int | Unset): Frequency of traffic limit should be a value as follows: 0: total; 1:
            daily; 2: weekly; 3: monthly.
        down_limit (int | Unset): Downlink speed limit in Kbps. The value of limit should be within the range of
            0–10485760.
        up_limit (int | Unset): Uplink speed limit in Kbps. The value of limit should be within the range of 0–10485760.
        start_time (int | Unset): The expiration date of the voucher, unit: MS
        time_used_sec (int | Unset): Used duration of voucher, unit: Second
        time_left_sec (int | Unset): Left duration of voucher, unit: Second
        timing_by_client_usage (bool | Unset): Whether the voucher is timing by usage and duration type is client
            duration. When this parameter is true, will not display parameter [timeUsedSec] and [timeLeftSec]
    """

    id: str | Unset = UNSET
    code: str | Unset = UNSET
    status: int | Unset = UNSET
    traffic_used: int | Unset = UNSET
    traffic_unused: int | Unset = UNSET
    traffic_limit: int | Unset = UNSET
    traffic_limit_frequency: int | Unset = UNSET
    down_limit: int | Unset = UNSET
    up_limit: int | Unset = UNSET
    start_time: int | Unset = UNSET
    time_used_sec: int | Unset = UNSET
    time_left_sec: int | Unset = UNSET
    timing_by_client_usage: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        code = self.code

        status = self.status

        traffic_used = self.traffic_used

        traffic_unused = self.traffic_unused

        traffic_limit = self.traffic_limit

        traffic_limit_frequency = self.traffic_limit_frequency

        down_limit = self.down_limit

        up_limit = self.up_limit

        start_time = self.start_time

        time_used_sec = self.time_used_sec

        time_left_sec = self.time_left_sec

        timing_by_client_usage = self.timing_by_client_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if traffic_used is not UNSET:
            field_dict["trafficUsed"] = traffic_used
        if traffic_unused is not UNSET:
            field_dict["trafficUnused"] = traffic_unused
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if time_used_sec is not UNSET:
            field_dict["timeUsedSec"] = time_used_sec
        if time_left_sec is not UNSET:
            field_dict["timeLeftSec"] = time_left_sec
        if timing_by_client_usage is not UNSET:
            field_dict["timingByClientUsage"] = timing_by_client_usage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        status = d.pop("status", UNSET)

        traffic_used = d.pop("trafficUsed", UNSET)

        traffic_unused = d.pop("trafficUnused", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        start_time = d.pop("startTime", UNSET)

        time_used_sec = d.pop("timeUsedSec", UNSET)

        time_left_sec = d.pop("timeLeftSec", UNSET)

        timing_by_client_usage = d.pop("timingByClientUsage", UNSET)

        simple_voucher_open_api_vo = cls(
            id=id,
            code=code,
            status=status,
            traffic_used=traffic_used,
            traffic_unused=traffic_unused,
            traffic_limit=traffic_limit,
            traffic_limit_frequency=traffic_limit_frequency,
            down_limit=down_limit,
            up_limit=up_limit,
            start_time=start_time,
            time_used_sec=time_used_sec,
            time_left_sec=time_left_sec,
            timing_by_client_usage=timing_by_client_usage,
        )

        simple_voucher_open_api_vo.additional_properties = d
        return simple_voucher_open_api_vo

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
