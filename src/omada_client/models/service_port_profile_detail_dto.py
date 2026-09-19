from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.service_port_profile_detail_dto_admin_status import (
    ServicePortProfileDetailDTOAdminStatus,
)
from ..models.service_port_profile_detail_dto_creation_mode import (
    ServicePortProfileDetailDTOCreationMode,
)
from ..models.service_port_profile_detail_dto_ether_type import (
    ServicePortProfileDetailDTOEtherType,
)
from ..models.service_port_profile_detail_dto_in_use import (
    ServicePortProfileDetailDTOInUse,
)
from ..models.service_port_profile_detail_dto_statistic_performance import (
    ServicePortProfileDetailDTOStatisticPerformance,
)
from ..models.service_port_profile_detail_dto_tag_action import (
    ServicePortProfileDetailDTOTagAction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicePortProfileDetailDTO")


@_attrs_define
class ServicePortProfileDetailDTO:
    """
    Attributes:
        service_port_id (str): Service port profile ID. The servicePortProfileId should be within the range of 1 to 127.
        service_port_profile_id (str): Service template ID. The servicePortProfileId should be within the range of 1 to
            127. It can be obtained from "Get service port profile list"
        svlan (int): Bound network VLAN ID after automatic flow creation. The svlan should be within the range of
            1-4094.
        gem_id (int): Gem Port ID for automatic flow creation. The gemPort should be within the range of 1-1023.
        user_vlan (int): User VLAN ID for automatic flow creation. The userVlan should be within the range of 0-4094.
        user_vlan_priority (int): User VLAN priority. The userVlanPriority should be within the range of -1 to 7, -1
            indicating not configuring the item.
        tag_action (ServicePortProfileDetailDTOTagAction): VLAN TAG operation after automatic flow creation
        inner_vlan (int): Inner VLAN ID for automatic flow creation. This parameter is associated with tagAction. When
            tagAction is TRANSLATE_AND_ADD/ADD_DOUBLE, this parameter is valid. The innerVlan should be within the range of
            0-4094, -1 indicating not configuring the item.
        inner_vlan_priority (int): Inner VLAN priority. This parameter is associated with tagAction. When tagAction is
            TRANSLATE_AND_ADD/ADD_DOUBLE, this parameter is valid. The innerVlanPriority should be within the range of -1 to
            7, -1 indicating not configuring the item.
        ether_type (ServicePortProfileDetailDTOEtherType): Message type
        inbound_traffic_profile_id (int): Inbound traffic profile ID. The inboundTrafficProfileId should be within the
            range of 1-1023, -1 indicating not configuring the item.
        outbound_traffic_profile_id (int): Outbound traffic profile ID. The outboundTrafficProfileId should be within
            the range of 1-1023, -1 indicating not configuring the item.
        statistic_performance (ServicePortProfileDetailDTOStatisticPerformance): Whether to enable traffic flow
            statistics
        admin_status (ServicePortProfileDetailDTOAdminStatus): Whether to enable traffic flow
        creation_mode (ServicePortProfileDetailDTOCreationMode): The creation mode
        entries_number (int): Service port amount. The entriesNumber should be within the range of 0 to 127.
        in_use (ServicePortProfileDetailDTOInUse): Indicate whether the profile has been used
        description (str | Unset): Service port description. Description should contain 1-32 characters, including
            uppercase and lowercase letters, numbers, and symbols(-@_:/.).
    """

    service_port_id: str
    service_port_profile_id: str
    svlan: int
    gem_id: int
    user_vlan: int
    user_vlan_priority: int
    tag_action: ServicePortProfileDetailDTOTagAction
    inner_vlan: int
    inner_vlan_priority: int
    ether_type: ServicePortProfileDetailDTOEtherType
    inbound_traffic_profile_id: int
    outbound_traffic_profile_id: int
    statistic_performance: ServicePortProfileDetailDTOStatisticPerformance
    admin_status: ServicePortProfileDetailDTOAdminStatus
    creation_mode: ServicePortProfileDetailDTOCreationMode
    entries_number: int
    in_use: ServicePortProfileDetailDTOInUse
    description: str | Unset = UNSET
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

        creation_mode = self.creation_mode.value

        entries_number = self.entries_number

        in_use = self.in_use.value

        description = self.description

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
                "creationMode": creation_mode,
                "entriesNumber": entries_number,
                "inUse": in_use,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

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

        tag_action = ServicePortProfileDetailDTOTagAction(d.pop("tagAction"))

        inner_vlan = d.pop("innerVlan")

        inner_vlan_priority = d.pop("innerVlanPriority")

        ether_type = ServicePortProfileDetailDTOEtherType(d.pop("etherType"))

        inbound_traffic_profile_id = d.pop("inboundTrafficProfileId")

        outbound_traffic_profile_id = d.pop("outboundTrafficProfileId")

        statistic_performance = ServicePortProfileDetailDTOStatisticPerformance(
            d.pop("statisticPerformance")
        )

        admin_status = ServicePortProfileDetailDTOAdminStatus(d.pop("adminStatus"))

        creation_mode = ServicePortProfileDetailDTOCreationMode(d.pop("creationMode"))

        entries_number = d.pop("entriesNumber")

        in_use = ServicePortProfileDetailDTOInUse(d.pop("inUse"))

        description = d.pop("description", UNSET)

        service_port_profile_detail_dto = cls(
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
            creation_mode=creation_mode,
            entries_number=entries_number,
            in_use=in_use,
            description=description,
        )

        service_port_profile_detail_dto.additional_properties = d
        return service_port_profile_detail_dto

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
