from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationEntity")


@_attrs_define
class ApplicationEntity:
    """Application list

    Attributes:
        application_name (str | Unset): Application name
        application_id (int | Unset): Application ID
        description (str | Unset): Description of application
        family (str | Unset): Family of application
    """

    application_name: str | Unset = UNSET
    application_id: int | Unset = UNSET
    description: str | Unset = UNSET
    family: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        application_id = self.application_id

        description = self.description

        family = self.family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if description is not UNSET:
            field_dict["description"] = description
        if family is not UNSET:
            field_dict["family"] = family

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        application_name = d.pop("applicationName", UNSET)

        application_id = d.pop("applicationId", UNSET)

        description = d.pop("description", UNSET)

        family = d.pop("family", UNSET)

        application_entity = cls(
            application_name=application_name,
            application_id=application_id,
            description=description,
            family=family,
        )

        application_entity.additional_properties = d
        return application_entity

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
