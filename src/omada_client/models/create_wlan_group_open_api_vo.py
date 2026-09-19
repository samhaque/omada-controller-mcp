from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWlanGroupOpenApiVO")


@_attrs_define
class CreateWlanGroupOpenApiVO:
    """
    Attributes:
        name (str): WLAN group name should contain 1 to 128 characters.
        clone (bool): Whether to clone SSID list from other WLAN group.
        cloned_wlan_id (str | Unset): WLAN group ID that needs to be cloned. Parameter [clonedWlanId] should not be null
            when Parameter [clone] is true.
    """

    name: str
    clone: bool
    cloned_wlan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        clone = self.clone

        cloned_wlan_id = self.cloned_wlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "clone": clone,
            }
        )
        if cloned_wlan_id is not UNSET:
            field_dict["clonedWlanId"] = cloned_wlan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        clone = d.pop("clone")

        cloned_wlan_id = d.pop("clonedWlanId", UNSET)

        create_wlan_group_open_api_vo = cls(
            name=name,
            clone=clone,
            cloned_wlan_id=cloned_wlan_id,
        )

        create_wlan_group_open_api_vo.additional_properties = d
        return create_wlan_group_open_api_vo

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
