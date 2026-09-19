from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.poe_recover_device_open_api_vo_fail_ports import (
        PoeRecoverDeviceOpenApiVOFailPorts,
    )


T = TypeVar("T", bound="PoeRecoverDeviceOpenApiVO")


@_attrs_define
class PoeRecoverDeviceOpenApiVO:
    """PoE recovery result returned by devices.

    Attributes:
        mac (str | Unset): Device MAC address.
        status (int | Unset): Device status: 0 - success, 1 - failed.
        success_ports (list[str] | Unset): List of ports that PoE recovery succeeded.
        fail_ports (PoeRecoverDeviceOpenApiVOFailPorts | Unset): List of ports that PoE recovery failed.
        select_ports (list[str] | Unset): The selected ports for poe recover.
    """

    mac: str | Unset = UNSET
    status: int | Unset = UNSET
    success_ports: list[str] | Unset = UNSET
    fail_ports: PoeRecoverDeviceOpenApiVOFailPorts | Unset = UNSET
    select_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        status = self.status

        success_ports: list[str] | Unset = UNSET
        if not isinstance(self.success_ports, Unset):
            success_ports = self.success_ports

        fail_ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fail_ports, Unset):
            fail_ports = self.fail_ports.to_dict()

        select_ports: list[str] | Unset = UNSET
        if not isinstance(self.select_ports, Unset):
            select_ports = self.select_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if status is not UNSET:
            field_dict["status"] = status
        if success_ports is not UNSET:
            field_dict["successPorts"] = success_ports
        if fail_ports is not UNSET:
            field_dict["failPorts"] = fail_ports
        if select_ports is not UNSET:
            field_dict["selectPorts"] = select_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.poe_recover_device_open_api_vo_fail_ports import (
            PoeRecoverDeviceOpenApiVOFailPorts,
        )

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        status = d.pop("status", UNSET)

        success_ports = cast(list[str], d.pop("successPorts", UNSET))

        _fail_ports = d.pop("failPorts", UNSET)
        fail_ports: PoeRecoverDeviceOpenApiVOFailPorts | Unset
        if isinstance(_fail_ports, Unset):
            fail_ports = UNSET
        else:
            fail_ports = PoeRecoverDeviceOpenApiVOFailPorts.from_dict(_fail_ports)

        select_ports = cast(list[str], d.pop("selectPorts", UNSET))

        poe_recover_device_open_api_vo = cls(
            mac=mac,
            status=status,
            success_ports=success_ports,
            fail_ports=fail_ports,
            select_ports=select_ports,
        )

        poe_recover_device_open_api_vo.additional_properties = d
        return poe_recover_device_open_api_vo

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
