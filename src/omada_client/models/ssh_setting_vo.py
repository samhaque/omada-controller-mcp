from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SshSettingVO")


@_attrs_define
class SshSettingVO:
    """
    Attributes:
        ssh_enable (bool):
        ssh_server_port (int | Unset):
        layer_3_access (bool | Unset):
        resource (int | Unset):
    """

    ssh_enable: bool
    ssh_server_port: int | Unset = UNSET
    layer_3_access: bool | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssh_enable = self.ssh_enable

        ssh_server_port = self.ssh_server_port

        layer_3_access = self.layer_3_access

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sshEnable": ssh_enable,
            }
        )
        if ssh_server_port is not UNSET:
            field_dict["sshServerPort"] = ssh_server_port
        if layer_3_access is not UNSET:
            field_dict["layer3Access"] = layer_3_access
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssh_enable = d.pop("sshEnable")

        ssh_server_port = d.pop("sshServerPort", UNSET)

        layer_3_access = d.pop("layer3Access", UNSET)

        resource = d.pop("resource", UNSET)

        ssh_setting_vo = cls(
            ssh_enable=ssh_enable,
            ssh_server_port=ssh_server_port,
            layer_3_access=layer_3_access,
            resource=resource,
        )

        ssh_setting_vo.additional_properties = d
        return ssh_setting_vo

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
