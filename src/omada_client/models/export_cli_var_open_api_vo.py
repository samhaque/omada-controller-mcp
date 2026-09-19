from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.device_export_cli_vo import DeviceExportCliVO


T = TypeVar("T", bound="ExportCliVarOpenApiVO")


@_attrs_define
class ExportCliVarOpenApiVO:
    """
    Attributes:
        type_ (int): Export type should be a value as follows: 0:CSV; 1:JSON
        devices (list[DeviceExportCliVO]): Devices
    """

    type_: int
    devices: list[DeviceExportCliVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()
            devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "devices": devices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_export_cli_vo import DeviceExportCliVO

        d = dict(src_dict)
        type_ = d.pop("type")

        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = DeviceExportCliVO.from_dict(devices_item_data)

            devices.append(devices_item)

        export_cli_var_open_api_vo = cls(
            type_=type_,
            devices=devices,
        )

        export_cli_var_open_api_vo.additional_properties = d
        return export_cli_var_open_api_vo

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
