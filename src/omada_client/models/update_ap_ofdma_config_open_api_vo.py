from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApOfdmaConfigOpenApiVO")


@_attrs_define
class UpdateApOfdmaConfigOpenApiVO:
    """
    Attributes:
        ofdma_enable_2_g (bool | Unset): Advanced feature OFDMA 2G config status. True: enable, false: disable.
        ofdma_enable_5_g (bool | Unset): Advanced feature OFDMA 5G1 config status. True: enable, false: disable.
        ofdma_enable_5_g_2 (bool | Unset): Advanced feature OFDMA 5G2 config status. True: enable, false: disable.
        ofdma_enable_6_g (bool | Unset): Advanced feature OFDMA 6G config status. True: enable, false: disable.
    """

    ofdma_enable_2_g: bool | Unset = UNSET
    ofdma_enable_5_g: bool | Unset = UNSET
    ofdma_enable_5_g_2: bool | Unset = UNSET
    ofdma_enable_6_g: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ofdma_enable_2_g = self.ofdma_enable_2_g

        ofdma_enable_5_g = self.ofdma_enable_5_g

        ofdma_enable_5_g_2 = self.ofdma_enable_5_g_2

        ofdma_enable_6_g = self.ofdma_enable_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ofdma_enable_2_g is not UNSET:
            field_dict["ofdmaEnable2g"] = ofdma_enable_2_g
        if ofdma_enable_5_g is not UNSET:
            field_dict["ofdmaEnable5g"] = ofdma_enable_5_g
        if ofdma_enable_5_g_2 is not UNSET:
            field_dict["ofdmaEnable5g2"] = ofdma_enable_5_g_2
        if ofdma_enable_6_g is not UNSET:
            field_dict["ofdmaEnable6g"] = ofdma_enable_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ofdma_enable_2_g = d.pop("ofdmaEnable2g", UNSET)

        ofdma_enable_5_g = d.pop("ofdmaEnable5g", UNSET)

        ofdma_enable_5_g_2 = d.pop("ofdmaEnable5g2", UNSET)

        ofdma_enable_6_g = d.pop("ofdmaEnable6g", UNSET)

        update_ap_ofdma_config_open_api_vo = cls(
            ofdma_enable_2_g=ofdma_enable_2_g,
            ofdma_enable_5_g=ofdma_enable_5_g,
            ofdma_enable_5_g_2=ofdma_enable_5_g_2,
            ofdma_enable_6_g=ofdma_enable_6_g,
        )

        update_ap_ofdma_config_open_api_vo.additional_properties = d
        return update_ap_ofdma_config_open_api_vo

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
