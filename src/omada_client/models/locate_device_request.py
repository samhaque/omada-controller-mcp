from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocateDeviceRequest")


@_attrs_define
class LocateDeviceRequest:
    """
    Attributes:
        locate_enable (bool | Unset):
        port_list (list[int] | Unset): Ports to be located
    """

    locate_enable: bool | Unset = UNSET
    port_list: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locate_enable = self.locate_enable

        port_list: list[int] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        locate_enable = d.pop("locateEnable", UNSET)

        port_list = cast(list[int], d.pop("portList", UNSET))

        locate_device_request = cls(
            locate_enable=locate_enable,
            port_list=port_list,
        )

        locate_device_request.additional_properties = d
        return locate_device_request

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
