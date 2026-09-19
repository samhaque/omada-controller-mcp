from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QosBwcEditOpenApiVO")


@_attrs_define
class QosBwcEditOpenApiVO:
    """
    Attributes:
        status (bool): The status of Bandwidth Control rule, valid values is true or false.
        udp_bandwidth_ctrl (bool): The UDP Bandwidth Control of Bandwidth Control rule, valid values is true or false.
        out_prioritization (bool): The Outbound TCP ACK Prioritize of Bandwidth Control rule, valid values is true or
            false.
        direction (int): The direction value selected in the Direction configuration should be a value as follows: 0:
            Inbound; 1: Outbound; 2: Both.
        in_bandwidth (int): The Inbound Bandwidth of Bandwidth Control rule should be within the range of 100-1000000.
        out_bandwidth (int): The Outbound Bandwidth of Bandwidth Control rule should be within the range of 100-1000000.
        class_ratio (list[int]): The ratio of class type, value's format is [class1 ratio, class2 ratio, class3 ratio,
            others ratio].
        wan (str | Unset): The wan of Bandwidth Control rule.
        udp_ratio (int | Unset): The Limited Bandwidth Ratio of Bandwidth Control rule. It should be within the range of
            0-100 when parameter [udpBandwidthCtrl] is true.
    """

    status: bool
    udp_bandwidth_ctrl: bool
    out_prioritization: bool
    direction: int
    in_bandwidth: int
    out_bandwidth: int
    class_ratio: list[int]
    wan: str | Unset = UNSET
    udp_ratio: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        udp_bandwidth_ctrl = self.udp_bandwidth_ctrl

        out_prioritization = self.out_prioritization

        direction = self.direction

        in_bandwidth = self.in_bandwidth

        out_bandwidth = self.out_bandwidth

        class_ratio = self.class_ratio

        wan = self.wan

        udp_ratio = self.udp_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "udpBandwidthCtrl": udp_bandwidth_ctrl,
                "outPrioritization": out_prioritization,
                "direction": direction,
                "inBandwidth": in_bandwidth,
                "outBandwidth": out_bandwidth,
                "classRatio": class_ratio,
            }
        )
        if wan is not UNSET:
            field_dict["wan"] = wan
        if udp_ratio is not UNSET:
            field_dict["udpRatio"] = udp_ratio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        udp_bandwidth_ctrl = d.pop("udpBandwidthCtrl")

        out_prioritization = d.pop("outPrioritization")

        direction = d.pop("direction")

        in_bandwidth = d.pop("inBandwidth")

        out_bandwidth = d.pop("outBandwidth")

        class_ratio = cast(list[int], d.pop("classRatio"))

        wan = d.pop("wan", UNSET)

        udp_ratio = d.pop("udpRatio", UNSET)

        qos_bwc_edit_open_api_vo = cls(
            status=status,
            udp_bandwidth_ctrl=udp_bandwidth_ctrl,
            out_prioritization=out_prioritization,
            direction=direction,
            in_bandwidth=in_bandwidth,
            out_bandwidth=out_bandwidth,
            class_ratio=class_ratio,
            wan=wan,
            udp_ratio=udp_ratio,
        )

        qos_bwc_edit_open_api_vo.additional_properties = d
        return qos_bwc_edit_open_api_vo

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
