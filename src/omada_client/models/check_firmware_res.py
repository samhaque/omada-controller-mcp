from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckFirmwareRes")


@_attrs_define
class CheckFirmwareRes:
    """
    Attributes:
        finished (bool | Unset): Whether the task is complete
        ap_mac_list (list[str] | Unset): List of the ap MAC address with firmware updates. E.g. AA-BB-CC-DD-11-22
        switch_mac_list (list[str] | Unset): List of switch MAC address with firmware updates. E.g. AA-BB-CC-DD-11-22
        gateway_mac_list (list[str] | Unset): List of gateway MAC address with firmware updates. E.g. AA-BB-CC-DD-11-22
    """

    finished: bool | Unset = UNSET
    ap_mac_list: list[str] | Unset = UNSET
    switch_mac_list: list[str] | Unset = UNSET
    gateway_mac_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finished = self.finished

        ap_mac_list: list[str] | Unset = UNSET
        if not isinstance(self.ap_mac_list, Unset):
            ap_mac_list = self.ap_mac_list

        switch_mac_list: list[str] | Unset = UNSET
        if not isinstance(self.switch_mac_list, Unset):
            switch_mac_list = self.switch_mac_list

        gateway_mac_list: list[str] | Unset = UNSET
        if not isinstance(self.gateway_mac_list, Unset):
            gateway_mac_list = self.gateway_mac_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finished is not UNSET:
            field_dict["finished"] = finished
        if ap_mac_list is not UNSET:
            field_dict["apMacList"] = ap_mac_list
        if switch_mac_list is not UNSET:
            field_dict["switchMacList"] = switch_mac_list
        if gateway_mac_list is not UNSET:
            field_dict["gatewayMacList"] = gateway_mac_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        finished = d.pop("finished", UNSET)

        ap_mac_list = cast(list[str], d.pop("apMacList", UNSET))

        switch_mac_list = cast(list[str], d.pop("switchMacList", UNSET))

        gateway_mac_list = cast(list[str], d.pop("gatewayMacList", UNSET))

        check_firmware_res = cls(
            finished=finished,
            ap_mac_list=ap_mac_list,
            switch_mac_list=switch_mac_list,
            gateway_mac_list=gateway_mac_list,
        )

        check_firmware_res.additional_properties = d
        return check_firmware_res

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
