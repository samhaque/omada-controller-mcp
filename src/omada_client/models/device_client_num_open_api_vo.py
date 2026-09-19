from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceClientNumOpenApiVO")


@_attrs_define
class DeviceClientNumOpenApiVO:
    """Client number under the device

    Attributes:
        site_id (str | Unset): Site id of the device
        mac (str | Unset): MAC address of the device
        client_num (int | Unset): Client number of the device
        client_num_2_g (int | Unset): Client number under 2g of the device
        client_num_5_g (int | Unset): Client number under 5g of the device
        client_num_5_g_2 (int | Unset): Client number under 5g2 of the device
        client_num_6_g (int | Unset): Client number under 6g of the device
    """

    site_id: str | Unset = UNSET
    mac: str | Unset = UNSET
    client_num: int | Unset = UNSET
    client_num_2_g: int | Unset = UNSET
    client_num_5_g: int | Unset = UNSET
    client_num_5_g_2: int | Unset = UNSET
    client_num_6_g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        mac = self.mac

        client_num = self.client_num

        client_num_2_g = self.client_num_2_g

        client_num_5_g = self.client_num_5_g

        client_num_5_g_2 = self.client_num_5_g_2

        client_num_6_g = self.client_num_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num
        if client_num_2_g is not UNSET:
            field_dict["clientNum2g"] = client_num_2_g
        if client_num_5_g is not UNSET:
            field_dict["clientNum5g"] = client_num_5_g
        if client_num_5_g_2 is not UNSET:
            field_dict["clientNum5g2"] = client_num_5_g_2
        if client_num_6_g is not UNSET:
            field_dict["clientNum6g"] = client_num_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        mac = d.pop("mac", UNSET)

        client_num = d.pop("clientNum", UNSET)

        client_num_2_g = d.pop("clientNum2g", UNSET)

        client_num_5_g = d.pop("clientNum5g", UNSET)

        client_num_5_g_2 = d.pop("clientNum5g2", UNSET)

        client_num_6_g = d.pop("clientNum6g", UNSET)

        device_client_num_open_api_vo = cls(
            site_id=site_id,
            mac=mac,
            client_num=client_num,
            client_num_2_g=client_num_2_g,
            client_num_5_g=client_num_5_g,
            client_num_5_g_2=client_num_5_g_2,
            client_num_6_g=client_num_6_g,
        )

        device_client_num_open_api_vo.additional_properties = d
        return device_client_num_open_api_vo

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
