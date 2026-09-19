from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperateMessage")


@_attrs_define
class OperateMessage:
    """
    Attributes:
        type_ (int): Message Type. 0: inbox; 1: outbox.
        operation (int): Operation Type. 1:delete; 2:read; 3:clear.
        ids (list[int] | Unset): Message ID list. When parameter [operation] is 1 or 2, parameter [ids] should not be
            null.
        sim_card (int | Unset): When the device supports Dual-SIM card, parameter [simCard] should not be null.1: SIM1;
            2: SIM2.
    """

    type_: int
    operation: int
    ids: list[int] | Unset = UNSET
    sim_card: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        operation = self.operation

        ids: list[int] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        sim_card = self.sim_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "operation": operation,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        operation = d.pop("operation")

        ids = cast(list[int], d.pop("ids", UNSET))

        sim_card = d.pop("simCard", UNSET)

        operate_message = cls(
            type_=type_,
            operation=operation,
            ids=ids,
            sim_card=sim_card,
        )

        operate_message.additional_properties = d
        return operate_message

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
