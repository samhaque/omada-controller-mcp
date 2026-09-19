from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wan_detail_vo import WanDetailVO


T = TypeVar("T", bound="WanDetails")


@_attrs_define
class WanDetails:
    """
    Attributes:
        wan_details (list[WanDetailVO] | Unset): Gateway wan port detail list
    """

    wan_details: list[WanDetailVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_details, Unset):
            wan_details = []
            for wan_details_item_data in self.wan_details:
                wan_details_item = wan_details_item_data.to_dict()
                wan_details.append(wan_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wan_details is not UNSET:
            field_dict["wanDetails"] = wan_details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_detail_vo import WanDetailVO

        d = dict(src_dict)
        _wan_details = d.pop("wanDetails", UNSET)
        wan_details: list[WanDetailVO] | Unset = UNSET
        if _wan_details is not UNSET:
            wan_details = []
            for wan_details_item_data in _wan_details:
                wan_details_item = WanDetailVO.from_dict(wan_details_item_data)

                wan_details.append(wan_details_item)

        wan_details = cls(
            wan_details=wan_details,
        )

        wan_details.additional_properties = d
        return wan_details

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
