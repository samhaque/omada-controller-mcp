from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.dba_profile_modify_dto_type import DBAProfileModifyDTOType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DBAProfileModifyDTO")


@_attrs_define
class DBAProfileModifyDTO:
    """
    Attributes:
        dba_id (int): DBA ID should be within the range of 1 to 512 and should not be null
        name (str | Unset): Name of DBA profile should contain 1 to 32 characters including digits, upper and lower
            letters, and the following six characters: -@_:/. .
        type_ (DBAProfileModifyDTOType | Unset): DBA bandwidth allocation methods.Type should be a value as follows:
            FIX, ASSURE, MAX, ASSURE_MAX, and FIX_ASSURE_MAX. The default value is FIX.
        fix (int | Unset): The value for fixed bandwidth is required when the Type is set to FIX or FIX_ASSURE_MAX. Fix
            should be within the range of 128 to 720000, with the unit in kbit/s.
        assure (int | Unset): The value for guaranteed bandwidth is required when the Type is set to ASSURE, ASSURE_MAX,
            or FIX_ASSURE_MAX. Assure should be within the range of 128 to 1200000, with the unit in kbit/s.
        max_ (int | Unset): The value for maximum bandwidth is required when the Type is set to MAX, ASSURE_MAX, or
            FIX_ASSURE_MAX. Max should be within the range of 128 to 1244160, with the unit in kbit/s.
    """

    dba_id: int
    name: str | Unset = UNSET
    type_: DBAProfileModifyDTOType | Unset = UNSET
    fix: int | Unset = UNSET
    assure: int | Unset = UNSET
    max_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dba_id = self.dba_id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        fix = self.fix

        assure = self.assure

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dbaId": dba_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if fix is not UNSET:
            field_dict["fix"] = fix
        if assure is not UNSET:
            field_dict["assure"] = assure
        if max_ is not UNSET:
            field_dict["max"] = max_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dba_id = d.pop("dbaId")

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DBAProfileModifyDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DBAProfileModifyDTOType(_type_)

        fix = d.pop("fix", UNSET)

        assure = d.pop("assure", UNSET)

        max_ = d.pop("max", UNSET)

        dba_profile_modify_dto = cls(
            dba_id=dba_id,
            name=name,
            type_=type_,
            fix=fix,
            assure=assure,
            max_=max_,
        )

        dba_profile_modify_dto.additional_properties = d
        return dba_profile_modify_dto

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
