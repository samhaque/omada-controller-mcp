from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CpuUsage")


@_attrs_define
class CpuUsage:
    """
    Attributes:
        name (str | Unset): Device name
        mac (str | Unset): Device MAC
        cpu_util (int | Unset): Device CPU utilization
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        type_ (str | Unset): Device type
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    cpu_util: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        cpu_util = self.cpu_util

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        cpu_usage = cls(
            name=name,
            mac=mac,
            cpu_util=cpu_util,
            model=model,
            model_version=model_version,
            type_=type_,
        )

        cpu_usage.additional_properties = d
        return cpu_usage

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
