from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IptvDslOpenApiVO")


@_attrs_define
class IptvDslOpenApiVO:
    """Configurations that appear only when DSL WAN port is selected.

    Attributes:
        modulation_type (int): Modulation Type should be a value as follows: 0: ADSL, 1: VDSL.
        ip_phone_vpi (int | Unset): IP Phone VPI should be a number between 0 and 255.
        ip_phone_vci (int | Unset): IP Phone VCI should be a number between 0 and 35535.
        iptv_vpi (int | Unset): IPTV VPI should be a number between 0 and 255.
        iptv_vci (int | Unset): IPTV VCI should be a number between 0 and 35535.
    """

    modulation_type: int
    ip_phone_vpi: int | Unset = UNSET
    ip_phone_vci: int | Unset = UNSET
    iptv_vpi: int | Unset = UNSET
    iptv_vci: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modulation_type = self.modulation_type

        ip_phone_vpi = self.ip_phone_vpi

        ip_phone_vci = self.ip_phone_vci

        iptv_vpi = self.iptv_vpi

        iptv_vci = self.iptv_vci

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modulationType": modulation_type,
            }
        )
        if ip_phone_vpi is not UNSET:
            field_dict["ipPhoneVpi"] = ip_phone_vpi
        if ip_phone_vci is not UNSET:
            field_dict["ipPhoneVci"] = ip_phone_vci
        if iptv_vpi is not UNSET:
            field_dict["iptvVpi"] = iptv_vpi
        if iptv_vci is not UNSET:
            field_dict["iptvVci"] = iptv_vci

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        modulation_type = d.pop("modulationType")

        ip_phone_vpi = d.pop("ipPhoneVpi", UNSET)

        ip_phone_vci = d.pop("ipPhoneVci", UNSET)

        iptv_vpi = d.pop("iptvVpi", UNSET)

        iptv_vci = d.pop("iptvVci", UNSET)

        iptv_dsl_open_api_vo = cls(
            modulation_type=modulation_type,
            ip_phone_vpi=ip_phone_vpi,
            ip_phone_vci=ip_phone_vci,
            iptv_vpi=iptv_vpi,
            iptv_vci=iptv_vci,
        )

        iptv_dsl_open_api_vo.additional_properties = d
        return iptv_dsl_open_api_vo

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
