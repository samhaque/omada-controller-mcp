from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandSteeringOpenApiVO")


@_attrs_define
class BandSteeringOpenApiVO:
    """Site band steering setting.

    Attributes:
        enable (bool): Band steer enable.
        connection_threshold (int | Unset): The range of connect threshold is from 2 to 256, with a default of 30.
        difference_threshold (int | Unset): The range of difference threshold is from 1 to 20, with a default of 4.
        max_failures (int | Unset): The range of maxFailures threshold is from 1 to 20, with a default of 5.
    """

    enable: bool
    connection_threshold: int | Unset = UNSET
    difference_threshold: int | Unset = UNSET
    max_failures: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        connection_threshold = self.connection_threshold

        difference_threshold = self.difference_threshold

        max_failures = self.max_failures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if connection_threshold is not UNSET:
            field_dict["connectionThreshold"] = connection_threshold
        if difference_threshold is not UNSET:
            field_dict["differenceThreshold"] = difference_threshold
        if max_failures is not UNSET:
            field_dict["maxFailures"] = max_failures

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        connection_threshold = d.pop("connectionThreshold", UNSET)

        difference_threshold = d.pop("differenceThreshold", UNSET)

        max_failures = d.pop("maxFailures", UNSET)

        band_steering_open_api_vo = cls(
            enable=enable,
            connection_threshold=connection_threshold,
            difference_threshold=difference_threshold,
            max_failures=max_failures,
        )

        band_steering_open_api_vo.additional_properties = d
        return band_steering_open_api_vo

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
