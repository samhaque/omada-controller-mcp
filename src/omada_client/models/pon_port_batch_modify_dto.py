from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.pon_port_modify_dto import PonPortModifyDTO


T = TypeVar("T", bound="PonPortBatchModifyDTO")


@_attrs_define
class PonPortBatchModifyDTO:
    """
    Attributes:
        dtos (list[PonPortModifyDTO]):
    """

    dtos: list[PonPortModifyDTO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dtos = []
        for dtos_item_data in self.dtos:
            dtos_item = dtos_item_data.to_dict()
            dtos.append(dtos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dtos": dtos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pon_port_modify_dto import PonPortModifyDTO

        d = dict(src_dict)
        dtos = []
        _dtos = d.pop("dtos")
        for dtos_item_data in _dtos:
            dtos_item = PonPortModifyDTO.from_dict(dtos_item_data)

            dtos.append(dtos_item)

        pon_port_batch_modify_dto = cls(
            dtos=dtos,
        )

        pon_port_batch_modify_dto.additional_properties = d
        return pon_port_batch_modify_dto

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
