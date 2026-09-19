from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClassRuleTemplateDetailOpenApiVO")


@_attrs_define
class ClassRuleTemplateDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): The ID of class rule.
        enable (bool | Unset): The status of class rule. valid values are true or false.
        ip_version (int | Unset): The IP Version of class rule should be a value as follows: 0: IPv4; 1: IPv6.
        local_ip (str | Unset): The ID of IP Group or IPv6 Group selected in the Local Address configuration. The ID can
            be obtained from 'Get group profile template list' interface.
        remote_ip (str | Unset): The ID of IP Group or IPv6 Group selected in the Remote Address configuration. The ID
            can be obtained from 'Get group profile template list' interface.
        dscp (str | Unset): The DSCP value selected in the DSCP configuration should be a value as follows: any: any; 8:
            IP precedence 1; 16: IP precedence 2; 24: IP precedence 3; 32: IP precedence 4; 40: IP precedence 5; 48: IP
            precedence 6; 56: IP precedence 7; 10: AF Class 1 (Low Drop); 12: AF Class 1 (Medium Drop); 14: AF Class 1 (High
            Drop); 18: AF Class 2 (Low Drop); 20: AF Class 2 (Medium Drop); 22: AF Class 2 (High Drop); 26: AF Class 3 (Low
            Drop); 28: AF Class 3 (Medium Drop); 30: AF Class 3 (High Drop); 34: AF Class 4 (Low Drop); 36: AF Class 4
            (Medium Drop); 38: AF Class 4 (High Drop); 46: EF Class.
        service_type (str | Unset): The ID of Gateway Qos Service selected in the Service Name configuration. The ID can
            be obtained from 'Get all Gateway QoS Service's ID and name info in siteTemplate' interface.
        class_type (int | Unset): The Class value selected in the Qos Class configuration should be a value as follows:
            1: Class 1, 2: Class 2, 3: Class 3.
    """

    id: str | Unset = UNSET
    enable: bool | Unset = UNSET
    ip_version: int | Unset = UNSET
    local_ip: str | Unset = UNSET
    remote_ip: str | Unset = UNSET
    dscp: str | Unset = UNSET
    service_type: str | Unset = UNSET
    class_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enable = self.enable

        ip_version = self.ip_version

        local_ip = self.local_ip

        remote_ip = self.remote_ip

        dscp = self.dscp

        service_type = self.service_type

        class_type = self.class_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if ip_version is not UNSET:
            field_dict["ipVersion"] = ip_version
        if local_ip is not UNSET:
            field_dict["localIp"] = local_ip
        if remote_ip is not UNSET:
            field_dict["remoteIp"] = remote_ip
        if dscp is not UNSET:
            field_dict["dscp"] = dscp
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type
        if class_type is not UNSET:
            field_dict["classType"] = class_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        enable = d.pop("enable", UNSET)

        ip_version = d.pop("ipVersion", UNSET)

        local_ip = d.pop("localIp", UNSET)

        remote_ip = d.pop("remoteIp", UNSET)

        dscp = d.pop("dscp", UNSET)

        service_type = d.pop("serviceType", UNSET)

        class_type = d.pop("classType", UNSET)

        class_rule_template_detail_open_api_vo = cls(
            id=id,
            enable=enable,
            ip_version=ip_version,
            local_ip=local_ip,
            remote_ip=remote_ip,
            dscp=dscp,
            service_type=service_type,
            class_type=class_type,
        )

        class_rule_template_detail_open_api_vo.additional_properties = d
        return class_rule_template_detail_open_api_vo

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
