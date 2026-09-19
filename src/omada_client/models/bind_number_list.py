from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.telephone_number_without_status_open_api_vo import (
        TelephoneNumberWithoutStatusOpenApiVO,
    )


T = TypeVar("T", bound="BindNumberList")


@_attrs_define
class BindNumberList:
    """
    Attributes:
        bind_number_list (list[TelephoneNumberWithoutStatusOpenApiVO]): The list of telephone number without status.
    """

    bind_number_list: list[TelephoneNumberWithoutStatusOpenApiVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bind_number_list = []
        for bind_number_list_item_data in self.bind_number_list:
            bind_number_list_item = bind_number_list_item_data.to_dict()
            bind_number_list.append(bind_number_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bindNumberList": bind_number_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telephone_number_without_status_open_api_vo import (
            TelephoneNumberWithoutStatusOpenApiVO,
        )

        d = dict(src_dict)
        bind_number_list = []
        _bind_number_list = d.pop("bindNumberList")
        for bind_number_list_item_data in _bind_number_list:
            bind_number_list_item = TelephoneNumberWithoutStatusOpenApiVO.from_dict(
                bind_number_list_item_data
            )

            bind_number_list.append(bind_number_list_item)

        bind_number_list = cls(
            bind_number_list=bind_number_list,
        )

        bind_number_list.additional_properties = d
        return bind_number_list

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
