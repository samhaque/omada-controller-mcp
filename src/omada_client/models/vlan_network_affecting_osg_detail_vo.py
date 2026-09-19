from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_detail_vo import OsgDetailVO


T = TypeVar("T", bound="VlanNetworkAffectingOsgDetailVO")


@_attrs_define
class VlanNetworkAffectingOsgDetailVO:
    """Gateway Info, only valid when type is gateway.

    Attributes:
        gateway_detail (OsgDetailVO | Unset): Gateway detail.
        affected_ports (list[int] | Unset): Affected gateway port list.
        native_vlan_ports (list[int] | Unset): Ports using this VLAN as the Native Network.
    """

    gateway_detail: OsgDetailVO | Unset = UNSET
    affected_ports: list[int] | Unset = UNSET
    native_vlan_ports: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_detail, Unset):
            gateway_detail = self.gateway_detail.to_dict()

        affected_ports: list[int] | Unset = UNSET
        if not isinstance(self.affected_ports, Unset):
            affected_ports = self.affected_ports

        native_vlan_ports: list[int] | Unset = UNSET
        if not isinstance(self.native_vlan_ports, Unset):
            native_vlan_ports = self.native_vlan_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway_detail is not UNSET:
            field_dict["gatewayDetail"] = gateway_detail
        if affected_ports is not UNSET:
            field_dict["affectedPorts"] = affected_ports
        if native_vlan_ports is not UNSET:
            field_dict["nativeVlanPorts"] = native_vlan_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_detail_vo import OsgDetailVO

        d = dict(src_dict)
        _gateway_detail = d.pop("gatewayDetail", UNSET)
        gateway_detail: OsgDetailVO | Unset
        if isinstance(_gateway_detail, Unset):
            gateway_detail = UNSET
        else:
            gateway_detail = OsgDetailVO.from_dict(_gateway_detail)

        affected_ports = cast(list[int], d.pop("affectedPorts", UNSET))

        native_vlan_ports = cast(list[int], d.pop("nativeVlanPorts", UNSET))

        vlan_network_affecting_osg_detail_vo = cls(
            gateway_detail=gateway_detail,
            affected_ports=affected_ports,
            native_vlan_ports=native_vlan_ports,
        )

        vlan_network_affecting_osg_detail_vo.additional_properties = d
        return vlan_network_affecting_osg_detail_vo

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
