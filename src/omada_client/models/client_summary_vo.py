from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientSummaryVO")


@_attrs_define
class ClientSummaryVO:
    """
    Attributes:
        total (int | Unset):
        wired_client (int | Unset):
        wireless_client (int | Unset):
    """

    total: int | Unset = UNSET
    wired_client: int | Unset = UNSET
    wireless_client: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        wired_client = self.wired_client

        wireless_client = self.wireless_client

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if wired_client is not UNSET:
            field_dict["wiredClient"] = wired_client
        if wireless_client is not UNSET:
            field_dict["wirelessClient"] = wireless_client

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        wired_client = d.pop("wiredClient", UNSET)

        wireless_client = d.pop("wirelessClient", UNSET)

        client_summary_vo = cls(
            total=total,
            wired_client=wired_client,
            wireless_client=wireless_client,
        )

        client_summary_vo.additional_properties = d
        return client_summary_vo

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
