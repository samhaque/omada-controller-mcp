from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_role_vo import ControllerRoleVO


T = TypeVar("T", bound="ModifyControllerRoleVO")


@_attrs_define
class ModifyControllerRoleVO:
    """
    Attributes:
        name (str): Role name should contain 1 to 128 characters.
        privilege (ControllerRoleVO | Unset): Role privilege
    """

    name: str
    privilege: ControllerRoleVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        privilege: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if privilege is not UNSET:
            field_dict["privilege"] = privilege

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.controller_role_vo import ControllerRoleVO

        d = dict(src_dict)
        name = d.pop("name")

        _privilege = d.pop("privilege", UNSET)
        privilege: ControllerRoleVO | Unset
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = ControllerRoleVO.from_dict(_privilege)

        modify_controller_role_vo = cls(
            name=name,
            privilege=privilege,
        )

        modify_controller_role_vo.additional_properties = d
        return modify_controller_role_vo

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
