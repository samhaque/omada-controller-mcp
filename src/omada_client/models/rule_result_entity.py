from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_entity import ApplicationEntity


T = TypeVar("T", bound="RuleResultEntity")


@_attrs_define
class RuleResultEntity:
    """
    Attributes:
        rule_name (str | Unset): Rule name
        rule_id (int | Unset): Rule ID
        schedule (str | Unset): Schedule profile ID
        qos (bool | Unset): Enable qos. true:enable / false:disable
        qos_class (int | Unset): Qos class category
        applications (list[ApplicationEntity] | Unset): Application list
    """

    rule_name: str | Unset = UNSET
    rule_id: int | Unset = UNSET
    schedule: str | Unset = UNSET
    qos: bool | Unset = UNSET
    qos_class: int | Unset = UNSET
    applications: list[ApplicationEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_name = self.rule_name

        rule_id = self.rule_id

        schedule = self.schedule

        qos = self.qos

        qos_class = self.qos_class

        applications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.to_dict()
                applications.append(applications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if qos is not UNSET:
            field_dict["qos"] = qos
        if qos_class is not UNSET:
            field_dict["qosClass"] = qos_class
        if applications is not UNSET:
            field_dict["applications"] = applications

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.application_entity import ApplicationEntity

        d = dict(src_dict)
        rule_name = d.pop("ruleName", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        schedule = d.pop("schedule", UNSET)

        qos = d.pop("qos", UNSET)

        qos_class = d.pop("qosClass", UNSET)

        _applications = d.pop("applications", UNSET)
        applications: list[ApplicationEntity] | Unset = UNSET
        if _applications is not UNSET:
            applications = []
            for applications_item_data in _applications:
                applications_item = ApplicationEntity.from_dict(applications_item_data)

                applications.append(applications_item)

        rule_result_entity = cls(
            rule_name=rule_name,
            rule_id=rule_id,
            schedule=schedule,
            qos=qos,
            qos_class=qos_class,
            applications=applications,
        )

        rule_result_entity.additional_properties = d
        return rule_result_entity

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
