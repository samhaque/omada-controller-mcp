from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ClientExportOpenApiVO")


@_attrs_define
class ClientExportOpenApiVO:
    """
    Attributes:
        format_ (int): Format should be a value as follows: 0: csv; 1: xlsx.
        tables (list[int]): Tables should be a list of follows: 0: online; 1: offline; 2: blocked; 3: past-connection,
            4: past-portal-auth.
    """

    format_: int
    tables: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        tables = self.tables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "tables": tables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        format_ = d.pop("format")

        tables = cast(list[int], d.pop("tables"))

        client_export_open_api_vo = cls(
            format_=format_,
            tables=tables,
        )

        client_export_open_api_vo.additional_properties = d
        return client_export_open_api_vo

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
