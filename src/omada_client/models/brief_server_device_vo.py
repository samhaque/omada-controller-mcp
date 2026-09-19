from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_range_open_api_vo import DhcpRangeOpenApiVO


T = TypeVar("T", bound="BriefServerDeviceVO")


@_attrs_define
class BriefServerDeviceVO:
    """List of devices acting as DHCP servers in this network

    Attributes:
        name (str | Unset): Dhcp Server Name
        mac (str | Unset): Dhcp Server Mac
        stack_id (str | Unset): Dhcp Server Stack ID
        model (str | Unset): Device Model
        model_version (str | Unset): Device Model Version
        type_ (str | Unset): Device Type
        ranges (list[DhcpRangeOpenApiVO] | Unset): Dhcp Server Ranges
        config_ranges (list[DhcpRangeOpenApiVO] | Unset): Dhcp Server Config Ranges
        dhcp_server_enable (bool | Unset): Whether DHCP Server is enabled
        dhcp_settings_auto (bool | Unset): Whether DHCP Setting is auto
        support_dhcp_reservation (bool | Unset): Whether the device supports DHCP Reservation
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    ranges: list[DhcpRangeOpenApiVO] | Unset = UNSET
    config_ranges: list[DhcpRangeOpenApiVO] | Unset = UNSET
    dhcp_server_enable: bool | Unset = UNSET
    dhcp_settings_auto: bool | Unset = UNSET
    support_dhcp_reservation: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        stack_id = self.stack_id

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        config_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config_ranges, Unset):
            config_ranges = []
            for config_ranges_item_data in self.config_ranges:
                config_ranges_item = config_ranges_item_data.to_dict()
                config_ranges.append(config_ranges_item)

        dhcp_server_enable = self.dhcp_server_enable

        dhcp_settings_auto = self.dhcp_settings_auto

        support_dhcp_reservation = self.support_dhcp_reservation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if config_ranges is not UNSET:
            field_dict["configRanges"] = config_ranges
        if dhcp_server_enable is not UNSET:
            field_dict["dhcpServerEnable"] = dhcp_server_enable
        if dhcp_settings_auto is not UNSET:
            field_dict["dhcpSettingsAuto"] = dhcp_settings_auto
        if support_dhcp_reservation is not UNSET:
            field_dict["supportDhcpReservation"] = support_dhcp_reservation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_range_open_api_vo import DhcpRangeOpenApiVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        _ranges = d.pop("ranges", UNSET)
        ranges: list[DhcpRangeOpenApiVO] | Unset = UNSET
        if _ranges is not UNSET:
            ranges = []
            for ranges_item_data in _ranges:
                ranges_item = DhcpRangeOpenApiVO.from_dict(ranges_item_data)

                ranges.append(ranges_item)

        _config_ranges = d.pop("configRanges", UNSET)
        config_ranges: list[DhcpRangeOpenApiVO] | Unset = UNSET
        if _config_ranges is not UNSET:
            config_ranges = []
            for config_ranges_item_data in _config_ranges:
                config_ranges_item = DhcpRangeOpenApiVO.from_dict(
                    config_ranges_item_data
                )

                config_ranges.append(config_ranges_item)

        dhcp_server_enable = d.pop("dhcpServerEnable", UNSET)

        dhcp_settings_auto = d.pop("dhcpSettingsAuto", UNSET)

        support_dhcp_reservation = d.pop("supportDhcpReservation", UNSET)

        brief_server_device_vo = cls(
            name=name,
            mac=mac,
            stack_id=stack_id,
            model=model,
            model_version=model_version,
            type_=type_,
            ranges=ranges,
            config_ranges=config_ranges,
            dhcp_server_enable=dhcp_server_enable,
            dhcp_settings_auto=dhcp_settings_auto,
            support_dhcp_reservation=support_dhcp_reservation,
        )

        brief_server_device_vo.additional_properties = d
        return brief_server_device_vo

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
