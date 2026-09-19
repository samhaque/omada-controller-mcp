from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.gem_port_modify_dto_encrypt import GemPortModifyDTOEncrypt
from ..types import UNSET, Unset

T = TypeVar("T", bound="GemPortModifyDTO")


@_attrs_define
class GemPortModifyDTO:
    """
    Attributes:
        gem_port_id (int): Gem port ID should be within the range of 1 to 1023
        line_profile_id (int | Unset): The ID of the associated Line Profile,lineProfile should be within the range of 1
            to 512.
        tcont_id (int | Unset): The ID of the T-cont to which the Gem Port is bound. TcontId should be a current
            existing T-cont ID.
        encrypt (GemPortModifyDTOEncrypt | Unset): Whether to enable data encryption feature. Encrypt should be a value
            as follows:ENABLE;DISABLE. Default value: DISABLE.
    """

    gem_port_id: int
    line_profile_id: int | Unset = UNSET
    tcont_id: int | Unset = UNSET
    encrypt: GemPortModifyDTOEncrypt | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gem_port_id = self.gem_port_id

        line_profile_id = self.line_profile_id

        tcont_id = self.tcont_id

        encrypt: str | Unset = UNSET
        if not isinstance(self.encrypt, Unset):
            encrypt = self.encrypt.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gemPortId": gem_port_id,
            }
        )
        if line_profile_id is not UNSET:
            field_dict["lineProfileId"] = line_profile_id
        if tcont_id is not UNSET:
            field_dict["tcontId"] = tcont_id
        if encrypt is not UNSET:
            field_dict["encrypt"] = encrypt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gem_port_id = d.pop("gemPortId")

        line_profile_id = d.pop("lineProfileId", UNSET)

        tcont_id = d.pop("tcontId", UNSET)

        _encrypt = d.pop("encrypt", UNSET)
        encrypt: GemPortModifyDTOEncrypt | Unset
        if isinstance(_encrypt, Unset):
            encrypt = UNSET
        else:
            encrypt = GemPortModifyDTOEncrypt(_encrypt)

        gem_port_modify_dto = cls(
            gem_port_id=gem_port_id,
            line_profile_id=line_profile_id,
            tcont_id=tcont_id,
            encrypt=encrypt,
        )

        gem_port_modify_dto.additional_properties = d
        return gem_port_modify_dto

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
