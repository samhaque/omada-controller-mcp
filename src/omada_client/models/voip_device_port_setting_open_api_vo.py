from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoipDevicePortSettingOpenApiVO")


@_attrs_define
class VoipDevicePortSettingOpenApiVO:
    """VOIP device port setting.

    Attributes:
        port (int | Unset): Port ID.
        number_id_for_outgoing_calls (str | Unset): The outgoing calls number ID of voip device.
        auto (bool | Unset): Whether to enable auto.
        number_id_list_for_incoming_calls (list[str] | Unset): The list of incoming calls number ID.
        vad_support_enable (bool | Unset): Whether to enable vad support.
        speaker_gain (int | Unset): The speaker gain of voip device.
        mic_gain (int | Unset): The mic gain of voip device.
    """

    port: int | Unset = UNSET
    number_id_for_outgoing_calls: str | Unset = UNSET
    auto: bool | Unset = UNSET
    number_id_list_for_incoming_calls: list[str] | Unset = UNSET
    vad_support_enable: bool | Unset = UNSET
    speaker_gain: int | Unset = UNSET
    mic_gain: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        number_id_for_outgoing_calls = self.number_id_for_outgoing_calls

        auto = self.auto

        number_id_list_for_incoming_calls: list[str] | Unset = UNSET
        if not isinstance(self.number_id_list_for_incoming_calls, Unset):
            number_id_list_for_incoming_calls = self.number_id_list_for_incoming_calls

        vad_support_enable = self.vad_support_enable

        speaker_gain = self.speaker_gain

        mic_gain = self.mic_gain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if number_id_for_outgoing_calls is not UNSET:
            field_dict["numberIdForOutgoingCalls"] = number_id_for_outgoing_calls
        if auto is not UNSET:
            field_dict["auto"] = auto
        if number_id_list_for_incoming_calls is not UNSET:
            field_dict["numberIdListForIncomingCalls"] = (
                number_id_list_for_incoming_calls
            )
        if vad_support_enable is not UNSET:
            field_dict["vadSupportEnable"] = vad_support_enable
        if speaker_gain is not UNSET:
            field_dict["speakerGain"] = speaker_gain
        if mic_gain is not UNSET:
            field_dict["micGain"] = mic_gain

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        number_id_for_outgoing_calls = d.pop("numberIdForOutgoingCalls", UNSET)

        auto = d.pop("auto", UNSET)

        number_id_list_for_incoming_calls = cast(
            list[str], d.pop("numberIdListForIncomingCalls", UNSET)
        )

        vad_support_enable = d.pop("vadSupportEnable", UNSET)

        speaker_gain = d.pop("speakerGain", UNSET)

        mic_gain = d.pop("micGain", UNSET)

        voip_device_port_setting_open_api_vo = cls(
            port=port,
            number_id_for_outgoing_calls=number_id_for_outgoing_calls,
            auto=auto,
            number_id_list_for_incoming_calls=number_id_list_for_incoming_calls,
            vad_support_enable=vad_support_enable,
            speaker_gain=speaker_gain,
            mic_gain=mic_gain,
        )

        voip_device_port_setting_open_api_vo.additional_properties = d
        return voip_device_port_setting_open_api_vo

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
