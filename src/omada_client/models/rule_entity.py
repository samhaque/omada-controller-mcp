from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleEntity")


@_attrs_define
class RuleEntity:
    """Rule list

    Attributes:
        rule_name (str | Unset): Rule name
        rule_id (int | Unset): Rule ID
    """

    rule_name: str | Unset = UNSET
    rule_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_name = self.rule_name

        rule_id = self.rule_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rule_name = d.pop("ruleName", UNSET)

        rule_id = d.pop("ruleId", UNSET)

        rule_entity = cls(
            rule_name=rule_name,
            rule_id=rule_id,
        )

        rule_entity.additional_properties = d
        return rule_entity

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
