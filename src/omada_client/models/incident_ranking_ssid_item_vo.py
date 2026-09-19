from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRankingSsidItemVO")


@_attrs_define
class IncidentRankingSsidItemVO:
    """Top SSIDs ranked by incident count

    Attributes:
        ssid_name (str | Unset): SSID name
        incidents (int | Unset): Number of incidents associated with this SSID
    """

    ssid_name: str | Unset = UNSET
    incidents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_name = self.ssid_name

        incidents = self.incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid_name is not UNSET:
            field_dict["ssidName"] = ssid_name
        if incidents is not UNSET:
            field_dict["incidents"] = incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssid_name = d.pop("ssidName", UNSET)

        incidents = d.pop("incidents", UNSET)

        incident_ranking_ssid_item_vo = cls(
            ssid_name=ssid_name,
            incidents=incidents,
        )

        incident_ranking_ssid_item_vo.additional_properties = d
        return incident_ranking_ssid_item_vo

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
