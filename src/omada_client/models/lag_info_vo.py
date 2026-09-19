from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LagInfoVO")


@_attrs_define
class LagInfoVO:
    """Device Lag Infos

    Attributes:
        lag_id (int | Unset):
        ports (list[int] | Unset):
        name (str | Unset):
        mlag_enable (bool | Unset):
    """

    lag_id: int | Unset = UNSET
    ports: list[int] | Unset = UNSET
    name: str | Unset = UNSET
    mlag_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lag_id = self.lag_id

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        name = self.name

        mlag_enable = self.mlag_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if ports is not UNSET:
            field_dict["ports"] = ports
        if name is not UNSET:
            field_dict["name"] = name
        if mlag_enable is not UNSET:
            field_dict["mlagEnable"] = mlag_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lag_id = d.pop("lagId", UNSET)

        ports = cast(list[int], d.pop("ports", UNSET))

        name = d.pop("name", UNSET)

        mlag_enable = d.pop("mlagEnable", UNSET)

        lag_info_vo = cls(
            lag_id=lag_id,
            ports=ports,
            name=name,
            mlag_enable=mlag_enable,
        )

        lag_info_vo.additional_properties = d
        return lag_info_vo

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
