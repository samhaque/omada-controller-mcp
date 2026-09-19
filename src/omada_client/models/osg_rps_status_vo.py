from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgRpsStatusVO")


@_attrs_define
class OsgRpsStatusVO:
    """
    Attributes:
        id (int | Unset):
        pg (bool | Unset):
        su (bool | Unset):
    """

    id: int | Unset = UNSET
    pg: bool | Unset = UNSET
    su: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        pg = self.pg

        su = self.su

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if pg is not UNSET:
            field_dict["pg"] = pg
        if su is not UNSET:
            field_dict["su"] = su

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        pg = d.pop("pg", UNSET)

        su = d.pop("su", UNSET)

        osg_rps_status_vo = cls(
            id=id,
            pg=pg,
            su=su,
        )

        osg_rps_status_vo.additional_properties = d
        return osg_rps_status_vo

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
