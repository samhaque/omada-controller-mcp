from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lag_info_vo import LagInfoVO
    from ..models.mlag_msg_vo import MlagMsgVO
    from ..models.osw_device_misc_vo import OswDeviceMiscVO
    from ..models.osw_port_vo import OswPortVO
    from ..models.osw_stack_port_group_vo import OswStackPortGroupVO
    from ..models.stack_msg_vo import StackMsgVO


T = TypeVar("T", bound="OuiBasedVlanDeviceInfoVO")


@_attrs_define
class OuiBasedVlanDeviceInfoVO:
    """
    Attributes:
        name (str | Unset): Device name,default value is the mac address of device
        mac (str | Unset): Device mac
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        status (int | Unset): Device status. The value must be one of the following: 0: Disconnected; 1: Disconnected
            (Migrating); 10: Provisioning; 11: Configuring; 12: Upgrading; 13: Rebooting; 14: Connected; 15: Connected
            (Wireless); 16: Connected (Migrating); 17: Connected (Wireless, Migrating); 20: Pending; 21: Pending (Wireless);
            22: Adopting; 23: Adopting (Wireless); 24: Adoption Failed; 25: Adoption Failed (Wireless); 26: Managed by
            Others; 27: Managed by Others (Wireless); 30: Heartbeat Missed; 31: Heartbeat Missed (Wireless); 32: Heartbeat
            Missed (Migrating); 33: Heartbeat Missed (Wireless, Migrating); 40: Isolated; 41: Isolated (Migrating); 50:
            Slice Configuring
        status_category (int | Unset): Device Status Category
        active (bool | Unset): Specifies whether the device is currently in an active state.
        old_firmware_used (str | Unset): The old firmware used by the device.
        old_firmware_device (bool | Unset): Whether the device is an old firmware device.
        oui_based_vlan_version (int | Unset): Specifies the OUI-based VLAN version: 0 indicates the feature is
            unsupported, while 1, 2, and 3 represent versions v1, v2, and v3 respectively.
        ip (str | Unset): IP Address
        version (str | Unset): The version.
        added_in_advanced (bool | Unset): Specifies whether the device was added offline in advance. A value of true
            indicates that the device was pre-added offline and has not yet been adopted.
        lag_list (list[int] | Unset): The lag list of the switch device.
        device_misc (OswDeviceMiscVO | Unset): Device Misc
        lags (list[LagInfoVO] | Unset): Device Lag Infos
        lan_list (list[str] | Unset): Lan list.
        ssid_ids (list[str] | Unset): The ssid list ap device used.
        device_series_type (int | Unset): DeviceSeriesType should be a value as follows: 0:advanced; 1:pro
        stack (bool | Unset): Parameter [stack] indicates whether the device supports stacking.
        unit (int | Unset): Unit ID.
        stack_ports (list[OswStackPortGroupVO] | Unset): Stack ports info.
        ports (list[OswPortVO] | Unset): The infos of ports.
        stack_msg (StackMsgVO | Unset): Stack Message
        mlag_msg (MlagMsgVO | Unset): M-LAG Message
        es (bool | Unset): Whether it is Agile Series Switch
        custom_ports (list[int] | Unset): The ports that has some vlan not included in port vlan.
        custom_lag_ids (list[int] | Unset): The lag ids that has some vlan not included in port vlan.
        support_layout (bool | Unset): Whether the device supports reporting port layout information.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    active: bool | Unset = UNSET
    old_firmware_used: str | Unset = UNSET
    old_firmware_device: bool | Unset = UNSET
    oui_based_vlan_version: int | Unset = UNSET
    ip: str | Unset = UNSET
    version: str | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    lag_list: list[int] | Unset = UNSET
    device_misc: OswDeviceMiscVO | Unset = UNSET
    lags: list[LagInfoVO] | Unset = UNSET
    lan_list: list[str] | Unset = UNSET
    ssid_ids: list[str] | Unset = UNSET
    device_series_type: int | Unset = UNSET
    stack: bool | Unset = UNSET
    unit: int | Unset = UNSET
    stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
    ports: list[OswPortVO] | Unset = UNSET
    stack_msg: StackMsgVO | Unset = UNSET
    mlag_msg: MlagMsgVO | Unset = UNSET
    es: bool | Unset = UNSET
    custom_ports: list[int] | Unset = UNSET
    custom_lag_ids: list[int] | Unset = UNSET
    support_layout: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        status = self.status

        status_category = self.status_category

        active = self.active

        old_firmware_used = self.old_firmware_used

        old_firmware_device = self.old_firmware_device

        oui_based_vlan_version = self.oui_based_vlan_version

        ip = self.ip

        version = self.version

        added_in_advanced = self.added_in_advanced

        lag_list: list[int] | Unset = UNSET
        if not isinstance(self.lag_list, Unset):
            lag_list = self.lag_list

        device_misc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_misc, Unset):
            device_misc = self.device_misc.to_dict()

        lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = []
            for lags_item_data in self.lags:
                lags_item = lags_item_data.to_dict()
                lags.append(lags_item)

        lan_list: list[str] | Unset = UNSET
        if not isinstance(self.lan_list, Unset):
            lan_list = self.lan_list

        ssid_ids: list[str] | Unset = UNSET
        if not isinstance(self.ssid_ids, Unset):
            ssid_ids = self.ssid_ids

        device_series_type = self.device_series_type

        stack = self.stack

        unit = self.unit

        stack_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_ports, Unset):
            stack_ports = []
            for stack_ports_item_data in self.stack_ports:
                stack_ports_item = stack_ports_item_data.to_dict()
                stack_ports.append(stack_ports_item)

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        stack_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_msg, Unset):
            stack_msg = self.stack_msg.to_dict()

        mlag_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_msg, Unset):
            mlag_msg = self.mlag_msg.to_dict()

        es = self.es

        custom_ports: list[int] | Unset = UNSET
        if not isinstance(self.custom_ports, Unset):
            custom_ports = self.custom_ports

        custom_lag_ids: list[int] | Unset = UNSET
        if not isinstance(self.custom_lag_ids, Unset):
            custom_lag_ids = self.custom_lag_ids

        support_layout = self.support_layout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if active is not UNSET:
            field_dict["active"] = active
        if old_firmware_used is not UNSET:
            field_dict["oldFirmwareUsed"] = old_firmware_used
        if old_firmware_device is not UNSET:
            field_dict["oldFirmwareDevice"] = old_firmware_device
        if oui_based_vlan_version is not UNSET:
            field_dict["ouiBasedVlanVersion"] = oui_based_vlan_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if version is not UNSET:
            field_dict["version"] = version
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if lag_list is not UNSET:
            field_dict["lagList"] = lag_list
        if device_misc is not UNSET:
            field_dict["deviceMisc"] = device_misc
        if lags is not UNSET:
            field_dict["lags"] = lags
        if lan_list is not UNSET:
            field_dict["lanList"] = lan_list
        if ssid_ids is not UNSET:
            field_dict["ssidIds"] = ssid_ids
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if stack is not UNSET:
            field_dict["stack"] = stack
        if unit is not UNSET:
            field_dict["unit"] = unit
        if stack_ports is not UNSET:
            field_dict["stackPorts"] = stack_ports
        if ports is not UNSET:
            field_dict["ports"] = ports
        if stack_msg is not UNSET:
            field_dict["stackMsg"] = stack_msg
        if mlag_msg is not UNSET:
            field_dict["mlagMsg"] = mlag_msg
        if es is not UNSET:
            field_dict["es"] = es
        if custom_ports is not UNSET:
            field_dict["customPorts"] = custom_ports
        if custom_lag_ids is not UNSET:
            field_dict["customLagIds"] = custom_lag_ids
        if support_layout is not UNSET:
            field_dict["supportLayout"] = support_layout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lag_info_vo import LagInfoVO
        from ..models.mlag_msg_vo import MlagMsgVO
        from ..models.osw_device_misc_vo import OswDeviceMiscVO
        from ..models.osw_port_vo import OswPortVO
        from ..models.osw_stack_port_group_vo import (
            OswStackPortGroupVO,
        )
        from ..models.stack_msg_vo import StackMsgVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        active = d.pop("active", UNSET)

        old_firmware_used = d.pop("oldFirmwareUsed", UNSET)

        old_firmware_device = d.pop("oldFirmwareDevice", UNSET)

        oui_based_vlan_version = d.pop("ouiBasedVlanVersion", UNSET)

        ip = d.pop("ip", UNSET)

        version = d.pop("version", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        lag_list = cast(list[int], d.pop("lagList", UNSET))

        _device_misc = d.pop("deviceMisc", UNSET)
        device_misc: OswDeviceMiscVO | Unset
        if isinstance(_device_misc, Unset):
            device_misc = UNSET
        else:
            device_misc = OswDeviceMiscVO.from_dict(_device_misc)

        _lags = d.pop("lags", UNSET)
        lags: list[LagInfoVO] | Unset = UNSET
        if _lags is not UNSET:
            lags = []
            for lags_item_data in _lags:
                lags_item = LagInfoVO.from_dict(lags_item_data)

                lags.append(lags_item)

        lan_list = cast(list[str], d.pop("lanList", UNSET))

        ssid_ids = cast(list[str], d.pop("ssidIds", UNSET))

        device_series_type = d.pop("deviceSeriesType", UNSET)

        stack = d.pop("stack", UNSET)

        unit = d.pop("unit", UNSET)

        _stack_ports = d.pop("stackPorts", UNSET)
        stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
        if _stack_ports is not UNSET:
            stack_ports = []
            for stack_ports_item_data in _stack_ports:
                stack_ports_item = OswStackPortGroupVO.from_dict(stack_ports_item_data)

                stack_ports.append(stack_ports_item)

        _ports = d.pop("ports", UNSET)
        ports: list[OswPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _stack_msg = d.pop("stackMsg", UNSET)
        stack_msg: StackMsgVO | Unset
        if isinstance(_stack_msg, Unset):
            stack_msg = UNSET
        else:
            stack_msg = StackMsgVO.from_dict(_stack_msg)

        _mlag_msg = d.pop("mlagMsg", UNSET)
        mlag_msg: MlagMsgVO | Unset
        if isinstance(_mlag_msg, Unset):
            mlag_msg = UNSET
        else:
            mlag_msg = MlagMsgVO.from_dict(_mlag_msg)

        es = d.pop("es", UNSET)

        custom_ports = cast(list[int], d.pop("customPorts", UNSET))

        custom_lag_ids = cast(list[int], d.pop("customLagIds", UNSET))

        support_layout = d.pop("supportLayout", UNSET)

        oui_based_vlan_device_info_vo = cls(
            name=name,
            mac=mac,
            type_=type_,
            model=model,
            model_version=model_version,
            status=status,
            status_category=status_category,
            active=active,
            old_firmware_used=old_firmware_used,
            old_firmware_device=old_firmware_device,
            oui_based_vlan_version=oui_based_vlan_version,
            ip=ip,
            version=version,
            added_in_advanced=added_in_advanced,
            lag_list=lag_list,
            device_misc=device_misc,
            lags=lags,
            lan_list=lan_list,
            ssid_ids=ssid_ids,
            device_series_type=device_series_type,
            stack=stack,
            unit=unit,
            stack_ports=stack_ports,
            ports=ports,
            stack_msg=stack_msg,
            mlag_msg=mlag_msg,
            es=es,
            custom_ports=custom_ports,
            custom_lag_ids=custom_lag_ids,
            support_layout=support_layout,
        )

        oui_based_vlan_device_info_vo.additional_properties = d
        return oui_based_vlan_device_info_vo

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
