from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemUsage")


@_attrs_define
class MemUsage:
    """
    Attributes:
        name (str | Unset): Device name
        mac (str | Unset): Device MAC
        mem_usage (int | Unset): Device memory usage such as 60 : 60%
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        type_ (str | Unset): Device type
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    mem_usage: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        mem_usage = self.mem_usage

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
        if mem_usage is not UNSET:
            field_dict["memUsage"] = mem_usage
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

        mem_usage = d.pop("memUsage", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        mem_usage = cls(
            name=name,
            mac=mac,
            mem_usage=mem_usage,
            model=model,
            model_version=model_version,
            type_=type_,
        )

        mem_usage.additional_properties = d
        return mem_usage

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
