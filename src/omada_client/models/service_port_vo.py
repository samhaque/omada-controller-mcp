from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.service_port_vo_active_status import ServicePortVOActiveStatus
from ..models.service_port_vo_admin_status import ServicePortVOAdminStatus
from ..models.service_port_vo_ether_type import ServicePortVOEtherType
from ..models.service_port_vo_statistic_performance import (
    ServicePortVOStatisticPerformance,
)
from ..models.service_port_vo_tag_action import ServicePortVOTagAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicePortVO")


@_attrs_define
class ServicePortVO:
    """Content

    Attributes:
        index (int): ID of service port.Index should be within the range of 1 to 8100
        description (str): Description of service port.Description should contain 1 to 32 characters including numbers,
            Upper and lower letters, -@_:/. .
        onu_id (int): OnuId should be within the range of 0 to 127
        admin_status (ServicePortVOAdminStatus): The enable status of the service flows matched by this Service Port.
            AdminStatus should be a value as follows: DISABLE,ENABLE. Default value: ENABLE.
        statistic_performance (ServicePortVOStatisticPerformance): The traffic statistics switch status for the service
            flows matched by this Service Port. StatisticPerformance should be a value as follows: DISABLE,ENABLE. Default
            value: DISABLE.
        active_status (ServicePortVOActiveStatus | Unset): Whether this service port is active.ActiveStatus should be a
            value as follows:ACTIVE,INACTIVE
        pon_port_id (int | Unset): PonPortId should be within the range of 1 to 16
        svlan (int | Unset): SVlan should be within the range of 1 to 4095
        gem_port_id (int | Unset): GemPortId should be within the range of 1 to 1023
        user_vlan (int | Unset): UserVlan should be within the range of 0 to 4095
        user_vlan_priority (str | Unset): UserVlanPriority should be within the range of -1 to 7
        tag_action (ServicePortVOTagAction | Unset): TagAction should be a value as
            follows:DEFAULT,TRANSPARENT,TRANSLATE,TRANSLATE_AND_ADD,ADD_DOUBLE
        inner_vlan (int | Unset): InnerVlan should be within the range of 0 to 4095
        inner_vlan_priority (str | Unset): InnerVlanPriority should be within the range of -1 to 7
        ether_type (ServicePortVOEtherType | Unset): EtherType should be a value as follows:NONE,IPV4OE,IPV6OE,PPPOE
        inbound_traffic_profile_id (str | Unset): InboundTrafficProfileId should be within the range of 0 to 512
        outbound_traffic_profile_id (str | Unset): OutboundTrafficProfileId should be within the range of 0 to 512
    """

    index: int
    description: str
    onu_id: int
    admin_status: ServicePortVOAdminStatus
    statistic_performance: ServicePortVOStatisticPerformance
    active_status: ServicePortVOActiveStatus | Unset = UNSET
    pon_port_id: int | Unset = UNSET
    svlan: int | Unset = UNSET
    gem_port_id: int | Unset = UNSET
    user_vlan: int | Unset = UNSET
    user_vlan_priority: str | Unset = UNSET
    tag_action: ServicePortVOTagAction | Unset = UNSET
    inner_vlan: int | Unset = UNSET
    inner_vlan_priority: str | Unset = UNSET
    ether_type: ServicePortVOEtherType | Unset = UNSET
    inbound_traffic_profile_id: str | Unset = UNSET
    outbound_traffic_profile_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        description = self.description

        onu_id = self.onu_id

        admin_status = self.admin_status.value

        statistic_performance = self.statistic_performance.value

        active_status: str | Unset = UNSET
        if not isinstance(self.active_status, Unset):
            active_status = self.active_status.value

        pon_port_id = self.pon_port_id

        svlan = self.svlan

        gem_port_id = self.gem_port_id

        user_vlan = self.user_vlan

        user_vlan_priority = self.user_vlan_priority

        tag_action: str | Unset = UNSET
        if not isinstance(self.tag_action, Unset):
            tag_action = self.tag_action.value

        inner_vlan = self.inner_vlan

        inner_vlan_priority = self.inner_vlan_priority

        ether_type: str | Unset = UNSET
        if not isinstance(self.ether_type, Unset):
            ether_type = self.ether_type.value

        inbound_traffic_profile_id = self.inbound_traffic_profile_id

        outbound_traffic_profile_id = self.outbound_traffic_profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "description": description,
                "onuId": onu_id,
                "adminStatus": admin_status,
                "statisticPerformance": statistic_performance,
            }
        )
        if active_status is not UNSET:
            field_dict["activeStatus"] = active_status
        if pon_port_id is not UNSET:
            field_dict["ponPortId"] = pon_port_id
        if svlan is not UNSET:
            field_dict["svlan"] = svlan
        if gem_port_id is not UNSET:
            field_dict["gemPortId"] = gem_port_id
        if user_vlan is not UNSET:
            field_dict["userVlan"] = user_vlan
        if user_vlan_priority is not UNSET:
            field_dict["userVlanPriority"] = user_vlan_priority
        if tag_action is not UNSET:
            field_dict["tagAction"] = tag_action
        if inner_vlan is not UNSET:
            field_dict["innerVlan"] = inner_vlan
        if inner_vlan_priority is not UNSET:
            field_dict["innerVlanPriority"] = inner_vlan_priority
        if ether_type is not UNSET:
            field_dict["etherType"] = ether_type
        if inbound_traffic_profile_id is not UNSET:
            field_dict["inboundTrafficProfileId"] = inbound_traffic_profile_id
        if outbound_traffic_profile_id is not UNSET:
            field_dict["outboundTrafficProfileId"] = outbound_traffic_profile_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        index = d.pop("index")

        description = d.pop("description")

        onu_id = d.pop("onuId")

        admin_status = ServicePortVOAdminStatus(d.pop("adminStatus"))

        statistic_performance = ServicePortVOStatisticPerformance(
            d.pop("statisticPerformance")
        )

        _active_status = d.pop("activeStatus", UNSET)
        active_status: ServicePortVOActiveStatus | Unset
        if isinstance(_active_status, Unset):
            active_status = UNSET
        else:
            active_status = ServicePortVOActiveStatus(_active_status)

        pon_port_id = d.pop("ponPortId", UNSET)

        svlan = d.pop("svlan", UNSET)

        gem_port_id = d.pop("gemPortId", UNSET)

        user_vlan = d.pop("userVlan", UNSET)

        user_vlan_priority = d.pop("userVlanPriority", UNSET)

        _tag_action = d.pop("tagAction", UNSET)
        tag_action: ServicePortVOTagAction | Unset
        if isinstance(_tag_action, Unset):
            tag_action = UNSET
        else:
            tag_action = ServicePortVOTagAction(_tag_action)

        inner_vlan = d.pop("innerVlan", UNSET)

        inner_vlan_priority = d.pop("innerVlanPriority", UNSET)

        _ether_type = d.pop("etherType", UNSET)
        ether_type: ServicePortVOEtherType | Unset
        if isinstance(_ether_type, Unset):
            ether_type = UNSET
        else:
            ether_type = ServicePortVOEtherType(_ether_type)

        inbound_traffic_profile_id = d.pop("inboundTrafficProfileId", UNSET)

        outbound_traffic_profile_id = d.pop("outboundTrafficProfileId", UNSET)

        service_port_vo = cls(
            index=index,
            description=description,
            onu_id=onu_id,
            admin_status=admin_status,
            statistic_performance=statistic_performance,
            active_status=active_status,
            pon_port_id=pon_port_id,
            svlan=svlan,
            gem_port_id=gem_port_id,
            user_vlan=user_vlan,
            user_vlan_priority=user_vlan_priority,
            tag_action=tag_action,
            inner_vlan=inner_vlan,
            inner_vlan_priority=inner_vlan_priority,
            ether_type=ether_type,
            inbound_traffic_profile_id=inbound_traffic_profile_id,
            outbound_traffic_profile_id=outbound_traffic_profile_id,
        )

        service_port_vo.additional_properties = d
        return service_port_vo

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
