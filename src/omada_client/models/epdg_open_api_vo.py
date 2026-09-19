from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EPDGOpenApiVO")


@_attrs_define
class EPDGOpenApiVO:
    """epdgs

    Attributes:
        qos_priority (int | Unset): QOS Priority
        type_ (int | Unset): Type. Such as: 0: domain, 1:ip.
        domain (str | Unset): Domain. If parameter [type] is 0, it should not be null.
        ip (str | Unset): Ip. If parameter [type] is 1, it should not be null.
    """

    qos_priority: int | Unset = UNSET
    type_: int | Unset = UNSET
    domain: str | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos_priority = self.qos_priority

        type_ = self.type_

        domain = self.domain

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qos_priority is not UNSET:
            field_dict["qosPriority"] = qos_priority
        if type_ is not UNSET:
            field_dict["type"] = type_
        if domain is not UNSET:
            field_dict["domain"] = domain
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        qos_priority = d.pop("qosPriority", UNSET)

        type_ = d.pop("type", UNSET)

        domain = d.pop("domain", UNSET)

        ip = d.pop("ip", UNSET)

        epdg_open_api_vo = cls(
            qos_priority=qos_priority,
            type_=type_,
            domain=domain,
            ip=ip,
        )

        epdg_open_api_vo.additional_properties = d
        return epdg_open_api_vo

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
