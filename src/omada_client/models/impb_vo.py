from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_vo import PortVO


T = TypeVar("T", bound="ImpbVO")


@_attrs_define
class ImpbVO:
    """The impbs selected.

    Attributes:
        id (str | Unset): id
        port (PortVO | Unset): The collection of forbidden router ports related to one device.
        ip (str | Unset): ip
        mac (str | Unset): mac
        client_name (str | Unset): clientName
        vlan (int | Unset): vlan
    """

    id: str | Unset = UNSET
    port: PortVO | Unset = UNSET
    ip: str | Unset = UNSET
    mac: str | Unset = UNSET
    client_name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        ip = self.ip

        mac = self.mac

        client_name = self.client_name

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if port is not UNSET:
            field_dict["port"] = port
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mac is not UNSET:
            field_dict["mac"] = mac
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_vo import PortVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _port = d.pop("port", UNSET)
        port: PortVO | Unset
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = PortVO.from_dict(_port)

        ip = d.pop("ip", UNSET)

        mac = d.pop("mac", UNSET)

        client_name = d.pop("clientName", UNSET)

        vlan = d.pop("vlan", UNSET)

        impb_vo = cls(
            id=id,
            port=port,
            ip=ip,
            mac=mac,
            client_name=client_name,
            vlan=vlan,
        )

        impb_vo.additional_properties = d
        return impb_vo

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
