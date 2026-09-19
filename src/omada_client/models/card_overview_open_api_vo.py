from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardOverviewOpenApiVO")


@_attrs_define
class CardOverviewOpenApiVO:
    """
    Attributes:
        type_ (str | Unset): The type of data
        total (int | Unset): The total number of devices
        pre_config (int | Unset): The number of preConfig devices
        connected (int | Unset): The number of connected devices
        disconnected_count (int | Unset): The number of disconnected devices
    """

    type_: str | Unset = UNSET
    total: int | Unset = UNSET
    pre_config: int | Unset = UNSET
    connected: int | Unset = UNSET
    disconnected_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        total = self.total

        pre_config = self.pre_config

        connected = self.connected

        disconnected_count = self.disconnected_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if total is not UNSET:
            field_dict["total"] = total
        if pre_config is not UNSET:
            field_dict["preConfig"] = pre_config
        if connected is not UNSET:
            field_dict["connected"] = connected
        if disconnected_count is not UNSET:
            field_dict["disconnectedCount"] = disconnected_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        total = d.pop("total", UNSET)

        pre_config = d.pop("preConfig", UNSET)

        connected = d.pop("connected", UNSET)

        disconnected_count = d.pop("disconnectedCount", UNSET)

        card_overview_open_api_vo = cls(
            type_=type_,
            total=total,
            pre_config=pre_config,
            connected=connected,
            disconnected_count=disconnected_count,
        )

        card_overview_open_api_vo.additional_properties = d
        return card_overview_open_api_vo

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
