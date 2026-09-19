from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CliConfigTemplateOpenApiVO")


@_attrs_define
class CliConfigTemplateOpenApiVO:
    """Get the CLI template configuration entry

    Attributes:
        cli_config (str): CLI configuration content
        omadac_id (str | Unset): Omada ID
        site_id (str | Unset): Site ID
        cli_type (int | Unset): CLI configuration type, it should be a value as follows: 0：site CLI.
        id (str | Unset): CLI configuration ID
        name (str | Unset): CLI configuration name
        device_type (str | Unset): Device type for CLI configuration application, it should be a value as follows:
            switch.
        description (str | Unset): CLI configuration description, it should be within the range of 0 - 256 characters.
        status (int | Unset): CLI configuration status, it should be a value as follows: 0: active, 1: inactive
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
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

        cli_config_template_open_api_vo = cls(
            cli_config=cli_config,
            omadac_id=omadac_id,
            site_id=site_id,
            cli_type=cli_type,
            id=id,
            name=name,
            device_type=device_type,
            description=description,
            status=status,
        )

        cli_config_template_open_api_vo.additional_properties = d
        return cli_config_template_open_api_vo

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
