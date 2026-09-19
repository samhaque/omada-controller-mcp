from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TcontModifyDTO")


@_attrs_define
class TcontModifyDTO:
    """
    Attributes:
        tcont_id (int): T-cont ID should be within the range of 1 to 127 and should not be null
        line_profile_id (int | Unset): The ID of the associated Line Profile,lineProfile should be within the range of 1
            to 512.
        dba_id (int | Unset): The DBA template ID bound to the T-cont. DbaId should be within the range of 0 to 512.
            Currently existing DBA templates, including DBA system templates, can also be referenced by the T-cont.
    """

    tcont_id: int
    line_profile_id: int | Unset = UNSET
    dba_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcont_id = self.tcont_id

        line_profile_id = self.line_profile_id

        dba_id = self.dba_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tcontId": tcont_id,
            }
        )
        if line_profile_id is not UNSET:
            field_dict["lineProfileId"] = line_profile_id
        if dba_id is not UNSET:
            field_dict["dbaId"] = dba_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tcont_id = d.pop("tcontId")

        line_profile_id = d.pop("lineProfileId", UNSET)

        dba_id = d.pop("dbaId", UNSET)

        tcont_modify_dto = cls(
            tcont_id=tcont_id,
            line_profile_id=line_profile_id,
            dba_id=dba_id,
        )

        tcont_modify_dto.additional_properties = d
        return tcont_modify_dto

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
