from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.auto_service_port_dto_auto_mode import AutoServicePortDTOAutoMode
from ..models.auto_service_port_dto_ether_type import AutoServicePortDTOEtherType
from ..models.auto_service_port_dto_tag_action import AutoServicePortDTOTagAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoServicePortDTO")


@_attrs_define
class AutoServicePortDTO:
    """
    Attributes:
        pon_port_id (int | Unset): PonPortId should be within the range of 1 to 16
        pon_port_str (str | Unset): String form of pon port
        svlan (int | Unset): SVlan should be within the range of 1 to 4095
        gem_port_id (int | Unset): GemPortId should be within the range of 1 to 1023
        user_vlan (int | Unset): UserVlan should be within the range of 0 to 4095
        user_vlan_priority (int | Unset): UserVlanPriority should be within the range of -1 to 7
        tag_action (AutoServicePortDTOTagAction | Unset): TagAction should be a value as
            follows:DEFAULT,TRANSPARENT,TRANSLATE,TRANSLATE_AND_ADD,ADD_DOUBLE
        inner_vlan (int | Unset): InnerVlan should be within the range of 0 to 4095
        inner_vlan_priority (int | Unset): InnerVlanPriority should be within the range of -1 to 7
        ether_type (AutoServicePortDTOEtherType | Unset): EtherType should be a value as
            follows:NONE,IPV4OE,IPV6OE,PPPOE
        inbound_traffic_profile_id (int | Unset): InboundTrafficProfileId should be within the range of 0 to 512
        outbound_traffic_profile_id (int | Unset): OutboundTrafficProfileId should be within the range of 0 to 512
        auto_mode (AutoServicePortDTOAutoMode | Unset): AutoMOde should be a value as follows:Disable,Enable
    """

    pon_port_id: int | Unset = UNSET
    pon_port_str: str | Unset = UNSET
    svlan: int | Unset = UNSET
    gem_port_id: int | Unset = UNSET
    user_vlan: int | Unset = UNSET
    user_vlan_priority: int | Unset = UNSET
    tag_action: AutoServicePortDTOTagAction | Unset = UNSET
    inner_vlan: int | Unset = UNSET
    inner_vlan_priority: int | Unset = UNSET
    ether_type: AutoServicePortDTOEtherType | Unset = UNSET
    inbound_traffic_profile_id: int | Unset = UNSET
    outbound_traffic_profile_id: int | Unset = UNSET
    auto_mode: AutoServicePortDTOAutoMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pon_port_id = self.pon_port_id

        pon_port_str = self.pon_port_str

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

        auto_mode: str | Unset = UNSET
        if not isinstance(self.auto_mode, Unset):
            auto_mode = self.auto_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pon_port_id is not UNSET:
            field_dict["ponPortId"] = pon_port_id
        if pon_port_str is not UNSET:
            field_dict["ponPortStr"] = pon_port_str
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
        if auto_mode is not UNSET:
            field_dict["autoMode"] = auto_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pon_port_id = d.pop("ponPortId", UNSET)

        pon_port_str = d.pop("ponPortStr", UNSET)

        svlan = d.pop("svlan", UNSET)

        gem_port_id = d.pop("gemPortId", UNSET)

        user_vlan = d.pop("userVlan", UNSET)

        user_vlan_priority = d.pop("userVlanPriority", UNSET)

        _tag_action = d.pop("tagAction", UNSET)
        tag_action: AutoServicePortDTOTagAction | Unset
        if isinstance(_tag_action, Unset):
            tag_action = UNSET
        else:
            tag_action = AutoServicePortDTOTagAction(_tag_action)

        inner_vlan = d.pop("innerVlan", UNSET)

        inner_vlan_priority = d.pop("innerVlanPriority", UNSET)

        _ether_type = d.pop("etherType", UNSET)
        ether_type: AutoServicePortDTOEtherType | Unset
        if isinstance(_ether_type, Unset):
            ether_type = UNSET
        else:
            ether_type = AutoServicePortDTOEtherType(_ether_type)

        inbound_traffic_profile_id = d.pop("inboundTrafficProfileId", UNSET)

        outbound_traffic_profile_id = d.pop("outboundTrafficProfileId", UNSET)

        _auto_mode = d.pop("autoMode", UNSET)
        auto_mode: AutoServicePortDTOAutoMode | Unset
        if isinstance(_auto_mode, Unset):
            auto_mode = UNSET
        else:
            auto_mode = AutoServicePortDTOAutoMode(_auto_mode)

        auto_service_port_dto = cls(
            pon_port_id=pon_port_id,
            pon_port_str=pon_port_str,
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
            auto_mode=auto_mode,
        )

        auto_service_port_dto.additional_properties = d
        return auto_service_port_dto

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
