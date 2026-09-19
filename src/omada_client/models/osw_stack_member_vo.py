from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_downlink_vo import OswDownlinkVO
    from ..models.osw_lag_vo import OswLagVO
    from ..models.osw_stack_member_port_cap_and_status_vo import (
        OswStackMemberPortCapAndStatusVO,
    )
    from ..models.osw_stack_member_port_vo import OswStackMemberPortVO
    from ..models.osw_stack_member_vo_stack_port_cap import OswStackMemberVOStackPortCap
    from ..models.osw_stack_port_cap_vo import OswStackPortCapVO
    from ..models.osw_stack_port_group_vo import OswStackPortGroupVO
    from ..models.osw_uplink_vo import OswUplinkVO


T = TypeVar("T", bound="OswStackMemberVO")


@_attrs_define
class OswStackMemberVO:
    """Stack member list

    Attributes:
        mac (str): Device Mac
        unit (int): Unit number of the local stacking system of the device
        priority (int): Priority of the device in the local stacking system
        stack_ports (list[OswStackPortGroupVO]): Stack port list
        omadac_id (str | Unset): OmadacId
        name (str | Unset): Device Name
        ip (str | Unset): IP
        status (int | Unset): Device Status
        member_status (int | Unset): Stack Member Status should be a value as follows: 0: master; 1: slaver; 2:
            notInitial; 3: licenseOverdue; 4: licenseUnactive
        compatible (int | Unset): Compatible Type
        model (str | Unset): Member Model
        model_version (str | Unset): Member Model Version
        show_model (str | Unset): ShowModel
        compound_model (str | Unset):
        version (str | Unset): Software Version
        active (bool | Unset): Indicates whether the device is activated
        license_status (int | Unset): License Status should be a value as follows: 0: UnActive; 1: Unbind; 2: Expired;
            3: Active; 4: NotMatch; 5: NearExpired
        due_time (int | Unset): Expiration time
        due_time_left (int | Unset): The number of milliseconds from the current time to the expiration time
        category (str | Unset): Category
        license_id (str | Unset): License Id
        license_unbinding_limit (int | Unset): The remaining number of times to unbind the license
        initial_unbinding_limit (int | Unset): The initial number of times to unbind the license
        uptime (str | Unset): Uptime
        cpu_util (int | Unset): Real-time CPU usage
        mem_uitl (int | Unset): Real-time memory usage
        poe_total_power (float | Unset): PoE Total Power (W)
        poe_remain (float | Unset): PoE Residual Power (W)
        poe_remain_percent (float | Unset): PoE Residual Power Percentage
        loopback_num (int | Unset): Number of loops
        loop (str | Unset): Loopback port
        block_num (int | Unset): Number of blocks
        block (str | Unset): Block port
        support_stack_group_speed (bool | Unset): Indicates whether the member device supports configuring the link
            speed of the stack port aggregation group
        stack_port_config_caps (list[OswStackPortCapVO] | Unset): Ports capability that support configuration as stack
            port
        default_group_speed_cap (list[int] | Unset): Stack port aggregation group default link speed capability
        port_caps (list[OswStackMemberPortCapAndStatusVO] | Unset): Port Information
        ports (list[OswStackMemberPortVO] | Unset): Including some port configuration information and port real-time
            status
        osw_stack_port_group_status (list[OswLagVO] | Unset): Including some port configuration information and port
            real-time status
        max_stack_groups (int | Unset): Maximum number of stacking port aggregation groups supported
        max_stack_unit_number (int | Unset): The maximum unit number supported by the device, starting from 1
        stack_port_cap (OswStackMemberVOStackPortCap | Unset):
        locate_enable (bool | Unset): Indicates whether the locate function is enabled
        in_whitelist (bool | Unset): Indicates whether it is in the whitelist
        device_series_type (int | Unset): DeviceSeriesType should be a value as follows: 0: advanced; 1: pro
        type_ (str | Unset): Type
        status_category (int | Unset):
        uplink (OswUplinkVO | Unset): Uplink Omada device
        downlink_list (list[OswDownlinkVO] | Unset): Downlink Omada device list
    """

    mac: str
    unit: int
    priority: int
    stack_ports: list[OswStackPortGroupVO]
    omadac_id: str | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    status: int | Unset = UNSET
    member_status: int | Unset = UNSET
    compatible: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    compound_model: str | Unset = UNSET
    version: str | Unset = UNSET
    active: bool | Unset = UNSET
    license_status: int | Unset = UNSET
    due_time: int | Unset = UNSET
    due_time_left: int | Unset = UNSET
    category: str | Unset = UNSET
    license_id: str | Unset = UNSET
    license_unbinding_limit: int | Unset = UNSET
    initial_unbinding_limit: int | Unset = UNSET
    uptime: str | Unset = UNSET
    cpu_util: int | Unset = UNSET
    mem_uitl: int | Unset = UNSET
    poe_total_power: float | Unset = UNSET
    poe_remain: float | Unset = UNSET
    poe_remain_percent: float | Unset = UNSET
    loopback_num: int | Unset = UNSET
    loop: str | Unset = UNSET
    block_num: int | Unset = UNSET
    block: str | Unset = UNSET
    support_stack_group_speed: bool | Unset = UNSET
    stack_port_config_caps: list[OswStackPortCapVO] | Unset = UNSET
    default_group_speed_cap: list[int] | Unset = UNSET
    port_caps: list[OswStackMemberPortCapAndStatusVO] | Unset = UNSET
    ports: list[OswStackMemberPortVO] | Unset = UNSET
    osw_stack_port_group_status: list[OswLagVO] | Unset = UNSET
    max_stack_groups: int | Unset = UNSET
    max_stack_unit_number: int | Unset = UNSET
    stack_port_cap: OswStackMemberVOStackPortCap | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    in_whitelist: bool | Unset = UNSET
    device_series_type: int | Unset = UNSET
    type_: str | Unset = UNSET
    status_category: int | Unset = UNSET
    uplink: OswUplinkVO | Unset = UNSET
    downlink_list: list[OswDownlinkVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        unit = self.unit

        priority = self.priority

        stack_ports = []
        for stack_ports_item_data in self.stack_ports:
            stack_ports_item = stack_ports_item_data.to_dict()
            stack_ports.append(stack_ports_item)

        omadac_id = self.omadac_id

        name = self.name

        ip = self.ip

        status = self.status

        member_status = self.member_status

        compatible = self.compatible

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        compound_model = self.compound_model

        version = self.version

        active = self.active

        license_status = self.license_status

        due_time = self.due_time

        due_time_left = self.due_time_left

        category = self.category

        license_id = self.license_id

        license_unbinding_limit = self.license_unbinding_limit

        initial_unbinding_limit = self.initial_unbinding_limit

        uptime = self.uptime

        cpu_util = self.cpu_util

        mem_uitl = self.mem_uitl

        poe_total_power = self.poe_total_power

        poe_remain = self.poe_remain

        poe_remain_percent = self.poe_remain_percent

        loopback_num = self.loopback_num

        loop = self.loop

        block_num = self.block_num

        block = self.block

        support_stack_group_speed = self.support_stack_group_speed

        stack_port_config_caps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_port_config_caps, Unset):
            stack_port_config_caps = []
            for stack_port_config_caps_item_data in self.stack_port_config_caps:
                stack_port_config_caps_item = stack_port_config_caps_item_data.to_dict()
                stack_port_config_caps.append(stack_port_config_caps_item)

        default_group_speed_cap: list[int] | Unset = UNSET
        if not isinstance(self.default_group_speed_cap, Unset):
            default_group_speed_cap = self.default_group_speed_cap

        port_caps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_caps, Unset):
            port_caps = []
            for port_caps_item_data in self.port_caps:
                port_caps_item = port_caps_item_data.to_dict()
                port_caps.append(port_caps_item)

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        osw_stack_port_group_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.osw_stack_port_group_status, Unset):
            osw_stack_port_group_status = []
            for (
                osw_stack_port_group_status_item_data
            ) in self.osw_stack_port_group_status:
                osw_stack_port_group_status_item = (
                    osw_stack_port_group_status_item_data.to_dict()
                )
                osw_stack_port_group_status.append(osw_stack_port_group_status_item)

        max_stack_groups = self.max_stack_groups

        max_stack_unit_number = self.max_stack_unit_number

        stack_port_cap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_port_cap, Unset):
            stack_port_cap = self.stack_port_cap.to_dict()

        locate_enable = self.locate_enable

        in_whitelist = self.in_whitelist

        device_series_type = self.device_series_type

        type_ = self.type_

        status_category = self.status_category

        uplink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink, Unset):
            uplink = self.uplink.to_dict()

        downlink_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_list, Unset):
            downlink_list = []
            for downlink_list_item_data in self.downlink_list:
                downlink_list_item = downlink_list_item_data.to_dict()
                downlink_list.append(downlink_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "unit": unit,
                "priority": priority,
                "stackPorts": stack_ports,
            }
        )
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status is not UNSET:
            field_dict["status"] = status
        if member_status is not UNSET:
            field_dict["memberStatus"] = member_status
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if compound_model is not UNSET:
            field_dict["compoundModel"] = compound_model
        if version is not UNSET:
            field_dict["version"] = version
        if active is not UNSET:
            field_dict["active"] = active
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if due_time is not UNSET:
            field_dict["dueTime"] = due_time
        if due_time_left is not UNSET:
            field_dict["dueTimeLeft"] = due_time_left
        if category is not UNSET:
            field_dict["category"] = category
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if license_unbinding_limit is not UNSET:
            field_dict["licenseUnbindingLimit"] = license_unbinding_limit
        if initial_unbinding_limit is not UNSET:
            field_dict["initialUnbindingLimit"] = initial_unbinding_limit
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if cpu_util is not UNSET:
            field_dict["cpuUtil"] = cpu_util
        if mem_uitl is not UNSET:
            field_dict["memUitl"] = mem_uitl
        if poe_total_power is not UNSET:
            field_dict["poeTotalPower"] = poe_total_power
        if poe_remain is not UNSET:
            field_dict["poeRemain"] = poe_remain
        if poe_remain_percent is not UNSET:
            field_dict["poeRemainPercent"] = poe_remain_percent
        if loopback_num is not UNSET:
            field_dict["loopbackNum"] = loopback_num
        if loop is not UNSET:
            field_dict["loop"] = loop
        if block_num is not UNSET:
            field_dict["blockNum"] = block_num
        if block is not UNSET:
            field_dict["block"] = block
        if support_stack_group_speed is not UNSET:
            field_dict["supportStackGroupSpeed"] = support_stack_group_speed
        if stack_port_config_caps is not UNSET:
            field_dict["stackPortConfigCaps"] = stack_port_config_caps
        if default_group_speed_cap is not UNSET:
            field_dict["defaultGroupSpeedCap"] = default_group_speed_cap
        if port_caps is not UNSET:
            field_dict["portCaps"] = port_caps
        if ports is not UNSET:
            field_dict["ports"] = ports
        if osw_stack_port_group_status is not UNSET:
            field_dict["oswStackPortGroupStatus"] = osw_stack_port_group_status
        if max_stack_groups is not UNSET:
            field_dict["maxStackGroups"] = max_stack_groups
        if max_stack_unit_number is not UNSET:
            field_dict["maxStackUnitNumber"] = max_stack_unit_number
        if stack_port_cap is not UNSET:
            field_dict["stackPortCap"] = stack_port_cap
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if in_whitelist is not UNSET:
            field_dict["inWhitelist"] = in_whitelist
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if uplink is not UNSET:
            field_dict["uplink"] = uplink
        if downlink_list is not UNSET:
            field_dict["downlinkList"] = downlink_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_downlink_vo import OswDownlinkVO
        from ..models.osw_lag_vo import OswLagVO
        from ..models.osw_stack_member_port_cap_and_status_vo import (
            OswStackMemberPortCapAndStatusVO,
        )
        from ..models.osw_stack_member_port_vo import (
            OswStackMemberPortVO,
        )
        from ..models.osw_stack_member_vo_stack_port_cap import (
            OswStackMemberVOStackPortCap,
        )
        from ..models.osw_stack_port_cap_vo import OswStackPortCapVO
        from ..models.osw_stack_port_group_vo import (
            OswStackPortGroupVO,
        )
        from ..models.osw_uplink_vo import OswUplinkVO

        d = dict(src_dict)
        mac = d.pop("mac")

        unit = d.pop("unit")

        priority = d.pop("priority")

        stack_ports = []
        _stack_ports = d.pop("stackPorts")
        for stack_ports_item_data in _stack_ports:
            stack_ports_item = OswStackPortGroupVO.from_dict(stack_ports_item_data)

            stack_ports.append(stack_ports_item)

        omadac_id = d.pop("omadacId", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        status = d.pop("status", UNSET)

        member_status = d.pop("memberStatus", UNSET)

        compatible = d.pop("compatible", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        compound_model = d.pop("compoundModel", UNSET)

        version = d.pop("version", UNSET)

        active = d.pop("active", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        due_time = d.pop("dueTime", UNSET)

        due_time_left = d.pop("dueTimeLeft", UNSET)

        category = d.pop("category", UNSET)

        license_id = d.pop("licenseId", UNSET)

        license_unbinding_limit = d.pop("licenseUnbindingLimit", UNSET)

        initial_unbinding_limit = d.pop("initialUnbindingLimit", UNSET)

        uptime = d.pop("uptime", UNSET)

        cpu_util = d.pop("cpuUtil", UNSET)

        mem_uitl = d.pop("memUitl", UNSET)

        poe_total_power = d.pop("poeTotalPower", UNSET)

        poe_remain = d.pop("poeRemain", UNSET)

        poe_remain_percent = d.pop("poeRemainPercent", UNSET)

        loopback_num = d.pop("loopbackNum", UNSET)

        loop = d.pop("loop", UNSET)

        block_num = d.pop("blockNum", UNSET)

        block = d.pop("block", UNSET)

        support_stack_group_speed = d.pop("supportStackGroupSpeed", UNSET)

        _stack_port_config_caps = d.pop("stackPortConfigCaps", UNSET)
        stack_port_config_caps: list[OswStackPortCapVO] | Unset = UNSET
        if _stack_port_config_caps is not UNSET:
            stack_port_config_caps = []
            for stack_port_config_caps_item_data in _stack_port_config_caps:
                stack_port_config_caps_item = OswStackPortCapVO.from_dict(
                    stack_port_config_caps_item_data
                )

                stack_port_config_caps.append(stack_port_config_caps_item)

        default_group_speed_cap = cast(list[int], d.pop("defaultGroupSpeedCap", UNSET))

        _port_caps = d.pop("portCaps", UNSET)
        port_caps: list[OswStackMemberPortCapAndStatusVO] | Unset = UNSET
        if _port_caps is not UNSET:
            port_caps = []
            for port_caps_item_data in _port_caps:
                port_caps_item = OswStackMemberPortCapAndStatusVO.from_dict(
                    port_caps_item_data
                )

                port_caps.append(port_caps_item)

        _ports = d.pop("ports", UNSET)
        ports: list[OswStackMemberPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswStackMemberPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _osw_stack_port_group_status = d.pop("oswStackPortGroupStatus", UNSET)
        osw_stack_port_group_status: list[OswLagVO] | Unset = UNSET
        if _osw_stack_port_group_status is not UNSET:
            osw_stack_port_group_status = []
            for osw_stack_port_group_status_item_data in _osw_stack_port_group_status:
                osw_stack_port_group_status_item = OswLagVO.from_dict(
                    osw_stack_port_group_status_item_data
                )

                osw_stack_port_group_status.append(osw_stack_port_group_status_item)

        max_stack_groups = d.pop("maxStackGroups", UNSET)

        max_stack_unit_number = d.pop("maxStackUnitNumber", UNSET)

        _stack_port_cap = d.pop("stackPortCap", UNSET)
        stack_port_cap: OswStackMemberVOStackPortCap | Unset
        if isinstance(_stack_port_cap, Unset):
            stack_port_cap = UNSET
        else:
            stack_port_cap = OswStackMemberVOStackPortCap.from_dict(_stack_port_cap)

        locate_enable = d.pop("locateEnable", UNSET)

        in_whitelist = d.pop("inWhitelist", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        type_ = d.pop("type", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        _uplink = d.pop("uplink", UNSET)
        uplink: OswUplinkVO | Unset
        if isinstance(_uplink, Unset):
            uplink = UNSET
        else:
            uplink = OswUplinkVO.from_dict(_uplink)

        _downlink_list = d.pop("downlinkList", UNSET)
        downlink_list: list[OswDownlinkVO] | Unset = UNSET
        if _downlink_list is not UNSET:
            downlink_list = []
            for downlink_list_item_data in _downlink_list:
                downlink_list_item = OswDownlinkVO.from_dict(downlink_list_item_data)

                downlink_list.append(downlink_list_item)

        osw_stack_member_vo = cls(
            mac=mac,
            unit=unit,
            priority=priority,
            stack_ports=stack_ports,
            omadac_id=omadac_id,
            name=name,
            ip=ip,
            status=status,
            member_status=member_status,
            compatible=compatible,
            model=model,
            model_version=model_version,
            show_model=show_model,
            compound_model=compound_model,
            version=version,
            active=active,
            license_status=license_status,
            due_time=due_time,
            due_time_left=due_time_left,
            category=category,
            license_id=license_id,
            license_unbinding_limit=license_unbinding_limit,
            initial_unbinding_limit=initial_unbinding_limit,
            uptime=uptime,
            cpu_util=cpu_util,
            mem_uitl=mem_uitl,
            poe_total_power=poe_total_power,
            poe_remain=poe_remain,
            poe_remain_percent=poe_remain_percent,
            loopback_num=loopback_num,
            loop=loop,
            block_num=block_num,
            block=block,
            support_stack_group_speed=support_stack_group_speed,
            stack_port_config_caps=stack_port_config_caps,
            default_group_speed_cap=default_group_speed_cap,
            port_caps=port_caps,
            ports=ports,
            osw_stack_port_group_status=osw_stack_port_group_status,
            max_stack_groups=max_stack_groups,
            max_stack_unit_number=max_stack_unit_number,
            stack_port_cap=stack_port_cap,
            locate_enable=locate_enable,
            in_whitelist=in_whitelist,
            device_series_type=device_series_type,
            type_=type_,
            status_category=status_category,
            uplink=uplink,
            downlink_list=downlink_list,
        )

        osw_stack_member_vo.additional_properties = d
        return osw_stack_member_vo

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
