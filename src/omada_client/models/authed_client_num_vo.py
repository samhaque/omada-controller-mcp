from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthedClientNumVO")


@_attrs_define
class AuthedClientNumVO:
    """
    Attributes:
        new_num (int | Unset):
        existing_num (int | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
    """

    new_num: int | Unset = UNSET
    existing_num: int | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_num = self.new_num

        existing_num = self.existing_num

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_num is not UNSET:
            field_dict["newNum"] = new_num
        if existing_num is not UNSET:
            field_dict["existingNum"] = existing_num
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        new_num = d.pop("newNum", UNSET)

        existing_num = d.pop("existingNum", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        authed_client_num_vo = cls(
            new_num=new_num,
            existing_num=existing_num,
            start_time=start_time,
            end_time=end_time,
        )

        authed_client_num_vo.additional_properties = d
        return authed_client_num_vo

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
