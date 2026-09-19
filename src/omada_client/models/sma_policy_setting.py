from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SmaPolicySetting")


@_attrs_define
class SmaPolicySetting:
    """
    Attributes:
        inbox_policy (int): Policy parameter [inboxPolicy] should be from 0 to 2. 0: If SMS inbox/outbox is full, delete
            the oldest read SMS; 1: If SMS inbox/outbox is full, send e-mail alert to Administrator;2: If SMS inbox/outbox
            is full, Forward new SMS with e-mail to Administrator.
        mail_server (str | Unset): Mail server ID.
        resource (int | Unset): SMS policy setting creation resource, such as: 0: new created, 1: from template, 2:
            override.
    """

    inbox_policy: int
    mail_server: str | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbox_policy = self.inbox_policy

        mail_server = self.mail_server

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inboxPolicy": inbox_policy,
            }
        )
        if mail_server is not UNSET:
            field_dict["mailServer"] = mail_server
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        inbox_policy = d.pop("inboxPolicy")

        mail_server = d.pop("mailServer", UNSET)

        resource = d.pop("resource", UNSET)

        sma_policy_setting = cls(
            inbox_policy=inbox_policy,
            mail_server=mail_server,
            resource=resource,
        )

        sma_policy_setting.additional_properties = d
        return sma_policy_setting

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
