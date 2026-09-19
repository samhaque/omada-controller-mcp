from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VlanNetworkDevicePortSupportVO")


@_attrs_define
class VlanNetworkDevicePortSupportVO:
    """Port list

    Attributes:
        port (str | Unset): Port Id
        standard_port (str | Unset): Standard Port of Stack
        lag_id (str | Unset): Lag Id
        mlag_id (str | Unset): Mlag Id
        support (bool | Unset): Indicate whether the port support current vlan.
    """

    port: str | Unset = UNSET
    standard_port: str | Unset = UNSET
    lag_id: str | Unset = UNSET
    mlag_id: str | Unset = UNSET
    support: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port = self.standard_port

        lag_id = self.lag_id

        mlag_id = self.mlag_id

        support = self.support

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if mlag_id is not UNSET:
            field_dict["mlagId"] = mlag_id
        if support is not UNSET:
            field_dict["support"] = support

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        lag_id = d.pop("lagId", UNSET)

        mlag_id = d.pop("mlagId", UNSET)

        support = d.pop("support", UNSET)

        vlan_network_device_port_support_vo = cls(
            port=port,
            standard_port=standard_port,
            lag_id=lag_id,
            mlag_id=mlag_id,
            support=support,
        )

        vlan_network_device_port_support_vo.additional_properties = d
        return vlan_network_device_port_support_vo

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
