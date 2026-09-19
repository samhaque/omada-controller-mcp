from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telephone_number_without_status_open_api_vo import (
        TelephoneNumberWithoutStatusOpenApiVO,
    )


T = TypeVar("T", bound="TelephoneNumberListUpdateOpenApiVO")


@_attrs_define
class TelephoneNumberListUpdateOpenApiVO:
    """
    Attributes:
        add_telephone_numbers (list[TelephoneNumberWithoutStatusOpenApiVO] | Unset): Telephone numbers to be added.
        delete_telephone_number_ids (list[str] | Unset): Telephone number IDs to be deleted.
        modify_telephone_numbers (list[TelephoneNumberWithoutStatusOpenApiVO] | Unset): Telephone numbers to be
            modified.
    """

    add_telephone_numbers: list[TelephoneNumberWithoutStatusOpenApiVO] | Unset = UNSET
    delete_telephone_number_ids: list[str] | Unset = UNSET
    modify_telephone_numbers: list[TelephoneNumberWithoutStatusOpenApiVO] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_telephone_numbers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.add_telephone_numbers, Unset):
            add_telephone_numbers = []
            for add_telephone_numbers_item_data in self.add_telephone_numbers:
                add_telephone_numbers_item = add_telephone_numbers_item_data.to_dict()
                add_telephone_numbers.append(add_telephone_numbers_item)

        delete_telephone_number_ids: list[str] | Unset = UNSET
        if not isinstance(self.delete_telephone_number_ids, Unset):
            delete_telephone_number_ids = self.delete_telephone_number_ids

        modify_telephone_numbers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modify_telephone_numbers, Unset):
            modify_telephone_numbers = []
            for modify_telephone_numbers_item_data in self.modify_telephone_numbers:
                modify_telephone_numbers_item = (
                    modify_telephone_numbers_item_data.to_dict()
                )
                modify_telephone_numbers.append(modify_telephone_numbers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_telephone_numbers is not UNSET:
            field_dict["addTelephoneNumbers"] = add_telephone_numbers
        if delete_telephone_number_ids is not UNSET:
            field_dict["deleteTelephoneNumberIds"] = delete_telephone_number_ids
        if modify_telephone_numbers is not UNSET:
            field_dict["modifyTelephoneNumbers"] = modify_telephone_numbers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telephone_number_without_status_open_api_vo import (
            TelephoneNumberWithoutStatusOpenApiVO,
        )

        d = dict(src_dict)
        _add_telephone_numbers = d.pop("addTelephoneNumbers", UNSET)
        add_telephone_numbers: list[TelephoneNumberWithoutStatusOpenApiVO] | Unset = (
            UNSET
        )
        if _add_telephone_numbers is not UNSET:
            add_telephone_numbers = []
            for add_telephone_numbers_item_data in _add_telephone_numbers:
                add_telephone_numbers_item = (
                    TelephoneNumberWithoutStatusOpenApiVO.from_dict(
                        add_telephone_numbers_item_data
                    )
                )

                add_telephone_numbers.append(add_telephone_numbers_item)

        delete_telephone_number_ids = cast(
            list[str], d.pop("deleteTelephoneNumberIds", UNSET)
        )

        _modify_telephone_numbers = d.pop("modifyTelephoneNumbers", UNSET)
        modify_telephone_numbers: (
            list[TelephoneNumberWithoutStatusOpenApiVO] | Unset
        ) = UNSET
        if _modify_telephone_numbers is not UNSET:
            modify_telephone_numbers = []
            for modify_telephone_numbers_item_data in _modify_telephone_numbers:
                modify_telephone_numbers_item = (
                    TelephoneNumberWithoutStatusOpenApiVO.from_dict(
                        modify_telephone_numbers_item_data
                    )
                )

                modify_telephone_numbers.append(modify_telephone_numbers_item)

        telephone_number_list_update_open_api_vo = cls(
            add_telephone_numbers=add_telephone_numbers,
            delete_telephone_number_ids=delete_telephone_number_ids,
            modify_telephone_numbers=modify_telephone_numbers,
        )

        telephone_number_list_update_open_api_vo.additional_properties = d
        return telephone_number_list_update_open_api_vo

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
