from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgPortInfoVO")


@_attrs_define
class OsgPortInfoVO:
    """Gateway port info list

    Attributes:
        port (int | Unset):
        name (str | Unset):
        type_ (int | Unset):
        physical_type (int | Unset):
        mode (int | Unset):
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    physical_type: int | Unset = UNSET
    mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        type_ = self.type_

        physical_type = self.physical_type

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if physical_type is not UNSET:
            field_dict["physicalType"] = physical_type
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        physical_type = d.pop("physicalType", UNSET)

        mode = d.pop("mode", UNSET)

        osg_port_info_vo = cls(
            port=port,
            name=name,
            type_=type_,
            physical_type=physical_type,
            mode=mode,
        )

        osg_port_info_vo.additional_properties = d
        return osg_port_info_vo

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
