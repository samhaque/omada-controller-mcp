from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseNumOpenApiVO")


@_attrs_define
class LicenseNumOpenApiVO:
    """License num

    Attributes:
        type_ (str): Type should be a value as follows: 1year; 2years; 3years; 4years; 5years; trial
        basic (int | Unset): Basic
        ap (int | Unset): Pro ap
        l_2_switch (int | Unset): Pro l2Switch
        l_3_switch (int | Unset): Pro l3Switch
        gateway (int | Unset): Pro gateway
    """

    type_: str
    basic: int | Unset = UNSET
    ap: int | Unset = UNSET
    l_2_switch: int | Unset = UNSET
    l_3_switch: int | Unset = UNSET
    gateway: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        basic = self.basic

        ap = self.ap

        l_2_switch = self.l_2_switch

        l_3_switch = self.l_3_switch

        gateway = self.gateway

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if basic is not UNSET:
            field_dict["basic"] = basic
        if ap is not UNSET:
            field_dict["ap"] = ap
        if l_2_switch is not UNSET:
            field_dict["l2Switch"] = l_2_switch
        if l_3_switch is not UNSET:
            field_dict["l3Switch"] = l_3_switch
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        basic = d.pop("basic", UNSET)

        ap = d.pop("ap", UNSET)

        l_2_switch = d.pop("l2Switch", UNSET)

        l_3_switch = d.pop("l3Switch", UNSET)

        gateway = d.pop("gateway", UNSET)

        license_num_open_api_vo = cls(
            type_=type_,
            basic=basic,
            ap=ap,
            l_2_switch=l_2_switch,
            l_3_switch=l_3_switch,
            gateway=gateway,
        )

        license_num_open_api_vo.additional_properties = d
        return license_num_open_api_vo

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
