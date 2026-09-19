from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isp_vo import IspVO


T = TypeVar("T", bound="IspInfoVO")


@_attrs_define
class IspInfoVO:
    """Isp info.

    Attributes:
        type_ (int | Unset): Isp type, should be a value as follows:0 : single ISP1 : multiple ISPs
        isp_arr (list[IspVO] | Unset): Isp info detail.
    """

    type_: int | Unset = UNSET
    isp_arr: list[IspVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        isp_arr: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.isp_arr, Unset):
            isp_arr = []
            for isp_arr_item_data in self.isp_arr:
                isp_arr_item = isp_arr_item_data.to_dict()
                isp_arr.append(isp_arr_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if isp_arr is not UNSET:
            field_dict["ispArr"] = isp_arr

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.isp_vo import IspVO

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _isp_arr = d.pop("ispArr", UNSET)
        isp_arr: list[IspVO] | Unset = UNSET
        if _isp_arr is not UNSET:
            isp_arr = []
            for isp_arr_item_data in _isp_arr:
                isp_arr_item = IspVO.from_dict(isp_arr_item_data)

                isp_arr.append(isp_arr_item)

        isp_info_vo = cls(
            type_=type_,
            isp_arr=isp_arr,
        )

        isp_info_vo.additional_properties = d
        return isp_info_vo

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
