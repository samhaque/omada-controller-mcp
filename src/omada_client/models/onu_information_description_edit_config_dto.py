from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="OnuInformationDescriptionEditConfigDTO")


@_attrs_define
class OnuInformationDescriptionEditConfigDTO:
    """
    Attributes:
        key (str): Identifier of ONU
        onu_description (str): ONU description should contain 1 to 32 characters, including uppercase and lowercase
            letters, numbers, and the symbols -@_:/.
    """

    key: str
    onu_description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        onu_description = self.onu_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "onuDescription": onu_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        onu_description = d.pop("onuDescription")

        onu_information_description_edit_config_dto = cls(
            key=key,
            onu_description=onu_description,
        )

        onu_information_description_edit_config_dto.additional_properties = d
        return onu_information_description_edit_config_dto

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
