from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRankingClientItemVO")


@_attrs_define
class IncidentRankingClientItemVO:
    """Top clients ranked by incident count

    Attributes:
        name (str | Unset): Display name of the client
        mac (str | Unset): MAC address of the client
        type_ (str | Unset): Device type of the client (e.g. iphone, android, pc)
        manager (bool | Unset): Whether this client is a managed client
        incidents (int | Unset): Number of incidents involving this client
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    type_: str | Unset = UNSET
    manager: bool | Unset = UNSET
    incidents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        type_ = self.type_

        manager = self.manager

        incidents = self.incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if manager is not UNSET:
            field_dict["manager"] = manager
        if incidents is not UNSET:
            field_dict["incidents"] = incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        manager = d.pop("manager", UNSET)

        incidents = d.pop("incidents", UNSET)

        incident_ranking_client_item_vo = cls(
            name=name,
            mac=mac,
            type_=type_,
            manager=manager,
            incidents=incidents,
        )

        incident_ranking_client_item_vo.additional_properties = d
        return incident_ranking_client_item_vo

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
