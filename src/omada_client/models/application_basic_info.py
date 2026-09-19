from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationBasicInfo")


@_attrs_define
class ApplicationBasicInfo:
    """The applications info using by the client.

    Attributes:
        application_name (str | Unset): The name of the application.
        application_id (int | Unset): The id of the application.
    """

    application_name: str | Unset = UNSET
    application_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        application_id = self.application_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        application_name = d.pop("applicationName", UNSET)

        application_id = d.pop("applicationId", UNSET)

        application_basic_info = cls(
            application_name=application_name,
            application_id=application_id,
        )

        application_basic_info.additional_properties = d
        return application_basic_info

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
