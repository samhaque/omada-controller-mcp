from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyCliTemplateOpenApiVO")


@_attrs_define
class ModifyCliTemplateOpenApiVO:
    """Modify the CLI template configuration entry

    Attributes:
        name (str): CLI configuration name, it should be within the range of 1 - 64 characters
        device_type (str): Device type for CLI configuration application, it should be a value as follows: switch.
        cli_config (str): CLI configuration content
        description (str | Unset): CLI configuration description, it should be within the range of 0 - 256 characters.
    """

    name: str
    device_type: str
    cli_config: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        device_type = self.device_type

        cli_config = self.cli_config

        description = self.description

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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        device_type = d.pop("deviceType")

        cli_config = d.pop("cliConfig")

        description = d.pop("description", UNSET)

        modify_cli_template_open_api_vo = cls(
            name=name,
            device_type=device_type,
            cli_config=cli_config,
            description=description,
        )

        modify_cli_template_open_api_vo.additional_properties = d
        return modify_cli_template_open_api_vo

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
