from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WlanGroupStatusOpenApiVO")


@_attrs_define
class WlanGroupStatusOpenApiVO:
    """
    Attributes:
        exceeded (bool | Unset): whether the number of WLAN groups exceeds the limit
        wlan_group_num (int | Unset): the number of wlan groups
    """

    exceeded: bool | Unset = UNSET
    wlan_group_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exceeded = self.exceeded

        wlan_group_num = self.wlan_group_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exceeded is not UNSET:
            field_dict["exceeded"] = exceeded
        if wlan_group_num is not UNSET:
            field_dict["wlanGroupNum"] = wlan_group_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exceeded = d.pop("exceeded", UNSET)

        wlan_group_num = d.pop("wlanGroupNum", UNSET)

        wlan_group_status_open_api_vo = cls(
            exceeded=exceeded,
            wlan_group_num=wlan_group_num,
        )

        wlan_group_status_open_api_vo.additional_properties = d
        return wlan_group_status_open_api_vo

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
