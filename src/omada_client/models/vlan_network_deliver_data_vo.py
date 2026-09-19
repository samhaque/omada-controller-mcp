from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_vo import LanNetworkVO
    from ..models.select_device_for_vlan_vo import SelectDeviceForVlanVO
    from ..models.select_port_binding_brief_vo import SelectPortBindingBriefVO
    from ..models.select_stack_for_vlan_vo import SelectStackForVlanVO


T = TypeVar("T", bound="VlanNetworkDeliverDataVO")


@_attrs_define
class VlanNetworkDeliverDataVO:
    """
    Attributes:
        success_devices (list[str] | Unset): Successfully delivered devices
        success_stacks (list[str] | Unset): Successfully delivered stacks
        fail_devices (list[str] | Unset): Failed devices
        fail_stacks (list[str] | Unset): Failed stacks
        delivering_devices (list[str] | Unset): Delivering devices
        delivering_stacks (list[str] | Unset): Delivering stacks
        done_devices_num (int | Unset): Delivered device num
        total_devices_num (int | Unset): Total device num
        state (int | Unset): Delivering state. 0: free ( it means the network has been already delivered)  1: delivering
            2. deliver done.
        lan_network (LanNetworkVO | Unset): LANNetworkVO
        affected_device_list (list[SelectDeviceForVlanVO] | Unset): Affected device list
        affected_stack_list (list[SelectStackForVlanVO] | Unset): Affected stack list
        device_config (SelectPortBindingBriefVO | Unset): Devcie config.
    """

    success_devices: list[str] | Unset = UNSET
    success_stacks: list[str] | Unset = UNSET
    fail_devices: list[str] | Unset = UNSET
    fail_stacks: list[str] | Unset = UNSET
    delivering_devices: list[str] | Unset = UNSET
    delivering_stacks: list[str] | Unset = UNSET
    done_devices_num: int | Unset = UNSET
    total_devices_num: int | Unset = UNSET
    state: int | Unset = UNSET
    lan_network: LanNetworkVO | Unset = UNSET
    affected_device_list: list[SelectDeviceForVlanVO] | Unset = UNSET
    affected_stack_list: list[SelectStackForVlanVO] | Unset = UNSET
    device_config: SelectPortBindingBriefVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_devices: list[str] | Unset = UNSET
        if not isinstance(self.success_devices, Unset):
            success_devices = self.success_devices

        success_stacks: list[str] | Unset = UNSET
        if not isinstance(self.success_stacks, Unset):
            success_stacks = self.success_stacks

        fail_devices: list[str] | Unset = UNSET
        if not isinstance(self.fail_devices, Unset):
            fail_devices = self.fail_devices

        fail_stacks: list[str] | Unset = UNSET
        if not isinstance(self.fail_stacks, Unset):
            fail_stacks = self.fail_stacks

        delivering_devices: list[str] | Unset = UNSET
        if not isinstance(self.delivering_devices, Unset):
            delivering_devices = self.delivering_devices

        delivering_stacks: list[str] | Unset = UNSET
        if not isinstance(self.delivering_stacks, Unset):
            delivering_stacks = self.delivering_stacks

        done_devices_num = self.done_devices_num

        total_devices_num = self.total_devices_num

        state = self.state

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_devices is not UNSET:
            field_dict["successDevices"] = success_devices
        if success_stacks is not UNSET:
            field_dict["successStacks"] = success_stacks
        if fail_devices is not UNSET:
            field_dict["failDevices"] = fail_devices
        if fail_stacks is not UNSET:
            field_dict["failStacks"] = fail_stacks
        if delivering_devices is not UNSET:
            field_dict["deliveringDevices"] = delivering_devices
        if delivering_stacks is not UNSET:
            field_dict["deliveringStacks"] = delivering_stacks
        if done_devices_num is not UNSET:
            field_dict["doneDevicesNum"] = done_devices_num
        if total_devices_num is not UNSET:
            field_dict["totalDevicesNum"] = total_devices_num
        if state is not UNSET:
            field_dict["state"] = state
        if lan_network is not UNSET:
            field_dict["lanNetwork"] = lan_network
        if affected_device_list is not UNSET:
            field_dict["affectedDeviceList"] = affected_device_list
        if affected_stack_list is not UNSET:
            field_dict["affectedStackList"] = affected_stack_list
        if device_config is not UNSET:
            field_dict["deviceConfig"] = device_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_vo import LanNetworkVO
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
        success_devices = cast(list[str], d.pop("successDevices", UNSET))

        success_stacks = cast(list[str], d.pop("successStacks", UNSET))

        fail_devices = cast(list[str], d.pop("failDevices", UNSET))

        fail_stacks = cast(list[str], d.pop("failStacks", UNSET))

        delivering_devices = cast(list[str], d.pop("deliveringDevices", UNSET))

        delivering_stacks = cast(list[str], d.pop("deliveringStacks", UNSET))

        done_devices_num = d.pop("doneDevicesNum", UNSET)

        total_devices_num = d.pop("totalDevicesNum", UNSET)

        state = d.pop("state", UNSET)

        _lan_network = d.pop("lanNetwork", UNSET)
        lan_network: LanNetworkVO | Unset
        if isinstance(_lan_network, Unset):
            lan_network = UNSET
        else:
            lan_network = LanNetworkVO.from_dict(_lan_network)

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

        vlan_network_deliver_data_vo = cls(
            success_devices=success_devices,
            success_stacks=success_stacks,
            fail_devices=fail_devices,
            fail_stacks=fail_stacks,
            delivering_devices=delivering_devices,
            delivering_stacks=delivering_stacks,
            done_devices_num=done_devices_num,
            total_devices_num=total_devices_num,
            state=state,
            lan_network=lan_network,
            affected_device_list=affected_device_list,
            affected_stack_list=affected_stack_list,
            device_config=device_config,
        )

        vlan_network_deliver_data_vo.additional_properties = d
        return vlan_network_deliver_data_vo

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
