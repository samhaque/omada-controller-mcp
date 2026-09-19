from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientMultiLinkInfo")


@_attrs_define
class ClientMultiLinkInfo:
    """(MLO) Client multi link info.

    Attributes:
        radio_id (int | Unset): (Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz; 2:5GHz-2; 3: 6GHz
        signal (int | Unset): (Wireless) Signal strength, unit: dBm.
    """

    radio_id: int | Unset = UNSET
    signal: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        signal = self.signal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if signal is not UNSET:
            field_dict["signal"] = signal

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id = d.pop("radioId", UNSET)

        signal = d.pop("signal", UNSET)

        client_multi_link_info = cls(
            radio_id=radio_id,
            signal=signal,
        )

        client_multi_link_info.additional_properties = d
        return client_multi_link_info

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
