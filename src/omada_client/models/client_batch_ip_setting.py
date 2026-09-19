from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_macip_setting import ClientMACIPSetting


T = TypeVar("T", bound="ClientBatchIPSetting")


@_attrs_define
class ClientBatchIPSetting:
    """Setting of ip.

    Attributes:
        use_fixed_addr (bool): Use fixed ip address.
        net_id (str | Unset): Network ID.
        server_type (str | Unset): DHCP Server Type.
        server_mac (str | Unset): DHCP Server Mac.
        server_stack_id (str | Unset): DHCP Server Stack ID.
        ip_list (list[ClientMACIPSetting] | Unset): List of ip and client mac.
    """

    use_fixed_addr: bool
    net_id: str | Unset = UNSET
    server_type: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    ip_list: list[ClientMACIPSetting] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use_fixed_addr = self.use_fixed_addr

        net_id = self.net_id

        server_type = self.server_type

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        ip_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip_list, Unset):
            ip_list = []
            for ip_list_item_data in self.ip_list:
                ip_list_item = ip_list_item_data.to_dict()
                ip_list.append(ip_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "useFixedAddr": use_fixed_addr,
            }
        )
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if server_type is not UNSET:
            field_dict["serverType"] = server_type
        if server_mac is not UNSET:
            field_dict["serverMac"] = server_mac
        if server_stack_id is not UNSET:
            field_dict["serverStackId"] = server_stack_id
        if ip_list is not UNSET:
            field_dict["ipList"] = ip_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_macip_setting import ClientMACIPSetting

        d = dict(src_dict)
        use_fixed_addr = d.pop("useFixedAddr")

        net_id = d.pop("netId", UNSET)

        server_type = d.pop("serverType", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        _ip_list = d.pop("ipList", UNSET)
        ip_list: list[ClientMACIPSetting] | Unset = UNSET
        if _ip_list is not UNSET:
            ip_list = []
            for ip_list_item_data in _ip_list:
                ip_list_item = ClientMACIPSetting.from_dict(ip_list_item_data)

                ip_list.append(ip_list_item)

        client_batch_ip_setting = cls(
            use_fixed_addr=use_fixed_addr,
            net_id=net_id,
            server_type=server_type,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
            ip_list=ip_list,
        )

        client_batch_ip_setting.additional_properties = d
        return client_batch_ip_setting

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
