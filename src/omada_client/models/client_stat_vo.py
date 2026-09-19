from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientStatVO")


@_attrs_define
class ClientStatVO:
    """
    Attributes:
        total (int | Unset):
        wireless (int | Unset):
        wired (int | Unset):
        num_offline (int | Unset):
        num2g (int | Unset):
        num5g (int | Unset):
        num6g (int | Unset):
        num_user (int | Unset):
        num_guest (int | Unset):
        ipc (int | Unset):
        num_wireless_user (int | Unset):
        num_wireless_guest (int | Unset):
        num_2_g_user (int | Unset):
        num_5_g_user (int | Unset):
        num_6_g_user (int | Unset):
        num_2_g_guest (int | Unset):
        num_5_g_guest (int | Unset):
        num_6_g_guest (int | Unset):
        poor (int | Unset):
        fair (int | Unset):
        no_data (int | Unset):
        good (int | Unset):
    """

    total: int | Unset = UNSET
    wireless: int | Unset = UNSET
    wired: int | Unset = UNSET
    num_offline: int | Unset = UNSET
    num2g: int | Unset = UNSET
    num5g: int | Unset = UNSET
    num6g: int | Unset = UNSET
    num_user: int | Unset = UNSET
    num_guest: int | Unset = UNSET
    ipc: int | Unset = UNSET
    num_wireless_user: int | Unset = UNSET
    num_wireless_guest: int | Unset = UNSET
    num_2_g_user: int | Unset = UNSET
    num_5_g_user: int | Unset = UNSET
    num_6_g_user: int | Unset = UNSET
    num_2_g_guest: int | Unset = UNSET
    num_5_g_guest: int | Unset = UNSET
    num_6_g_guest: int | Unset = UNSET
    poor: int | Unset = UNSET
    fair: int | Unset = UNSET
    no_data: int | Unset = UNSET
    good: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        wireless = self.wireless

        wired = self.wired

        num_offline = self.num_offline

        num2g = self.num2g

        num5g = self.num5g

        num6g = self.num6g

        num_user = self.num_user

        num_guest = self.num_guest

        ipc = self.ipc

        num_wireless_user = self.num_wireless_user

        num_wireless_guest = self.num_wireless_guest

        num_2_g_user = self.num_2_g_user

        num_5_g_user = self.num_5_g_user

        num_6_g_user = self.num_6_g_user

        num_2_g_guest = self.num_2_g_guest

        num_5_g_guest = self.num_5_g_guest

        num_6_g_guest = self.num_6_g_guest

        poor = self.poor

        fair = self.fair

        no_data = self.no_data

        good = self.good

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if wired is not UNSET:
            field_dict["wired"] = wired
        if num_offline is not UNSET:
            field_dict["numOffline"] = num_offline
        if num2g is not UNSET:
            field_dict["num2g"] = num2g
        if num5g is not UNSET:
            field_dict["num5g"] = num5g
        if num6g is not UNSET:
            field_dict["num6g"] = num6g
        if num_user is not UNSET:
            field_dict["numUser"] = num_user
        if num_guest is not UNSET:
            field_dict["numGuest"] = num_guest
        if ipc is not UNSET:
            field_dict["ipc"] = ipc
        if num_wireless_user is not UNSET:
            field_dict["numWirelessUser"] = num_wireless_user
        if num_wireless_guest is not UNSET:
            field_dict["numWirelessGuest"] = num_wireless_guest
        if num_2_g_user is not UNSET:
            field_dict["num2gUser"] = num_2_g_user
        if num_5_g_user is not UNSET:
            field_dict["num5gUser"] = num_5_g_user
        if num_6_g_user is not UNSET:
            field_dict["num6gUser"] = num_6_g_user
        if num_2_g_guest is not UNSET:
            field_dict["num2gGuest"] = num_2_g_guest
        if num_5_g_guest is not UNSET:
            field_dict["num5gGuest"] = num_5_g_guest
        if num_6_g_guest is not UNSET:
            field_dict["num6gGuest"] = num_6_g_guest
        if poor is not UNSET:
            field_dict["poor"] = poor
        if fair is not UNSET:
            field_dict["fair"] = fair
        if no_data is not UNSET:
            field_dict["noData"] = no_data
        if good is not UNSET:
            field_dict["good"] = good

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        wireless = d.pop("wireless", UNSET)

        wired = d.pop("wired", UNSET)

        num_offline = d.pop("numOffline", UNSET)

        num2g = d.pop("num2g", UNSET)

        num5g = d.pop("num5g", UNSET)

        num6g = d.pop("num6g", UNSET)

        num_user = d.pop("numUser", UNSET)

        num_guest = d.pop("numGuest", UNSET)

        ipc = d.pop("ipc", UNSET)

        num_wireless_user = d.pop("numWirelessUser", UNSET)

        num_wireless_guest = d.pop("numWirelessGuest", UNSET)

        num_2_g_user = d.pop("num2gUser", UNSET)

        num_5_g_user = d.pop("num5gUser", UNSET)

        num_6_g_user = d.pop("num6gUser", UNSET)

        num_2_g_guest = d.pop("num2gGuest", UNSET)

        num_5_g_guest = d.pop("num5gGuest", UNSET)

        num_6_g_guest = d.pop("num6gGuest", UNSET)

        poor = d.pop("poor", UNSET)

        fair = d.pop("fair", UNSET)

        no_data = d.pop("noData", UNSET)

        good = d.pop("good", UNSET)

        client_stat_vo = cls(
            total=total,
            wireless=wireless,
            wired=wired,
            num_offline=num_offline,
            num2g=num2g,
            num5g=num5g,
            num6g=num6g,
            num_user=num_user,
            num_guest=num_guest,
            ipc=ipc,
            num_wireless_user=num_wireless_user,
            num_wireless_guest=num_wireless_guest,
            num_2_g_user=num_2_g_user,
            num_5_g_user=num_5_g_user,
            num_6_g_user=num_6_g_user,
            num_2_g_guest=num_2_g_guest,
            num_5_g_guest=num_5_g_guest,
            num_6_g_guest=num_6_g_guest,
            poor=poor,
            fair=fair,
            no_data=no_data,
            good=good,
        )

        client_stat_vo.additional_properties = d
        return client_stat_vo

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
