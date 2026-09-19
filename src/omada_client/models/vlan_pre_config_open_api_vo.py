from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_query_open_api_v3vo import LanNetworkQueryOpenApiV3VO
    from ..models.select_device_for_vlan_vo import SelectDeviceForVlanVO
    from ..models.select_port_binding_brief_vo import SelectPortBindingBriefVO
    from ..models.select_stack_for_vlan_vo import SelectStackForVlanVO


T = TypeVar("T", bound="VlanPreConfigOpenApiVO")


@_attrs_define
class VlanPreConfigOpenApiVO:
    """VlanPreConfigOpenApiVO

    Attributes:
        lan_network (LanNetworkQueryOpenApiV3VO | Unset): LANNetworkQueryOpenApiVO
        affected_device_list (list[SelectDeviceForVlanVO] | Unset): Affected device list
        affected_stack_list (list[SelectStackForVlanVO] | Unset): Affected stack list
        device_config (SelectPortBindingBriefVO | Unset): Devcie config.
        network_segment_changed (bool | Unset): Indicate whether the network segment change when modifying network
        total_affected_device_num (int | Unset): Indicate total affected devices num, including devices with ports that
            have Network Tags Setting set to Allow all
    """

    lan_network: LanNetworkQueryOpenApiV3VO | Unset = UNSET
    affected_device_list: list[SelectDeviceForVlanVO] | Unset = UNSET
    affected_stack_list: list[SelectStackForVlanVO] | Unset = UNSET
    device_config: SelectPortBindingBriefVO | Unset = UNSET
    network_segment_changed: bool | Unset = UNSET
    total_affected_device_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lan_network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan_network, Unset):
            lan_network = self.lan_network.to_dict()

        affected_device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.affected_device_list, Unset):
            affected_device_list = []
            for affected_device_list_item_data in self.affected_device_list:
                affected_device_list_item = affected_device_list_item_data.to_dict()
                affected_device_list.append(affected_device_list_item)

        affected_stack_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.affected_stack_list, Unset):
            affected_stack_list = []
            for affected_stack_list_item_data in self.affected_stack_list:
                affected_stack_list_item = affected_stack_list_item_data.to_dict()
                affected_stack_list.append(affected_stack_list_item)

        device_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_config, Unset):
            device_config = self.device_config.to_dict()

        network_segment_changed = self.network_segment_changed

        total_affected_device_num = self.total_affected_device_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lan_network is not UNSET:
            field_dict["lanNetwork"] = lan_network
        if affected_device_list is not UNSET:
            field_dict["affectedDeviceList"] = affected_device_list
        if affected_stack_list is not UNSET:
            field_dict["affectedStackList"] = affected_stack_list
        if device_config is not UNSET:
            field_dict["deviceConfig"] = device_config
        if network_segment_changed is not UNSET:
            field_dict["networkSegmentChanged"] = network_segment_changed
        if total_affected_device_num is not UNSET:
            field_dict["totalAffectedDeviceNum"] = total_affected_device_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_query_open_api_v3vo import (
            LanNetworkQueryOpenApiV3VO,
        )
        from ..models.select_device_for_vlan_vo import (
            SelectDeviceForVlanVO,
        )
        from ..models.select_port_binding_brief_vo import (
            SelectPortBindingBriefVO,
        )
        from ..models.select_stack_for_vlan_vo import (
            SelectStackForVlanVO,
        )

        d = dict(src_dict)
        _lan_network = d.pop("lanNetwork", UNSET)
        lan_network: LanNetworkQueryOpenApiV3VO | Unset
        if isinstance(_lan_network, Unset):
            lan_network = UNSET
        else:
            lan_network = LanNetworkQueryOpenApiV3VO.from_dict(_lan_network)

        _affected_device_list = d.pop("affectedDeviceList", UNSET)
        affected_device_list: list[SelectDeviceForVlanVO] | Unset = UNSET
        if _affected_device_list is not UNSET:
            affected_device_list = []
            for affected_device_list_item_data in _affected_device_list:
                affected_device_list_item = SelectDeviceForVlanVO.from_dict(
                    affected_device_list_item_data
                )

                affected_device_list.append(affected_device_list_item)

        _affected_stack_list = d.pop("affectedStackList", UNSET)
        affected_stack_list: list[SelectStackForVlanVO] | Unset = UNSET
        if _affected_stack_list is not UNSET:
            affected_stack_list = []
            for affected_stack_list_item_data in _affected_stack_list:
                affected_stack_list_item = SelectStackForVlanVO.from_dict(
                    affected_stack_list_item_data
                )

                affected_stack_list.append(affected_stack_list_item)

        _device_config = d.pop("deviceConfig", UNSET)
        device_config: SelectPortBindingBriefVO | Unset
        if isinstance(_device_config, Unset):
            device_config = UNSET
        else:
            device_config = SelectPortBindingBriefVO.from_dict(_device_config)

        network_segment_changed = d.pop("networkSegmentChanged", UNSET)

        total_affected_device_num = d.pop("totalAffectedDeviceNum", UNSET)

        vlan_pre_config_open_api_vo = cls(
            lan_network=lan_network,
            affected_device_list=affected_device_list,
            affected_stack_list=affected_stack_list,
            device_config=device_config,
            network_segment_changed=network_segment_changed,
            total_affected_device_num=total_affected_device_num,
        )

        vlan_pre_config_open_api_vo.additional_properties = d
        return vlan_pre_config_open_api_vo

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
