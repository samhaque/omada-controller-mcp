from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspClientOverallVO")


@_attrs_define
class MspClientOverallVO:
    """
    Attributes:
        total_client_num (int | Unset):
        wired_user (int | Unset):
        wireless_user (int | Unset):
        wireless_guest (int | Unset):
    """

    total_client_num: int | Unset = UNSET
    wired_user: int | Unset = UNSET
    wireless_user: int | Unset = UNSET
    wireless_guest: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_client_num = self.total_client_num

        wired_user = self.wired_user

        wireless_user = self.wireless_user

        wireless_guest = self.wireless_guest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_client_num is not UNSET:
            field_dict["totalClientNum"] = total_client_num
        if wired_user is not UNSET:
            field_dict["wiredUser"] = wired_user
        if wireless_user is not UNSET:
            field_dict["wirelessUser"] = wireless_user
        if wireless_guest is not UNSET:
            field_dict["wirelessGuest"] = wireless_guest

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_client_num = d.pop("totalClientNum", UNSET)

        wired_user = d.pop("wiredUser", UNSET)

        wireless_user = d.pop("wirelessUser", UNSET)

        wireless_guest = d.pop("wirelessGuest", UNSET)

        msp_client_overall_vo = cls(
            total_client_num=total_client_num,
            wired_user=wired_user,
            wireless_user=wireless_user,
            wireless_guest=wireless_guest,
        )

        msp_client_overall_vo.additional_properties = d
        return msp_client_overall_vo

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
