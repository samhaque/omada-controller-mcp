from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QosBwcOpenApiVO")


@_attrs_define
class QosBwcOpenApiVO:
    """
    Attributes:
        wan (str): The ID of WAN port to which this Bandwidth Control applies. Each WAN port can only be configured with
            one rule. WAN ID can be obtained from 'Get WAN ports info for Gateway QoS' interface.
        status (bool): The status of Bandwidth Control rule, valid values are true or false.
        udp_bandwidth_ctrl (bool): The UDP Bandwidth Control of Bandwidth Control rule, valid values are true or false.
        out_prioritization (bool): The Outbound TCP ACK Prioritize of Bandwidth Control rule, valid values are true or
            false.
        direction (int): The direction value selected in the Direction configuration should be a value as follows: 0:
            Inbound; 1: Outbound; 2: Both.
        in_bandwidth (int): The Inbound Bandwidth of Bandwidth Control rule should be within the range of 100-1000000.
        out_bandwidth (int): The Outbound Bandwidth of Bandwidth Control rule should be within the range of 100-1000000.
        class_ratio (list[int]): The ratio of class type, value's format is [class1 ratio, class2 ratio, class3 ratio,
            others ratio], and the total sum should be 100.
        udp_ratio (int | Unset): The Limited Bandwidth Ratio of Bandwidth Control rule. It should be within the range of
            0-100 when parameter [udpBandwidthCtrl] is true.
    """

    wan: str
    status: bool
    udp_bandwidth_ctrl: bool
    out_prioritization: bool
    direction: int
    in_bandwidth: int
    out_bandwidth: int
    class_ratio: list[int]
    udp_ratio: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan = self.wan

        status = self.status

        udp_bandwidth_ctrl = self.udp_bandwidth_ctrl

        out_prioritization = self.out_prioritization

        direction = self.direction

        in_bandwidth = self.in_bandwidth

        out_bandwidth = self.out_bandwidth

        class_ratio = self.class_ratio

        udp_ratio = self.udp_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wan": wan,
                "status": status,
                "udpBandwidthCtrl": udp_bandwidth_ctrl,
                "outPrioritization": out_prioritization,
                "direction": direction,
                "inBandwidth": in_bandwidth,
                "outBandwidth": out_bandwidth,
                "classRatio": class_ratio,
            }
        )
        if udp_ratio is not UNSET:
            field_dict["udpRatio"] = udp_ratio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wan = d.pop("wan")

        status = d.pop("status")

        udp_bandwidth_ctrl = d.pop("udpBandwidthCtrl")

        out_prioritization = d.pop("outPrioritization")

        direction = d.pop("direction")

        in_bandwidth = d.pop("inBandwidth")

        out_bandwidth = d.pop("outBandwidth")

        class_ratio = cast(list[int], d.pop("classRatio"))

        udp_ratio = d.pop("udpRatio", UNSET)

        qos_bwc_open_api_vo = cls(
            wan=wan,
            status=status,
            udp_bandwidth_ctrl=udp_bandwidth_ctrl,
            out_prioritization=out_prioritization,
            direction=direction,
            in_bandwidth=in_bandwidth,
            out_bandwidth=out_bandwidth,
            class_ratio=class_ratio,
            udp_ratio=udp_ratio,
        )

        qos_bwc_open_api_vo.additional_properties = d
        return qos_bwc_open_api_vo

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
