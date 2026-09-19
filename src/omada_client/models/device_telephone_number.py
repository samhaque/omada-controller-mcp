from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telephone_number_with_status_open_api_vo import (
        TelephoneNumberWithStatusOpenApiVO,
    )


T = TypeVar("T", bound="DeviceTelephoneNumber")


@_attrs_define
class DeviceTelephoneNumber:
    """
    Attributes:
        id (str | Unset): The ID of voip device.
        mac (str | Unset): The mac of voip device.
        bind_number_list (list[TelephoneNumberWithStatusOpenApiVO] | Unset): The list of telephone number.
    """

    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    bind_number_list: list[TelephoneNumberWithStatusOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac = self.mac

        bind_number_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bind_number_list, Unset):
            bind_number_list = []
            for bind_number_list_item_data in self.bind_number_list:
                bind_number_list_item = bind_number_list_item_data.to_dict()
                bind_number_list.append(bind_number_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if bind_number_list is not UNSET:
            field_dict["bindNumberList"] = bind_number_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telephone_number_with_status_open_api_vo import (
            TelephoneNumberWithStatusOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        _bind_number_list = d.pop("bindNumberList", UNSET)
        bind_number_list: list[TelephoneNumberWithStatusOpenApiVO] | Unset = UNSET
        if _bind_number_list is not UNSET:
            bind_number_list = []
            for bind_number_list_item_data in _bind_number_list:
                bind_number_list_item = TelephoneNumberWithStatusOpenApiVO.from_dict(
                    bind_number_list_item_data
                )

                bind_number_list.append(bind_number_list_item)

        device_telephone_number = cls(
            id=id,
            mac=mac,
            bind_number_list=bind_number_list,
        )

        device_telephone_number.additional_properties = d
        return device_telephone_number

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
