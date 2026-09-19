from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_entry_vo import LanNetworkEntryVO
    from ..models.osw_qos_rule_device_vo import OswQosRuleDeviceVO


T = TypeVar("T", bound="OswQosRuleVO")


@_attrs_define
class OswQosRuleVO:
    """
    Attributes:
        name (str): The name of Qos rule.
        status (bool): The status of Qos rule, true: enable, false:disable
        type_ (int): The type of Qos rule, 0:Network, 1:Port, 2:Custom
        ip_version (list[int]): The selected ipVersion list of Qos rule, IPv4:[0], IPv6:[1], IPv4&IPv6:[0,1]
        queue (int): The queue of Qos rule(0-7).
        id (str | Unset): The Qos rule id. This parameter is not required when creating or modifying Qos rule.
        index (int | Unset): The index of Qos rule. This parameter is not required when creating or modifying Qos rule.
        lan_network_entries (list[LanNetworkEntryVO] | Unset): It can be issued when the type is either "Network" or
            "Custom". For the "Network" type, multiple options are available; for the "Custom" type, a single option is
            required.
        protocol (int | Unset): Network Protocol(Reference to chapter 5.5.1 ACL Protocol Template at Home page). When
            the type is "Custom", it can be issued.
        dscp (int | Unset): The dscp value(0-63). When the type is "Custom", it can be issued.
        dscp_re_enable (bool | Unset): Whether to enable DSCP remark
        dscp_re (int | Unset): The remarked dscp value(0-63). If it is set to "Auto", the actual issued value is 64.
        bind_type (int | Unset): Switch port bind type(0: all switch port, 1: custom switch port).
        device_list (list[OswQosRuleDeviceVO] | Unset): List of switch devices to which QoS rule are bound, only for
            bindType 1
        s_port (int | Unset): The source port(0-65535). When the type is "Custom" and the protocol is TCP or UDP, it can
            be issued.
        d_port (int | Unset): The destination port(0-65535). When the type is "Custom" and the protocol is TCP or UDP,
            it can be issued.
    """

    name: str
    status: bool
    type_: int
    ip_version: list[int]
    queue: int
    id: str | Unset = UNSET
    index: int | Unset = UNSET
    lan_network_entries: list[LanNetworkEntryVO] | Unset = UNSET
    protocol: int | Unset = UNSET
    dscp: int | Unset = UNSET
    dscp_re_enable: bool | Unset = UNSET
    dscp_re: int | Unset = UNSET
    bind_type: int | Unset = UNSET
    device_list: list[OswQosRuleDeviceVO] | Unset = UNSET
    s_port: int | Unset = UNSET
    d_port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        type_ = self.type_

        ip_version = self.ip_version

        queue = self.queue

        id = self.id

        index = self.index

        lan_network_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_network_entries, Unset):
            lan_network_entries = []
            for lan_network_entries_item_data in self.lan_network_entries:
                lan_network_entries_item = lan_network_entries_item_data.to_dict()
                lan_network_entries.append(lan_network_entries_item)

        protocol = self.protocol

        dscp = self.dscp

        dscp_re_enable = self.dscp_re_enable

        dscp_re = self.dscp_re

        bind_type = self.bind_type

        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        s_port = self.s_port

        d_port = self.d_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "type": type_,
                "ipVersion": ip_version,
                "queue": queue,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if lan_network_entries is not UNSET:
            field_dict["lanNetworkEntries"] = lan_network_entries
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if dscp is not UNSET:
            field_dict["dscp"] = dscp
        if dscp_re_enable is not UNSET:
            field_dict["dscpReEnable"] = dscp_re_enable
        if dscp_re is not UNSET:
            field_dict["dscpRe"] = dscp_re
        if bind_type is not UNSET:
            field_dict["bindType"] = bind_type
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list
        if s_port is not UNSET:
            field_dict["sPort"] = s_port
        if d_port is not UNSET:
            field_dict["dPort"] = d_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_entry_vo import LanNetworkEntryVO
        from ..models.osw_qos_rule_device_vo import OswQosRuleDeviceVO

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        type_ = d.pop("type")

        ip_version = cast(list[int], d.pop("ipVersion"))

        queue = d.pop("queue")

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        _lan_network_entries = d.pop("lanNetworkEntries", UNSET)
        lan_network_entries: list[LanNetworkEntryVO] | Unset = UNSET
        if _lan_network_entries is not UNSET:
            lan_network_entries = []
            for lan_network_entries_item_data in _lan_network_entries:
                lan_network_entries_item = LanNetworkEntryVO.from_dict(
                    lan_network_entries_item_data
                )

                lan_network_entries.append(lan_network_entries_item)

        protocol = d.pop("protocol", UNSET)

        dscp = d.pop("dscp", UNSET)

        dscp_re_enable = d.pop("dscpReEnable", UNSET)

        dscp_re = d.pop("dscpRe", UNSET)

        bind_type = d.pop("bindType", UNSET)

        _device_list = d.pop("deviceList", UNSET)
        device_list: list[OswQosRuleDeviceVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = OswQosRuleDeviceVO.from_dict(device_list_item_data)

                device_list.append(device_list_item)

        s_port = d.pop("sPort", UNSET)

        d_port = d.pop("dPort", UNSET)

        osw_qos_rule_vo = cls(
            name=name,
            status=status,
            type_=type_,
            ip_version=ip_version,
            queue=queue,
            id=id,
            index=index,
            lan_network_entries=lan_network_entries,
            protocol=protocol,
            dscp=dscp,
            dscp_re_enable=dscp_re_enable,
            dscp_re=dscp_re,
            bind_type=bind_type,
            device_list=device_list,
            s_port=s_port,
            d_port=d_port,
        )

        osw_qos_rule_vo.additional_properties = d
        return osw_qos_rule_vo

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
