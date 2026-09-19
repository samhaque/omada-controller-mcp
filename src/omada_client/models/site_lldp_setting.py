from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_ap_lldp_setting_vo import SiteApLldpSettingVO


T = TypeVar("T", bound="SiteLldpSetting")


@_attrs_define
class SiteLldpSetting:
    """Site LLDP setting.

    Attributes:
        lldp (SiteApLldpSettingVO | Unset): Site LLDP.
    """

    lldp: SiteApLldpSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lldp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lldp, Unset):
            lldp = self.lldp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lldp is not UNSET:
            field_dict["lldp"] = lldp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_ap_lldp_setting_vo import (
            SiteApLldpSettingVO,
        )

        d = dict(src_dict)
        _lldp = d.pop("lldp", UNSET)
        lldp: SiteApLldpSettingVO | Unset
        if isinstance(_lldp, Unset):
            lldp = UNSET
        else:
            lldp = SiteApLldpSettingVO.from_dict(_lldp)

        site_lldp_setting = cls(
            lldp=lldp,
        )

        site_lldp_setting.additional_properties = d
        return site_lldp_setting

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
