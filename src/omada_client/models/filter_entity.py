from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_entity import RuleEntity


T = TypeVar("T", bound="FilterEntity")


@_attrs_define
class FilterEntity:
    """
    Attributes:
        filter_name (str | Unset): Filter name
        filter_id (int | Unset): Filter ID
        description (str | Unset): Description of filter
        rules (list[RuleEntity] | Unset): Rule list
    """

    filter_name: str | Unset = UNSET
    filter_id: int | Unset = UNSET
    description: str | Unset = UNSET
    rules: list[RuleEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_name = self.filter_name

        filter_id = self.filter_id

        description = self.description

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_name is not UNSET:
            field_dict["filterName"] = filter_name
        if filter_id is not UNSET:
            field_dict["filterId"] = filter_id
        if description is not UNSET:
            field_dict["description"] = description
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rule_entity import RuleEntity

        d = dict(src_dict)
        filter_name = d.pop("filterName", UNSET)

        filter_id = d.pop("filterId", UNSET)

        description = d.pop("description", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: list[RuleEntity] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = RuleEntity.from_dict(rules_item_data)

                rules.append(rules_item)

        filter_entity = cls(
            filter_name=filter_name,
            filter_id=filter_id,
            description=description,
            rules=rules,
        )

        filter_entity.additional_properties = d
        return filter_entity

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
