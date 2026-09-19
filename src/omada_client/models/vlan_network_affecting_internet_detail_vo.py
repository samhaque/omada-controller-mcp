from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_wan_lan_status_vo import CheckWanLanStatusVO


T = TypeVar("T", bound="VlanNetworkAffectingInternetDetailVO")


@_attrs_define
class VlanNetworkAffectingInternetDetailVO:
    """Internet Info, only valid when enable WAN Settings Overrides.

    Attributes:
        internet_vo (CheckWanLanStatusVO | Unset): Internet Detail.
        affected_ports (list[int] | Unset): Affected Internet gateway port list.
    """

    internet_vo: CheckWanLanStatusVO | Unset = UNSET
    affected_ports: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        internet_vo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internet_vo, Unset):
            internet_vo = self.internet_vo.to_dict()

        affected_ports: list[int] | Unset = UNSET
        if not isinstance(self.affected_ports, Unset):
            affected_ports = self.affected_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if internet_vo is not UNSET:
            field_dict["internetVO"] = internet_vo
        if affected_ports is not UNSET:
            field_dict["affectedPorts"] = affected_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.check_wan_lan_status_vo import (
            CheckWanLanStatusVO,
        )

        d = dict(src_dict)
        _internet_vo = d.pop("internetVO", UNSET)
        internet_vo: CheckWanLanStatusVO | Unset
        if isinstance(_internet_vo, Unset):
            internet_vo = UNSET
        else:
            internet_vo = CheckWanLanStatusVO.from_dict(_internet_vo)

        affected_ports = cast(list[int], d.pop("affectedPorts", UNSET))

        vlan_network_affecting_internet_detail_vo = cls(
            internet_vo=internet_vo,
            affected_ports=affected_ports,
        )

        vlan_network_affecting_internet_detail_vo.additional_properties = d
        return vlan_network_affecting_internet_detail_vo

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
