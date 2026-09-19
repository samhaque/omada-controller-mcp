from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QosBwcDetailOpenApiVO")


@_attrs_define
class QosBwcDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): The ID of Bandwidth Control rule.
        wan (str | Unset): The ID of WAN port to which this Bandwidth Control applies.
        status (bool | Unset): The status of Bandwidth Control rule, valid values are true or false.
        udp_bandwidth_ctrl (bool | Unset): The UDP Bandwidth Control of Bandwidth Control rule, valid values are true or
            false.
        udp_ratio (int | Unset): The Limited Bandwidth Ratio of Bandwidth Control rule. It should be within the range of
            0-100 when parameter [udpBandwidthCtrl] is true.
        out_prioritization (bool | Unset): The Outbound TCP ACK Prioritize of Bandwidth Control rule, valid values are
            true or false.
        direction (int | Unset): The direction value selected in the Direction configuration should be a value as
            follows: 0: Inbound; 1: Outbound; 2: Both.
        in_bandwidth (int | Unset): The Inbound Bandwidth of Bandwidth Control rule should be within the range of
            100-1000000.
        out_bandwidth (int | Unset): The Outbound Bandwidth of Bandwidth Control rule should be within the range of
            100-1000000.
        class_ratio (list[int] | Unset): The ratio of class type, value's format is [class1 ratio, class2 ratio, class3
            ratio, others ratio].
    """

    id: str | Unset = UNSET
    wan: str | Unset = UNSET
    status: bool | Unset = UNSET
    udp_bandwidth_ctrl: bool | Unset = UNSET
    udp_ratio: int | Unset = UNSET
    out_prioritization: bool | Unset = UNSET
    direction: int | Unset = UNSET
    in_bandwidth: int | Unset = UNSET
    out_bandwidth: int | Unset = UNSET
    class_ratio: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        wan = self.wan

        status = self.status

        udp_bandwidth_ctrl = self.udp_bandwidth_ctrl

        udp_ratio = self.udp_ratio

        out_prioritization = self.out_prioritization

        direction = self.direction

        in_bandwidth = self.in_bandwidth

        out_bandwidth = self.out_bandwidth

        class_ratio: list[int] | Unset = UNSET
        if not isinstance(self.class_ratio, Unset):
            class_ratio = self.class_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if wan is not UNSET:
            field_dict["wan"] = wan
        if status is not UNSET:
            field_dict["status"] = status
        if udp_bandwidth_ctrl is not UNSET:
            field_dict["udpBandwidthCtrl"] = udp_bandwidth_ctrl
        if udp_ratio is not UNSET:
            field_dict["udpRatio"] = udp_ratio
        if out_prioritization is not UNSET:
            field_dict["outPrioritization"] = out_prioritization
        if direction is not UNSET:
            field_dict["direction"] = direction
        if in_bandwidth is not UNSET:
            field_dict["inBandwidth"] = in_bandwidth
        if out_bandwidth is not UNSET:
            field_dict["outBandwidth"] = out_bandwidth
        if class_ratio is not UNSET:
            field_dict["classRatio"] = class_ratio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        wan = d.pop("wan", UNSET)

        status = d.pop("status", UNSET)

        udp_bandwidth_ctrl = d.pop("udpBandwidthCtrl", UNSET)

        udp_ratio = d.pop("udpRatio", UNSET)

        out_prioritization = d.pop("outPrioritization", UNSET)

        direction = d.pop("direction", UNSET)

        in_bandwidth = d.pop("inBandwidth", UNSET)

        out_bandwidth = d.pop("outBandwidth", UNSET)

        class_ratio = cast(list[int], d.pop("classRatio", UNSET))

        qos_bwc_detail_open_api_vo = cls(
            id=id,
            wan=wan,
            status=status,
            udp_bandwidth_ctrl=udp_bandwidth_ctrl,
            udp_ratio=udp_ratio,
            out_prioritization=out_prioritization,
            direction=direction,
            in_bandwidth=in_bandwidth,
            out_bandwidth=out_bandwidth,
            class_ratio=class_ratio,
        )

        qos_bwc_detail_open_api_vo.additional_properties = d
        return qos_bwc_detail_open_api_vo

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
