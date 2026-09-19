from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="BatchCopySiteTemplateOpenApiVO")


@_attrs_define
class BatchCopySiteTemplateOpenApiVO:
    """
    Attributes:
        name (str): Name of the site should contain 1 to 64 characters.
        target_omadacs (list[str]): The target Customer ID needs to be obtained from the interface "Obtain the customer
            ID with permission to modify site templates".
    """

    name: str
    target_omadacs: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        target_omadacs = self.target_omadacs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "targetOmadacs": target_omadacs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        target_omadacs = cast(list[str], d.pop("targetOmadacs"))

        batch_copy_site_template_open_api_vo = cls(
            name=name,
            target_omadacs=target_omadacs,
        )

        batch_copy_site_template_open_api_vo.additional_properties = d
        return batch_copy_site_template_open_api_vo

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
