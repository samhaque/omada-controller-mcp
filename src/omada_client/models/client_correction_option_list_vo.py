from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_correction_option_vo import ClientCorrectionOptionVO


T = TypeVar("T", bound="ClientCorrectionOptionListVO")


@_attrs_define
class ClientCorrectionOptionListVO:
    """
    Attributes:
        type_list (list[ClientCorrectionOptionVO] | Unset):
        vendor_list (list[ClientCorrectionOptionVO] | Unset):
    """

    type_list: list[ClientCorrectionOptionVO] | Unset = UNSET
    vendor_list: list[ClientCorrectionOptionVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.type_list, Unset):
            type_list = []
            for type_list_item_data in self.type_list:
                type_list_item = type_list_item_data.to_dict()
                type_list.append(type_list_item)

        vendor_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vendor_list, Unset):
            vendor_list = []
            for vendor_list_item_data in self.vendor_list:
                vendor_list_item = vendor_list_item_data.to_dict()
                vendor_list.append(vendor_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_list is not UNSET:
            field_dict["typeList"] = type_list
        if vendor_list is not UNSET:
            field_dict["vendorList"] = vendor_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_correction_option_vo import (
            ClientCorrectionOptionVO,
        )

        d = dict(src_dict)
        _type_list = d.pop("typeList", UNSET)
        type_list: list[ClientCorrectionOptionVO] | Unset = UNSET
        if _type_list is not UNSET:
            type_list = []
            for type_list_item_data in _type_list:
                type_list_item = ClientCorrectionOptionVO.from_dict(type_list_item_data)

                type_list.append(type_list_item)

        _vendor_list = d.pop("vendorList", UNSET)
        vendor_list: list[ClientCorrectionOptionVO] | Unset = UNSET
        if _vendor_list is not UNSET:
            vendor_list = []
            for vendor_list_item_data in _vendor_list:
                vendor_list_item = ClientCorrectionOptionVO.from_dict(
                    vendor_list_item_data
                )

                vendor_list.append(vendor_list_item)

        client_correction_option_list_vo = cls(
            type_list=type_list,
            vendor_list=vendor_list,
        )

        client_correction_option_list_vo.additional_properties = d
        return client_correction_option_list_vo

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
