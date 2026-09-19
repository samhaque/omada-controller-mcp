from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.msp_role_vo import MspRoleVO


T = TypeVar("T", bound="MspRoleDetailVO")


@_attrs_define
class MspRoleDetailVO:
    """
    Attributes:
        id (str | Unset): Role ID
        name (int | Unset): Role type
        default_role (bool | Unset): Whether role is default role
        privilege (MspRoleVO | Unset): Role privilege.
    """

    id: str | Unset = UNSET
    name: int | Unset = UNSET
    default_role: bool | Unset = UNSET
    privilege: MspRoleVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        default_role = self.default_role

        privilege: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if default_role is not UNSET:
            field_dict["defaultRole"] = default_role
        if privilege is not UNSET:
            field_dict["privilege"] = privilege

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.msp_role_vo import MspRoleVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        default_role = d.pop("defaultRole", UNSET)

        _privilege = d.pop("privilege", UNSET)
        privilege: MspRoleVO | Unset
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = MspRoleVO.from_dict(_privilege)

        msp_role_detail_vo = cls(
            id=id,
            name=name,
            default_role=default_role,
            privilege=privilege,
        )

        msp_role_detail_vo.additional_properties = d
        return msp_role_detail_vo

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
