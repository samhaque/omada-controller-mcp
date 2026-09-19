from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_export_cli_vo_variable_map import DeviceExportCliVOVariableMap


T = TypeVar("T", bound="DeviceExportCliVO")


@_attrs_define
class DeviceExportCliVO:
    """Devices

    Attributes:
        device_mac (str): Device mac
        variable_map (DeviceExportCliVOVariableMap | Unset): The values of different user-defined variables.
    """

    device_mac: str
    variable_map: DeviceExportCliVOVariableMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        variable_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variable_map, Unset):
            variable_map = self.variable_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceMac": device_mac,
            }
        )
        if variable_map is not UNSET:
            field_dict["variableMap"] = variable_map

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_export_cli_vo_variable_map import (
            DeviceExportCliVOVariableMap,
        )

        d = dict(src_dict)
        device_mac = d.pop("deviceMac")

        _variable_map = d.pop("variableMap", UNSET)
        variable_map: DeviceExportCliVOVariableMap | Unset
        if isinstance(_variable_map, Unset):
            variable_map = UNSET
        else:
            variable_map = DeviceExportCliVOVariableMap.from_dict(_variable_map)

        device_export_cli_vo = cls(
            device_mac=device_mac,
            variable_map=variable_map,
        )

        device_export_cli_vo.additional_properties = d
        return device_export_cli_vo

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
