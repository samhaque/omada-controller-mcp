from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_open_api_vo_new_value import AuditLogOpenApiVONewValue
    from ..models.audit_log_open_api_vo_old_value import AuditLogOpenApiVOOldValue


T = TypeVar("T", bound="AuditLogOpenApiVO")


@_attrs_define
class AuditLogOpenApiVO:
    """
    Attributes:
        time (int | Unset): Log Creation TimeStamp, Unit:ms Example: 1677660067182.
        operator (str | Unset): Operator Example: user1.
        resource (str | Unset): Log Creation Resource. It should be a value as follows: WEB、Open API Example: WEB.
        ip (str | Unset): User Login IP address Example: 127.0.0.1.
        audit_type (str | Unset): Log Type Example: Log.
        level (str | Unset): Log Level. It should be a value as follows: Error, Warning, Information. Example:
            Information.
        result (str | Unset): Operation Result, it should be a value as follows: Succeed、Failed Example: Succeed.
        content (str | Unset): Log Content Example: Dashboard Tab test-Tab added successfully..
        label (str | Unset): Configuration card or request path, may be empty. Example: MENU.CLIENTS or
            /openapi/v1/{omadacId}/sites/{siteId}/site/reset/log-notification.
        old_value (AuditLogOpenApiVOOldValue | Unset): Configuration before modification, may be empty. Example: {'dpi':
            'false', 'loggingTraffic': 'false'}.
        new_value (AuditLogOpenApiVONewValue | Unset): Configuration after modification, may be empty. Example: {'dpi':
            'true', 'loggingTraffic': 'true'}.
    """

    time: int | Unset = UNSET
    operator: str | Unset = UNSET
    resource: str | Unset = UNSET
    ip: str | Unset = UNSET
    audit_type: str | Unset = UNSET
    level: str | Unset = UNSET
    result: str | Unset = UNSET
    content: str | Unset = UNSET
    label: str | Unset = UNSET
    old_value: AuditLogOpenApiVOOldValue | Unset = UNSET
    new_value: AuditLogOpenApiVONewValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        operator = self.operator

        resource = self.resource

        ip = self.ip

        audit_type = self.audit_type

        level = self.level

        result = self.result

        content = self.content

        label = self.label

        old_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.old_value, Unset):
            old_value = self.old_value.to_dict()

        new_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_value, Unset):
            new_value = self.new_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if operator is not UNSET:
            field_dict["operator"] = operator
        if resource is not UNSET:
            field_dict["resource"] = resource
        if ip is not UNSET:
            field_dict["ip"] = ip
        if audit_type is not UNSET:
            field_dict["auditType"] = audit_type
        if level is not UNSET:
            field_dict["level"] = level
        if result is not UNSET:
            field_dict["result"] = result
        if content is not UNSET:
            field_dict["content"] = content
        if label is not UNSET:
            field_dict["label"] = label
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if new_value is not UNSET:
            field_dict["newValue"] = new_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_log_open_api_vo_new_value import (
            AuditLogOpenApiVONewValue,
        )
        from ..models.audit_log_open_api_vo_old_value import (
            AuditLogOpenApiVOOldValue,
        )

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        operator = d.pop("operator", UNSET)

        resource = d.pop("resource", UNSET)

        ip = d.pop("ip", UNSET)

        audit_type = d.pop("auditType", UNSET)

        level = d.pop("level", UNSET)

        result = d.pop("result", UNSET)

        content = d.pop("content", UNSET)

        label = d.pop("label", UNSET)

        _old_value = d.pop("oldValue", UNSET)
        old_value: AuditLogOpenApiVOOldValue | Unset
        if isinstance(_old_value, Unset):
            old_value = UNSET
        else:
            old_value = AuditLogOpenApiVOOldValue.from_dict(_old_value)

        _new_value = d.pop("newValue", UNSET)
        new_value: AuditLogOpenApiVONewValue | Unset
        if isinstance(_new_value, Unset):
            new_value = UNSET
        else:
            new_value = AuditLogOpenApiVONewValue.from_dict(_new_value)

        audit_log_open_api_vo = cls(
            time=time,
            operator=operator,
            resource=resource,
            ip=ip,
            audit_type=audit_type,
            level=level,
            result=result,
            content=content,
            label=label,
            old_value=old_value,
            new_value=new_value,
        )

        audit_log_open_api_vo.additional_properties = d
        return audit_log_open_api_vo

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
