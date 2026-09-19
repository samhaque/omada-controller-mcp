from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.select_lag_for_vlan_vo import SelectLagForVlanVO
    from ..models.select_port_for_vlan_vo import SelectPortForVlanVO


T = TypeVar("T", bound="SelectDeviceForVlanVO")


@_attrs_define
class SelectDeviceForVlanVO:
    """Affected device list

    Attributes:
        name (str | Unset): Device Name.
        mac (str | Unset): Device Mac.
        mode (str | Unset): Device Model.
        model_version (str | Unset): Device Model Version.
        type_ (str | Unset): Device type, 1: gateway  2: switch
        es (bool | Unset): Whether the switch is Agile Series Switch
        status_category (int | Unset): Device status category, 0: Disconnected, 1: Connected, 2: Pending,3: Heartbeat
            Missed, 4: Isolated
        compatible (int | Unset): Device firmware and controller compatibility type.Compatible should be a value as
            follows: 0:COMPATIBLE;1:HIGH_MAJOR_VER;2:LOW_MAJOR_VER;3:HIGH_MINOR_VER;4:LOW_MINOR_VER;7:HIGH_COMPONENT_VER;10:
            DEVICE_NOT_COMPATIBLE;11:HIGH_ADOPT_COMMPONENT;12:DEVICE_CATEGORY_NOT_COMPATIBLE;14:DEVICE_NOT_COMPATIBLE_IN_CLU
            STER
        ports (list[SelectPortForVlanVO] | Unset): Device Ports
        lags (list[SelectLagForVlanVO] | Unset): Switch Lags, only valid when type is 2.
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
        manually_select (bool | Unset): Whether the device is manually selected.
        es_allow_all_port_exceed (bool | Unset): It indicates whether there exists allow all port of Agile Series Switch
            that can only use partly of currently creating vlans
        replaced_device (bool | Unset): It indicates whether the switch is the dhcp server device that is replaced in
            the first step
        mlag_peer_device_mac (str | Unset): Mlag peer device mac, only valid when the device is in a mlag group.
        support_layout (bool | Unset): Whether the device supports reporting port layout information.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    mode: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    es: bool | Unset = UNSET
    status_category: int | Unset = UNSET
    compatible: int | Unset = UNSET
    ports: list[SelectPortForVlanVO] | Unset = UNSET
    lags: list[SelectLagForVlanVO] | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    manually_select: bool | Unset = UNSET
    es_allow_all_port_exceed: bool | Unset = UNSET
    replaced_device: bool | Unset = UNSET
    mlag_peer_device_mac: str | Unset = UNSET
    support_layout: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        mode = self.mode

        model_version = self.model_version

        type_ = self.type_

        es = self.es

        status_category = self.status_category

        compatible = self.compatible

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = []
            for lags_item_data in self.lags:
                lags_item = lags_item_data.to_dict()
                lags.append(lags_item)

        added_in_advanced = self.added_in_advanced

        manually_select = self.manually_select

        es_allow_all_port_exceed = self.es_allow_all_port_exceed

        replaced_device = self.replaced_device

        mlag_peer_device_mac = self.mlag_peer_device_mac

        support_layout = self.support_layout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mode is not UNSET:
            field_dict["mode"] = mode
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if es is not UNSET:
            field_dict["es"] = es
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if ports is not UNSET:
            field_dict["ports"] = ports
        if lags is not UNSET:
            field_dict["lags"] = lags
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if manually_select is not UNSET:
            field_dict["manuallySelect"] = manually_select
        if es_allow_all_port_exceed is not UNSET:
            field_dict["esAllowAllPortExceed"] = es_allow_all_port_exceed
        if replaced_device is not UNSET:
            field_dict["replacedDevice"] = replaced_device
        if mlag_peer_device_mac is not UNSET:
            field_dict["mlagPeerDeviceMac"] = mlag_peer_device_mac
        if support_layout is not UNSET:
            field_dict["supportLayout"] = support_layout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.select_lag_for_vlan_vo import SelectLagForVlanVO
        from ..models.select_port_for_vlan_vo import (
            SelectPortForVlanVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        mode = d.pop("mode", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        es = d.pop("es", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        compatible = d.pop("compatible", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[SelectPortForVlanVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = SelectPortForVlanVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _lags = d.pop("lags", UNSET)
        lags: list[SelectLagForVlanVO] | Unset = UNSET
        if _lags is not UNSET:
            lags = []
            for lags_item_data in _lags:
                lags_item = SelectLagForVlanVO.from_dict(lags_item_data)

                lags.append(lags_item)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        manually_select = d.pop("manuallySelect", UNSET)

        es_allow_all_port_exceed = d.pop("esAllowAllPortExceed", UNSET)

        replaced_device = d.pop("replacedDevice", UNSET)

        mlag_peer_device_mac = d.pop("mlagPeerDeviceMac", UNSET)

        support_layout = d.pop("supportLayout", UNSET)

        select_device_for_vlan_vo = cls(
            name=name,
            mac=mac,
            mode=mode,
            model_version=model_version,
            type_=type_,
            es=es,
            status_category=status_category,
            compatible=compatible,
            ports=ports,
            lags=lags,
            added_in_advanced=added_in_advanced,
            manually_select=manually_select,
            es_allow_all_port_exceed=es_allow_all_port_exceed,
            replaced_device=replaced_device,
            mlag_peer_device_mac=mlag_peer_device_mac,
            support_layout=support_layout,
        )

        select_device_for_vlan_vo.additional_properties = d
        return select_device_for_vlan_vo

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
