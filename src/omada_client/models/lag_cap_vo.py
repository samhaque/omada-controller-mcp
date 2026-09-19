from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LagCapVO")


@_attrs_define
class LagCapVO:
    """Capability of lag

    Attributes:
        lacp_mod_support (bool | Unset): Lacp Mod Support
        lag_hash_alg_support (bool | Unset): Lag Hash Algorithm Support
        lag_hash_algs (list[int] | Unset): Support Lag Hash Algorithms, 0: SRC_MAC; 1: DST_MAC; 2: SRC_MAC_DST_MAC; 3:
            SRC_IP; 4: DST_IP; 5: SRC_IP_DST_IP
    """

    lacp_mod_support: bool | Unset = UNSET
    lag_hash_alg_support: bool | Unset = UNSET
    lag_hash_algs: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lacp_mod_support = self.lacp_mod_support

        lag_hash_alg_support = self.lag_hash_alg_support

        lag_hash_algs: list[int] | Unset = UNSET
        if not isinstance(self.lag_hash_algs, Unset):
            lag_hash_algs = self.lag_hash_algs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lacp_mod_support is not UNSET:
            field_dict["lacpModSupport"] = lacp_mod_support
        if lag_hash_alg_support is not UNSET:
            field_dict["lagHashAlgSupport"] = lag_hash_alg_support
        if lag_hash_algs is not UNSET:
            field_dict["lagHashAlgs"] = lag_hash_algs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lacp_mod_support = d.pop("lacpModSupport", UNSET)

        lag_hash_alg_support = d.pop("lagHashAlgSupport", UNSET)

        lag_hash_algs = cast(list[int], d.pop("lagHashAlgs", UNSET))

        lag_cap_vo = cls(
            lacp_mod_support=lacp_mod_support,
            lag_hash_alg_support=lag_hash_alg_support,
            lag_hash_algs=lag_hash_algs,
        )

        lag_cap_vo.additional_properties = d
        return lag_cap_vo

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
