from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_location_detail_vo import DeviceLocationDetailVO
    from ..models.osw_qos_config_vo import OswQosConfigVO
    from ..models.osw_snmp_vo import OswSnmpVO
    from ..models.osw_stp_rpvst_vo import OswStpRpvstVO


T = TypeVar("T", bound="OswStackDetailConfigOpenApiVO")


@_attrs_define
class OswStackDetailConfigOpenApiVO:
    """
    Attributes:
        name (str | Unset): Stack Name
        led_setting (int | Unset): LED setting should be a value as follows: 0:off; 1:on; 2:Use Site Settings
        mvlan_network_id (str | Unset): Management VLAN network ID
        mvlan_bridge_vlan (int | Unset): Only valid when mvlanNetworkId is bridge vlan
        loopback_detect_enable (bool | Unset): LoopbackDetect enable status
        stp (int | Unset): Spanning Tree Protocol should be a value as follows: 1: STP; 2: RSTP; 3: MSTP; 4: RPVST 0:
            OFF
        snmp (OswSnmpVO | Unset): Snmp setting
        priority (int | Unset): STP priority should be an integer from 0 to 61440 and divisible by 4096
        hello_time (int | Unset): STP helloTime should be should be within the range of 1-10
        max_age (int | Unset): STP maxAge should be should be within the range of 6-40
        forward_delay (int | Unset): STP should be should be within the range of 4-30
        tx_hold_count (int | Unset): STP txHoldCount should be should be within the range of 1-20
        max_hops (int | Unset): STP maxHops should be should be within the range of 1-40
        mstp (OswStpRpvstVO | Unset): STP RPVST Config, must not be null when stp is 4.
        tag_ids (list[str] | Unset): Tag ID List
        jumbo (int | Unset): Jumbo should be should be within the range of 1518-9216
        lag_hash_alg (int | Unset): It should be a value as follows: 0: SRC MAC; 1: DST MAC; 2: SRC MAC + DST MAC; 3:
            SRC IP; 4: DST IP; 5: SRC IP + DST IP
        location (DeviceLocationDetailVO | Unset): Device location
        qos_config (OswQosConfigVO | Unset): Switch qos config
        remember_device (int | Unset): Whether to remember the device.RememberDevice should be a value as follows:
            0:off, 1:on, 2: follow site
    """

    name: str | Unset = UNSET
    led_setting: int | Unset = UNSET
    mvlan_network_id: str | Unset = UNSET
    mvlan_bridge_vlan: int | Unset = UNSET
    loopback_detect_enable: bool | Unset = UNSET
    stp: int | Unset = UNSET
    snmp: OswSnmpVO | Unset = UNSET
    priority: int | Unset = UNSET
    hello_time: int | Unset = UNSET
    max_age: int | Unset = UNSET
    forward_delay: int | Unset = UNSET
    tx_hold_count: int | Unset = UNSET
    max_hops: int | Unset = UNSET
    mstp: OswStpRpvstVO | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    jumbo: int | Unset = UNSET
    lag_hash_alg: int | Unset = UNSET
    location: DeviceLocationDetailVO | Unset = UNSET
    qos_config: OswQosConfigVO | Unset = UNSET
    remember_device: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        led_setting = self.led_setting

        mvlan_network_id = self.mvlan_network_id

        mvlan_bridge_vlan = self.mvlan_bridge_vlan

        loopback_detect_enable = self.loopback_detect_enable

        stp = self.stp

        snmp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        priority = self.priority

        hello_time = self.hello_time

        max_age = self.max_age

        forward_delay = self.forward_delay

        tx_hold_count = self.tx_hold_count

        max_hops = self.max_hops

        mstp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mstp, Unset):
            mstp = self.mstp.to_dict()

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        jumbo = self.jumbo

        lag_hash_alg = self.lag_hash_alg

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        qos_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qos_config, Unset):
            qos_config = self.qos_config.to_dict()

        remember_device = self.remember_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if led_setting is not UNSET:
            field_dict["ledSetting"] = led_setting
        if mvlan_network_id is not UNSET:
            field_dict["mvlanNetworkId"] = mvlan_network_id
        if mvlan_bridge_vlan is not UNSET:
            field_dict["mvlanBridgeVlan"] = mvlan_bridge_vlan
        if loopback_detect_enable is not UNSET:
            field_dict["loopbackDetectEnable"] = loopback_detect_enable
        if stp is not UNSET:
            field_dict["stp"] = stp
        if snmp is not UNSET:
            field_dict["snmp"] = snmp
        if priority is not UNSET:
            field_dict["priority"] = priority
        if hello_time is not UNSET:
            field_dict["helloTime"] = hello_time
        if max_age is not UNSET:
            field_dict["maxAge"] = max_age
        if forward_delay is not UNSET:
            field_dict["forwardDelay"] = forward_delay
        if tx_hold_count is not UNSET:
            field_dict["txHoldCount"] = tx_hold_count
        if max_hops is not UNSET:
            field_dict["maxHops"] = max_hops
        if mstp is not UNSET:
            field_dict["mstp"] = mstp
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if jumbo is not UNSET:
            field_dict["jumbo"] = jumbo
        if lag_hash_alg is not UNSET:
            field_dict["lagHashAlg"] = lag_hash_alg
        if location is not UNSET:
            field_dict["location"] = location
        if qos_config is not UNSET:
            field_dict["qosConfig"] = qos_config
        if remember_device is not UNSET:
            field_dict["rememberDevice"] = remember_device

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_location_detail_vo import (
            DeviceLocationDetailVO,
        )
        from ..models.osw_qos_config_vo import OswQosConfigVO
        from ..models.osw_snmp_vo import OswSnmpVO
        from ..models.osw_stp_rpvst_vo import OswStpRpvstVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        led_setting = d.pop("ledSetting", UNSET)

        mvlan_network_id = d.pop("mvlanNetworkId", UNSET)

        mvlan_bridge_vlan = d.pop("mvlanBridgeVlan", UNSET)

        loopback_detect_enable = d.pop("loopbackDetectEnable", UNSET)

        stp = d.pop("stp", UNSET)

        _snmp = d.pop("snmp", UNSET)
        snmp: OswSnmpVO | Unset
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = OswSnmpVO.from_dict(_snmp)

        priority = d.pop("priority", UNSET)

        hello_time = d.pop("helloTime", UNSET)

        max_age = d.pop("maxAge", UNSET)

        forward_delay = d.pop("forwardDelay", UNSET)

        tx_hold_count = d.pop("txHoldCount", UNSET)

        max_hops = d.pop("maxHops", UNSET)

        _mstp = d.pop("mstp", UNSET)
        mstp: OswStpRpvstVO | Unset
        if isinstance(_mstp, Unset):
            mstp = UNSET
        else:
            mstp = OswStpRpvstVO.from_dict(_mstp)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        jumbo = d.pop("jumbo", UNSET)

        lag_hash_alg = d.pop("lagHashAlg", UNSET)

        _location = d.pop("location", UNSET)
        location: DeviceLocationDetailVO | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeviceLocationDetailVO.from_dict(_location)

        _qos_config = d.pop("qosConfig", UNSET)
        qos_config: OswQosConfigVO | Unset
        if isinstance(_qos_config, Unset):
            qos_config = UNSET
        else:
            qos_config = OswQosConfigVO.from_dict(_qos_config)

        remember_device = d.pop("rememberDevice", UNSET)

        osw_stack_detail_config_open_api_vo = cls(
            name=name,
            led_setting=led_setting,
            mvlan_network_id=mvlan_network_id,
            mvlan_bridge_vlan=mvlan_bridge_vlan,
            loopback_detect_enable=loopback_detect_enable,
            stp=stp,
            snmp=snmp,
            priority=priority,
            hello_time=hello_time,
            max_age=max_age,
            forward_delay=forward_delay,
            tx_hold_count=tx_hold_count,
            max_hops=max_hops,
            mstp=mstp,
            tag_ids=tag_ids,
            jumbo=jumbo,
            lag_hash_alg=lag_hash_alg,
            location=location,
            qos_config=qos_config,
            remember_device=remember_device,
        )

        osw_stack_detail_config_open_api_vo.additional_properties = d
        return osw_stack_detail_config_open_api_vo

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
