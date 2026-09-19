from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ControllerPort")


@_attrs_define
class ControllerPort:
    """
    Attributes:
        manage_http_port (int | Unset): Controller HTTP Port should be 80 or between 1024 and 65535
        manage_https_port (int | Unset): Controller HTTPS Port should be 443 or between 1024 and 65535
        host_name (str | Unset): Host name
        auto_refresh (bool | Unset): Auto refresh status
    """

    manage_http_port: int | Unset = UNSET
    manage_https_port: int | Unset = UNSET
    host_name: str | Unset = UNSET
    auto_refresh: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        manage_http_port = self.manage_http_port

        manage_https_port = self.manage_https_port

        host_name = self.host_name

        auto_refresh = self.auto_refresh

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if manage_http_port is not UNSET:
            field_dict["manageHttpPort"] = manage_http_port
        if manage_https_port is not UNSET:
            field_dict["manageHttpsPort"] = manage_https_port
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if auto_refresh is not UNSET:
            field_dict["autoRefresh"] = auto_refresh

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        manage_http_port = d.pop("manageHttpPort", UNSET)

        manage_https_port = d.pop("manageHttpsPort", UNSET)

        host_name = d.pop("hostName", UNSET)

        auto_refresh = d.pop("autoRefresh", UNSET)

        controller_port = cls(
            manage_http_port=manage_http_port,
            manage_https_port=manage_https_port,
            host_name=host_name,
            auto_refresh=auto_refresh,
        )

        controller_port.additional_properties = d
        return controller_port

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
