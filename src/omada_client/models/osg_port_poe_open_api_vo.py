from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgPortPoeOpenApiVO")


@_attrs_define
class OsgPortPoeOpenApiVO:
    """Port Poe setting list.

    Attributes:
        port_id (int | Unset): The number of the port.
        port_name (str | Unset): The name of the port.
        enable (bool | Unset): The port enabled or not.
    """

    port_id: int | Unset = UNSET
    port_name: str | Unset = UNSET
    enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        port_name = self.port_name

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        port_name = d.pop("portName", UNSET)

        enable = d.pop("enable", UNSET)

        osg_port_poe_open_api_vo = cls(
            port_id=port_id,
            port_name=port_name,
            enable=enable,
        )

        osg_port_poe_open_api_vo.additional_properties = d
        return osg_port_poe_open_api_vo

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
