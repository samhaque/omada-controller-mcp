from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRankingDeviceItemVO")


@_attrs_define
class IncidentRankingDeviceItemVO:
    """Top devices ranked by incident count

    Attributes:
        name (str | Unset): Display name of the device
        mac (str | Unset): MAC address of the device
        model (str | Unset): Device model (e.g. EAP225)
        model_version (str | Unset): Device model version (e.g. 3.0)
        type_ (str | Unset): Device type (e.g. ap, gateway, switch)
        incidents (int | Unset): Number of incidents involving this device
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    incidents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        incidents = self.incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if incidents is not UNSET:
            field_dict["incidents"] = incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        incidents = d.pop("incidents", UNSET)

        incident_ranking_device_item_vo = cls(
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            type_=type_,
            incidents=incidents,
        )

        incident_ranking_device_item_vo.additional_properties = d
        return incident_ranking_device_item_vo

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
