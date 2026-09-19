from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_lag_vo import OswLagVO
    from ..models.osw_port_vo import OswPortVO
    from ..models.osw_stack_data_vo_osw_data_vo import OswStackDataVOOswDataVO
    from ..models.osw_stand_port_vo import OswStandPortVO
    from ..models.osw_uplink_vo import OswUplinkVO
    from ..models.port_vo import PortVO


T = TypeVar("T", bound="OswDataVO")


@_attrs_define
class OswDataVO:
    """
    Attributes:
        stack_id (str | Unset): Stack Id
        stack_name (str | Unset): Stack name
        unit (int | Unset): Unit
        stack_osw_data (OswStackDataVOOswDataVO | Unset): stackOswData
        mac (str | Unset): Device mac
        name (str | Unset): Device name,default value is the mac address of device
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        show_model (str | Unset): Model complex shown in the front end.Ap：model+(country)+modelVersion,EAP225(EU) v3.0
            Gateway/Switch：model+modelVersion,Osg v3.0
        un_selectedable_ports (list[PortVO] | Unset): The unSelectedable ports of the device.
        port_num (int | Unset): The number of ports of one device.
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        uplink (OswUplinkVO | Unset): Uplink Omada device
        ports (list[OswPortVO] | Unset): Port List
        lags (list[OswLagVO] | Unset): Lag List
        network_not_associated_standard_ports (list[OswStandPortVO] | Unset): The ports not associated with network.
        network_not_associated_lags (list[int] | Unset): The lags not associated with network.
        dhcp_snoop_ports (list[PortVO] | Unset): The ports dhcp snooping selected.
    """

    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    unit: int | Unset = UNSET
    stack_osw_data: OswStackDataVOOswDataVO | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    un_selectedable_ports: list[PortVO] | Unset = UNSET
    port_num: int | Unset = UNSET
    status: int | Unset = UNSET
    uplink: OswUplinkVO | Unset = UNSET
    ports: list[OswPortVO] | Unset = UNSET
    lags: list[OswLagVO] | Unset = UNSET
    network_not_associated_standard_ports: list[OswStandPortVO] | Unset = UNSET
    network_not_associated_lags: list[int] | Unset = UNSET
    dhcp_snoop_ports: list[PortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        stack_name = self.stack_name

        unit = self.unit

        stack_osw_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_osw_data, Unset):
            stack_osw_data = self.stack_osw_data.to_dict()

        mac = self.mac

        name = self.name

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        un_selectedable_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.un_selectedable_ports, Unset):
            un_selectedable_ports = []
            for un_selectedable_ports_item_data in self.un_selectedable_ports:
                un_selectedable_ports_item = un_selectedable_ports_item_data.to_dict()
                un_selectedable_ports.append(un_selectedable_ports_item)

        port_num = self.port_num

        status = self.status

        uplink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink, Unset):
            uplink = self.uplink.to_dict()

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = []
            for lags_item_data in self.lags:
                lags_item = lags_item_data.to_dict()
                lags.append(lags_item)

        network_not_associated_standard_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_not_associated_standard_ports, Unset):
            network_not_associated_standard_ports = []
            for (
                network_not_associated_standard_ports_item_data
            ) in self.network_not_associated_standard_ports:
                network_not_associated_standard_ports_item = (
                    network_not_associated_standard_ports_item_data.to_dict()
                )
                network_not_associated_standard_ports.append(
                    network_not_associated_standard_ports_item
                )

        network_not_associated_lags: list[int] | Unset = UNSET
        if not isinstance(self.network_not_associated_lags, Unset):
            network_not_associated_lags = self.network_not_associated_lags

        dhcp_snoop_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dhcp_snoop_ports, Unset):
            dhcp_snoop_ports = []
            for dhcp_snoop_ports_item_data in self.dhcp_snoop_ports:
                dhcp_snoop_ports_item = dhcp_snoop_ports_item_data.to_dict()
                dhcp_snoop_ports.append(dhcp_snoop_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if unit is not UNSET:
            field_dict["unit"] = unit
        if stack_osw_data is not UNSET:
            field_dict["stackOswData"] = stack_osw_data
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if un_selectedable_ports is not UNSET:
            field_dict["unSelectedablePorts"] = un_selectedable_ports
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if status is not UNSET:
            field_dict["status"] = status
        if uplink is not UNSET:
            field_dict["uplink"] = uplink
        if ports is not UNSET:
            field_dict["ports"] = ports
        if lags is not UNSET:
            field_dict["lags"] = lags
        if network_not_associated_standard_ports is not UNSET:
            field_dict["networkNotAssociatedStandardPorts"] = (
                network_not_associated_standard_ports
            )
        if network_not_associated_lags is not UNSET:
            field_dict["networkNotAssociatedLags"] = network_not_associated_lags
        if dhcp_snoop_ports is not UNSET:
            field_dict["dhcpSnoopPorts"] = dhcp_snoop_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_lag_vo import OswLagVO
        from ..models.osw_port_vo import OswPortVO
        from ..models.osw_stack_data_vo_osw_data_vo import (
            OswStackDataVOOswDataVO,
        )
        from ..models.osw_stand_port_vo import OswStandPortVO
        from ..models.osw_uplink_vo import OswUplinkVO
        from ..models.port_vo import PortVO

        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        unit = d.pop("unit", UNSET)

        _stack_osw_data = d.pop("stackOswData", UNSET)
        stack_osw_data: OswStackDataVOOswDataVO | Unset
        if isinstance(_stack_osw_data, Unset):
            stack_osw_data = UNSET
        else:
            stack_osw_data = OswStackDataVOOswDataVO.from_dict(_stack_osw_data)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        _un_selectedable_ports = d.pop("unSelectedablePorts", UNSET)
        un_selectedable_ports: list[PortVO] | Unset = UNSET
        if _un_selectedable_ports is not UNSET:
            un_selectedable_ports = []
            for un_selectedable_ports_item_data in _un_selectedable_ports:
                un_selectedable_ports_item = PortVO.from_dict(
                    un_selectedable_ports_item_data
                )

                un_selectedable_ports.append(un_selectedable_ports_item)

        port_num = d.pop("portNum", UNSET)

        status = d.pop("status", UNSET)

        _uplink = d.pop("uplink", UNSET)
        uplink: OswUplinkVO | Unset
        if isinstance(_uplink, Unset):
            uplink = UNSET
        else:
            uplink = OswUplinkVO.from_dict(_uplink)

        _ports = d.pop("ports", UNSET)
        ports: list[OswPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _lags = d.pop("lags", UNSET)
        lags: list[OswLagVO] | Unset = UNSET
        if _lags is not UNSET:
            lags = []
            for lags_item_data in _lags:
                lags_item = OswLagVO.from_dict(lags_item_data)

                lags.append(lags_item)

        _network_not_associated_standard_ports = d.pop(
            "networkNotAssociatedStandardPorts", UNSET
        )
        network_not_associated_standard_ports: list[OswStandPortVO] | Unset = UNSET
        if _network_not_associated_standard_ports is not UNSET:
            network_not_associated_standard_ports = []
            for (
                network_not_associated_standard_ports_item_data
            ) in _network_not_associated_standard_ports:
                network_not_associated_standard_ports_item = OswStandPortVO.from_dict(
                    network_not_associated_standard_ports_item_data
                )

                network_not_associated_standard_ports.append(
                    network_not_associated_standard_ports_item
                )

        network_not_associated_lags = cast(
            list[int], d.pop("networkNotAssociatedLags", UNSET)
        )

        _dhcp_snoop_ports = d.pop("dhcpSnoopPorts", UNSET)
        dhcp_snoop_ports: list[PortVO] | Unset = UNSET
        if _dhcp_snoop_ports is not UNSET:
            dhcp_snoop_ports = []
            for dhcp_snoop_ports_item_data in _dhcp_snoop_ports:
                dhcp_snoop_ports_item = PortVO.from_dict(dhcp_snoop_ports_item_data)

                dhcp_snoop_ports.append(dhcp_snoop_ports_item)

        osw_data_vo = cls(
            stack_id=stack_id,
            stack_name=stack_name,
            unit=unit,
            stack_osw_data=stack_osw_data,
            mac=mac,
            name=name,
            type_=type_,
            model=model,
            model_version=model_version,
            show_model=show_model,
            un_selectedable_ports=un_selectedable_ports,
            port_num=port_num,
            status=status,
            uplink=uplink,
            ports=ports,
            lags=lags,
            network_not_associated_standard_ports=network_not_associated_standard_ports,
            network_not_associated_lags=network_not_associated_lags,
            dhcp_snoop_ports=dhcp_snoop_ports,
        )

        osw_data_vo.additional_properties = d
        return osw_data_vo

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
