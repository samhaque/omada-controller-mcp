from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPsecFailoverStatusOpenApiVO")


@_attrs_define
class IPsecFailoverStatusOpenApiVO:
    """Setting of the IPSec failover.

    Attributes:
        backup_wan (str | Unset): Backup WAN of the IPSec failover.
        status (bool | Unset): Backup VPN status.
    """

    backup_wan: str | Unset = UNSET
    status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backup_wan = self.backup_wan

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup_wan is not UNSET:
            field_dict["backupWan"] = backup_wan
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backup_wan = d.pop("backupWan", UNSET)

        status = d.pop("status", UNSET)

        i_psec_failover_status_open_api_vo = cls(
            backup_wan=backup_wan,
            status=status,
        )

        i_psec_failover_status_open_api_vo.additional_properties = d
        return i_psec_failover_status_open_api_vo

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
