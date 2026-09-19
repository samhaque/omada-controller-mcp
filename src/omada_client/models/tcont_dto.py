from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TcontDTO")


@_attrs_define
class TcontDTO:
    """
    Attributes:
        tcont_id (int): T-cont ID should be within the range of 1 to 127 and should not be null
        dba_id (int): The DBA template ID bound to the T-cont. DbaId should be a within the range of 0 to 512. Currently
            existing DBA templates, including DBA system templates, can also be referenced by the T-cont.
        line_profile_id (int | Unset): The ID of the associated Line Profile,lineProfile should be within the range of 1
            to 512.
        gem_port_ids (list[int] | Unset): A list of GEM Port IDs bound to this T-Cont.
        is_in_use (bool | Unset): Whether the T-cont has been used. If it has been used, it cannot be deleted. True
            indicates it has been used, while false indicates it has not been used.
    """

    tcont_id: int
    dba_id: int
    line_profile_id: int | Unset = UNSET
    gem_port_ids: list[int] | Unset = UNSET
    is_in_use: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcont_id = self.tcont_id

        dba_id = self.dba_id

        line_profile_id = self.line_profile_id

        gem_port_ids: list[int] | Unset = UNSET
        if not isinstance(self.gem_port_ids, Unset):
            gem_port_ids = self.gem_port_ids

        is_in_use = self.is_in_use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tcontId": tcont_id,
                "dbaId": dba_id,
            }
        )
        if line_profile_id is not UNSET:
            field_dict["lineProfileId"] = line_profile_id
        if gem_port_ids is not UNSET:
            field_dict["gemPortIds"] = gem_port_ids
        if is_in_use is not UNSET:
            field_dict["isInUse"] = is_in_use

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tcont_id = d.pop("tcontId")

        dba_id = d.pop("dbaId")

        line_profile_id = d.pop("lineProfileId", UNSET)

        gem_port_ids = cast(list[int], d.pop("gemPortIds", UNSET))

        is_in_use = d.pop("isInUse", UNSET)

        tcont_dto = cls(
            tcont_id=tcont_id,
            dba_id=dba_id,
            line_profile_id=line_profile_id,
            gem_port_ids=gem_port_ids,
            is_in_use=is_in_use,
        )

        tcont_dto.additional_properties = d
        return tcont_dto

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
