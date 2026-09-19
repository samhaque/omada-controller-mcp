from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortStatVO")


@_attrs_define
class PortStatVO:
    """Port total traffic map

    Attributes:
        rx (int | Unset): Total receive traffic of the port, in bytes
        tx (int | Unset): Total transmit traffic of the port, in bytes
        all_ (int | Unset): Total traffic of the port, in bytes
    """

    rx: int | Unset = UNSET
    tx: int | Unset = UNSET
    all_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rx = self.rx

        tx = self.tx

        all_ = self.all_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        all_ = d.pop("all", UNSET)

        port_stat_vo = cls(
            rx=rx,
            tx=tx,
            all_=all_,
        )

        port_stat_vo.additional_properties = d
        return port_stat_vo

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
