from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWipsConfigOpenApiVO")


@_attrs_define
class UpdateWipsConfigOpenApiVO:
    """
    Attributes:
        status (bool): Wireless IPS config status; true:enable, false:disable.
        deauth_en (bool): Wireless IPS deauthenticate config status; true:enable, false:disable.
        dynamic_en (bool): Wireless IPS dynamic block list config status; true:enable, false:disable.
        lock_time (int | Unset): Wireless IPS device locking duration config status; It should be within the range of
            300–36000; this field is required when parameter [dynamicEn] is true.
    """

    status: bool
    deauth_en: bool
    dynamic_en: bool
    lock_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        deauth_en = self.deauth_en

        dynamic_en = self.dynamic_en

        lock_time = self.lock_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "deauthEn": deauth_en,
                "dynamicEn": dynamic_en,
            }
        )
        if lock_time is not UNSET:
            field_dict["lockTime"] = lock_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        deauth_en = d.pop("deauthEn")

        dynamic_en = d.pop("dynamicEn")

        lock_time = d.pop("lockTime", UNSET)

        update_wips_config_open_api_vo = cls(
            status=status,
            deauth_en=deauth_en,
            dynamic_en=dynamic_en,
            lock_time=lock_time,
        )

        update_wips_config_open_api_vo.additional_properties = d
        return update_wips_config_open_api_vo

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
