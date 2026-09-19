from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.airtime_fairness_setting_vo import AirtimeFairnessSettingVO
    from ..models.beacon_control_vo import BeaconControlVO


T = TypeVar("T", bound="SiteBeaconControlSetting")


@_attrs_define
class SiteBeaconControlSetting:
    """Site beacon control setting.

    Attributes:
        beacon_control (BeaconControlVO | Unset): Site beacon control.
        airtime_fairness (AirtimeFairnessSettingVO | Unset): Site airtimeFairness.
    """

    beacon_control: BeaconControlVO | Unset = UNSET
    airtime_fairness: AirtimeFairnessSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beacon_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.beacon_control, Unset):
            beacon_control = self.beacon_control.to_dict()

        airtime_fairness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.airtime_fairness, Unset):
            airtime_fairness = self.airtime_fairness.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beacon_control is not UNSET:
            field_dict["beaconControl"] = beacon_control
        if airtime_fairness is not UNSET:
            field_dict["airtimeFairness"] = airtime_fairness

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.airtime_fairness_setting_vo import (
            AirtimeFairnessSettingVO,
        )
        from ..models.beacon_control_vo import BeaconControlVO

        d = dict(src_dict)
        _beacon_control = d.pop("beaconControl", UNSET)
        beacon_control: BeaconControlVO | Unset
        if isinstance(_beacon_control, Unset):
            beacon_control = UNSET
        else:
            beacon_control = BeaconControlVO.from_dict(_beacon_control)

        _airtime_fairness = d.pop("airtimeFairness", UNSET)
        airtime_fairness: AirtimeFairnessSettingVO | Unset
        if isinstance(_airtime_fairness, Unset):
            airtime_fairness = UNSET
        else:
            airtime_fairness = AirtimeFairnessSettingVO.from_dict(_airtime_fairness)

        site_beacon_control_setting = cls(
            beacon_control=beacon_control,
            airtime_fairness=airtime_fairness,
        )

        site_beacon_control_setting.additional_properties = d
        return site_beacon_control_setting

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
