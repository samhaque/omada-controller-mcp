from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_action_entity import RequestActionEntity


T = TypeVar("T", bound="BatchRequestEntity")


@_attrs_define
class BatchRequestEntity:
    """
    Attributes:
        interrupt (bool | Unset): Indicates whether to interrupt execution when encountering an error while executing
            openAPI, defaults to true
        actions (list[RequestActionEntity] | Unset): List of OpenAPIs that require batch execution. Up to 20 entries are
            allowed for the action list
    """

    interrupt: bool | Unset = UNSET
    actions: list[RequestActionEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interrupt = self.interrupt

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interrupt is not UNSET:
            field_dict["interrupt"] = interrupt
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.request_action_entity import RequestActionEntity

        d = dict(src_dict)
        interrupt = d.pop("interrupt", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[RequestActionEntity] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = RequestActionEntity.from_dict(actions_item_data)

                actions.append(actions_item)

        batch_request_entity = cls(
            interrupt=interrupt,
            actions=actions,
        )

        batch_request_entity.additional_properties = d
        return batch_request_entity

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
