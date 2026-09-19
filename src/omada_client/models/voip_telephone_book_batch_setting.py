from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="VoipTelephoneBookBatchSetting")


@_attrs_define
class VoipTelephoneBookBatchSetting:
    """
    Attributes:
        contact_ids (list[str]): Delete the contact ID of contact person.
        select_type (str): SpeedDialNumberType should be a value as follows: all, include, exclude.
        force_delete (bool): Other configurations depending on selected contacts (call forwarding rules for instance)
            will be deleted together if this field is true. Otherwise, a pre-check will be executed and an error message
            will be returned when this contact is already used in some other configurations.
    """

    contact_ids: list[str]
    select_type: str
    force_delete: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_ids = self.contact_ids

        select_type = self.select_type

        force_delete = self.force_delete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactIds": contact_ids,
                "selectType": select_type,
                "forceDelete": force_delete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        contact_ids = cast(list[str], d.pop("contactIds"))

        select_type = d.pop("selectType")

        force_delete = d.pop("forceDelete")

        voip_telephone_book_batch_setting = cls(
            contact_ids=contact_ids,
            select_type=select_type,
            force_delete=force_delete,
        )

        voip_telephone_book_batch_setting.additional_properties = d
        return voip_telephone_book_batch_setting

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
