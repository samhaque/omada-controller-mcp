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


T = TypeVar("T", bound="SelectDeviceForVlanTemplateVO")


@_attrs_define
class SelectDeviceForVlanTemplateVO:
    """
    Attributes:
        name (str | Unset): Device Name.
        mac (str | Unset): Device mac for Site Setting or Device template ID for Site Template Setting
        mode (str | Unset): Device Model.
        model_version (str | Unset): Device Model Version.
        type_ (str | Unset): Device type should be a value as follows: 1:gateway;  2:switch
        compatible (int | Unset): Device firmware and controller compatibility type.Compatible should be a value as
            follows: 0:COMPATIBLE; 1:HIGH_MAJOR_VER; 2:LOW_MAJOR_VER; 3:HIGH_MINOR_VER; 4:LOW_MINOR_VER;
            7:HIGH_COMPONENT_VER; 10:DEVICE_NOT_COMPATIBLE; 11:HIGH_ADOPT_COMMPONENT; 12:DEVICE_CATEGORY_NOT_COMPATIBLE;
            14:DEVICE_NOT_COMPATIBLE_IN_CLUSTER
        ports (list[SelectPortForVlanVO] | Unset): Device Ports
        lags (list[SelectLagForVlanVO] | Unset): Switch Lags, only valid when type is 2.
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    mode: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    compatible: int | Unset = UNSET
    ports: list[SelectPortForVlanVO] | Unset = UNSET
    lags: list[SelectLagForVlanVO] | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        mode = self.mode

        model_version = self.model_version

        type_ = self.type_

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
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if ports is not UNSET:
            field_dict["ports"] = ports
        if lags is not UNSET:
            field_dict["lags"] = lags
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced

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

        select_device_for_vlan_template_vo = cls(
            name=name,
            mac=mac,
            mode=mode,
            model_version=model_version,
            type_=type_,
            compatible=compatible,
            ports=ports,
            lags=lags,
            added_in_advanced=added_in_advanced,
        )

        select_device_for_vlan_template_vo.additional_properties = d
        return select_device_for_vlan_template_vo

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
