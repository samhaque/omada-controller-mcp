from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_vo import RoleVO


T = TypeVar("T", bound="RoleDetailVO")


@_attrs_define
class RoleDetailVO:
    """
    Attributes:
        name (str): Role name should contain 1 to 128 ASCII characters.
        id (str | Unset): Role Detail ID
        type_ (int | Unset): Role Type should be a value as follows: 0: standard; 1: customer; 2: msp.
        default_role (bool | Unset): Whether role is default role.
        source (int | Unset): Role created resource. It should be a value as follows: 0: default; 1:create by standard
            controller or customer controller; 2: create by MSP
        privilege (RoleVO | Unset): Role privilege
        has_all_privilege (bool | Unset): Whether role has all site privilege.
        owner (bool | Unset): Whether role is owner.
    """

    name: str
    id: str | Unset = UNSET
    type_: int | Unset = UNSET
    default_role: bool | Unset = UNSET
    source: int | Unset = UNSET
    privilege: RoleVO | Unset = UNSET
    has_all_privilege: bool | Unset = UNSET
    owner: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        type_ = self.type_

        default_role = self.default_role

        source = self.source

        privilege: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.to_dict()

        has_all_privilege = self.has_all_privilege

        owner = self.owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if default_role is not UNSET:
            field_dict["defaultRole"] = default_role
        if source is not UNSET:
            field_dict["source"] = source
        if privilege is not UNSET:
            field_dict["privilege"] = privilege
        if has_all_privilege is not UNSET:
            field_dict["hasAllPrivilege"] = has_all_privilege
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.role_vo import RoleVO

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        default_role = d.pop("defaultRole", UNSET)

        source = d.pop("source", UNSET)

        _privilege = d.pop("privilege", UNSET)
        privilege: RoleVO | Unset
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = RoleVO.from_dict(_privilege)

        has_all_privilege = d.pop("hasAllPrivilege", UNSET)

        owner = d.pop("owner", UNSET)

        role_detail_vo = cls(
            name=name,
            id=id,
            type_=type_,
            default_role=default_role,
            source=source,
            privilege=privilege,
            has_all_privilege=has_all_privilege,
            owner=owner,
        )

        role_detail_vo.additional_properties = d
        return role_detail_vo

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
