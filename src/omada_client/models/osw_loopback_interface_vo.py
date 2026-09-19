from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswLoopbackInterfaceVO")


@_attrs_define
class OswLoopbackInterfaceVO:
    """
    Attributes:
        status (int): Interface status.0: disable, 1: enable.
        name (str): Loopback Interface name.
        loopback_id (int): Loopback ID.
        ip (str): IP address.
        vrf_id (str | Unset): VRF ID. This field is non-empty when the device supports VRF.
    """

    status: int
    name: str
    loopback_id: int
    ip: str
    vrf_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        name = self.name

        loopback_id = self.loopback_id

        ip = self.ip

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "name": name,
                "loopbackId": loopback_id,
                "ip": ip,
            }
        )
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        name = d.pop("name")

        loopback_id = d.pop("loopbackId")

        ip = d.pop("ip")

        vrf_id = d.pop("vrfId", UNSET)

        osw_loopback_interface_vo = cls(
            status=status,
            name=name,
            loopback_id=loopback_id,
            ip=ip,
            vrf_id=vrf_id,
        )

        osw_loopback_interface_vo.additional_properties = d
        return osw_loopback_interface_vo

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
