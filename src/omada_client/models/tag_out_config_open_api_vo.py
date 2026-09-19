from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.tag_out_item_open_api_vo import TagOutItemOpenApiVO


T = TypeVar("T", bound="TagOutConfigOpenApiVO")


@_attrs_define
class TagOutConfigOpenApiVO:
    """
    Attributes:
        tag_config_list (list[TagOutItemOpenApiVO]): The Tag Outbound configuration of class type, must contains class
            1, class 2, class 3 and others.
    """

    tag_config_list: list[TagOutItemOpenApiVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_config_list = []
        for tag_config_list_item_data in self.tag_config_list:
            tag_config_list_item = tag_config_list_item_data.to_dict()
            tag_config_list.append(tag_config_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagConfigList": tag_config_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tag_out_item_open_api_vo import (
            TagOutItemOpenApiVO,
        )

        d = dict(src_dict)
        tag_config_list = []
        _tag_config_list = d.pop("tagConfigList")
        for tag_config_list_item_data in _tag_config_list:
            tag_config_list_item = TagOutItemOpenApiVO.from_dict(
                tag_config_list_item_data
            )

            tag_config_list.append(tag_config_list_item)

        tag_out_config_open_api_vo = cls(
            tag_config_list=tag_config_list,
        )

        tag_out_config_open_api_vo.additional_properties = d
        return tag_out_config_open_api_vo

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
