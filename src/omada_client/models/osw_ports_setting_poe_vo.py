from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_port_status_vo import OswPortStatusVO
    from ..models.osw_stack_lag_vo import OswStackLagVO
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswPortsSettingPoeVO")


@_attrs_define
class OswPortsSettingPoeVO:
    """
    Attributes:
        port (int | Unset): Port
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
        config_stack (bool | Unset): Indicates whether the current port is configured as a stack port (joined a stack
            aggregation group)
        config_mlag_peer_link (bool | Unset): Indicates whether the current port is configured as M-LAG peer Link
        config_mlag_dad (bool | Unset): Indicates whether the current port is configured as M-LAG dad Link
        stack_ports_group_index (int | Unset): Number of the stacking port aggregation group to join
        port_name (str | Unset): Port Name
        switch_mac (str | Unset): Switch Mac to which the port belongs
        switch_name (str | Unset): Switch Name to which the port belongs
        switch_type (int | Unset): Switch Type to which the port belongs
        switch_status_category (int | Unset): Category of switch status, switchStatusCategory should be a value as
            follows: 0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated.Only 'Disconnected' and 'Connected'
            and 'Heartbeat' switches ports will be displayed.
        switch_support_poe (int | Unset): Indicates whether the switch supports PoE, switchSupportPoe should be a value
            as follows: 0:Not Support;1:Support.
        site (str | Unset): Site to which the port belongs
        tag_ids (list[str] | Unset): Port label ID List
        tag_name (str | Unset): Port label Name
        connected_status (int | Unset): Port connected status should be a value as follows: 0: Connected; 1:
            Disconnected; 2: Disable
        mad_used (bool | Unset): Mad Used
        disable (bool | Unset): Indicates whether to disable the port
        type_ (int | Unset): Type should be a value as follows: 1: Copper; 2: Combo; 3: SFP
        operation (str | Unset): Operation should be a value as follows: SWITCHING; MIRRORING; AGGREGATING
        support_poe (bool | Unset): Indicates whether PoE is supported
        poe_display_type (int | Unset): PoeDisplayType should be a value as follows: -1: Not Support POE; 0: Support
            POE; 1: POE(4W); 2: POE(7W); 3: POE(15.4W); 4: POE+(30W); 5: POE++(45W); 6: POE++(60W); 7: POE++(75W); 8:
            POE++(90W); 9: POE++(100W).
        poe (int | Unset): PoE switch should be a value as follows: 0: Off; 1: 802.3at/af
        port_status (OswPortStatusVO | Unset): Port Status
        link_speed (int | Unset): Link Speed should be a value as follows: 0: auto; 1: 10M; 2: 100M; 3: 1000M; 4: 10G
        duplex (int | Unset): Duplex should be a value as follows: 0: Auto; 1: Half; 2: Full
        lag_setting (OswStackLagVO | Unset): Basic configuration of the LAG
        stack_id (str | Unset): Stack ID to which the port belongs
        stack_name (str | Unset): Stack Name to which the port belongs
        unit (int | Unset): Stack Unit to which the port belongs
        poe_status (float | Unset): Poe Status
        pd_class (str | Unset): Poe PD Class
        power (float | Unset): Poe Power
        voltage (float | Unset): Poe Voltage
        current (float | Unset): Poe Current
    """

    port: int | Unset = UNSET
    standard_port: OswStandPortVO | Unset = UNSET
    config_stack: bool | Unset = UNSET
    config_mlag_peer_link: bool | Unset = UNSET
    config_mlag_dad: bool | Unset = UNSET
    stack_ports_group_index: int | Unset = UNSET
    port_name: str | Unset = UNSET
    switch_mac: str | Unset = UNSET
    switch_name: str | Unset = UNSET
    switch_type: int | Unset = UNSET
    switch_status_category: int | Unset = UNSET
    switch_support_poe: int | Unset = UNSET
    site: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    tag_name: str | Unset = UNSET
    connected_status: int | Unset = UNSET
    mad_used: bool | Unset = UNSET
    disable: bool | Unset = UNSET
    type_: int | Unset = UNSET
    operation: str | Unset = UNSET
    support_poe: bool | Unset = UNSET
    poe_display_type: int | Unset = UNSET
    poe: int | Unset = UNSET
    port_status: OswPortStatusVO | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    lag_setting: OswStackLagVO | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    unit: int | Unset = UNSET
    poe_status: float | Unset = UNSET
    pd_class: str | Unset = UNSET
    power: float | Unset = UNSET
    voltage: float | Unset = UNSET
    current: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        config_stack = self.config_stack

        config_mlag_peer_link = self.config_mlag_peer_link

        config_mlag_dad = self.config_mlag_dad

        stack_ports_group_index = self.stack_ports_group_index

        port_name = self.port_name

        switch_mac = self.switch_mac

        switch_name = self.switch_name

        switch_type = self.switch_type

        switch_status_category = self.switch_status_category

        switch_support_poe = self.switch_support_poe

        site = self.site

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        tag_name = self.tag_name

        connected_status = self.connected_status

        mad_used = self.mad_used

        disable = self.disable

        type_ = self.type_

        operation = self.operation

        support_poe = self.support_poe

        poe_display_type = self.poe_display_type

        poe = self.poe

        port_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_status, Unset):
            port_status = self.port_status.to_dict()

        link_speed = self.link_speed

        duplex = self.duplex

        lag_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_setting, Unset):
            lag_setting = self.lag_setting.to_dict()

        stack_id = self.stack_id

        stack_name = self.stack_name

        unit = self.unit

        poe_status = self.poe_status

        pd_class = self.pd_class

        power = self.power

        voltage = self.voltage

        current = self.current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if config_stack is not UNSET:
            field_dict["configStack"] = config_stack
        if config_mlag_peer_link is not UNSET:
            field_dict["configMlagPeerLink"] = config_mlag_peer_link
        if config_mlag_dad is not UNSET:
            field_dict["configMlagDad"] = config_mlag_dad
        if stack_ports_group_index is not UNSET:
            field_dict["stackPortsGroupIndex"] = stack_ports_group_index
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if switch_mac is not UNSET:
            field_dict["switchMac"] = switch_mac
        if switch_name is not UNSET:
            field_dict["switchName"] = switch_name
        if switch_type is not UNSET:
            field_dict["switchType"] = switch_type
        if switch_status_category is not UNSET:
            field_dict["switchStatusCategory"] = switch_status_category
        if switch_support_poe is not UNSET:
            field_dict["switchSupportPoe"] = switch_support_poe
        if site is not UNSET:
            field_dict["site"] = site
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if tag_name is not UNSET:
            field_dict["tagName"] = tag_name
        if connected_status is not UNSET:
            field_dict["connectedStatus"] = connected_status
        if mad_used is not UNSET:
            field_dict["madUsed"] = mad_used
        if disable is not UNSET:
            field_dict["disable"] = disable
        if type_ is not UNSET:
            field_dict["type"] = type_
        if operation is not UNSET:
            field_dict["operation"] = operation
        if support_poe is not UNSET:
            field_dict["supportPoe"] = support_poe
        if poe_display_type is not UNSET:
            field_dict["poeDisplayType"] = poe_display_type
        if poe is not UNSET:
            field_dict["poe"] = poe
        if port_status is not UNSET:
            field_dict["portStatus"] = port_status
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if lag_setting is not UNSET:
            field_dict["lagSetting"] = lag_setting
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if unit is not UNSET:
            field_dict["unit"] = unit
        if poe_status is not UNSET:
            field_dict["poeStatus"] = poe_status
        if pd_class is not UNSET:
            field_dict["pdClass"] = pd_class
        if power is not UNSET:
            field_dict["power"] = power
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if current is not UNSET:
            field_dict["current"] = current

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_port_status_vo import OswPortStatusVO
        from ..models.osw_stack_lag_vo import OswStackLagVO
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        _standard_port = d.pop("standardPort", UNSET)
        standard_port: OswStandPortVO | Unset
        if isinstance(_standard_port, Unset):
            standard_port = UNSET
        else:
            standard_port = OswStandPortVO.from_dict(_standard_port)

        config_stack = d.pop("configStack", UNSET)

        config_mlag_peer_link = d.pop("configMlagPeerLink", UNSET)

        config_mlag_dad = d.pop("configMlagDad", UNSET)

        stack_ports_group_index = d.pop("stackPortsGroupIndex", UNSET)

        port_name = d.pop("portName", UNSET)

        switch_mac = d.pop("switchMac", UNSET)

        switch_name = d.pop("switchName", UNSET)

        switch_type = d.pop("switchType", UNSET)

        switch_status_category = d.pop("switchStatusCategory", UNSET)

        switch_support_poe = d.pop("switchSupportPoe", UNSET)

        site = d.pop("site", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        tag_name = d.pop("tagName", UNSET)

        connected_status = d.pop("connectedStatus", UNSET)

        mad_used = d.pop("madUsed", UNSET)

        disable = d.pop("disable", UNSET)

        type_ = d.pop("type", UNSET)

        operation = d.pop("operation", UNSET)

        support_poe = d.pop("supportPoe", UNSET)

        poe_display_type = d.pop("poeDisplayType", UNSET)

        poe = d.pop("poe", UNSET)

        _port_status = d.pop("portStatus", UNSET)
        port_status: OswPortStatusVO | Unset
        if isinstance(_port_status, Unset):
            port_status = UNSET
        else:
            port_status = OswPortStatusVO.from_dict(_port_status)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        _lag_setting = d.pop("lagSetting", UNSET)
        lag_setting: OswStackLagVO | Unset
        if isinstance(_lag_setting, Unset):
            lag_setting = UNSET
        else:
            lag_setting = OswStackLagVO.from_dict(_lag_setting)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        unit = d.pop("unit", UNSET)

        poe_status = d.pop("poeStatus", UNSET)

        pd_class = d.pop("pdClass", UNSET)

        power = d.pop("power", UNSET)

        voltage = d.pop("voltage", UNSET)

        current = d.pop("current", UNSET)

        osw_ports_setting_poe_vo = cls(
            port=port,
            standard_port=standard_port,
            config_stack=config_stack,
            config_mlag_peer_link=config_mlag_peer_link,
            config_mlag_dad=config_mlag_dad,
            stack_ports_group_index=stack_ports_group_index,
            port_name=port_name,
            switch_mac=switch_mac,
            switch_name=switch_name,
            switch_type=switch_type,
            switch_status_category=switch_status_category,
            switch_support_poe=switch_support_poe,
            site=site,
            tag_ids=tag_ids,
            tag_name=tag_name,
            connected_status=connected_status,
            mad_used=mad_used,
            disable=disable,
            type_=type_,
            operation=operation,
            support_poe=support_poe,
            poe_display_type=poe_display_type,
            poe=poe,
            port_status=port_status,
            link_speed=link_speed,
            duplex=duplex,
            lag_setting=lag_setting,
            stack_id=stack_id,
            stack_name=stack_name,
            unit=unit,
            poe_status=poe_status,
            pd_class=pd_class,
            power=power,
            voltage=voltage,
            current=current,
        )

        osw_ports_setting_poe_vo.additional_properties = d
        return osw_ports_setting_poe_vo

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
