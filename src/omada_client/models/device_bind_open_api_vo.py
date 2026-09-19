from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceBindOpenApiVO")


@_attrs_define
class DeviceBindOpenApiVO:
    """Switch choose for binding device template.

    Attributes:
        mac (str | Unset): Switch MAC address, like AA-BB-CC-DD-EE-FF.
        device_template_id (str | Unset): Switch device template ID.
    """

    mac: str | Unset = UNSET
    device_template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        device_template_id = self.device_template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if device_template_id is not UNSET:
            field_dict["deviceTemplateId"] = device_template_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        device_template_id = d.pop("deviceTemplateId", UNSET)

        device_bind_open_api_vo = cls(
            mac=mac,
            device_template_id=device_template_id,
        )

        device_bind_open_api_vo.additional_properties = d
        return device_bind_open_api_vo

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
