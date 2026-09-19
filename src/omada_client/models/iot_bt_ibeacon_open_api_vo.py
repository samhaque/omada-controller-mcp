from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_bt_detail_open_api_vo import ApBtDetailOpenApiVO


T = TypeVar("T", bound="IotBtIbeaconOpenApiVO")


@_attrs_define
class IotBtIbeaconOpenApiVO:
    """
    Attributes:
        name (str): The Bluetooth Advertising seting name.
        id (str | Unset): The Bluetooth Advertising entry ID.
        bound_device_num (int | Unset): The quantity of devices bound to this configuration.
        mac_list (list[str] | Unset): List of device MAC addresses bound to this configuration.
        enable (bool | Unset): Whether to enable the Bluetooth Advertising setting.
        transmit_power (int | Unset): Broadcast transmission power.<br />The parameter [transmitPower] should be a value
            as follows:[-20, -18, -15, -12, -10, -9, -6, -5, -3, 0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 20]
        measure_power (int | Unset): RSSI Calibration Value. The parameter [measurePower] is used to input the RSSI
            measured at a 1-meter distance from the device, enabling positioning functionality.
        adv_interval (int | Unset): Advertising interval.
        uuid (str | Unset): The UUID (Universally Unique Identifier) of the advertising ibeacon packet.
        major (str | Unset): The major value of adverting ibeacon packet, indicating a larger group.
        minor (str | Unset): The minor value of adverting ibeacon packet, indicating a smaller group.
        select_mac_info (list[ApBtDetailOpenApiVO] | Unset): Detailed information about the devices bound to this
            configuration.
        build_in (int | Unset): Whether it is a built-in configuration: [0:true; 1:false].
    """

    name: str
    id: str | Unset = UNSET
    bound_device_num: int | Unset = UNSET
    mac_list: list[str] | Unset = UNSET
    enable: bool | Unset = UNSET
    transmit_power: int | Unset = UNSET
    measure_power: int | Unset = UNSET
    adv_interval: int | Unset = UNSET
    uuid: str | Unset = UNSET
    major: str | Unset = UNSET
    minor: str | Unset = UNSET
    select_mac_info: list[ApBtDetailOpenApiVO] | Unset = UNSET
    build_in: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        bound_device_num = self.bound_device_num

        mac_list: list[str] | Unset = UNSET
        if not isinstance(self.mac_list, Unset):
            mac_list = self.mac_list

        enable = self.enable

        transmit_power = self.transmit_power

        measure_power = self.measure_power

        adv_interval = self.adv_interval

        uuid = self.uuid

        major = self.major

        minor = self.minor

        select_mac_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.select_mac_info, Unset):
            select_mac_info = []
            for select_mac_info_item_data in self.select_mac_info:
                select_mac_info_item = select_mac_info_item_data.to_dict()
                select_mac_info.append(select_mac_info_item)

        build_in = self.build_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if bound_device_num is not UNSET:
            field_dict["boundDeviceNum"] = bound_device_num
        if mac_list is not UNSET:
            field_dict["macList"] = mac_list
        if enable is not UNSET:
            field_dict["enable"] = enable
        if transmit_power is not UNSET:
            field_dict["transmitPower"] = transmit_power
        if measure_power is not UNSET:
            field_dict["measurePower"] = measure_power
        if adv_interval is not UNSET:
            field_dict["advInterval"] = adv_interval
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if major is not UNSET:
            field_dict["major"] = major
        if minor is not UNSET:
            field_dict["minor"] = minor
        if select_mac_info is not UNSET:
            field_dict["selectMacInfo"] = select_mac_info
        if build_in is not UNSET:
            field_dict["buildIn"] = build_in

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_bt_detail_open_api_vo import (
            ApBtDetailOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        bound_device_num = d.pop("boundDeviceNum", UNSET)

        mac_list = cast(list[str], d.pop("macList", UNSET))

        enable = d.pop("enable", UNSET)

        transmit_power = d.pop("transmitPower", UNSET)

        measure_power = d.pop("measurePower", UNSET)

        adv_interval = d.pop("advInterval", UNSET)

        uuid = d.pop("uuid", UNSET)

        major = d.pop("major", UNSET)

        minor = d.pop("minor", UNSET)

        _select_mac_info = d.pop("selectMacInfo", UNSET)
        select_mac_info: list[ApBtDetailOpenApiVO] | Unset = UNSET
        if _select_mac_info is not UNSET:
            select_mac_info = []
            for select_mac_info_item_data in _select_mac_info:
                select_mac_info_item = ApBtDetailOpenApiVO.from_dict(
                    select_mac_info_item_data
                )

                select_mac_info.append(select_mac_info_item)

        build_in = d.pop("buildIn", UNSET)

        iot_bt_ibeacon_open_api_vo = cls(
            name=name,
            id=id,
            bound_device_num=bound_device_num,
            mac_list=mac_list,
            enable=enable,
            transmit_power=transmit_power,
            measure_power=measure_power,
            adv_interval=adv_interval,
            uuid=uuid,
            major=major,
            minor=minor,
            select_mac_info=select_mac_info,
            build_in=build_in,
        )

        iot_bt_ibeacon_open_api_vo.additional_properties = d
        return iot_bt_ibeacon_open_api_vo

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
