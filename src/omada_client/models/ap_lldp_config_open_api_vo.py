from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApLldpConfigOpenApiVO")


@_attrs_define
class ApLldpConfigOpenApiVO:
    """
    Attributes:
        lldp_enable (int | Unset): Parameter [lldpEnable] should be a value as follows: 0:off; 1:on; 2:Use Site
            Settings.
        support_lldp (bool | Unset): Whether the lldp function is supported.
    """

    lldp_enable: int | Unset = UNSET
    support_lldp: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lldp_enable = self.lldp_enable

        support_lldp = self.support_lldp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lldp_enable is not UNSET:
            field_dict["lldpEnable"] = lldp_enable
        if support_lldp is not UNSET:
            field_dict["supportLldp"] = support_lldp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lldp_enable = d.pop("lldpEnable", UNSET)

        support_lldp = d.pop("supportLldp", UNSET)

        ap_lldp_config_open_api_vo = cls(
            lldp_enable=lldp_enable,
            support_lldp=support_lldp,
        )

        ap_lldp_config_open_api_vo.additional_properties = d
        return ap_lldp_config_open_api_vo

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
