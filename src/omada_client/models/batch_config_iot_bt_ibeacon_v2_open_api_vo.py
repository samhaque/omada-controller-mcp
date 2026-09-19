from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchConfigIotBtIbeaconV2OpenApiVO")


@_attrs_define
class BatchConfigIotBtIbeaconV2OpenApiVO:
    """Ibeacon config.

    Attributes:
        enable (bool | Unset): Whether to enable the Bluetooth Advertising setting.(Disable by default)
        measure_power (int | Unset): RSSI Calibration Value. The parameter [measurePower] is used to input the RSSI
            measured at a 1-meter distance from the device, enabling positioning functionality.(-65 by default)
        adv_interval (int | Unset): Advertising interval in milliseconds.(500 by default)
        uuid (str | Unset): The UUID (Universally Unique Identifier) of the advertising ibeacon packet.
        major (str | Unset): The major value of adverting ibeacon packet, indicating a larger group.
        minor (str | Unset): The minor value of adverting ibeacon packet, indicating a smaller group.
    """

    enable: bool | Unset = UNSET
    measure_power: int | Unset = UNSET
    adv_interval: int | Unset = UNSET
    uuid: str | Unset = UNSET
    major: str | Unset = UNSET
    minor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        measure_power = self.measure_power

        adv_interval = self.adv_interval

        uuid = self.uuid

        major = self.major

        minor = self.minor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        measure_power = d.pop("measurePower", UNSET)

        adv_interval = d.pop("advInterval", UNSET)

        uuid = d.pop("uuid", UNSET)

        major = d.pop("major", UNSET)

        minor = d.pop("minor", UNSET)

        batch_config_iot_bt_ibeacon_v2_open_api_vo = cls(
            enable=enable,
            measure_power=measure_power,
            adv_interval=adv_interval,
            uuid=uuid,
            major=major,
            minor=minor,
        )

        batch_config_iot_bt_ibeacon_v2_open_api_vo.additional_properties = d
        return batch_config_iot_bt_ibeacon_v2_open_api_vo

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
