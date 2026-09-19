from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DohCustomizedServerOpenApiVO")


@_attrs_define
class DohCustomizedServerOpenApiVO:
    """Custom Service list. Up to 2 DoH default and custom Servers can be selected, setting the parameter [enable] to true
    indicates the selection of the custom server.

        Attributes:
            enable (bool): Custom service enable status
            name (str): Custom service name, should contain 1 to 64 characters
            server (str): Custom service IP or domain
    """

    enable: bool
    name: str
    server: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        name = self.name

        server = self.server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "name": name,
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        name = d.pop("name")

        server = d.pop("server")

        doh_customized_server_open_api_vo = cls(
            enable=enable,
            name=name,
            server=server,
        )

        doh_customized_server_open_api_vo.additional_properties = d
        return doh_customized_server_open_api_vo

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
