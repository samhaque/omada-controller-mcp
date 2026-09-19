from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_brief_port_info_open_api_vo import OswBriefPortInfoOpenApiVO


T = TypeVar("T", bound="OswCableTestTestingPortOpenApiVO")


@_attrs_define
class OswCableTestTestingPortOpenApiVO:
    """
    Attributes:
        port_list (list[OswBriefPortInfoOpenApiVO] | Unset): Port list
    """

    port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = []
            for port_list_item_data in self.port_list:
                port_list_item = port_list_item_data.to_dict()
                port_list.append(port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_brief_port_info_open_api_vo import (
            OswBriefPortInfoOpenApiVO,
        )

        d = dict(src_dict)
        _port_list = d.pop("portList", UNSET)
        port_list: list[OswBriefPortInfoOpenApiVO] | Unset = UNSET
        if _port_list is not UNSET:
            port_list = []
            for port_list_item_data in _port_list:
                port_list_item = OswBriefPortInfoOpenApiVO.from_dict(
                    port_list_item_data
                )

                port_list.append(port_list_item)

        osw_cable_test_testing_port_open_api_vo = cls(
            port_list=port_list,
        )

        osw_cable_test_testing_port_open_api_vo.additional_properties = d
        return osw_cable_test_testing_port_open_api_vo

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
