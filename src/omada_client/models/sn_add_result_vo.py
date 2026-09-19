from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnAddResultVO")


@_attrs_define
class SnAddResultVO:
    """Devices add result

    Attributes:
        sn (str | Unset): Serial number
        device_key (str | Unset): Device key(QR code)
        name (str | Unset): Device name
        mac (str | Unset): Device mac
        status (int | Unset): Device add status should be a value as follows: 0: success; 1: waiting to do; 2：importing;
            -51451：Device ID not found; -52201：Device is offline; -52202：Device is already bounded; -52208：Device is offline
            during processing; -52200：Device not exit; -53100：Invalid SN code; -53101：SN code already exists;
            -53102：Incorrect local Username/Password; -53103：Device error; -53113: Too many PRECONFIGURED devices in this
            account. Available licenses are not enough; -53114: This device has been added by another Controller; -53118:
            Omada Pro devices can only be added on the Omada Pro Controller; -53119: Omada devices can only be added on the
            Omada Controller; -39045: Failed to add the device due to duplicate SN codes. Please contact our TP-Link
            Support.
        site_name (str | Unset): If device management records exist when adding devices by SN, you need to forget
            devices in this site. Otherwise this field will have no value.
        customer_name (str | Unset): If device management records exist when adding devices by SN, you need to forget
            devices in this customer. Otherwise this field will have no value.
        online (bool | Unset): Device online or offline
        support_ippt (bool | Unset): Support ip pass-through or not。
    """

    sn: str | Unset = UNSET
    device_key: str | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    status: int | Unset = UNSET
    site_name: str | Unset = UNSET
    customer_name: str | Unset = UNSET
    online: bool | Unset = UNSET
    support_ippt: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sn = self.sn

        device_key = self.device_key

        name = self.name

        mac = self.mac

        status = self.status

        site_name = self.site_name

        customer_name = self.customer_name

        online = self.online

        support_ippt = self.support_ippt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sn is not UNSET:
            field_dict["sn"] = sn
        if device_key is not UNSET:
            field_dict["deviceKey"] = device_key
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if status is not UNSET:
            field_dict["status"] = status
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if online is not UNSET:
            field_dict["online"] = online
        if support_ippt is not UNSET:
            field_dict["supportIppt"] = support_ippt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sn = d.pop("sn", UNSET)

        device_key = d.pop("deviceKey", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        status = d.pop("status", UNSET)

        site_name = d.pop("siteName", UNSET)

        customer_name = d.pop("customerName", UNSET)

        online = d.pop("online", UNSET)

        support_ippt = d.pop("supportIppt", UNSET)

        sn_add_result_vo = cls(
            sn=sn,
            device_key=device_key,
            name=name,
            mac=mac,
            status=status,
            site_name=site_name,
            customer_name=customer_name,
            online=online,
            support_ippt=support_ippt,
        )

        sn_add_result_vo.additional_properties = d
        return sn_add_result_vo

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
