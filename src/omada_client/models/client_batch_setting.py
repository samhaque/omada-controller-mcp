from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_batch_ip_setting import ClientBatchIPSetting
    from ..models.client_lock_to_ap_setting import ClientLockToAPSetting
    from ..models.client_rate_limit_setting import ClientRateLimitSetting


T = TypeVar("T", bound="ClientBatchSetting")


@_attrs_define
class ClientBatchSetting:
    """
    Attributes:
        mac_list (list[str] | Unset): List of clients' mac.
        ip_setting (ClientBatchIPSetting | Unset): Setting of ip.
        rate_limit (ClientRateLimitSetting | Unset): Setting of rate limit.
        lock_to_ap (ClientLockToAPSetting | Unset):
    """

    mac_list: list[str] | Unset = UNSET
    ip_setting: ClientBatchIPSetting | Unset = UNSET
    rate_limit: ClientRateLimitSetting | Unset = UNSET
    lock_to_ap: ClientLockToAPSetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac_list: list[str] | Unset = UNSET
        if not isinstance(self.mac_list, Unset):
            mac_list = self.mac_list

        ip_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_setting, Unset):
            ip_setting = self.ip_setting.to_dict()

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        lock_to_ap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lock_to_ap, Unset):
            lock_to_ap = self.lock_to_ap.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac_list is not UNSET:
            field_dict["macList"] = mac_list
        if ip_setting is not UNSET:
            field_dict["ipSetting"] = ip_setting
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if lock_to_ap is not UNSET:
            field_dict["lockToAp"] = lock_to_ap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_batch_ip_setting import (
            ClientBatchIPSetting,
        )
        from ..models.client_lock_to_ap_setting import (
            ClientLockToAPSetting,
        )
        from ..models.client_rate_limit_setting import (
            ClientRateLimitSetting,
        )

        d = dict(src_dict)
        mac_list = cast(list[str], d.pop("macList", UNSET))

        _ip_setting = d.pop("ipSetting", UNSET)
        ip_setting: ClientBatchIPSetting | Unset
        if isinstance(_ip_setting, Unset):
            ip_setting = UNSET
        else:
            ip_setting = ClientBatchIPSetting.from_dict(_ip_setting)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: ClientRateLimitSetting | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = ClientRateLimitSetting.from_dict(_rate_limit)

        _lock_to_ap = d.pop("lockToAp", UNSET)
        lock_to_ap: ClientLockToAPSetting | Unset
        if isinstance(_lock_to_ap, Unset):
            lock_to_ap = UNSET
        else:
            lock_to_ap = ClientLockToAPSetting.from_dict(_lock_to_ap)

        client_batch_setting = cls(
            mac_list=mac_list,
            ip_setting=ip_setting,
            rate_limit=rate_limit,
            lock_to_ap=lock_to_ap,
        )

        client_batch_setting.additional_properties = d
        return client_batch_setting

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
