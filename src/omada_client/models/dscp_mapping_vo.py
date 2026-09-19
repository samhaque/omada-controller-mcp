from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.dscp_mapping_vo_mapping import DscpMappingVOMapping


T = TypeVar("T", bound="DscpMappingVO")


@_attrs_define
class DscpMappingVO:
    """
    Attributes:
        mapping (DscpMappingVOMapping): The Queue-DSCP mapping map. The key corresponds to the queue and the value
            corresponds to the DSCP value list
    """

    mapping: DscpMappingVOMapping
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mapping = self.mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mapping": mapping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dscp_mapping_vo_mapping import (
            DscpMappingVOMapping,
        )

        d = dict(src_dict)
        mapping = DscpMappingVOMapping.from_dict(d.pop("mapping"))

        dscp_mapping_vo = cls(
            mapping=mapping,
        )

        dscp_mapping_vo.additional_properties = d
        return dscp_mapping_vo

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
