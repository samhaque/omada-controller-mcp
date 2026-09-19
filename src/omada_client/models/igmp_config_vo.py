from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_info_vo import OswStackInfoVO


T = TypeVar("T", bound="IgmpConfigVO")


@_attrs_define
class IgmpConfigVO:
    """The querier configs for IGMP snooping(ipv4).

    Attributes:
        network_id (str | Unset): The primary id of the network.
        network_name (str | Unset): The name of the network.Name should contain 1 to 128 characters.
        vlan (int | Unset): The vlan of the network.The vlan should be within the range of 1 to 4090.
        mac (str | Unset): The unique identification of the device.
        device_name (str | Unset): The name of the device.
        device_type (str | Unset): Device type:ap, gateway, switch, olt
        device_model (str | Unset): Model of device,for example:EAP225
        device_model_version (str | Unset): Model version of device,for example:3.0
        stack_id (str | Unset): The id of the stacking devices.
        stack_name (str | Unset): The name of the stacking devices.
        osw_stack (OswStackInfoVO | Unset): The osw stack.
        query_interval (int | Unset): The time interval for the IGMP query to send query messages (unit: s).
        maximum_response_time (int | Unset): The maximum response time of the host to the general query message (unit:
            s).
        last_member_query_interval (int | Unset): The time interval for the device to send a specific group of query
            messages (unit: s).
        last_member_query_count (int | Unset): The number of specific group query messages sent by the device.
        general_query_source_ip (str | Unset): The source IP of the general query message sent.
    """

    network_id: str | Unset = UNSET
    network_name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    device_model: str | Unset = UNSET
    device_model_version: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    osw_stack: OswStackInfoVO | Unset = UNSET
    query_interval: int | Unset = UNSET
    maximum_response_time: int | Unset = UNSET
    last_member_query_interval: int | Unset = UNSET
    last_member_query_count: int | Unset = UNSET
    general_query_source_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        network_name = self.network_name

        vlan = self.vlan

        mac = self.mac

        device_name = self.device_name

        device_type = self.device_type

        device_model = self.device_model

        device_model_version = self.device_model_version

        stack_id = self.stack_id

        stack_name = self.stack_name

        osw_stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osw_stack, Unset):
            osw_stack = self.osw_stack.to_dict()

        query_interval = self.query_interval

        maximum_response_time = self.maximum_response_time

        last_member_query_interval = self.last_member_query_interval

        last_member_query_count = self.last_member_query_count

        general_query_source_ip = self.general_query_source_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if mac is not UNSET:
            field_dict["mac"] = mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if device_model_version is not UNSET:
            field_dict["deviceModelVersion"] = device_model_version
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if osw_stack is not UNSET:
            field_dict["oswStack"] = osw_stack
        if query_interval is not UNSET:
            field_dict["queryInterval"] = query_interval
        if maximum_response_time is not UNSET:
            field_dict["maximumResponseTime"] = maximum_response_time
        if last_member_query_interval is not UNSET:
            field_dict["lastMemberQueryInterval"] = last_member_query_interval
        if last_member_query_count is not UNSET:
            field_dict["lastMemberQueryCount"] = last_member_query_count
        if general_query_source_ip is not UNSET:
            field_dict["generalQuerySourceIp"] = general_query_source_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_info_vo import OswStackInfoVO

        d = dict(src_dict)
        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        vlan = d.pop("vlan", UNSET)

        mac = d.pop("mac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        device_model_version = d.pop("deviceModelVersion", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        _osw_stack = d.pop("oswStack", UNSET)
        osw_stack: OswStackInfoVO | Unset
        if isinstance(_osw_stack, Unset):
            osw_stack = UNSET
        else:
            osw_stack = OswStackInfoVO.from_dict(_osw_stack)

        query_interval = d.pop("queryInterval", UNSET)

        maximum_response_time = d.pop("maximumResponseTime", UNSET)

        last_member_query_interval = d.pop("lastMemberQueryInterval", UNSET)

        last_member_query_count = d.pop("lastMemberQueryCount", UNSET)

        general_query_source_ip = d.pop("generalQuerySourceIp", UNSET)

        igmp_config_vo = cls(
            network_id=network_id,
            network_name=network_name,
            vlan=vlan,
            mac=mac,
            device_name=device_name,
            device_type=device_type,
            device_model=device_model,
            device_model_version=device_model_version,
            stack_id=stack_id,
            stack_name=stack_name,
            osw_stack=osw_stack,
            query_interval=query_interval,
            maximum_response_time=maximum_response_time,
            last_member_query_interval=last_member_query_interval,
            last_member_query_count=last_member_query_count,
            general_query_source_ip=general_query_source_ip,
        )

        igmp_config_vo.additional_properties = d
        return igmp_config_vo

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
