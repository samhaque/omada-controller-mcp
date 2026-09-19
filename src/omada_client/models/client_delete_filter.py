from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientDeleteFilter")


@_attrs_define
class ClientDeleteFilter:
    """
    Attributes:
        start (int | Unset): Start timestamp, in seconds, such as 1682000000.
        end (int | Unset): End timestamp, in seconds, such as 1682000000.
        wireless (bool | Unset): Wireless, filter by wireless field if provided.
        guest (bool | Unset): Guest, filter by guest field if provided.
        rate_limit (bool | Unset): RateLimit, filter by rateLimit field if provided.
        block (bool | Unset): Block, filter by block field if provided.
        connect_success (bool | Unset): Connect success, filter by connectSuccess field if provided.
        search_key (str | Unset): Searching for clients to delete, Searching by client mac, client name.
    """

    start: int | Unset = UNSET
    end: int | Unset = UNSET
    wireless: bool | Unset = UNSET
    guest: bool | Unset = UNSET
    rate_limit: bool | Unset = UNSET
    block: bool | Unset = UNSET
    connect_success: bool | Unset = UNSET
    search_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        wireless = self.wireless

        guest = self.guest

        rate_limit = self.rate_limit

        block = self.block

        connect_success = self.connect_success

        search_key = self.search_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if guest is not UNSET:
            field_dict["guest"] = guest
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if block is not UNSET:
            field_dict["block"] = block
        if connect_success is not UNSET:
            field_dict["connectSuccess"] = connect_success
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        wireless = d.pop("wireless", UNSET)

        guest = d.pop("guest", UNSET)

        rate_limit = d.pop("rateLimit", UNSET)

        block = d.pop("block", UNSET)

        connect_success = d.pop("connectSuccess", UNSET)

        search_key = d.pop("searchKey", UNSET)

        client_delete_filter = cls(
            start=start,
            end=end,
            wireless=wireless,
            guest=guest,
            rate_limit=rate_limit,
            block=block,
            connect_success=connect_success,
            search_key=search_key,
        )

        client_delete_filter.additional_properties = d
        return client_delete_filter

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
