from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wan_port_mapping_vo import WanPortMappingVO


T = TypeVar("T", bound="WanMappingVO")


@_attrs_define
class WanMappingVO:
    """
    Attributes:
        wan_relation (list[WanPortMappingVO] | Unset):
        enable_wan_ports (list[str] | Unset):
    """

    wan_relation: list[WanPortMappingVO] | Unset = UNSET
    enable_wan_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_relation: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_relation, Unset):
            wan_relation = []
            for wan_relation_item_data in self.wan_relation:
                wan_relation_item = wan_relation_item_data.to_dict()
                wan_relation.append(wan_relation_item)

        enable_wan_ports: list[str] | Unset = UNSET
        if not isinstance(self.enable_wan_ports, Unset):
            enable_wan_ports = self.enable_wan_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wan_relation is not UNSET:
            field_dict["wanRelation"] = wan_relation
        if enable_wan_ports is not UNSET:
            field_dict["enableWanPorts"] = enable_wan_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_port_mapping_vo import WanPortMappingVO

        d = dict(src_dict)
        _wan_relation = d.pop("wanRelation", UNSET)
        wan_relation: list[WanPortMappingVO] | Unset = UNSET
        if _wan_relation is not UNSET:
            wan_relation = []
            for wan_relation_item_data in _wan_relation:
                wan_relation_item = WanPortMappingVO.from_dict(wan_relation_item_data)

                wan_relation.append(wan_relation_item)

        enable_wan_ports = cast(list[str], d.pop("enableWanPorts", UNSET))

        wan_mapping_vo = cls(
            wan_relation=wan_relation,
            enable_wan_ports=enable_wan_ports,
        )

        wan_mapping_vo.additional_properties = d
        return wan_mapping_vo

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
