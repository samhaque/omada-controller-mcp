from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApPortStatusVO")


@_attrs_define
class ApPortStatusVO:
    """Port Status

    Attributes:
        tx (int | Unset): Tx Bytes
        rx (int | Unset): Rx Bytes
    """

    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx = self.tx

        rx = self.rx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        ap_port_status_vo = cls(
            tx=tx,
            rx=rx,
        )

        ap_port_status_vo.additional_properties = d
        return ap_port_status_vo

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
