from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocateStackResultOpenApiVO")


@_attrs_define
class LocateStackResultOpenApiVO:
    """Locate stack ports error information

    Attributes:
        stack_id (str | Unset): Stack Id
        error_code (int | Unset): Error code
        error_msg (str | Unset): Error message
    """

    stack_id: str | Unset = UNSET
    error_code: int | Unset = UNSET
    error_msg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        error_code = self.error_code

        error_msg = self.error_msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_msg is not UNSET:
            field_dict["errorMsg"] = error_msg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_msg = d.pop("errorMsg", UNSET)

        locate_stack_result_open_api_vo = cls(
            stack_id=stack_id,
            error_code=error_code,
            error_msg=error_msg,
        )

        locate_stack_result_open_api_vo.additional_properties = d
        return locate_stack_result_open_api_vo

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
