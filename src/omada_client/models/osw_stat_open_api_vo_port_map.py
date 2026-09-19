from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.port_stat_vo import PortStatVO


T = TypeVar("T", bound="OswStatOpenApiVOPortMap")


@_attrs_define
class OswStatOpenApiVOPortMap:
    """Port total traffic map"""

    additional_properties: dict[str, PortStatVO] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_stat_vo import PortStatVO

        d = dict(src_dict)
        osw_stat_open_api_vo_port_map = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PortStatVO.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        osw_stat_open_api_vo_port_map.additional_properties = additional_properties
        return osw_stat_open_api_vo_port_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PortStatVO:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: PortStatVO) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
