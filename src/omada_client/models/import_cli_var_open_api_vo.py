from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_export_cli_vo import DeviceExportCliVO


T = TypeVar("T", bound="ImportCliVarOpenApiVO")


@_attrs_define
class ImportCliVarOpenApiVO:
    """
    Attributes:
        devices (list[DeviceExportCliVO] | Unset): Devices
    """

    devices: list[DeviceExportCliVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_export_cli_vo import DeviceExportCliVO

        d = dict(src_dict)
        _devices = d.pop("devices", UNSET)
        devices: list[DeviceExportCliVO] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = DeviceExportCliVO.from_dict(devices_item_data)

                devices.append(devices_item)

        import_cli_var_open_api_vo = cls(
            devices=devices,
        )

        import_cli_var_open_api_vo.additional_properties = d
        return import_cli_var_open_api_vo

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
