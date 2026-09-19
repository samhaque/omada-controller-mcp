from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ipv4DsLiteOpenApiVO")


@_attrs_define
class Ipv4DsLiteOpenApiVO:
    """It is required when [protoType] is 5.

    Attributes:
        dslite (int): Parameter [dslite] should be one of the following values: 0:Auto; 1:Manual; 2:Transix; 3:Xpass;
            4:V6 connect.
        aftr_name (str | Unset): It is required when [dslite] is 1. Address Family Transition Router which should be a
            domain name or IPV6 address.
    """

    dslite: int
    aftr_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dslite = self.dslite

        aftr_name = self.aftr_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dslite": dslite,
            }
        )
        if aftr_name is not UNSET:
            field_dict["aftrName"] = aftr_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dslite = d.pop("dslite")

        aftr_name = d.pop("aftrName", UNSET)

        ipv_4_ds_lite_open_api_vo = cls(
            dslite=dslite,
            aftr_name=aftr_name,
        )

        ipv_4_ds_lite_open_api_vo.additional_properties = d
        return ipv_4_ds_lite_open_api_vo

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
