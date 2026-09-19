from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionLimitRuleTemplateOpenApiVO")


@_attrs_define
class SessionLimitRuleTemplateOpenApiVO:
    """
    Attributes:
        name (str): Name should contain 1 to 64 characters.
        status (bool): Status of the session limit rule.
        source_type (int): Source type should be a value as follows: 0: network; 1: IP group; 2: IP.
        max_session (int): Max sessions should be within the range of 1–999999.
        source_ids (list[str] | Unset): Source IDs of the session limit rule, only for network and IP group type.Network
            can be created using 'Create LAN network template' interface, and network ID can be obtained from 'Get LAN
            network template list' interface. IP group can be created using 'Create a new group profile template' interface,
            and IP group ID can be obtained from 'Get group profile template list' interface.
        ip (str | Unset): IP of the session limit rule.
    """

    name: str
    status: bool
    source_type: int
    max_session: int
    source_ids: list[str] | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        source_type = self.source_type

        max_session = self.max_session

        source_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_ids, Unset):
            source_ids = self.source_ids

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "sourceType": source_type,
                "maxSession": max_session,
            }
        )
        if source_ids is not UNSET:
            field_dict["sourceIds"] = source_ids
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        source_type = d.pop("sourceType")

        max_session = d.pop("maxSession")

        source_ids = cast(list[str], d.pop("sourceIds", UNSET))

        ip = d.pop("ip", UNSET)

        session_limit_rule_template_open_api_vo = cls(
            name=name,
            status=status,
            source_type=source_type,
            max_session=max_session,
            source_ids=source_ids,
            ip=ip,
        )

        session_limit_rule_template_open_api_vo.additional_properties = d
        return session_limit_rule_template_open_api_vo

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
