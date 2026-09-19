from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LagInfoOpenApiVO")


@_attrs_define
class LagInfoOpenApiVO:
    """Switch lag info.

    Attributes:
        lag (int | Unset): Lag number.
        ports (list[int] | Unset): Ports in lag
        name (str | Unset): Lag name.
    """

    lag: int | Unset = UNSET
    ports: list[int] | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lag = self.lag

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lag is not UNSET:
            field_dict["lag"] = lag
        if ports is not UNSET:
            field_dict["ports"] = ports
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lag = d.pop("lag", UNSET)

        ports = cast(list[int], d.pop("ports", UNSET))

        name = d.pop("name", UNSET)

        lag_info_open_api_vo = cls(
            lag=lag,
            ports=ports,
            name=name,
        )

        lag_info_open_api_vo.additional_properties = d
        return lag_info_open_api_vo

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
