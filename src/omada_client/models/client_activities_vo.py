from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientActivitiesVO")


@_attrs_define
class ClientActivitiesVO:
    """
    Attributes:
        new_eap_client_num (int | Unset):
        new_switch_client_num (int | Unset):
        active_eap_client_num (int | Unset):
        active_switch_client_num (int | Unset):
        disconnect_eap_client_num (int | Unset):
        disconnect_switch_client_num (int | Unset):
        time (int | Unset):
    """

    new_eap_client_num: int | Unset = UNSET
    new_switch_client_num: int | Unset = UNSET
    active_eap_client_num: int | Unset = UNSET
    active_switch_client_num: int | Unset = UNSET
    disconnect_eap_client_num: int | Unset = UNSET
    disconnect_switch_client_num: int | Unset = UNSET
    time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_eap_client_num = self.new_eap_client_num

        new_switch_client_num = self.new_switch_client_num

        active_eap_client_num = self.active_eap_client_num

        active_switch_client_num = self.active_switch_client_num

        disconnect_eap_client_num = self.disconnect_eap_client_num

        disconnect_switch_client_num = self.disconnect_switch_client_num

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_eap_client_num is not UNSET:
            field_dict["newEapClientNum"] = new_eap_client_num
        if new_switch_client_num is not UNSET:
            field_dict["newSwitchClientNum"] = new_switch_client_num
        if active_eap_client_num is not UNSET:
            field_dict["activeEapClientNum"] = active_eap_client_num
        if active_switch_client_num is not UNSET:
            field_dict["activeSwitchClientNum"] = active_switch_client_num
        if disconnect_eap_client_num is not UNSET:
            field_dict["disconnectEapClientNum"] = disconnect_eap_client_num
        if disconnect_switch_client_num is not UNSET:
            field_dict["disconnectSwitchClientNum"] = disconnect_switch_client_num
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        new_eap_client_num = d.pop("newEapClientNum", UNSET)

        new_switch_client_num = d.pop("newSwitchClientNum", UNSET)

        active_eap_client_num = d.pop("activeEapClientNum", UNSET)

        active_switch_client_num = d.pop("activeSwitchClientNum", UNSET)

        disconnect_eap_client_num = d.pop("disconnectEapClientNum", UNSET)

        disconnect_switch_client_num = d.pop("disconnectSwitchClientNum", UNSET)

        time = d.pop("time", UNSET)

        client_activities_vo = cls(
            new_eap_client_num=new_eap_client_num,
            new_switch_client_num=new_switch_client_num,
            active_eap_client_num=active_eap_client_num,
            active_switch_client_num=active_switch_client_num,
            disconnect_eap_client_num=disconnect_eap_client_num,
            disconnect_switch_client_num=disconnect_switch_client_num,
            time=time,
        )

        client_activities_vo.additional_properties = d
        return client_activities_vo

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
