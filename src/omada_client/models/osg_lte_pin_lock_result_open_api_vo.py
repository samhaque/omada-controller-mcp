from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgLtePinLockResultOpenApiVO")


@_attrs_define
class OsgLtePinLockResultOpenApiVO:
    """
    Attributes:
        try_pin_limit (int | Unset): The number of times PIN code can be tried.
        try_pin_result (bool | Unset): The result of trying the PIN.
        try_puk_limit (int | Unset): The number of times PUK code can be tried
        try_puk_result (bool | Unset): The result of trying the PUK.
    """

    try_pin_limit: int | Unset = UNSET
    try_pin_result: bool | Unset = UNSET
    try_puk_limit: int | Unset = UNSET
    try_puk_result: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        try_pin_limit = self.try_pin_limit

        try_pin_result = self.try_pin_result

        try_puk_limit = self.try_puk_limit

        try_puk_result = self.try_puk_result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if try_pin_limit is not UNSET:
            field_dict["tryPinLimit"] = try_pin_limit
        if try_pin_result is not UNSET:
            field_dict["tryPinResult"] = try_pin_result
        if try_puk_limit is not UNSET:
            field_dict["tryPukLimit"] = try_puk_limit
        if try_puk_result is not UNSET:
            field_dict["tryPukResult"] = try_puk_result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        try_pin_limit = d.pop("tryPinLimit", UNSET)

        try_pin_result = d.pop("tryPinResult", UNSET)

        try_puk_limit = d.pop("tryPukLimit", UNSET)

        try_puk_result = d.pop("tryPukResult", UNSET)

        osg_lte_pin_lock_result_open_api_vo = cls(
            try_pin_limit=try_pin_limit,
            try_pin_result=try_pin_result,
            try_puk_limit=try_puk_limit,
            try_puk_result=try_puk_result,
        )

        osg_lte_pin_lock_result_open_api_vo.additional_properties = d
        return osg_lte_pin_lock_result_open_api_vo

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
