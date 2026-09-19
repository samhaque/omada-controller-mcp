from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wan_health_item_vo import WanHealthItemVO


T = TypeVar("T", bound="WanHealthListVO")


@_attrs_define
class WanHealthListVO:
    """WAN health score detail

    Attributes:
        wan_list (list[WanHealthItemVO] | Unset):
    """

    wan_list: list[WanHealthItemVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_list, Unset):
            wan_list = []
            for wan_list_item_data in self.wan_list:
                wan_list_item = wan_list_item_data.to_dict()
                wan_list.append(wan_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wan_list is not UNSET:
            field_dict["wanList"] = wan_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_health_item_vo import WanHealthItemVO

        d = dict(src_dict)
        _wan_list = d.pop("wanList", UNSET)
        wan_list: list[WanHealthItemVO] | Unset = UNSET
        if _wan_list is not UNSET:
            wan_list = []
            for wan_list_item_data in _wan_list:
                wan_list_item = WanHealthItemVO.from_dict(wan_list_item_data)

                wan_list.append(wan_list_item)

        wan_health_list_vo = cls(
            wan_list=wan_list,
        )

        wan_health_list_vo.additional_properties = d
        return wan_health_list_vo

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
