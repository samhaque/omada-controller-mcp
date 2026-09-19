from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doh_customized_server_open_api_vo import DohCustomizedServerOpenApiVO


T = TypeVar("T", bound="DohSettingOpenApiVO")


@_attrs_define
class DohSettingOpenApiVO:
    """DNS proxy DoH setting, valid when parameter [type] is 1

    Attributes:
        default_servers (list[int] | Unset): Preconfigured Server List. DefaultServers should be a value as follows:
            0:Google, 1：Cloudflare, 4：CleanBrowsing, 5：Quad9_1, 6: Quad9_2. Up to 2 DoH default and custom servers can be
            selected. For example, defaultServers : [0, 1] represents that you have selected default services Google and
            Cloudflare
        customized_servers (list[DohCustomizedServerOpenApiVO] | Unset): Custom Service list. Up to 2 DoH default and
            custom Servers can be selected, setting the parameter [enable] to true indicates the selection of the custom
            server.
    """

    default_servers: list[int] | Unset = UNSET
    customized_servers: list[DohCustomizedServerOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_servers: list[int] | Unset = UNSET
        if not isinstance(self.default_servers, Unset):
            default_servers = self.default_servers

        customized_servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.customized_servers, Unset):
            customized_servers = []
            for customized_servers_item_data in self.customized_servers:
                customized_servers_item = customized_servers_item_data.to_dict()
                customized_servers.append(customized_servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_servers is not UNSET:
            field_dict["defaultServers"] = default_servers
        if customized_servers is not UNSET:
            field_dict["customizedServers"] = customized_servers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.doh_customized_server_open_api_vo import (
            DohCustomizedServerOpenApiVO,
        )

        d = dict(src_dict)
        default_servers = cast(list[int], d.pop("defaultServers", UNSET))

        _customized_servers = d.pop("customizedServers", UNSET)
        customized_servers: list[DohCustomizedServerOpenApiVO] | Unset = UNSET
        if _customized_servers is not UNSET:
            customized_servers = []
            for customized_servers_item_data in _customized_servers:
                customized_servers_item = DohCustomizedServerOpenApiVO.from_dict(
                    customized_servers_item_data
                )

                customized_servers.append(customized_servers_item)

        doh_setting_open_api_vo = cls(
            default_servers=default_servers,
            customized_servers=customized_servers,
        )

        doh_setting_open_api_vo.additional_properties = d
        return doh_setting_open_api_vo

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
