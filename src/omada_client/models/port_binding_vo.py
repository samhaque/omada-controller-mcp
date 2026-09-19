from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortBindingVO")


@_attrs_define
class PortBindingVO:
    """Device List

    Attributes:
        mac (str | Unset): Device mac for Site Setting or Device template ID for Site Template Setting
        type_ (int | Unset): Device type, 1: gateway  2: switch  3: ap
        ports (list[str] | Unset): Selected ports.
        lags (list[int] | Unset): Selected lags.
        stack_id (str | Unset): Stack ID.Site Template Setting ignores this field
    """

    mac: str | Unset = UNSET
    type_: int | Unset = UNSET
    ports: list[str] | Unset = UNSET
    lags: list[int] | Unset = UNSET
    stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        type_ = self.type_

        ports: list[str] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        lags: list[int] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = self.lags

        stack_id = self.stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ports is not UNSET:
            field_dict["ports"] = ports
        if lags is not UNSET:
            field_dict["lags"] = lags
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        ports = cast(list[str], d.pop("ports", UNSET))

        lags = cast(list[int], d.pop("lags", UNSET))

        stack_id = d.pop("stackId", UNSET)

        port_binding_vo = cls(
            mac=mac,
            type_=type_,
            ports=ports,
            lags=lags,
            stack_id=stack_id,
        )

        port_binding_vo.additional_properties = d
        return port_binding_vo

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
