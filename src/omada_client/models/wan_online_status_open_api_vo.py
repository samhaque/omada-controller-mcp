from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanOnlineStatusOpenApiVO")


@_attrs_define
class WanOnlineStatusOpenApiVO:
    """WAN online status list

    Attributes:
        port_uuid (str | Unset): The port UUID of WAN
        online_detection (int | Unset): Port Online Detection
    """

    port_uuid: str | Unset = UNSET
    online_detection: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        online_detection = self.online_detection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if online_detection is not UNSET:
            field_dict["onlineDetection"] = online_detection

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid = d.pop("portUuid", UNSET)

        online_detection = d.pop("onlineDetection", UNSET)

        wan_online_status_open_api_vo = cls(
            port_uuid=port_uuid,
            online_detection=online_detection,
        )

        wan_online_status_open_api_vo.additional_properties = d
        return wan_online_status_open_api_vo

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
