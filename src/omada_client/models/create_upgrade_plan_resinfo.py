from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUpgradePlanResinfo")


@_attrs_define
class CreateUpgradePlanResinfo:
    """
    Attributes:
        upgrade_id_list (list[str] | Unset): Upgrade ID list
    """

    upgrade_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upgrade_id_list: list[str] | Unset = UNSET
        if not isinstance(self.upgrade_id_list, Unset):
            upgrade_id_list = self.upgrade_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upgrade_id_list is not UNSET:
            field_dict["upgradeIdList"] = upgrade_id_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upgrade_id_list = cast(list[str], d.pop("upgradeIdList", UNSET))

        create_upgrade_plan_resinfo = cls(
            upgrade_id_list=upgrade_id_list,
        )

        create_upgrade_plan_resinfo.additional_properties = d
        return create_upgrade_plan_resinfo

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
