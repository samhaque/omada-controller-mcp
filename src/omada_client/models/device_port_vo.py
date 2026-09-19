from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_info_vo import OswStackInfoVO
    from ..models.port_vo import PortVO


T = TypeVar("T", bound="DevicePortVO")


@_attrs_define
class DevicePortVO:
    """The collection of related devices.

    Attributes:
        mac (str | Unset): The unique identification of one device.
        device_name (str | Unset): The name of one device.
        device_type (str | Unset): Device type:ap, gateway, switch, olt
        device_model (str | Unset): Model of device,for example:EAP225
        device_model_version (str | Unset): Model version of device,for example:3.0
        stack_id (str | Unset): The stack id of devices.
        stack_name (str | Unset): The name of the stacking devices.
        osw_stack (OswStackInfoVO | Unset): The osw stack.
        static_router_ports (list[PortVO] | Unset): The collection of static router ports related to one device.
        forbidden_router_ports (list[PortVO] | Unset): The collection of forbidden router ports related to one device.
    """

    mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    device_model: str | Unset = UNSET
    device_model_version: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    osw_stack: OswStackInfoVO | Unset = UNSET
    static_router_ports: list[PortVO] | Unset = UNSET
    forbidden_router_ports: list[PortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        device_name = self.device_name

        device_type = self.device_type

        device_model = self.device_model

        device_model_version = self.device_model_version

        stack_id = self.stack_id

        stack_name = self.stack_name

        osw_stack: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osw_stack, Unset):
            osw_stack = self.osw_stack.to_dict()

        static_router_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.static_router_ports, Unset):
            static_router_ports = []
            for static_router_ports_item_data in self.static_router_ports:
                static_router_ports_item = static_router_ports_item_data.to_dict()
                static_router_ports.append(static_router_ports_item)

        forbidden_router_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.forbidden_router_ports, Unset):
            forbidden_router_ports = []
            for forbidden_router_ports_item_data in self.forbidden_router_ports:
                forbidden_router_ports_item = forbidden_router_ports_item_data.to_dict()
                forbidden_router_ports.append(forbidden_router_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if osw_stack is not UNSET:
            field_dict["oswStack"] = osw_stack
        if static_router_ports is not UNSET:
            field_dict["staticRouterPorts"] = static_router_ports
        if forbidden_router_ports is not UNSET:
            field_dict["forbiddenRouterPorts"] = forbidden_router_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_info_vo import OswStackInfoVO
        from ..models.port_vo import PortVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        device_model_version = d.pop("deviceModelVersion", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        _osw_stack = d.pop("oswStack", UNSET)
        osw_stack: OswStackInfoVO | Unset
        if isinstance(_osw_stack, Unset):
            osw_stack = UNSET
        else:
            osw_stack = OswStackInfoVO.from_dict(_osw_stack)

        _static_router_ports = d.pop("staticRouterPorts", UNSET)
        static_router_ports: list[PortVO] | Unset = UNSET
        if _static_router_ports is not UNSET:
            static_router_ports = []
            for static_router_ports_item_data in _static_router_ports:
                static_router_ports_item = PortVO.from_dict(
                    static_router_ports_item_data
                )

                static_router_ports.append(static_router_ports_item)

        _forbidden_router_ports = d.pop("forbiddenRouterPorts", UNSET)
        forbidden_router_ports: list[PortVO] | Unset = UNSET
        if _forbidden_router_ports is not UNSET:
            forbidden_router_ports = []
            for forbidden_router_ports_item_data in _forbidden_router_ports:
                forbidden_router_ports_item = PortVO.from_dict(
                    forbidden_router_ports_item_data
                )

                forbidden_router_ports.append(forbidden_router_ports_item)

        device_port_vo = cls(
            mac=mac,
            device_name=device_name,
            device_type=device_type,
            device_model=device_model,
            device_model_version=device_model_version,
            stack_id=stack_id,
            stack_name=stack_name,
            osw_stack=osw_stack,
            static_router_ports=static_router_ports,
            forbidden_router_ports=forbidden_router_ports,
        )

        device_port_vo.additional_properties = d
        return device_port_vo

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
