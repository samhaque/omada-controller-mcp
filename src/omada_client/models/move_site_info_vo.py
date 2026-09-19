from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveSiteInfoVO")


@_attrs_define
class MoveSiteInfoVO:
    """MoveSite results for each device.

    Attributes:
        mac (str | Unset): Mac address
        name (str | Unset): Name
        move_site_status (int | Unset): Move site status.MoveSiteStatus should be a value as follows:0: Device is in
            MoveSite;1: MoveSite Success;2: MoveSite Failed
        error_code (int | Unset): Error code
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    move_site_status: int | Unset = UNSET
    error_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        move_site_status = self.move_site_status

        error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if move_site_status is not UNSET:
            field_dict["moveSiteStatus"] = move_site_status
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        move_site_status = d.pop("moveSiteStatus", UNSET)

        error_code = d.pop("errorCode", UNSET)

        move_site_info_vo = cls(
            mac=mac,
            name=name,
            move_site_status=move_site_status,
            error_code=error_code,
        )

        move_site_info_vo.additional_properties = d
        return move_site_info_vo

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
