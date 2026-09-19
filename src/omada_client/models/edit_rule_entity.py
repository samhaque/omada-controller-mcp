from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditRuleEntity")


@_attrs_define
class EditRuleEntity:
    """
    Attributes:
        rule_name (str): Rule name. It should be 1 - 128 characters
        schedule (str): Schedule profile ID, which can be queried by request： Get time range profile list.
        qos (bool): Enable qos. true:enable / false:disable
        applications (list[int]): Application ID list can be obtained from 'Get application list' interface.
        qos_class (int | Unset): The Class value selected in the Qos Class configuration, required when qos is enable.
            Valid values is 0: Others, 1: Class 1, 2: Class 2, 3: Class 3.
    """

    rule_name: str
    schedule: str
    qos: bool
    applications: list[int]
    qos_class: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_name = self.rule_name

        schedule = self.schedule

        qos = self.qos

        applications = self.applications

        qos_class = self.qos_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ruleName": rule_name,
                "schedule": schedule,
                "qos": qos,
                "applications": applications,
            }
        )
        if qos_class is not UNSET:
            field_dict["qosClass"] = qos_class

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rule_name = d.pop("ruleName")

        schedule = d.pop("schedule")

        qos = d.pop("qos")

        applications = cast(list[int], d.pop("applications"))

        qos_class = d.pop("qosClass", UNSET)

        edit_rule_entity = cls(
            rule_name=rule_name,
            schedule=schedule,
            qos=qos,
            applications=applications,
            qos_class=qos_class,
        )

        edit_rule_entity.additional_properties = d
        return edit_rule_entity

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
