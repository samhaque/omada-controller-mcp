from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgCapVO")


@_attrs_define
class OsgCapVO:
    """
    Attributes:
        support_config_sync (bool | Unset):
        need_full_sync (bool | Unset):
        support_running_config (bool | Unset):
        support_client_port_info (bool | Unset):
        support_dhcp_client (bool | Unset):
        support_arp_table_get (bool | Unset):
    """

    support_config_sync: bool | Unset = UNSET
    need_full_sync: bool | Unset = UNSET
    support_running_config: bool | Unset = UNSET
    support_client_port_info: bool | Unset = UNSET
    support_dhcp_client: bool | Unset = UNSET
    support_arp_table_get: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_config_sync = self.support_config_sync

        need_full_sync = self.need_full_sync

        support_running_config = self.support_running_config

        support_client_port_info = self.support_client_port_info

        support_dhcp_client = self.support_dhcp_client

        support_arp_table_get = self.support_arp_table_get

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support_config_sync is not UNSET:
            field_dict["supportConfigSync"] = support_config_sync
        if need_full_sync is not UNSET:
            field_dict["needFullSync"] = need_full_sync
        if support_running_config is not UNSET:
            field_dict["supportRunningConfig"] = support_running_config
        if support_client_port_info is not UNSET:
            field_dict["supportClientPortInfo"] = support_client_port_info
        if support_dhcp_client is not UNSET:
            field_dict["supportDhcpClient"] = support_dhcp_client
        if support_arp_table_get is not UNSET:
            field_dict["supportArpTableGet"] = support_arp_table_get

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support_config_sync = d.pop("supportConfigSync", UNSET)

        need_full_sync = d.pop("needFullSync", UNSET)

        support_running_config = d.pop("supportRunningConfig", UNSET)

        support_client_port_info = d.pop("supportClientPortInfo", UNSET)

        support_dhcp_client = d.pop("supportDhcpClient", UNSET)

        support_arp_table_get = d.pop("supportArpTableGet", UNSET)

        osg_cap_vo = cls(
            support_config_sync=support_config_sync,
            need_full_sync=need_full_sync,
            support_running_config=support_running_config,
            support_client_port_info=support_client_port_info,
            support_dhcp_client=support_dhcp_client,
            support_arp_table_get=support_arp_table_get,
        )

        osg_cap_vo.additional_properties = d
        return osg_cap_vo

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
