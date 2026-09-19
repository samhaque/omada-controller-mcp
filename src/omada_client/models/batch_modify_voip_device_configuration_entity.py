from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchModifyVoipDeviceConfigurationEntity")


@_attrs_define
class BatchModifyVoipDeviceConfigurationEntity:
    """Telephony settings.

    Attributes:
        vad_support_enable (bool | Unset): Whether to enable vad support.
        speaker_gain (int | Unset): The speaker gain of voip device.
        mic_gain (int | Unset): The mic gain of voip device.
        call_blocking_enable (bool | Unset): Whether to enable callBlocking.
        call_blocking_profile_id (str | Unset): The call blocking profile ID of voip device.When callBlockingEnable is
            true, it can not be null.
        call_blocking_profile_name (str | Unset): The call blocking profile name of voip device.
        digit_map_profile_id (str | Unset): The digit map profile ID of voip device.
        digit_map_profile_name (str | Unset): The digit map profile name of voip device.
    """

    vad_support_enable: bool | Unset = UNSET
    speaker_gain: int | Unset = UNSET
    mic_gain: int | Unset = UNSET
    call_blocking_enable: bool | Unset = UNSET
    call_blocking_profile_id: str | Unset = UNSET
    call_blocking_profile_name: str | Unset = UNSET
    digit_map_profile_id: str | Unset = UNSET
    digit_map_profile_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vad_support_enable = self.vad_support_enable

        speaker_gain = self.speaker_gain

        mic_gain = self.mic_gain

        call_blocking_enable = self.call_blocking_enable

        call_blocking_profile_id = self.call_blocking_profile_id

        call_blocking_profile_name = self.call_blocking_profile_name

        digit_map_profile_id = self.digit_map_profile_id

        digit_map_profile_name = self.digit_map_profile_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vad_support_enable is not UNSET:
            field_dict["vadSupportEnable"] = vad_support_enable
        if speaker_gain is not UNSET:
            field_dict["speakerGain"] = speaker_gain
        if mic_gain is not UNSET:
            field_dict["micGain"] = mic_gain
        if call_blocking_enable is not UNSET:
            field_dict["callBlockingEnable"] = call_blocking_enable
        if call_blocking_profile_id is not UNSET:
            field_dict["callBlockingProfileId"] = call_blocking_profile_id
        if call_blocking_profile_name is not UNSET:
            field_dict["callBlockingProfileName"] = call_blocking_profile_name
        if digit_map_profile_id is not UNSET:
            field_dict["digitMapProfileId"] = digit_map_profile_id
        if digit_map_profile_name is not UNSET:
            field_dict["digitMapProfileName"] = digit_map_profile_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vad_support_enable = d.pop("vadSupportEnable", UNSET)

        speaker_gain = d.pop("speakerGain", UNSET)

        mic_gain = d.pop("micGain", UNSET)

        call_blocking_enable = d.pop("callBlockingEnable", UNSET)

        call_blocking_profile_id = d.pop("callBlockingProfileId", UNSET)

        call_blocking_profile_name = d.pop("callBlockingProfileName", UNSET)

        digit_map_profile_id = d.pop("digitMapProfileId", UNSET)

        digit_map_profile_name = d.pop("digitMapProfileName", UNSET)

        batch_modify_voip_device_configuration_entity = cls(
            vad_support_enable=vad_support_enable,
            speaker_gain=speaker_gain,
            mic_gain=mic_gain,
            call_blocking_enable=call_blocking_enable,
            call_blocking_profile_id=call_blocking_profile_id,
            call_blocking_profile_name=call_blocking_profile_name,
            digit_map_profile_id=digit_map_profile_id,
            digit_map_profile_name=digit_map_profile_name,
        )

        batch_modify_voip_device_configuration_entity.additional_properties = d
        return batch_modify_voip_device_configuration_entity

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
