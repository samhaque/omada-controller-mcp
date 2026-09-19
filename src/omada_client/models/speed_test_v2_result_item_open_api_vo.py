from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpeedTestV2ResultItemOpenApiVO")


@_attrs_define
class SpeedTestV2ResultItemOpenApiVO:
    """
    Attributes:
        port_id (int | Unset): The id of physical wan port.
        virtual_wan_entry_id (int | Unset): The entry id of virtual wan.
        time (int | Unset): Time of speed test.
        isp (str | Unset): Name of isp.
        status (int | Unset): The status of this wan port speed test result.
        server_name (str | Unset): Name of speed test server.
        server_location (str | Unset): Location of speed test server.
        latency (int | Unset): The latency of this wan port speed test result.
        down (int | Unset): The download speed of this wan port speed test result.
        up (int | Unset): The upload speed of this wan port speed test result.
    """

    port_id: int | Unset = UNSET
    virtual_wan_entry_id: int | Unset = UNSET
    time: int | Unset = UNSET
    isp: str | Unset = UNSET
    status: int | Unset = UNSET
    server_name: str | Unset = UNSET
    server_location: str | Unset = UNSET
    latency: int | Unset = UNSET
    down: int | Unset = UNSET
    up: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        virtual_wan_entry_id = self.virtual_wan_entry_id

        time = self.time

        isp = self.isp

        status = self.status

        server_name = self.server_name

        server_location = self.server_location

        latency = self.latency

        down = self.down

        up = self.up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if virtual_wan_entry_id is not UNSET:
            field_dict["virtualWanEntryId"] = virtual_wan_entry_id
        if time is not UNSET:
            field_dict["time"] = time
        if isp is not UNSET:
            field_dict["isp"] = isp
        if status is not UNSET:
            field_dict["status"] = status
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if server_location is not UNSET:
            field_dict["serverLocation"] = server_location
        if latency is not UNSET:
            field_dict["latency"] = latency
        if down is not UNSET:
            field_dict["down"] = down
        if up is not UNSET:
            field_dict["up"] = up

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        virtual_wan_entry_id = d.pop("virtualWanEntryId", UNSET)

        time = d.pop("time", UNSET)

        isp = d.pop("isp", UNSET)

        status = d.pop("status", UNSET)

        server_name = d.pop("serverName", UNSET)

        server_location = d.pop("serverLocation", UNSET)

        latency = d.pop("latency", UNSET)

        down = d.pop("down", UNSET)

        up = d.pop("up", UNSET)

        speed_test_v2_result_item_open_api_vo = cls(
            port_id=port_id,
            virtual_wan_entry_id=virtual_wan_entry_id,
            time=time,
            isp=isp,
            status=status,
            server_name=server_name,
            server_location=server_location,
            latency=latency,
            down=down,
            up=up,
        )

        speed_test_v2_result_item_open_api_vo.additional_properties = d
        return speed_test_v2_result_item_open_api_vo

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
