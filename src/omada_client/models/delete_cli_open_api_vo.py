from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCliOpenApiVO")


@_attrs_define
class DeleteCliOpenApiVO:
    """Delete the CLI configuration entry

    Attributes:
        config_ids (list[str] | Unset): List of IDs to be deleted.
    """

    config_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_ids: list[str] | Unset = UNSET
        if not isinstance(self.config_ids, Unset):
            config_ids = self.config_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_ids is not UNSET:
            field_dict["configIds"] = config_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        config_ids = cast(list[str], d.pop("configIds", UNSET))

        delete_cli_open_api_vo = cls(
            config_ids=config_ids,
        )

        delete_cli_open_api_vo.additional_properties = d
        return delete_cli_open_api_vo

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
