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


T = TypeVar("T", bound="CliConfigOpenApiVO")


@_attrs_define
class CliConfigOpenApiVO:
    """Get the CLI configuration entry

    Attributes:
        cli_config (str): CLI configuration content
        omadac_id (str | Unset): Omada ID
        site_id (str | Unset): Site ID
        cli_type (int | Unset): CLI configuration type, it should be a value as follows: 0：site CLI； 1：device CLI.
        id (str | Unset): CLI configuration ID
        name (str | Unset): CLI configuration name
        device_type (str | Unset): Device type for CLI configuration application, it should be a value as follows:
            switch.
        description (str | Unset): CLI configuration description, it should be within the range of 0 - 256 characters.
        status (int | Unset): CLI configuration status, it should be a value as follows: 0: active, 1: inactive
        devices (list[DeviceCliVO] | Unset): List of devices bound to the CLI configuration. Only device CLI has this
            field.
        stacks (list[StackCliVO] | Unset): List of stacks bound to the CLI configuration, only device CLI has this
            field.
        model (str | Unset): Device model of model cli
        model_version (str | Unset): Device model version of model cli
    """

    cli_config: str
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    cli_type: int | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    description: str | Unset = UNSET
    status: int | Unset = UNSET
    devices: list[DeviceCliVO] | Unset = UNSET
    stacks: list[StackCliVO] | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cli_config = self.cli_config

        omadac_id = self.omadac_id

        site_id = self.site_id

        cli_type = self.cli_type

        id = self.id

        name = self.name

        device_type = self.device_type

        description = self.description

        status = self.status

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
                "cliConfig": cli_config,
            }
        )
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if cli_type is not UNSET:
            field_dict["cliType"] = cli_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
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
        cli_config = d.pop("cliConfig")

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        cli_type = d.pop("cliType", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        device_type = d.pop("deviceType", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

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

        cli_config_open_api_vo = cls(
            cli_config=cli_config,
            omadac_id=omadac_id,
            site_id=site_id,
            cli_type=cli_type,
            id=id,
            name=name,
            device_type=device_type,
            description=description,
            status=status,
            devices=devices,
            stacks=stacks,
            model=model,
            model_version=model_version,
        )

        cli_config_open_api_vo.additional_properties = d
        return cli_config_open_api_vo

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
