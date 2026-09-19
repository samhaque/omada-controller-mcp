from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidSimpleOpenApiVO")


@_attrs_define
class SsidSimpleOpenApiVO:
    """SSID list with MAC-Based authentication configured

    Attributes:
        id (str | Unset): ID of SSID
        ssid_id (str | Unset): SSID ID, kept for backward compatibility and equivalent to id. This field will be removed
            in a future release; use id instead.
        ssid_name (str | Unset): This field represents SSID name
    """

    id: str | Unset = UNSET
    ssid_id: str | Unset = UNSET
    ssid_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ssid_id = self.ssid_id

        ssid_name = self.ssid_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ssid_id is not UNSET:
            field_dict["ssidId"] = ssid_id
        if ssid_name is not UNSET:
            field_dict["ssidName"] = ssid_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        ssid_id = d.pop("ssidId", UNSET)

        ssid_name = d.pop("ssidName", UNSET)

        ssid_simple_open_api_vo = cls(
            id=id,
            ssid_id=ssid_id,
            ssid_name=ssid_name,
        )

        ssid_simple_open_api_vo.additional_properties = d
        return ssid_simple_open_api_vo

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
