from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.service_port_profile_list_detail_dto_admin_status import (
    ServicePortProfileListDetailDTOAdminStatus,
)
from ..models.service_port_profile_list_detail_dto_creation_mode import (
    ServicePortProfileListDetailDTOCreationMode,
)
from ..models.service_port_profile_list_detail_dto_ether_type import (
    ServicePortProfileListDetailDTOEtherType,
)
from ..models.service_port_profile_list_detail_dto_in_use import (
    ServicePortProfileListDetailDTOInUse,
)
from ..models.service_port_profile_list_detail_dto_statistic_performance import (
    ServicePortProfileListDetailDTOStatisticPerformance,
)
from ..models.service_port_profile_list_detail_dto_tag_action import (
    ServicePortProfileListDetailDTOTagAction,
)

T = TypeVar("T", bound="ServicePortProfileListDetailDTO")


@_attrs_define
class ServicePortProfileListDetailDTO:
    """Content

    Attributes:
        service_port_id (str): Display Service Port Entry ID. The servicePortId should be within the range of 1 to 127.
        service_port_profile_id (str): Service template ID. The servicePortProfileId should be within the range of 1 to
            127.
        svlan (int): The value of the SVLAN. The svlan should be within the range of 1 to 4094.
        gem_id (int): The value of the GEM ID. The gemId should be within the range of 1-1023
        user_vlan (int): The value of the User VLAN. The userVlan should be within the range of 1 to 4094.
        user_vlan_priority (int): The value of the User VLAN Priority. The userVlanPriority should be within the range
            of 0 to 7.A value of -1 means that the item is not configured.
        tag_action (ServicePortProfileListDetailDTOTagAction): TAG Action
        inner_vlan (int): The innerVlan should be within the range of 1 to 4094.This configuration item appears if and
            only if Translate-And-Add/Add/Add-Double is selected for tag_action, using -1 means that the item is not
            configured, and the effect will be displayed as --.
        inner_vlan_priority (int): The innerVlanPriority should be within the range of 0 to 7. Only takes effect when
            Translate-And-Add/Add/Add-Double is selected for tag_action. Using -1 means that the item is not configured, and
            is displayed as --.
        ether_type (ServicePortProfileListDetailDTOEtherType): The Ether Type value
        inbound_traffic_profile_id (int): The inboundTrafficProfileId should be within the range of 1 to 1023 (Traffic
            profiles that already exist on the system). Using -1 means that the item is not configured, and is displayed as
            --.
        outbound_traffic_profile_id (int): The outboundTrafficProfileId should be within the range of 1 to 1023 (Traffic
            profiles that already exist in the system). Using -1 means that the item is not configured, and is displayed as
            --.
        statistic_performance (ServicePortProfileListDetailDTOStatisticPerformance): The statistic performance
        admin_status (ServicePortProfileListDetailDTOAdminStatus): The admin status
        description (str): The description should be 1-32 characters, including uppercase and lowercase letters,
            numbers, and underscores.
        creation_mode (ServicePortProfileListDetailDTOCreationMode): The creation mode
        entries_number (int): Number of service ports. The entriesNumber should be within the range of 0 to 127.
        in_use (ServicePortProfileListDetailDTOInUse): Indicate whether the profile has been used
    """

    service_port_id: str
    service_port_profile_id: str
    svlan: int
    gem_id: int
    user_vlan: int
    user_vlan_priority: int
    tag_action: ServicePortProfileListDetailDTOTagAction
    inner_vlan: int
    inner_vlan_priority: int
    ether_type: ServicePortProfileListDetailDTOEtherType
    inbound_traffic_profile_id: int
    outbound_traffic_profile_id: int
    statistic_performance: ServicePortProfileListDetailDTOStatisticPerformance
    admin_status: ServicePortProfileListDetailDTOAdminStatus
    description: str
    creation_mode: ServicePortProfileListDetailDTOCreationMode
    entries_number: int
    in_use: ServicePortProfileListDetailDTOInUse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_port_id = self.service_port_id

        service_port_profile_id = self.service_port_profile_id

        svlan = self.svlan

        gem_id = self.gem_id

        user_vlan = self.user_vlan

        user_vlan_priority = self.user_vlan_priority

        tag_action = self.tag_action.value

        inner_vlan = self.inner_vlan

        inner_vlan_priority = self.inner_vlan_priority

        ether_type = self.ether_type.value

        inbound_traffic_profile_id = self.inbound_traffic_profile_id

        outbound_traffic_profile_id = self.outbound_traffic_profile_id

        statistic_performance = self.statistic_performance.value

        admin_status = self.admin_status.value

        description = self.description

        creation_mode = self.creation_mode.value

        entries_number = self.entries_number

        in_use = self.in_use.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "servicePortId": service_port_id,
                "servicePortProfileId": service_port_profile_id,
                "svlan": svlan,
                "gemId": gem_id,
                "userVlan": user_vlan,
                "userVlanPriority": user_vlan_priority,
                "tagAction": tag_action,
                "innerVlan": inner_vlan,
                "innerVlanPriority": inner_vlan_priority,
                "etherType": ether_type,
                "inboundTrafficProfileId": inbound_traffic_profile_id,
                "outboundTrafficProfileId": outbound_traffic_profile_id,
                "statisticPerformance": statistic_performance,
                "adminStatus": admin_status,
                "description": description,
                "creationMode": creation_mode,
                "entriesNumber": entries_number,
                "inUse": in_use,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_port_id = d.pop("servicePortId")

        service_port_profile_id = d.pop("servicePortProfileId")

        svlan = d.pop("svlan")

        gem_id = d.pop("gemId")

        user_vlan = d.pop("userVlan")

        user_vlan_priority = d.pop("userVlanPriority")

        tag_action = ServicePortProfileListDetailDTOTagAction(d.pop("tagAction"))

        inner_vlan = d.pop("innerVlan")

        inner_vlan_priority = d.pop("innerVlanPriority")

        ether_type = ServicePortProfileListDetailDTOEtherType(d.pop("etherType"))

        inbound_traffic_profile_id = d.pop("inboundTrafficProfileId")

        outbound_traffic_profile_id = d.pop("outboundTrafficProfileId")

        statistic_performance = ServicePortProfileListDetailDTOStatisticPerformance(
            d.pop("statisticPerformance")
        )

        admin_status = ServicePortProfileListDetailDTOAdminStatus(d.pop("adminStatus"))

        description = d.pop("description")

        creation_mode = ServicePortProfileListDetailDTOCreationMode(
            d.pop("creationMode")
        )

        entries_number = d.pop("entriesNumber")

        in_use = ServicePortProfileListDetailDTOInUse(d.pop("inUse"))

        service_port_profile_list_detail_dto = cls(
            service_port_id=service_port_id,
            service_port_profile_id=service_port_profile_id,
            svlan=svlan,
            gem_id=gem_id,
            user_vlan=user_vlan,
            user_vlan_priority=user_vlan_priority,
            tag_action=tag_action,
            inner_vlan=inner_vlan,
            inner_vlan_priority=inner_vlan_priority,
            ether_type=ether_type,
            inbound_traffic_profile_id=inbound_traffic_profile_id,
            outbound_traffic_profile_id=outbound_traffic_profile_id,
            statistic_performance=statistic_performance,
            admin_status=admin_status,
            description=description,
            creation_mode=creation_mode,
            entries_number=entries_number,
            in_use=in_use,
        )

        service_port_profile_list_detail_dto.additional_properties = d
        return service_port_profile_list_detail_dto

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
