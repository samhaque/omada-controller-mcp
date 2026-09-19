from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApL3AccessConfigOpenApiVO")


@_attrs_define
class ApL3AccessConfigOpenApiVO:
    """
    Attributes:
        enable (bool | Unset): Whether to enable the EAP L3 Accessibility setting.
        support_l3_access (bool | Unset): Whether the L3Access function is supported.
    """

    enable: bool | Unset = UNSET
    support_l3_access: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        support_l3_access = self.support_l3_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if support_l3_access is not UNSET:
            field_dict["supportL3Access"] = support_l3_access

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        support_l3_access = d.pop("supportL3Access", UNSET)

        ap_l3_access_config_open_api_vo = cls(
            enable=enable,
            support_l3_access=support_l3_access,
        )

        ap_l3_access_config_open_api_vo.additional_properties = d
        return ap_l3_access_config_open_api_vo

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
