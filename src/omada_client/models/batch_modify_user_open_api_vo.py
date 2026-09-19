from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchModifyUserOpenApiVO")


@_attrs_define
class BatchModifyUserOpenApiVO:
    """
    Attributes:
        user_ids (list[str] | Unset): The list of user IDs that need to be configured in bulk
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permission
        start_time (int | Unset): The start time of the user's validity period. time range: start timestamp
            (Millisecond).
        end_time (int | Unset): The end time of the user's validity period. time range: end timestamp (Millisecond).
    """

    user_ids: list[str] | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if temporary_enable is not UNSET:
            field_dict["temporaryEnable"] = temporary_enable
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_ids = cast(list[str], d.pop("userIds", UNSET))

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        batch_modify_user_open_api_vo = cls(
            user_ids=user_ids,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
        )

        batch_modify_user_open_api_vo.additional_properties = d
        return batch_modify_user_open_api_vo

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
