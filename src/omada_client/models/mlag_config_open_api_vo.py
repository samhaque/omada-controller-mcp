from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mlag_member_config_vo import MlagMemberConfigVO


T = TypeVar("T", bound="MlagConfigOpenApiVO")


@_attrs_define
class MlagConfigOpenApiVO:
    """
    Attributes:
        name (str): MLAG group name should be between 1 and 31 characters. Only letters, numbers, and the following
            symbols are allowed: - . / : @ _ + #
        members_config (list[MlagMemberConfigVO] | Unset): M-LAG group members configuration
    """

    name: str
    members_config: list[MlagMemberConfigVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        members_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members_config, Unset):
            members_config = []
            for members_config_item_data in self.members_config:
                members_config_item = members_config_item_data.to_dict()
                members_config.append(members_config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if members_config is not UNSET:
            field_dict["membersConfig"] = members_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mlag_member_config_vo import MlagMemberConfigVO

        d = dict(src_dict)
        name = d.pop("name")

        _members_config = d.pop("membersConfig", UNSET)
        members_config: list[MlagMemberConfigVO] | Unset = UNSET
        if _members_config is not UNSET:
            members_config = []
            for members_config_item_data in _members_config:
                members_config_item = MlagMemberConfigVO.from_dict(
                    members_config_item_data
                )

                members_config.append(members_config_item)

        mlag_config_open_api_vo = cls(
            name=name,
            members_config=members_config,
        )

        mlag_config_open_api_vo.additional_properties = d
        return mlag_config_open_api_vo

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
