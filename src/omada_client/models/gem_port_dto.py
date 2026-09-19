from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.gem_port_dto_encrypt import GemPortDTOEncrypt
from ..types import UNSET, Unset

T = TypeVar("T", bound="GemPortDTO")


@_attrs_define
class GemPortDTO:
    """
    Attributes:
        gem_port_id (int): Gem port ID should be within the range of 1 to 1023
        tcont_id (int): The ID of the T-cont to which the Gem Port is bound. TcontId should be s current existing T-cont
            ID.
        encrypt (GemPortDTOEncrypt): Whether to enable data encryption feature. Encrypt should be a value as follows:
            ENABLE;DISABLE. Default value: DISABLE.
        line_profile_id (int | Unset): The ID of the associated Line Profile,lineProfile should be within the range of 1
            to 512.
        is_in_use (bool | Unset): Whether the Gem Port is in use: if it is in use, deletion is not allowed. true
            indicates it is in use, while false indicates it is not in use. This field should not be provided.
        gem_mapping_id (list[int] | Unset): Gem Mapping Id using the gem port should be null
    """

    gem_port_id: int
    tcont_id: int
    encrypt: GemPortDTOEncrypt
    line_profile_id: int | Unset = UNSET
    is_in_use: bool | Unset = UNSET
    gem_mapping_id: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gem_port_id = self.gem_port_id

        tcont_id = self.tcont_id

        encrypt = self.encrypt.value

        line_profile_id = self.line_profile_id

        is_in_use = self.is_in_use

        gem_mapping_id: list[int] | Unset = UNSET
        if not isinstance(self.gem_mapping_id, Unset):
            gem_mapping_id = self.gem_mapping_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gemPortId": gem_port_id,
                "tcontId": tcont_id,
                "encrypt": encrypt,
            }
        )
        if line_profile_id is not UNSET:
            field_dict["lineProfileId"] = line_profile_id
        if is_in_use is not UNSET:
            field_dict["isInUse"] = is_in_use
        if gem_mapping_id is not UNSET:
            field_dict["gemMappingId"] = gem_mapping_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gem_port_id = d.pop("gemPortId")

        tcont_id = d.pop("tcontId")

        encrypt = GemPortDTOEncrypt(d.pop("encrypt"))

        line_profile_id = d.pop("lineProfileId", UNSET)

        is_in_use = d.pop("isInUse", UNSET)

        gem_mapping_id = cast(list[int], d.pop("gemMappingId", UNSET))

        gem_port_dto = cls(
            gem_port_id=gem_port_id,
            tcont_id=tcont_id,
            encrypt=encrypt,
            line_profile_id=line_profile_id,
            is_in_use=is_in_use,
            gem_mapping_id=gem_mapping_id,
        )

        gem_port_dto.additional_properties = d
        return gem_port_dto

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
