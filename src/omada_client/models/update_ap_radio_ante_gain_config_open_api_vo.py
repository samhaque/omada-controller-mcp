from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="UpdateApRadioAnteGainConfigOpenApiVO")


@_attrs_define
class UpdateApRadioAnteGainConfigOpenApiVO:
    """Antenna gain list.

    Attributes:
        radio_id (int): The value of parameter [radioId] should be between 0 and 3. 0: 2.4 GHz, 1: 5 GHz, 2: 5 GHz-2, 3:
            6 GHz.
        ante_gain (int): Antenna Gain. The value of [anteGain] should be between 0 and 30.
    """

    radio_id: int
    ante_gain: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        ante_gain = self.ante_gain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radioId": radio_id,
                "anteGain": ante_gain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id = d.pop("radioId")

        ante_gain = d.pop("anteGain")

        update_ap_radio_ante_gain_config_open_api_vo = cls(
            radio_id=radio_id,
            ante_gain=ante_gain,
        )

        update_ap_radio_ante_gain_config_open_api_vo.additional_properties = d
        return update_ap_radio_ante_gain_config_open_api_vo

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
