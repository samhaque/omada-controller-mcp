from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stp_mstp_config_open_api_vo import OswStpMstpConfigOpenApiVO
    from ..models.osw_stp_rpvst_vo import OswStpRpvstVO


T = TypeVar("T", bound="SwitchLoopbackControl")


@_attrs_define
class SwitchLoopbackControl:
    """
    Attributes:
        loopback_detect_enable (bool | Unset): LoopbackDetectEnable
        stp (int | Unset): STP should be a value as follows: 0: OFF 1: STP 2: RSTP 3: MSTP 4: RPVST
        priority (int | Unset): Parameter [priority] should be an integer from 0 to 61440 and divisible by 4096.
        hello_time (int | Unset): helloTime should be between 1 and 10.
        max_age (int | Unset): maxAge should be between 6 and 40.
        forward_delay (int | Unset): forwardDelay should be between 4 and 30.
        tx_hold_count (int | Unset): txHoldCount should be between 1 and 20.
        max_hops (int | Unset): maxHops should be between 1 and 40. maxHops is only allowed when the STP type is MSTP.
        mstp (OswStpMstpConfigOpenApiVO | Unset): STP MSTP Config, must not be null when stp is 3.
        rpvst (OswStpRpvstVO | Unset): STP RPVST Config, must not be null when stp is 4.
    """

    loopback_detect_enable: bool | Unset = UNSET
    stp: int | Unset = UNSET
    priority: int | Unset = UNSET
    hello_time: int | Unset = UNSET
    max_age: int | Unset = UNSET
    forward_delay: int | Unset = UNSET
    tx_hold_count: int | Unset = UNSET
    max_hops: int | Unset = UNSET
    mstp: OswStpMstpConfigOpenApiVO | Unset = UNSET
    rpvst: OswStpRpvstVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loopback_detect_enable = self.loopback_detect_enable

        stp = self.stp

        priority = self.priority

        hello_time = self.hello_time

        max_age = self.max_age

        forward_delay = self.forward_delay

        tx_hold_count = self.tx_hold_count

        max_hops = self.max_hops

        mstp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mstp, Unset):
            mstp = self.mstp.to_dict()

        rpvst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rpvst, Unset):
            rpvst = self.rpvst.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if loopback_detect_enable is not UNSET:
            field_dict["loopbackDetectEnable"] = loopback_detect_enable
        if stp is not UNSET:
            field_dict["stp"] = stp
        if priority is not UNSET:
            field_dict["priority"] = priority
        if hello_time is not UNSET:
            field_dict["helloTime"] = hello_time
        if max_age is not UNSET:
            field_dict["maxAge"] = max_age
        if forward_delay is not UNSET:
            field_dict["forwardDelay"] = forward_delay
        if tx_hold_count is not UNSET:
            field_dict["txHoldCount"] = tx_hold_count
        if max_hops is not UNSET:
            field_dict["maxHops"] = max_hops
        if mstp is not UNSET:
            field_dict["mstp"] = mstp
        if rpvst is not UNSET:
            field_dict["rpvst"] = rpvst

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stp_mstp_config_open_api_vo import (
            OswStpMstpConfigOpenApiVO,
        )
        from ..models.osw_stp_rpvst_vo import OswStpRpvstVO

        d = dict(src_dict)
        loopback_detect_enable = d.pop("loopbackDetectEnable", UNSET)

        stp = d.pop("stp", UNSET)

        priority = d.pop("priority", UNSET)

        hello_time = d.pop("helloTime", UNSET)

        max_age = d.pop("maxAge", UNSET)

        forward_delay = d.pop("forwardDelay", UNSET)

        tx_hold_count = d.pop("txHoldCount", UNSET)

        max_hops = d.pop("maxHops", UNSET)

        _mstp = d.pop("mstp", UNSET)
        mstp: OswStpMstpConfigOpenApiVO | Unset
        if isinstance(_mstp, Unset):
            mstp = UNSET
        else:
            mstp = OswStpMstpConfigOpenApiVO.from_dict(_mstp)

        _rpvst = d.pop("rpvst", UNSET)
        rpvst: OswStpRpvstVO | Unset
        if isinstance(_rpvst, Unset):
            rpvst = UNSET
        else:
            rpvst = OswStpRpvstVO.from_dict(_rpvst)

        switch_loopback_control = cls(
            loopback_detect_enable=loopback_detect_enable,
            stp=stp,
            priority=priority,
            hello_time=hello_time,
            max_age=max_age,
            forward_delay=forward_delay,
            tx_hold_count=tx_hold_count,
            max_hops=max_hops,
            mstp=mstp,
            rpvst=rpvst,
        )

        switch_loopback_control.additional_properties = d
        return switch_loopback_control

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
