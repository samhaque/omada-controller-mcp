from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogLevel")


@_attrs_define
class LogLevel:
    """
    Attributes:
        type_ (str | Unset): Log level type should be a value as follows: AUTO; CUSTOM
        other_module (str | Unset): Log level of other module should be a value as follows: WARN; INFO; DEBUG
        manager_module (str | Unset): Log level of manager module should be a value as follows: WARN; INFO; DEBUG
        client_module (str | Unset): Log level of client module should be a value as follows: WARN; INFO; DEBUG
        monitor_module (str | Unset): Log level of monitor module should be a value as follows: WARN; INFO; DEBUG
        system_module (str | Unset): Log level of system module should be a value as follows: WARN; INFO; DEBUG
        account_module (str | Unset): Log level of account module should be a value as follows: WARN; INFO; DEBUG
        log_module (str | Unset): Log level of log module should be a value as follows: WARN; INFO; DEBUG
    """

    type_: str | Unset = UNSET
    other_module: str | Unset = UNSET
    manager_module: str | Unset = UNSET
    client_module: str | Unset = UNSET
    monitor_module: str | Unset = UNSET
    system_module: str | Unset = UNSET
    account_module: str | Unset = UNSET
    log_module: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        other_module = self.other_module

        manager_module = self.manager_module

        client_module = self.client_module

        monitor_module = self.monitor_module

        system_module = self.system_module

        account_module = self.account_module

        log_module = self.log_module

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if other_module is not UNSET:
            field_dict["otherModule"] = other_module
        if manager_module is not UNSET:
            field_dict["managerModule"] = manager_module
        if client_module is not UNSET:
            field_dict["clientModule"] = client_module
        if monitor_module is not UNSET:
            field_dict["monitorModule"] = monitor_module
        if system_module is not UNSET:
            field_dict["systemModule"] = system_module
        if account_module is not UNSET:
            field_dict["accountModule"] = account_module
        if log_module is not UNSET:
            field_dict["logModule"] = log_module

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        other_module = d.pop("otherModule", UNSET)

        manager_module = d.pop("managerModule", UNSET)

        client_module = d.pop("clientModule", UNSET)

        monitor_module = d.pop("monitorModule", UNSET)

        system_module = d.pop("systemModule", UNSET)

        account_module = d.pop("accountModule", UNSET)

        log_module = d.pop("logModule", UNSET)

        log_level = cls(
            type_=type_,
            other_module=other_module,
            manager_module=manager_module,
            client_module=client_module,
            monitor_module=monitor_module,
            system_module=system_module,
            account_module=account_module,
            log_module=log_module,
        )

        log_level.additional_properties = d
        return log_level

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
