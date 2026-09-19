from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ApUpdateWlanGroupOpenApiVO")


@_attrs_define
class ApUpdateWlanGroupOpenApiVO:
    """
    Attributes:
        wlan_group_id (str): The wlan group Id that the AP should switch to, must be in the same site as the AP and
            cannot be the current wlan group.
    """

    wlan_group_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wlan_group_id = self.wlan_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wlanGroupId": wlan_group_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wlan_group_id = d.pop("wlanGroupId")

        ap_update_wlan_group_open_api_vo = cls(
            wlan_group_id=wlan_group_id,
        )

        ap_update_wlan_group_open_api_vo.additional_properties = d
        return ap_update_wlan_group_open_api_vo

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
