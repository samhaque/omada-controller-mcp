from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpgradePort")


@_attrs_define
class UpgradePort:
    """
    Attributes:
        upgrade_https_port (int | Unset): Upgrade HTTPS Port should be between 1024 and 65535
    """

    upgrade_https_port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upgrade_https_port = self.upgrade_https_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upgrade_https_port is not UNSET:
            field_dict["upgradeHttpsPort"] = upgrade_https_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upgrade_https_port = d.pop("upgradeHttpsPort", UNSET)

        upgrade_port = cls(
            upgrade_https_port=upgrade_https_port,
        )

        upgrade_port.additional_properties = d
        return upgrade_port

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
