from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum")


@_attrs_define
class ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum:
    """The firmware quantity map for each channel: The key is channel: (0: stable; 1: Release Candidate(RC); 2: Beta), The
    Value is the quantity

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        model_firmware_pool_grid_info_model_latest_fw_info_fw_num = cls()

        model_firmware_pool_grid_info_model_latest_fw_info_fw_num.additional_properties = d
        return model_firmware_pool_grid_info_model_latest_fw_info_fw_num

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
