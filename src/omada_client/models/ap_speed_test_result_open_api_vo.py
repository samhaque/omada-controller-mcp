from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApSpeedTestResultOpenApiVO")


@_attrs_define
class ApSpeedTestResultOpenApiVO:
    """Speed measurement results of uplink and downlink devices.

    Attributes:
        role (int | Unset): Uplink or downlink AP for the current AP. The parameter [role] should be a value as
            follows:[0:Uplink; 1:Downlink].
        down_rate (float | Unset): Downlink rate
        up_rate (float | Unset): Uplink rate
        time (int | Unset): Time in milliseconds.
        status (int | Unset): The parameter [status] should be a value as follows:[-2:Device error; -1:System error;
            0:No result; 1:Normal results].
        error_code (int | Unset): This field will only be present if status is an error status.
        error_msg (str | Unset): This field will only be present if status is an error status.
    """

    role: int | Unset = UNSET
    down_rate: float | Unset = UNSET
    up_rate: float | Unset = UNSET
    time: int | Unset = UNSET
    status: int | Unset = UNSET
    error_code: int | Unset = UNSET
    error_msg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        down_rate = self.down_rate

        up_rate = self.up_rate

        time = self.time

        status = self.status

        error_code = self.error_code

        error_msg = self.error_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if down_rate is not UNSET:
            field_dict["downRate"] = down_rate
        if up_rate is not UNSET:
            field_dict["upRate"] = up_rate
        if time is not UNSET:
            field_dict["time"] = time
        if status is not UNSET:
            field_dict["status"] = status
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_msg is not UNSET:
            field_dict["errorMsg"] = error_msg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        role = d.pop("role", UNSET)

        down_rate = d.pop("downRate", UNSET)

        up_rate = d.pop("upRate", UNSET)

        time = d.pop("time", UNSET)

        status = d.pop("status", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        ap_speed_test_result_open_api_vo = cls(
            role=role,
            down_rate=down_rate,
            up_rate=up_rate,
            time=time,
            status=status,
            error_code=error_code,
            error_msg=error_msg,
        )

        ap_speed_test_result_open_api_vo.additional_properties = d
        return ap_speed_test_result_open_api_vo

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
