from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.locate_osw_result_open_api_vo import LocateOswResultOpenApiVO
    from ..models.locate_stack_result_open_api_vo import LocateStackResultOpenApiVO


T = TypeVar("T", bound="LocateOswPortsResultOpenApiVO")


@_attrs_define
class LocateOswPortsResultOpenApiVO:
    """
    Attributes:
        locate_osw_ports_result_list (list[LocateOswResultOpenApiVO] | Unset): Locate switch ports error information
        locate_stack_ports_result_list (list[LocateStackResultOpenApiVO] | Unset): Locate stack ports error information
    """

    locate_osw_ports_result_list: list[LocateOswResultOpenApiVO] | Unset = UNSET
    locate_stack_ports_result_list: list[LocateStackResultOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locate_osw_ports_result_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locate_osw_ports_result_list, Unset):
            locate_osw_ports_result_list = []
            for (
                locate_osw_ports_result_list_item_data
            ) in self.locate_osw_ports_result_list:
                locate_osw_ports_result_list_item = (
                    locate_osw_ports_result_list_item_data.to_dict()
                )
                locate_osw_ports_result_list.append(locate_osw_ports_result_list_item)

        locate_stack_ports_result_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locate_stack_ports_result_list, Unset):
            locate_stack_ports_result_list = []
            for (
                locate_stack_ports_result_list_item_data
            ) in self.locate_stack_ports_result_list:
                locate_stack_ports_result_list_item = (
                    locate_stack_ports_result_list_item_data.to_dict()
                )
                locate_stack_ports_result_list.append(
                    locate_stack_ports_result_list_item
                )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locate_osw_ports_result_list is not UNSET:
            field_dict["locateOswPortsResultList"] = locate_osw_ports_result_list
        if locate_stack_ports_result_list is not UNSET:
            field_dict["locateStackPortsResultList"] = locate_stack_ports_result_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.locate_osw_result_open_api_vo import (
            LocateOswResultOpenApiVO,
        )
        from ..models.locate_stack_result_open_api_vo import (
            LocateStackResultOpenApiVO,
        )

        d = dict(src_dict)
        _locate_osw_ports_result_list = d.pop("locateOswPortsResultList", UNSET)
        locate_osw_ports_result_list: list[LocateOswResultOpenApiVO] | Unset = UNSET
        if _locate_osw_ports_result_list is not UNSET:
            locate_osw_ports_result_list = []
            for locate_osw_ports_result_list_item_data in _locate_osw_ports_result_list:
                locate_osw_ports_result_list_item = LocateOswResultOpenApiVO.from_dict(
                    locate_osw_ports_result_list_item_data
                )

                locate_osw_ports_result_list.append(locate_osw_ports_result_list_item)

        _locate_stack_ports_result_list = d.pop("locateStackPortsResultList", UNSET)
        locate_stack_ports_result_list: list[LocateStackResultOpenApiVO] | Unset = UNSET
        if _locate_stack_ports_result_list is not UNSET:
            locate_stack_ports_result_list = []
            for (
                locate_stack_ports_result_list_item_data
            ) in _locate_stack_ports_result_list:
                locate_stack_ports_result_list_item = (
                    LocateStackResultOpenApiVO.from_dict(
                        locate_stack_ports_result_list_item_data
                    )
                )

                locate_stack_ports_result_list.append(
                    locate_stack_ports_result_list_item
                )

        locate_osw_ports_result_open_api_vo = cls(
            locate_osw_ports_result_list=locate_osw_ports_result_list,
            locate_stack_ports_result_list=locate_stack_ports_result_list,
        )

        locate_osw_ports_result_open_api_vo.additional_properties = d
        return locate_osw_ports_result_open_api_vo

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
