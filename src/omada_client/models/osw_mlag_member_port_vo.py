from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_mlag_member_port_vo_mac_lag_names import (
        OswMlagMemberPortVOMacLagNames,
    )
    from ..models.osw_mlag_member_port_vo_mac_ports import OswMlagMemberPortVOMacPorts


T = TypeVar("T", bound="OswMlagMemberPortVO")


@_attrs_define
class OswMlagMemberPortVO:
    """
    Attributes:
        lag_id (int | Unset):
        mlag_enable (bool | Unset):
        mac_lag_names (OswMlagMemberPortVOMacLagNames | Unset):
        mac_ports (OswMlagMemberPortVOMacPorts | Unset):
    """

    lag_id: int | Unset = UNSET
    mlag_enable: bool | Unset = UNSET
    mac_lag_names: OswMlagMemberPortVOMacLagNames | Unset = UNSET
    mac_ports: OswMlagMemberPortVOMacPorts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lag_id = self.lag_id

        mlag_enable = self.mlag_enable

        mac_lag_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mac_lag_names, Unset):
            mac_lag_names = self.mac_lag_names.to_dict()

        mac_ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mac_ports, Unset):
            mac_ports = self.mac_ports.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if mlag_enable is not UNSET:
            field_dict["mlagEnable"] = mlag_enable
        if mac_lag_names is not UNSET:
            field_dict["macLagNames"] = mac_lag_names
        if mac_ports is not UNSET:
            field_dict["macPorts"] = mac_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_mlag_member_port_vo_mac_lag_names import (
            OswMlagMemberPortVOMacLagNames,
        )
        from ..models.osw_mlag_member_port_vo_mac_ports import (
            OswMlagMemberPortVOMacPorts,
        )

        d = dict(src_dict)
        lag_id = d.pop("lagId", UNSET)

        mlag_enable = d.pop("mlagEnable", UNSET)

        _mac_lag_names = d.pop("macLagNames", UNSET)
        mac_lag_names: OswMlagMemberPortVOMacLagNames | Unset
        if isinstance(_mac_lag_names, Unset):
            mac_lag_names = UNSET
        else:
            mac_lag_names = OswMlagMemberPortVOMacLagNames.from_dict(_mac_lag_names)

        _mac_ports = d.pop("macPorts", UNSET)
        mac_ports: OswMlagMemberPortVOMacPorts | Unset
        if isinstance(_mac_ports, Unset):
            mac_ports = UNSET
        else:
            mac_ports = OswMlagMemberPortVOMacPorts.from_dict(_mac_ports)

        osw_mlag_member_port_vo = cls(
            lag_id=lag_id,
            mlag_enable=mlag_enable,
            mac_lag_names=mac_lag_names,
            mac_ports=mac_ports,
        )

        osw_mlag_member_port_vo.additional_properties = d
        return osw_mlag_member_port_vo

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
