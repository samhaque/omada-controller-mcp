from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyBriefDevice")


@_attrs_define
class TopologyBriefDevice:
    """Brief device information.

    Attributes:
        type_ (str | Unset): Device type.
        mac (str | Unset): Device mac.
        name (str | Unset): Device name.
        model (str | Unset): Device model.
        model_version (str | Unset): Device modelVersion.
        health_score (int | Unset): Device healthScore.
        ippt (bool | Unset): Odu device in ippt mode or not.
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    health_score: int | Unset = UNSET
    ippt: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        health_score = self.health_score

        ippt = self.ippt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if ippt is not UNSET:
            field_dict["ippt"] = ippt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        health_score = d.pop("healthScore", UNSET)

        ippt = d.pop("ippt", UNSET)

        topology_brief_device = cls(
            type_=type_,
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            health_score=health_score,
            ippt=ippt,
        )

        topology_brief_device.additional_properties = d
        return topology_brief_device

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
