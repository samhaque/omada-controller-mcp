from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DDMStatusRequestVO")


@_attrs_define
class DDMStatusRequestVO:
    """
    Attributes:
        port_list (list[str] | Unset): Port list of device
    """

    port_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_list: list[str] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_list = cast(list[str], d.pop("portList", UNSET))

        ddm_status_request_vo = cls(
            port_list=port_list,
        )

        ddm_status_request_vo.additional_properties = d
        return ddm_status_request_vo

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
