from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationUpDownTrafficDetailOpenApiVO")


@_attrs_define
class ApplicationUpDownTrafficDetailOpenApiVO:
    """Application uplink and downlink traffic data.

    Attributes:
        up (int | Unset): Up traffic.
        down (int | Unset): Down traffic.
        up_packet (int | Unset): Number of upstream packets
        down_packet (int | Unset): Number of downstream packets
        application_id (int | Unset): Application ID.
        application_name (str | Unset): Application name, such as: Microsoft Bing, Baidu and Microsoft Services.
    """

    up: int | Unset = UNSET
    down: int | Unset = UNSET
    up_packet: int | Unset = UNSET
    down_packet: int | Unset = UNSET
    application_id: int | Unset = UNSET
    application_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up = self.up

        down = self.down

        up_packet = self.up_packet

        down_packet = self.down_packet

        application_id = self.application_id

        application_name = self.application_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if up is not UNSET:
            field_dict["up"] = up
        if down is not UNSET:
            field_dict["down"] = down
        if up_packet is not UNSET:
            field_dict["upPacket"] = up_packet
        if down_packet is not UNSET:
            field_dict["downPacket"] = down_packet
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        up = d.pop("up", UNSET)

        down = d.pop("down", UNSET)

        up_packet = d.pop("upPacket", UNSET)

        down_packet = d.pop("downPacket", UNSET)

        application_id = d.pop("applicationId", UNSET)

        application_name = d.pop("applicationName", UNSET)

        application_up_down_traffic_detail_open_api_vo = cls(
            up=up,
            down=down,
            up_packet=up_packet,
            down_packet=down_packet,
            application_id=application_id,
            application_name=application_name,
        )

        application_up_down_traffic_detail_open_api_vo.additional_properties = d
        return application_up_down_traffic_detail_open_api_vo

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
