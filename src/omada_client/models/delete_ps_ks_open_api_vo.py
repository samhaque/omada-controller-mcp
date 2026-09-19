from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeletePSKsOpenApiVO")


@_attrs_define
class DeletePSKsOpenApiVO:
    """
    Attributes:
        ppsk_name_list (list[str]): PSK names that need to be deleted to the PPSK Profile
    """

    ppsk_name_list: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ppsk_name_list = self.ppsk_name_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ppskNameList": ppsk_name_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ppsk_name_list = cast(list[str], d.pop("ppskNameList"))

        delete_ps_ks_open_api_vo = cls(
            ppsk_name_list=ppsk_name_list,
        )

        delete_ps_ks_open_api_vo.additional_properties = d
        return delete_ps_ks_open_api_vo

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
