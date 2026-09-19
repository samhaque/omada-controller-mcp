from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QosBwcWanInfoOpenApiVO")


@_attrs_define
class QosBwcWanInfoOpenApiVO:
    """
    Attributes:
        id (str | Unset): WAN port ID.
        name (str | Unset): WAN port name.
        configured (bool | Unset): Whether the port has been configured with QoS Bandwidth Control.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    configured: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        configured = self.configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if configured is not UNSET:
            field_dict["configured"] = configured

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        configured = d.pop("configured", UNSET)

        qos_bwc_wan_info_open_api_vo = cls(
            id=id,
            name=name,
            configured=configured,
        )

        qos_bwc_wan_info_open_api_vo.additional_properties = d
        return qos_bwc_wan_info_open_api_vo

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
