from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telephone_number_with_status_vo import TelephoneNumberWithStatusVO


T = TypeVar("T", bound="NumberRegistrationResult")


@_attrs_define
class NumberRegistrationResult:
    """
    Attributes:
        registration_result_list (list[TelephoneNumberWithStatusVO] | Unset): The list of registration result.
    """

    registration_result_list: list[TelephoneNumberWithStatusVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registration_result_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.registration_result_list, Unset):
            registration_result_list = []
            for registration_result_list_item_data in self.registration_result_list:
                registration_result_list_item = (
                    registration_result_list_item_data.to_dict()
                )
                registration_result_list.append(registration_result_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registration_result_list is not UNSET:
            field_dict["registrationResultList"] = registration_result_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telephone_number_with_status_vo import (
            TelephoneNumberWithStatusVO,
        )

        d = dict(src_dict)
        _registration_result_list = d.pop("registrationResultList", UNSET)
        registration_result_list: list[TelephoneNumberWithStatusVO] | Unset = UNSET
        if _registration_result_list is not UNSET:
            registration_result_list = []
            for registration_result_list_item_data in _registration_result_list:
                registration_result_list_item = TelephoneNumberWithStatusVO.from_dict(
                    registration_result_list_item_data
                )

                registration_result_list.append(registration_result_list_item)

        number_registration_result = cls(
            registration_result_list=registration_result_list,
        )

        number_registration_result.additional_properties = d
        return number_registration_result

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
