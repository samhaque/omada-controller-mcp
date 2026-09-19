from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_member_cable_test_vo import OswStackMemberCableTestVO


T = TypeVar("T", bound="OswStackCableTestVO")


@_attrs_define
class OswStackCableTestVO:
    """
    Attributes:
        name (str | Unset): stack name
        stack_id (str | Unset): stack ID
        member (list[OswStackMemberCableTestVO] | Unset): stack member list
    """

    name: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    member: list[OswStackMemberCableTestVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        stack_id = self.stack_id

        member: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = []
            for member_item_data in self.member:
                member_item = member_item_data.to_dict()
                member.append(member_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_member_cable_test_vo import (
            OswStackMemberCableTestVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        stack_id = d.pop("stackId", UNSET)

        _member = d.pop("member", UNSET)
        member: list[OswStackMemberCableTestVO] | Unset = UNSET
        if _member is not UNSET:
            member = []
            for member_item_data in _member:
                member_item = OswStackMemberCableTestVO.from_dict(member_item_data)

                member.append(member_item)

        osw_stack_cable_test_vo = cls(
            name=name,
            stack_id=stack_id,
            member=member,
        )

        osw_stack_cable_test_vo.additional_properties = d
        return osw_stack_cable_test_vo

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
