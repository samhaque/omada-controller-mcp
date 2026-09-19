from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStackLocateOpenApiVO")


@_attrs_define
class OswStackLocateOpenApiVO:
    """
    Attributes:
        locate_enable (bool): Indicates whether locate is enabled
        select_all (bool | Unset): Indicates whether to select the entire stack
        macs (list[str] | Unset): Selected Device
        standard_ports (list[str] | Unset): Standard port should be in the format of unit/slot/portId. e.g. 1/0/1 . When
            parameter[standardPorts] is not empty, paramter[selectAll] and [macs] are not needed
    """

    locate_enable: bool
    select_all: bool | Unset = UNSET
    macs: list[str] | Unset = UNSET
    standard_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locate_enable = self.locate_enable

        select_all = self.select_all

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        standard_ports: list[str] | Unset = UNSET
        if not isinstance(self.standard_ports, Unset):
            standard_ports = self.standard_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locateEnable": locate_enable,
            }
        )
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if macs is not UNSET:
            field_dict["macs"] = macs
        if standard_ports is not UNSET:
            field_dict["standardPorts"] = standard_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        locate_enable = d.pop("locateEnable")

        select_all = d.pop("selectAll", UNSET)

        macs = cast(list[str], d.pop("macs", UNSET))

        standard_ports = cast(list[str], d.pop("standardPorts", UNSET))

        osw_stack_locate_open_api_vo = cls(
            locate_enable=locate_enable,
            select_all=select_all,
            macs=macs,
            standard_ports=standard_ports,
        )

        osw_stack_locate_open_api_vo.additional_properties = d
        return osw_stack_locate_open_api_vo

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
