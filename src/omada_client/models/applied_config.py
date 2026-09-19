from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppliedConfig")


@_attrs_define
class AppliedConfig:
    """
    Attributes:
        applied_config (int | Unset): The value of parameter [appliedConfig] should be 1 or 2. 1: apply recommended
            config. 2: apply previous config.
    """

    applied_config: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_config = self.applied_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_config is not UNSET:
            field_dict["appliedConfig"] = applied_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        applied_config = d.pop("appliedConfig", UNSET)

        applied_config = cls(
            applied_config=applied_config,
        )

        applied_config.additional_properties = d
        return applied_config

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
