from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdoptTipOpenApiVO")


@_attrs_define
class AdoptTipOpenApiVO:
    """
    Attributes:
        adopt_device_num (int | Unset): Adopted device num
        recommend_device_num (int | Unset): Recommend adopt device num
    """

    adopt_device_num: int | Unset = UNSET
    recommend_device_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adopt_device_num = self.adopt_device_num

        recommend_device_num = self.recommend_device_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adopt_device_num is not UNSET:
            field_dict["adoptDeviceNum"] = adopt_device_num
        if recommend_device_num is not UNSET:
            field_dict["recommendDeviceNum"] = recommend_device_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        adopt_device_num = d.pop("adoptDeviceNum", UNSET)

        recommend_device_num = d.pop("recommendDeviceNum", UNSET)

        adopt_tip_open_api_vo = cls(
            adopt_device_num=adopt_device_num,
            recommend_device_num=recommend_device_num,
        )

        adopt_tip_open_api_vo.additional_properties = d
        return adopt_tip_open_api_vo

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
