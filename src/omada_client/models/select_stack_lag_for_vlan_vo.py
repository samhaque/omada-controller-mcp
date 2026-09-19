from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_brief_vo import DeviceBriefVO


T = TypeVar("T", bound="SelectStackLagForVlanVO")


@_attrs_define
class SelectStackLagForVlanVO:
    """Lags

    Attributes:
        name (str | Unset): Name.
        enable (bool | Unset): Whether the port is affected.
        select_by_user (bool | Unset): Whether the port is selected by user.
        un_select_by_user (bool | Unset): Whether the auto-select port is unselected by user.
        default_vlan (int | Unset): The vlan of default network.
        edit_enable (bool | Unset): Whether the port is selectable.
        need_confirm (bool | Unset): Whether the port needs confirm for binding non-default vlan.
        need_confirm_cascade_port (bool | Unset): Whether the port needs confirm for being cascade port.
        controller_linked_port (bool | Unset): Whether the port is connected to the Controller.
        auto_select (bool | Unset): Whether the port needs to be automatically selected.
        reasons (list[int] | Unset): Only valid when editEnable is false. It indicates the reason why the port is not
            selectable.Each Item should be a value as follows: -2: The port has been added to LAG. Lag member port can not
            be selected; -8: The port is wan port. Wan port can not be selected; -10: The AP’s LAN port cannot be
            configured; -12: The port's tags setting is not custom and therefore it can not be selected when creating multi
            vlan; -13: The port is stack port. Stack port can not be selected; -14: The number of VLANs has reached the
            limit of the Easy Managed Switch.
        downlink_devices (list[DeviceBriefVO] | Unset): The downlink devices of the port
        upper_device (DeviceBriefVO | Unset): The upper device of the port
        native_is_default (bool | Unset): It indicates whether the native network of the port is default.
        native_network_vlan (int | Unset): The native network vlan of the port.
        native_network_name (str | Unset): The native network name of the port.
        osw_port_network_tags_setting (int | Unset): The port network tag setting. 0:allow all, 1:block all, 2:custom
        need_confirm_voice_network (bool | Unset): When creating single vlan and the port's voice network is enabled,
            needConfirmVoiceNetwork is true.
        id (int | Unset): Lag ID
        ports (list[int] | Unset): The ports in the lag. Each item is Integer, for example: [1, 2].
        st_ports (list[str] | Unset): The ports in the lag. Each item is String, for example: [1/0/1, 1/0/2].
    """

    name: str | Unset = UNSET
    enable: bool | Unset = UNSET
    select_by_user: bool | Unset = UNSET
    un_select_by_user: bool | Unset = UNSET
    default_vlan: int | Unset = UNSET
    edit_enable: bool | Unset = UNSET
    need_confirm: bool | Unset = UNSET
    need_confirm_cascade_port: bool | Unset = UNSET
    controller_linked_port: bool | Unset = UNSET
    auto_select: bool | Unset = UNSET
    reasons: list[int] | Unset = UNSET
    downlink_devices: list[DeviceBriefVO] | Unset = UNSET
    upper_device: DeviceBriefVO | Unset = UNSET
    native_is_default: bool | Unset = UNSET
    native_network_vlan: int | Unset = UNSET
    native_network_name: str | Unset = UNSET
    osw_port_network_tags_setting: int | Unset = UNSET
    need_confirm_voice_network: bool | Unset = UNSET
    id: int | Unset = UNSET
    ports: list[int] | Unset = UNSET
    st_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enable = self.enable

        select_by_user = self.select_by_user

        un_select_by_user = self.un_select_by_user

        default_vlan = self.default_vlan

        edit_enable = self.edit_enable

        need_confirm = self.need_confirm

        need_confirm_cascade_port = self.need_confirm_cascade_port

        controller_linked_port = self.controller_linked_port

        auto_select = self.auto_select

        reasons: list[int] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = self.reasons

        downlink_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_devices, Unset):
            downlink_devices = []
            for downlink_devices_item_data in self.downlink_devices:
                downlink_devices_item = downlink_devices_item_data.to_dict()
                downlink_devices.append(downlink_devices_item)

        upper_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upper_device, Unset):
            upper_device = self.upper_device.to_dict()

        native_is_default = self.native_is_default

        native_network_vlan = self.native_network_vlan

        native_network_name = self.native_network_name

        osw_port_network_tags_setting = self.osw_port_network_tags_setting

        need_confirm_voice_network = self.need_confirm_voice_network

        id = self.id

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        st_ports: list[str] | Unset = UNSET
        if not isinstance(self.st_ports, Unset):
            st_ports = self.st_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enable is not UNSET:
            field_dict["Enable"] = enable
        if select_by_user is not UNSET:
            field_dict["selectByUser"] = select_by_user
        if un_select_by_user is not UNSET:
            field_dict["unSelectByUser"] = un_select_by_user
        if default_vlan is not UNSET:
            field_dict["defaultVlan"] = default_vlan
        if edit_enable is not UNSET:
            field_dict["editEnable"] = edit_enable
        if need_confirm is not UNSET:
            field_dict["needConfirm"] = need_confirm
        if need_confirm_cascade_port is not UNSET:
            field_dict["needConfirmCascadePort"] = need_confirm_cascade_port
        if controller_linked_port is not UNSET:
            field_dict["controllerLinkedPort"] = controller_linked_port
        if auto_select is not UNSET:
            field_dict["autoSelect"] = auto_select
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if downlink_devices is not UNSET:
            field_dict["downlinkDevices"] = downlink_devices
        if upper_device is not UNSET:
            field_dict["upperDevice"] = upper_device
        if native_is_default is not UNSET:
            field_dict["nativeIsDefault"] = native_is_default
        if native_network_vlan is not UNSET:
            field_dict["nativeNetworkVlan"] = native_network_vlan
        if native_network_name is not UNSET:
            field_dict["nativeNetworkName"] = native_network_name
        if osw_port_network_tags_setting is not UNSET:
            field_dict["oswPortNetworkTagsSetting"] = osw_port_network_tags_setting
        if need_confirm_voice_network is not UNSET:
            field_dict["needConfirmVoiceNetwork"] = need_confirm_voice_network
        if id is not UNSET:
            field_dict["id"] = id
        if ports is not UNSET:
            field_dict["ports"] = ports
        if st_ports is not UNSET:
            field_dict["stPorts"] = st_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_brief_vo import DeviceBriefVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enable = d.pop("Enable", UNSET)

        select_by_user = d.pop("selectByUser", UNSET)

        un_select_by_user = d.pop("unSelectByUser", UNSET)

        default_vlan = d.pop("defaultVlan", UNSET)

        edit_enable = d.pop("editEnable", UNSET)

        need_confirm = d.pop("needConfirm", UNSET)

        need_confirm_cascade_port = d.pop("needConfirmCascadePort", UNSET)

        controller_linked_port = d.pop("controllerLinkedPort", UNSET)

        auto_select = d.pop("autoSelect", UNSET)

        reasons = cast(list[int], d.pop("reasons", UNSET))

        _downlink_devices = d.pop("downlinkDevices", UNSET)
        downlink_devices: list[DeviceBriefVO] | Unset = UNSET
        if _downlink_devices is not UNSET:
            downlink_devices = []
            for downlink_devices_item_data in _downlink_devices:
                downlink_devices_item = DeviceBriefVO.from_dict(
                    downlink_devices_item_data
                )

                downlink_devices.append(downlink_devices_item)

        _upper_device = d.pop("upperDevice", UNSET)
        upper_device: DeviceBriefVO | Unset
        if isinstance(_upper_device, Unset):
            upper_device = UNSET
        else:
            upper_device = DeviceBriefVO.from_dict(_upper_device)

        native_is_default = d.pop("nativeIsDefault", UNSET)

        native_network_vlan = d.pop("nativeNetworkVlan", UNSET)

        native_network_name = d.pop("nativeNetworkName", UNSET)

        osw_port_network_tags_setting = d.pop("oswPortNetworkTagsSetting", UNSET)

        need_confirm_voice_network = d.pop("needConfirmVoiceNetwork", UNSET)

        id = d.pop("id", UNSET)

        ports = cast(list[int], d.pop("ports", UNSET))

        st_ports = cast(list[str], d.pop("stPorts", UNSET))

        select_stack_lag_for_vlan_vo = cls(
            name=name,
            enable=enable,
            select_by_user=select_by_user,
            un_select_by_user=un_select_by_user,
            default_vlan=default_vlan,
            edit_enable=edit_enable,
            need_confirm=need_confirm,
            need_confirm_cascade_port=need_confirm_cascade_port,
            controller_linked_port=controller_linked_port,
            auto_select=auto_select,
            reasons=reasons,
            downlink_devices=downlink_devices,
            upper_device=upper_device,
            native_is_default=native_is_default,
            native_network_vlan=native_network_vlan,
            native_network_name=native_network_name,
            osw_port_network_tags_setting=osw_port_network_tags_setting,
            need_confirm_voice_network=need_confirm_voice_network,
            id=id,
            ports=ports,
            st_ports=st_ports,
        )

        select_stack_lag_for_vlan_vo.additional_properties = d
        return select_stack_lag_for_vlan_vo

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
