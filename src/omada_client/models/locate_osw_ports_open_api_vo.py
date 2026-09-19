from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_normal_port_list_vo import OswNormalPortListVO
    from ..models.osw_stack_port_list_vo import OswStackPortListVO


T = TypeVar("T", bound="LocateOswPortsOpenApiVO")


@_attrs_define
class LocateOswPortsOpenApiVO:
    """
    Attributes:
        locate_enable (bool): Whether locate function is enabled
        port_list_v_os (list[OswNormalPortListVO] | Unset): List of Switch MAC and ports.
        stack_port_list_v_os (list[OswStackPortListVO] | Unset): List of Stack ID and Standard Ports.
    """

    locate_enable: bool
    port_list_v_os: list[OswNormalPortListVO] | Unset = UNSET
    stack_port_list_v_os: list[OswStackPortListVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locate_enable = self.locate_enable

        port_list_v_os: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_list_v_os, Unset):
            port_list_v_os = []
            for port_list_v_os_item_data in self.port_list_v_os:
                port_list_v_os_item = port_list_v_os_item_data.to_dict()
                port_list_v_os.append(port_list_v_os_item)

        stack_port_list_v_os: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_port_list_v_os, Unset):
            stack_port_list_v_os = []
            for stack_port_list_v_os_item_data in self.stack_port_list_v_os:
                stack_port_list_v_os_item = stack_port_list_v_os_item_data.to_dict()
                stack_port_list_v_os.append(stack_port_list_v_os_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locateEnable": locate_enable,
            }
        )
        if port_list_v_os is not UNSET:
            field_dict["portListVOs"] = port_list_v_os
        if stack_port_list_v_os is not UNSET:
            field_dict["stackPortListVOs"] = stack_port_list_v_os

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_normal_port_list_vo import (
            OswNormalPortListVO,
        )
        from ..models.osw_stack_port_list_vo import OswStackPortListVO

        d = dict(src_dict)
        locate_enable = d.pop("locateEnable")

        _port_list_v_os = d.pop("portListVOs", UNSET)
        port_list_v_os: list[OswNormalPortListVO] | Unset = UNSET
        if _port_list_v_os is not UNSET:
            port_list_v_os = []
            for port_list_v_os_item_data in _port_list_v_os:
                port_list_v_os_item = OswNormalPortListVO.from_dict(
                    port_list_v_os_item_data
                )

                port_list_v_os.append(port_list_v_os_item)

        _stack_port_list_v_os = d.pop("stackPortListVOs", UNSET)
        stack_port_list_v_os: list[OswStackPortListVO] | Unset = UNSET
        if _stack_port_list_v_os is not UNSET:
            stack_port_list_v_os = []
            for stack_port_list_v_os_item_data in _stack_port_list_v_os:
                stack_port_list_v_os_item = OswStackPortListVO.from_dict(
                    stack_port_list_v_os_item_data
                )

                stack_port_list_v_os.append(stack_port_list_v_os_item)

        locate_osw_ports_open_api_vo = cls(
            locate_enable=locate_enable,
            port_list_v_os=port_list_v_os,
            stack_port_list_v_os=stack_port_list_v_os,
        )

        locate_osw_ports_open_api_vo.additional_properties = d
        return locate_osw_ports_open_api_vo

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
