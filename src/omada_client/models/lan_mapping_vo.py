from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_port_mapping_vo import LanPortMappingVO


T = TypeVar("T", bound="LanMappingVO")


@_attrs_define
class LanMappingVO:
    """
    Attributes:
        lan_relation (list[LanPortMappingVO] | Unset):
    """

    lan_relation: list[LanPortMappingVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lan_relation: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_relation, Unset):
            lan_relation = []
            for lan_relation_item_data in self.lan_relation:
                lan_relation_item = lan_relation_item_data.to_dict()
                lan_relation.append(lan_relation_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan_relation is not UNSET:
            field_dict["lanRelation"] = lan_relation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_port_mapping_vo import LanPortMappingVO

        d = dict(src_dict)
        _lan_relation = d.pop("lanRelation", UNSET)
        lan_relation: list[LanPortMappingVO] | Unset = UNSET
        if _lan_relation is not UNSET:
            lan_relation = []
            for lan_relation_item_data in _lan_relation:
                lan_relation_item = LanPortMappingVO.from_dict(lan_relation_item_data)

                lan_relation.append(lan_relation_item)

        lan_mapping_vo = cls(
            lan_relation=lan_relation,
        )

        lan_mapping_vo.additional_properties = d
        return lan_mapping_vo

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
