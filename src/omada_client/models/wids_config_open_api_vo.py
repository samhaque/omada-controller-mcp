from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WidsConfigOpenApiVO")


@_attrs_define
class WidsConfigOpenApiVO:
    """
    Attributes:
        status (bool | Unset): Wireless IDS config status; true:enable, false:disable.
        level (int | Unset): Wireless IDS detection level; It should be a value as follows: 0:High; 1:Low; 2:Custom.
        detection (list[int] | Unset): Wireless IDS detection type, the value is returned only when level is custom(2);
            It should be a value as follows: 0: Signature_disassociation_broadcast; 1: Signature_deauth_broadcast; 2:
            Detect_apspoofing; 3: Detect_adhoc_using_valid_ssid; 4: Detect_malformed_large_duration; 5:
            Detect_overflow_eapol_key; 6: Detect_ap_impersonation; 7: Detect_ht_greenfield; 8: Detect_incomplete_ie; 9:
            Detect_malformed_htie; 10: Detect_malformed_frame_auth; 11: Detect_malformed_assoc_req; 12:
            Detect_valid_ssid_misuse; 13: Detect_adhoc_network; 14: Detect_client_flood; 16:
            Detect_power_save_dos_flood_attack; 17: Detect_violence_break.
    """

    status: bool | Unset = UNSET
    level: int | Unset = UNSET
    detection: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        level = self.level

        detection: list[int] | Unset = UNSET
        if not isinstance(self.detection, Unset):
            detection = self.detection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if level is not UNSET:
            field_dict["level"] = level
        if detection is not UNSET:
            field_dict["detection"] = detection

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        level = d.pop("level", UNSET)

        detection = cast(list[int], d.pop("detection", UNSET))

        wids_config_open_api_vo = cls(
            status=status,
            level=level,
            detection=detection,
        )

        wids_config_open_api_vo.additional_properties = d
        return wids_config_open_api_vo

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
