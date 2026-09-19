from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.privilege_result_vo_sites_item_additional_property import (
        PrivilegeResultVOSitesItemAdditionalProperty,
    )


T = TypeVar("T", bound="PrivilegeResultVOSitesItem")


@_attrs_define
class PrivilegeResultVOSitesItem:
    """user site privilege list"""

    additional_properties: dict[str, PrivilegeResultVOSitesItemAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.privilege_result_vo_sites_item_additional_property import (
            PrivilegeResultVOSitesItemAdditionalProperty,
        )

        d = dict(src_dict)
        privilege_result_vo_sites_item = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                PrivilegeResultVOSitesItemAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        privilege_result_vo_sites_item.additional_properties = additional_properties
        return privilege_result_vo_sites_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PrivilegeResultVOSitesItemAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: PrivilegeResultVOSitesItemAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
