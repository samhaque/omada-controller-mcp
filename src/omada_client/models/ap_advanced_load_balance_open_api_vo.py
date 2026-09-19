from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApAdvancedLoadBalanceOpenApiVO")


@_attrs_define
class ApAdvancedLoadBalanceOpenApiVO:
    """
    Attributes:
        max_clients_enable_2_g (bool | Unset): Whether the device enable maximum associated clients 2g.
        max_clients_2_g (int | Unset): The maximum number of clients connected to the 2G band. MaxClients2g should be
            within the range of 1–512.
        rssi_enable_2_g (bool | Unset): Whether the device enable rssi 2g.
        threshold2g (int | Unset): The RSSI threshold for the 2G band. threshold2g should be within the range of -95–0.
        max_clients_enable_5_g (bool | Unset): Whether the device enable maximum associated clients 5g.
        max_clients_5_g (int | Unset): The maximum number of clients connected to the 5G band. MaxClients5g should be
            within the range of 1–512.
        rssi_enable_5_g (bool | Unset): Whether the device enable rssi 5g.
        threshold5g (int | Unset): The RSSI threshold for the 5G band. threshold5g should be within the range of -95–0.
        max_clients_enable_5_g_2 (bool | Unset): Whether the device enable maximum associated clients 5g2.
        max_clients_5_g_2 (int | Unset): The maximum number of clients connected to the 5G2 band. MaxClients5g2 should
            be within the range of 1–512.
        rssi_enable_5_g_2 (bool | Unset): Whether the device enable rssi 5g2.
        threshold5g2 (int | Unset): The RSSI threshold for the 5G2 band. threshold5g2 should be within the range of
            -95–0.
        max_clients_enable_6_g (bool | Unset): Whether the device enable maximum associated clients 6g.
        max_clients_6_g (int | Unset): The maximum number of clients connected to the 6G band. MaxClients6g should be
            within the range of 1–512.
        rssi_enable_6_g (bool | Unset): Whether the device enable rssi 6g.
        threshold6g (int | Unset): The RSSI threshold for the 6G band. threshold6g should be within the range of -95–0.
    """

    max_clients_enable_2_g: bool | Unset = UNSET
    max_clients_2_g: int | Unset = UNSET
    rssi_enable_2_g: bool | Unset = UNSET
    threshold2g: int | Unset = UNSET
    max_clients_enable_5_g: bool | Unset = UNSET
    max_clients_5_g: int | Unset = UNSET
    rssi_enable_5_g: bool | Unset = UNSET
    threshold5g: int | Unset = UNSET
    max_clients_enable_5_g_2: bool | Unset = UNSET
    max_clients_5_g_2: int | Unset = UNSET
    rssi_enable_5_g_2: bool | Unset = UNSET
    threshold5g2: int | Unset = UNSET
    max_clients_enable_6_g: bool | Unset = UNSET
    max_clients_6_g: int | Unset = UNSET
    rssi_enable_6_g: bool | Unset = UNSET
    threshold6g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_clients_enable_2_g = self.max_clients_enable_2_g

        max_clients_2_g = self.max_clients_2_g

        rssi_enable_2_g = self.rssi_enable_2_g

        threshold2g = self.threshold2g

        max_clients_enable_5_g = self.max_clients_enable_5_g

        max_clients_5_g = self.max_clients_5_g

        rssi_enable_5_g = self.rssi_enable_5_g

        threshold5g = self.threshold5g

        max_clients_enable_5_g_2 = self.max_clients_enable_5_g_2

        max_clients_5_g_2 = self.max_clients_5_g_2

        rssi_enable_5_g_2 = self.rssi_enable_5_g_2

        threshold5g2 = self.threshold5g2

        max_clients_enable_6_g = self.max_clients_enable_6_g

        max_clients_6_g = self.max_clients_6_g

        rssi_enable_6_g = self.rssi_enable_6_g

        threshold6g = self.threshold6g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_clients_enable_2_g is not UNSET:
            field_dict["maxClientsEnable2g"] = max_clients_enable_2_g
        if max_clients_2_g is not UNSET:
            field_dict["maxClients2g"] = max_clients_2_g
        if rssi_enable_2_g is not UNSET:
            field_dict["rssiEnable2g"] = rssi_enable_2_g
        if threshold2g is not UNSET:
            field_dict["threshold2g"] = threshold2g
        if max_clients_enable_5_g is not UNSET:
            field_dict["maxClientsEnable5g"] = max_clients_enable_5_g
        if max_clients_5_g is not UNSET:
            field_dict["maxClients5g"] = max_clients_5_g
        if rssi_enable_5_g is not UNSET:
            field_dict["rssiEnable5g"] = rssi_enable_5_g
        if threshold5g is not UNSET:
            field_dict["threshold5g"] = threshold5g
        if max_clients_enable_5_g_2 is not UNSET:
            field_dict["maxClientsEnable5g2"] = max_clients_enable_5_g_2
        if max_clients_5_g_2 is not UNSET:
            field_dict["maxClients5g2"] = max_clients_5_g_2
        if rssi_enable_5_g_2 is not UNSET:
            field_dict["rssiEnable5g2"] = rssi_enable_5_g_2
        if threshold5g2 is not UNSET:
            field_dict["threshold5g2"] = threshold5g2
        if max_clients_enable_6_g is not UNSET:
            field_dict["maxClientsEnable6g"] = max_clients_enable_6_g
        if max_clients_6_g is not UNSET:
            field_dict["maxClients6g"] = max_clients_6_g
        if rssi_enable_6_g is not UNSET:
            field_dict["rssiEnable6g"] = rssi_enable_6_g
        if threshold6g is not UNSET:
            field_dict["threshold6g"] = threshold6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_clients_enable_2_g = d.pop("maxClientsEnable2g", UNSET)

        max_clients_2_g = d.pop("maxClients2g", UNSET)

        rssi_enable_2_g = d.pop("rssiEnable2g", UNSET)

        threshold2g = d.pop("threshold2g", UNSET)

        max_clients_enable_5_g = d.pop("maxClientsEnable5g", UNSET)

        max_clients_5_g = d.pop("maxClients5g", UNSET)

        rssi_enable_5_g = d.pop("rssiEnable5g", UNSET)

        threshold5g = d.pop("threshold5g", UNSET)

        max_clients_enable_5_g_2 = d.pop("maxClientsEnable5g2", UNSET)

        max_clients_5_g_2 = d.pop("maxClients5g2", UNSET)

        rssi_enable_5_g_2 = d.pop("rssiEnable5g2", UNSET)

        threshold5g2 = d.pop("threshold5g2", UNSET)

        max_clients_enable_6_g = d.pop("maxClientsEnable6g", UNSET)

        max_clients_6_g = d.pop("maxClients6g", UNSET)

        rssi_enable_6_g = d.pop("rssiEnable6g", UNSET)

        threshold6g = d.pop("threshold6g", UNSET)

        ap_advanced_load_balance_open_api_vo = cls(
            max_clients_enable_2_g=max_clients_enable_2_g,
            max_clients_2_g=max_clients_2_g,
            rssi_enable_2_g=rssi_enable_2_g,
            threshold2g=threshold2g,
            max_clients_enable_5_g=max_clients_enable_5_g,
            max_clients_5_g=max_clients_5_g,
            rssi_enable_5_g=rssi_enable_5_g,
            threshold5g=threshold5g,
            max_clients_enable_5_g_2=max_clients_enable_5_g_2,
            max_clients_5_g_2=max_clients_5_g_2,
            rssi_enable_5_g_2=rssi_enable_5_g_2,
            threshold5g2=threshold5g2,
            max_clients_enable_6_g=max_clients_enable_6_g,
            max_clients_6_g=max_clients_6_g,
            rssi_enable_6_g=rssi_enable_6_g,
            threshold6g=threshold6g,
        )

        ap_advanced_load_balance_open_api_vo.additional_properties = d
        return ap_advanced_load_balance_open_api_vo

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
