from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MirroredLag")


@_attrs_define
class MirroredLag:
    """Monitored LAG

    Attributes:
        lag_id (int | Unset): Lag ID
        lag_name (str | Unset): Lag Name
    """

    lag_id: int | Unset = UNSET
    lag_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lag_id = self.lag_id

        lag_name = self.lag_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if lag_name is not UNSET:
            field_dict["lagName"] = lag_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lag_id = d.pop("lagId", UNSET)

        lag_name = d.pop("lagName", UNSET)

        mirrored_lag = cls(
            lag_id=lag_id,
            lag_name=lag_name,
        )

        mirrored_lag.additional_properties = d
        return mirrored_lag

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
