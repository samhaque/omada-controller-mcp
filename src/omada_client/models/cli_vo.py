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


T = TypeVar("T", bound="CliVO")


@_attrs_define
class CliVO:
    """
    Attributes:
        id (str | Unset): CLI configuration ID
        name (str | Unset): CLI configuration name
        description (str | Unset): CLI configuration description, it should be within the range of 0 - 256 characters.
        status (int | Unset): CLI configuration status, it should be a value as follows: 0: active, 1: inactive
        apply (bool | Unset): Whether the CLI configuration can be applied. Only the CLI configuration in inactive state
            can be applied.
        devices (list[DeviceCliVO] | Unset): List of devices bound to the CLI configuration, only device CLI has this
            field.
        stacks (list[StackCliVO] | Unset): List of stacks bound to the CLI configuration, only device CLI has this
            field.
        model (str | Unset):
        model_version (str | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    status: int | Unset = UNSET
    apply: bool | Unset = UNSET
    devices: list[DeviceCliVO] | Unset = UNSET
    stacks: list[StackCliVO] | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        status = self.status

        apply = self.apply

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if apply is not UNSET:
            field_dict["apply"] = apply
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
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        apply = d.pop("apply", UNSET)

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

        cli_vo = cls(
            id=id,
            name=name,
            description=description,
            status=status,
            apply=apply,
            devices=devices,
            stacks=stacks,
            model=model,
            model_version=model_version,
        )

        cli_vo.additional_properties = d
        return cli_vo

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
