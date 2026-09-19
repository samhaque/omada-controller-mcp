from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ClassRuleTemplateOpenApiVO")


@_attrs_define
class ClassRuleTemplateOpenApiVO:
    """
    Attributes:
        enable (bool): The status of class rule. valid values are true or false.
        ip_version (int): The IP Version of class rule should be a value as follows: 0: IPv4; 1: IPv6.
        local_ip (str): The ID of IP Group or IPv6 Group selected in the Local Address configuration. The ID can be
            obtained from 'Get group profile template list' interface.
        remote_ip (str): The ID of IP Group or IPv6 Group selected in the Remote Address configuration. The ID can be
            obtained from 'Get group profile template list' interface.
        dscp (str): The DSCP value selected in the DSCP configuration should be a value as follows: any: any; 8: IP
            precedence 1; 16: IP precedence 2; 24: IP precedence 3; 32: IP precedence 4; 40: IP precedence 5; 48: IP
            precedence 6; 56: IP precedence 7; 10: AF Class 1 (Low Drop); 12: AF Class 1 (Medium Drop); 14: AF Class 1 (High
            Drop); 18: AF Class 2 (Low Drop); 20: AF Class 2 (Medium Drop); 22: AF Class 2 (High Drop); 26: AF Class 3 (Low
            Drop); 28: AF Class 3 (Medium Drop); 30: AF Class 3 (High Drop); 34: AF Class 4 (Low Drop); 36: AF Class 4
            (Medium Drop); 38: AF Class 4 (High Drop); 46: EF Class.
        service_type (str): The ID of Gateway Qos Service selected in the Service Name configuration. The ID can be
            obtained from 'Get all Gateway QoS Service's ID and name info in siteTemplate' interface.
        class_type (int): The Class value selected in the Qos Class configuration should be a value as follows: 1: Class
            1, 2: Class 2, 3: Class 3.
    """

    enable: bool
    ip_version: int
    local_ip: str
    remote_ip: str
    dscp: str
    service_type: str
    class_type: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        ip_version = self.ip_version

        local_ip = self.local_ip

        remote_ip = self.remote_ip

        dscp = self.dscp

        service_type = self.service_type

        class_type = self.class_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "ipVersion": ip_version,
                "localIp": local_ip,
                "remoteIp": remote_ip,
                "dscp": dscp,
                "serviceType": service_type,
                "classType": class_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        ip_version = d.pop("ipVersion")

        local_ip = d.pop("localIp")

        remote_ip = d.pop("remoteIp")

        dscp = d.pop("dscp")

        service_type = d.pop("serviceType")

        class_type = d.pop("classType")

        class_rule_template_open_api_vo = cls(
            enable=enable,
            ip_version=ip_version,
            local_ip=local_ip,
            remote_ip=remote_ip,
            dscp=dscp,
            service_type=service_type,
            class_type=class_type,
        )

        class_rule_template_open_api_vo.additional_properties = d
        return class_rule_template_open_api_vo

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
