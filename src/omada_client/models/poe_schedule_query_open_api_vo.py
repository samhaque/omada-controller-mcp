from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poe_schedule_query_open_api_vo_poe_ports_map import (
        PoeScheduleQueryOpenApiVOPoePortsMap,
    )


T = TypeVar("T", bound="PoeScheduleQueryOpenApiVO")


@_attrs_define
class PoeScheduleQueryOpenApiVO:
    """
    Attributes:
        name (str): PoE Schedule Name should contain 1 to 128 characters.
        status (bool): PoE Schedule Status.
        turn_on_time (str): Time Range ID, cannot be empty.
        poe_ports_map (PoeScheduleQueryOpenApiVOPoePortsMap): Key:Mac("String"), Value:Set of Ports("Integer")
        id (str | Unset): PoE Schedule Individual ID.
        site_id (str | Unset): Site ID
        next_execute (int | Unset): Show PoE Schedule next execution timestamp.
        not_in_dst (bool | Unset): When notInDst is true, not displayed in DST.
    """

    name: str
    status: bool
    turn_on_time: str
    poe_ports_map: PoeScheduleQueryOpenApiVOPoePortsMap
    id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    next_execute: int | Unset = UNSET
    not_in_dst: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        turn_on_time = self.turn_on_time

        poe_ports_map = self.poe_ports_map.to_dict()

        id = self.id

        site_id = self.site_id

        next_execute = self.next_execute

        not_in_dst = self.not_in_dst

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "turnOnTime": turn_on_time,
                "poePortsMap": poe_ports_map,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if next_execute is not UNSET:
            field_dict["nextExecute"] = next_execute
        if not_in_dst is not UNSET:
            field_dict["notInDst"] = not_in_dst

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.poe_schedule_query_open_api_vo_poe_ports_map import (
            PoeScheduleQueryOpenApiVOPoePortsMap,
        )

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        turn_on_time = d.pop("turnOnTime")

        poe_ports_map = PoeScheduleQueryOpenApiVOPoePortsMap.from_dict(
            d.pop("poePortsMap")
        )

        id = d.pop("id", UNSET)

        site_id = d.pop("siteId", UNSET)

        next_execute = d.pop("nextExecute", UNSET)

        not_in_dst = d.pop("notInDst", UNSET)

        poe_schedule_query_open_api_vo = cls(
            name=name,
            status=status,
            turn_on_time=turn_on_time,
            poe_ports_map=poe_ports_map,
            id=id,
            site_id=site_id,
            next_execute=next_execute,
            not_in_dst=not_in_dst,
        )

        poe_schedule_query_open_api_vo.additional_properties = d
        return poe_schedule_query_open_api_vo

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
