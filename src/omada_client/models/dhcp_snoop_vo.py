from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_vo import DeviceVO
    from ..models.osw_lag_vo import OswLagVO
    from ..models.osw_port_vo import OswPortVO
    from ..models.osw_stack_info_vo import OswStackInfoVO
    from ..models.port_vo import PortVO


T = TypeVar("T", bound="DhcpSnoopVO")


@_attrs_define
class DhcpSnoopVO:
    """
    Attributes:
        id (str | Unset): The primary id of the dhcp snoop.
        omadac_id (str | Unset): The id of the omada the dhcp snoop belongs to.
        site_id (str | Unset): The id of the site the dhcp snoop belongs to.
        name (str | Unset): The name of the dhcp snoop.
        mac (str | Unset): The mac of the general device.
        device_name (str | Unset): The name of the device.
        device_type (str | Unset): Device type:ap、gateway、switch、olt
        device_model (str | Unset): Model of device,for example:EAP225
        device_model_version (str | Unset): Model version of device,for example:3.0
        show_model (str | Unset): The client showModel
        stack_id (str | Unset): The stack of the stack device.
        stack_name (str | Unset): The name of the stacking devices.
        osw_stack (OswStackInfoVO | Unset): The osw stack.
        ports (list[PortVO] | Unset): The ports selected.
        status (int | Unset): The connected status of the device.
        un_selectedable_ports (list[PortVO] | Unset): The unSelectedable ports of the device.
        all_ports (list[OswPortVO] | Unset): All Port list in one device.
        all_lags (list[OswLagVO] | Unset): All lag list in one device.
        devices (list[DeviceVO] | Unset): The devices selected to create entries.
    """

    id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    device_model: str | Unset = UNSET
    device_model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    osw_stack: OswStackInfoVO | Unset = UNSET
    ports: list[PortVO] | Unset = UNSET
    status: int | Unset = UNSET
    un_selectedable_ports: list[PortVO] | Unset = UNSET
    all_ports: list[OswPortVO] | Unset = UNSET
    all_lags: list[OswLagVO] | Unset = UNSET
    devices: list[DeviceVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        omadac_id = self.omadac_id

        site_id = self.site_id

        name = self.name

        mac = self.mac

        device_name = self.device_name

        device_type = self.device_type

        device_model = self.device_model

        device_model_version = self.device_model_version

        show_model = self.show_model

        stack_id = self.stack_id

        stack_name = self.stack_name

        osw_stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osw_stack, Unset):
            osw_stack = self.osw_stack.to_dict()

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        status = self.status

        un_selectedable_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.un_selectedable_ports, Unset):
            un_selectedable_ports = []
            for un_selectedable_ports_item_data in self.un_selectedable_ports:
                un_selectedable_ports_item = un_selectedable_ports_item_data.to_dict()
                un_selectedable_ports.append(un_selectedable_ports_item)

        all_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_ports, Unset):
            all_ports = []
            for all_ports_item_data in self.all_ports:
                all_ports_item = all_ports_item_data.to_dict()
                all_ports.append(all_ports_item)

        all_lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_lags, Unset):
            all_lags = []
            for all_lags_item_data in self.all_lags:
                all_lags_item = all_lags_item_data.to_dict()
                all_lags.append(all_lags_item)

        devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if device_model_version is not UNSET:
            field_dict["deviceModelVersion"] = device_model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if osw_stack is not UNSET:
            field_dict["oswStack"] = osw_stack
        if ports is not UNSET:
            field_dict["ports"] = ports
        if status is not UNSET:
            field_dict["status"] = status
        if un_selectedable_ports is not UNSET:
            field_dict["unSelectedablePorts"] = un_selectedable_ports
        if all_ports is not UNSET:
            field_dict["allPorts"] = all_ports
        if all_lags is not UNSET:
            field_dict["allLags"] = all_lags
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_vo import DeviceVO
        from ..models.osw_lag_vo import OswLagVO
        from ..models.osw_port_vo import OswPortVO
        from ..models.osw_stack_info_vo import OswStackInfoVO
        from ..models.port_vo import PortVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        device_model_version = d.pop("deviceModelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        _osw_stack = d.pop("oswStack", UNSET)
        osw_stack: OswStackInfoVO | Unset
        if isinstance(_osw_stack, Unset):
            osw_stack = UNSET
        else:
            osw_stack = OswStackInfoVO.from_dict(_osw_stack)

        _ports = d.pop("ports", UNSET)
        ports: list[PortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = PortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        status = d.pop("status", UNSET)

        _un_selectedable_ports = d.pop("unSelectedablePorts", UNSET)
        un_selectedable_ports: list[PortVO] | Unset = UNSET
        if _un_selectedable_ports is not UNSET:
            un_selectedable_ports = []
            for un_selectedable_ports_item_data in _un_selectedable_ports:
                un_selectedable_ports_item = PortVO.from_dict(
                    un_selectedable_ports_item_data
                )

                un_selectedable_ports.append(un_selectedable_ports_item)

        _all_ports = d.pop("allPorts", UNSET)
        all_ports: list[OswPortVO] | Unset = UNSET
        if _all_ports is not UNSET:
            all_ports = []
            for all_ports_item_data in _all_ports:
                all_ports_item = OswPortVO.from_dict(all_ports_item_data)

                all_ports.append(all_ports_item)

        _all_lags = d.pop("allLags", UNSET)
        all_lags: list[OswLagVO] | Unset = UNSET
        if _all_lags is not UNSET:
            all_lags = []
            for all_lags_item_data in _all_lags:
                all_lags_item = OswLagVO.from_dict(all_lags_item_data)

                all_lags.append(all_lags_item)

        _devices = d.pop("devices", UNSET)
        devices: list[DeviceVO] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = DeviceVO.from_dict(devices_item_data)

                devices.append(devices_item)

        dhcp_snoop_vo = cls(
            id=id,
            omadac_id=omadac_id,
            site_id=site_id,
            name=name,
            mac=mac,
            device_name=device_name,
            device_type=device_type,
            device_model=device_model,
            device_model_version=device_model_version,
            show_model=show_model,
            stack_id=stack_id,
            stack_name=stack_name,
            osw_stack=osw_stack,
            ports=ports,
            status=status,
            un_selectedable_ports=un_selectedable_ports,
            all_ports=all_ports,
            all_lags=all_lags,
            devices=devices,
        )

        dhcp_snoop_vo.additional_properties = d
        return dhcp_snoop_vo

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
