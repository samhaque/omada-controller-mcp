from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpeedTestV2ResultItemVO")


@_attrs_define
class SpeedTestV2ResultItemVO:
    """
    Attributes:
        port_id (int | Unset): The id of physical wan port.
        virtual_wan_entry_id (int | Unset): The entry id of virtual wan.
        time (int | Unset): Time of speed test.
        port_name (str | Unset): The name of wan or virtual wan.
        isp (str | Unset): Name of isp.
        server_name (str | Unset): Name of speed test server.
        server_location (str | Unset): Location of speed test server.
        status (int | Unset): The status of this wan port speed test result.
        latency (int | Unset): The latency of this wan port speed test result.
        down (int | Unset): The download speed of this wan port speed test result.
        up (int | Unset): The upload speed of this wan port speed test result.
        progress (float | Unset): The progress of this wan port speed test result.
    """

    port_id: int | Unset = UNSET
    virtual_wan_entry_id: int | Unset = UNSET
    time: int | Unset = UNSET
    port_name: str | Unset = UNSET
    isp: str | Unset = UNSET
    server_name: str | Unset = UNSET
    server_location: str | Unset = UNSET
    status: int | Unset = UNSET
    latency: int | Unset = UNSET
    down: int | Unset = UNSET
    up: int | Unset = UNSET
    progress: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        virtual_wan_entry_id = self.virtual_wan_entry_id

        time = self.time

        port_name = self.port_name

        isp = self.isp

        server_name = self.server_name

        server_location = self.server_location

        status = self.status

        latency = self.latency

        down = self.down

        up = self.up

        progress = self.progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if virtual_wan_entry_id is not UNSET:
            field_dict["virtualWanEntryId"] = virtual_wan_entry_id
        if time is not UNSET:
            field_dict["time"] = time
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if isp is not UNSET:
            field_dict["isp"] = isp
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if server_location is not UNSET:
            field_dict["serverLocation"] = server_location
        if status is not UNSET:
            field_dict["status"] = status
        if latency is not UNSET:
            field_dict["latency"] = latency
        if down is not UNSET:
            field_dict["down"] = down
        if up is not UNSET:
            field_dict["up"] = up
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        virtual_wan_entry_id = d.pop("virtualWanEntryId", UNSET)

        time = d.pop("time", UNSET)

        port_name = d.pop("portName", UNSET)

        isp = d.pop("isp", UNSET)

        server_name = d.pop("serverName", UNSET)

        server_location = d.pop("serverLocation", UNSET)

        status = d.pop("status", UNSET)

        latency = d.pop("latency", UNSET)

        down = d.pop("down", UNSET)

        up = d.pop("up", UNSET)

        progress = d.pop("progress", UNSET)

        speed_test_v2_result_item_vo = cls(
            port_id=port_id,
            virtual_wan_entry_id=virtual_wan_entry_id,
            time=time,
            port_name=port_name,
            isp=isp,
            server_name=server_name,
            server_location=server_location,
            status=status,
            latency=latency,
            down=down,
            up=up,
            progress=progress,
        )

        speed_test_v2_result_item_vo.additional_properties = d
        return speed_test_v2_result_item_vo

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
