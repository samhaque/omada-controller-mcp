from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPsecFailoverSettingOpenApiVO")


@_attrs_define
class IPsecFailoverSettingOpenApiVO:
    """Setting of the IPSec failover.

    Attributes:
        failover (bool | Unset): Indicates whether to use the IPSec failover.
        backup_wan (str | Unset): Backup WAN of the IPSec failover.
        failback (bool | Unset): Failback of the IPSec failover.
        failback_time (int | Unset): Failback time should be within the range of 10–3600s.
    """

    failover: bool | Unset = UNSET
    backup_wan: str | Unset = UNSET
    failback: bool | Unset = UNSET
    failback_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failover = self.failover

        backup_wan = self.backup_wan

        failback = self.failback

        failback_time = self.failback_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failover is not UNSET:
            field_dict["failover"] = failover
        if backup_wan is not UNSET:
            field_dict["backupWan"] = backup_wan
        if failback is not UNSET:
            field_dict["failback"] = failback
        if failback_time is not UNSET:
            field_dict["failbackTime"] = failback_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        failover = d.pop("failover", UNSET)

        backup_wan = d.pop("backupWan", UNSET)

        failback = d.pop("failback", UNSET)

        failback_time = d.pop("failbackTime", UNSET)

        i_psec_failover_setting_open_api_vo = cls(
            failover=failover,
            backup_wan=backup_wan,
            failback=failback,
            failback_time=failback_time,
        )

        i_psec_failover_setting_open_api_vo.additional_properties = d
        return i_psec_failover_setting_open_api_vo

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
