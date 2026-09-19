from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyConfirmResultOpenApiVO")


@_attrs_define
class ModifyConfirmResultOpenApiVO:
    """
    Attributes:
        need_confirm (bool | Unset): needConfirm indicates whether the digit map configuration conflicts with the "end
            with #" configuration of the current device.
    """

    need_confirm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        need_confirm = self.need_confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if need_confirm is not UNSET:
            field_dict["needConfirm"] = need_confirm

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        need_confirm = d.pop("needConfirm", UNSET)

        modify_confirm_result_open_api_vo = cls(
            need_confirm=need_confirm,
        )

        modify_confirm_result_open_api_vo.additional_properties = d
        return modify_confirm_result_open_api_vo

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
