from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_cli_vo import DeviceCliVO
    from ..models.stack_cli_vo import StackCliVO


T = TypeVar("T", bound="ModifyCliOpenApiVO")


@_attrs_define
class ModifyCliOpenApiVO:
    """Modify the CLI configuration entry

    Attributes:
        name (str): CLI configuration name, it should be within the range of 1 - 64 characters
        device_type (str): Device type for CLI configuration application, it should be a value as follows: switch.
        cli_config (str): CLI configuration content
        description (str | Unset): CLI configuration description, it should be within the range of 0 - 256 characters.
        devices (list[DeviceCliVO] | Unset): List of devices bound to the CLI configuration.
        stacks (list[StackCliVO] | Unset): List of stacks bound to the CLI configuration, only device CLI has this
            field.
        model (str | Unset): Device model of model cli
        model_version (str | Unset): Device model version of model cli
    """

    name: str
    device_type: str
    cli_config: str
    description: str | Unset = UNSET
    devices: list[DeviceCliVO] | Unset = UNSET
    stacks: list[StackCliVO] | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        device_type = self.device_type

        cli_config = self.cli_config

        description = self.description

        devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        stacks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stacks, Unset):
            stacks = []
            for stacks_item_data in self.stacks:
                stacks_item = stacks_item_data.to_dict()
                stacks.append(stacks_item)

        model = self.model

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "deviceType": device_type,
                "cliConfig": cli_config,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if devices is not UNSET:
            field_dict["devices"] = devices
        if stacks is not UNSET:
            field_dict["stacks"] = stacks
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_cli_vo import DeviceCliVO
        from ..models.stack_cli_vo import StackCliVO

        d = dict(src_dict)
        name = d.pop("name")

        device_type = d.pop("deviceType")

        cli_config = d.pop("cliConfig")

        description = d.pop("description", UNSET)

        _devices = d.pop("devices", UNSET)
        devices: list[DeviceCliVO] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = DeviceCliVO.from_dict(devices_item_data)

                devices.append(devices_item)

        _stacks = d.pop("stacks", UNSET)
        stacks: list[StackCliVO] | Unset = UNSET
        if _stacks is not UNSET:
            stacks = []
            for stacks_item_data in _stacks:
                stacks_item = StackCliVO.from_dict(stacks_item_data)

                stacks.append(stacks_item)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        modify_cli_open_api_vo = cls(
            name=name,
            device_type=device_type,
            cli_config=cli_config,
            description=description,
            devices=devices,
            stacks=stacks,
            model=model,
            model_version=model_version,
        )

        modify_cli_open_api_vo.additional_properties = d
        return modify_cli_open_api_vo

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
