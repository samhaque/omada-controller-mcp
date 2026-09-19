from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanOnlineStatusOpenApiVO")


@_attrs_define
class VirtualWanOnlineStatusOpenApiVO:
    """Virtual WAN online status list

    Attributes:
        virtual_wan_id (str | Unset): This field represents VirtualWan ID. VirtualWan ID can be obtained from 'Query
            available virtual WAN list' interface
        online_detection (int | Unset): Port Online Detection
    """

    virtual_wan_id: str | Unset = UNSET
    online_detection: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_wan_id = self.virtual_wan_id

        online_detection = self.online_detection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id
        if online_detection is not UNSET:
            field_dict["onlineDetection"] = online_detection

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        virtual_wan_id = d.pop("virtualWanId", UNSET)

        online_detection = d.pop("onlineDetection", UNSET)

        virtual_wan_online_status_open_api_vo = cls(
            virtual_wan_id=virtual_wan_id,
            online_detection=online_detection,
        )

        virtual_wan_online_status_open_api_vo.additional_properties = d
        return virtual_wan_online_status_open_api_vo

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
