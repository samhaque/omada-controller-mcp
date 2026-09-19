from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectLocalUsersOpenApiVO")


@_attrs_define
class SelectLocalUsersOpenApiVO:
    """
    Attributes:
        type_ (int): Select type. It should be a value as follows: 0: Represents selecting all localUsers, this
            selection does not pass parameter [ids]. 1: Parameter [ids] includes the IDs of the localUsers to be selected.
            2: Parameter [ids] includes the IDs of the localUsers not to be selected
        ids (list[str] | Unset): IDs of localUsers to be deleted in batch operation
    """

    type_: int
    ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        ids = cast(list[str], d.pop("ids", UNSET))

        select_local_users_open_api_vo = cls(
            type_=type_,
            ids=ids,
        )

        select_local_users_open_api_vo.additional_properties = d
        return select_local_users_open_api_vo

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
