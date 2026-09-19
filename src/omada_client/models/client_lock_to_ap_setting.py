from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientLockToAPSetting")


@_attrs_define
class ClientLockToAPSetting:
    """
    Attributes:
        enable (bool): Lock to AP enable
        aps (list[str] | Unset): AP MAC list. Use capital letters and separator, for example: AA-AA-AA-AA-AA-AA.
    """

    enable: bool
    aps: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        aps: list[str] | Unset = UNSET
        if not isinstance(self.aps, Unset):
            aps = self.aps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if aps is not UNSET:
            field_dict["aps"] = aps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        aps = cast(list[str], d.pop("aps", UNSET))

        client_lock_to_ap_setting = cls(
            enable=enable,
            aps=aps,
        )

        client_lock_to_ap_setting.additional_properties = d
        return client_lock_to_ap_setting

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
