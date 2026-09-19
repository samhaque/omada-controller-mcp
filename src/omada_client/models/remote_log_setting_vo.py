from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteLogSettingVO")


@_attrs_define
class RemoteLogSettingVO:
    """Site remote logging.

    Attributes:
        enable (bool): Whether to enable the feature
        host (str | Unset): The IP address of the remote log server
        port (int | Unset): Port of the remote log server, port should be within the range of 1-65535
        more_client_log (bool | Unset): Whether it contains client log
        resource (int | Unset): Data Source. Resource should be a value as follows: 0: new created; 1: from template; 2:
            override
    """

    enable: bool
    host: str | Unset = UNSET
    port: int | Unset = UNSET
    more_client_log: bool | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        host = self.host

        port = self.port

        more_client_log = self.more_client_log

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host
        if port is not UNSET:
            field_dict["port"] = port
        if more_client_log is not UNSET:
            field_dict["moreClientLog"] = more_client_log
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        host = d.pop("host", UNSET)

        port = d.pop("port", UNSET)

        more_client_log = d.pop("moreClientLog", UNSET)

        resource = d.pop("resource", UNSET)

        remote_log_setting_vo = cls(
            enable=enable,
            host=host,
            port=port,
            more_client_log=more_client_log,
            resource=resource,
        )

        remote_log_setting_vo.additional_properties = d
        return remote_log_setting_vo

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
