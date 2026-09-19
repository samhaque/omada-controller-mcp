from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckMacTypeOpenApiVO")


@_attrs_define
class CheckMacTypeOpenApiVO:
    """
    Attributes:
        device (bool | Unset): Whether the mac is device
        device_type (str | Unset): Device type:ap、switch、gateway、olt、IPC、NVR.
    """

    device: bool | Unset = UNSET
    device_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device

        device_type = self.device_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device = d.pop("device", UNSET)

        device_type = d.pop("deviceType", UNSET)

        check_mac_type_open_api_vo = cls(
            device=device,
            device_type=device_type,
        )

        check_mac_type_open_api_vo.additional_properties = d
        return check_mac_type_open_api_vo

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
