from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AirtimeFairnessSettingOpenApiVO")


@_attrs_define
class AirtimeFairnessSettingOpenApiVO:
    """Site airtime fairness setting.

    Attributes:
        enable2g (bool): Whether to enable 2G airtime fairness
        enable5g (bool): Whether to enable 5G airtime fairness
        enable6g (bool): Whether to enable 6G airtime fairness
    """

    enable2g: bool
    enable5g: bool
    enable6g: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable2g = self.enable2g

        enable5g = self.enable5g

        enable6g = self.enable6g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable2g": enable2g,
                "enable5g": enable5g,
                "enable6g": enable6g,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable2g = d.pop("enable2g")

        enable5g = d.pop("enable5g")

        enable6g = d.pop("enable6g")

        airtime_fairness_setting_open_api_vo = cls(
            enable2g=enable2g,
            enable5g=enable5g,
            enable6g=enable6g,
        )

        airtime_fairness_setting_open_api_vo.additional_properties = d
        return airtime_fairness_setting_open_api_vo

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
