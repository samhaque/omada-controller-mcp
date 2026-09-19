from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoamingOpenApiVO")


@_attrs_define
class RoamingOpenApiVO:
    """Site roaming.

    Attributes:
        fast_roaming_enable (bool): Whether to enable fast roaming
        ai_roaming_enable (bool): Whether to enable AI roaming, this configuration will take effect only when fast
            roaming is enabled
        dual_band_11_k_report_enable (bool | Unset): Whether to enable 802.11k report. It has been deprecated.
        force_disassociation_enable (bool | Unset): Whether to enable forced disassociation. Note: This field will no
            longer be supported since Omada Controller 5.14.24.40.
        non_stick_roaming_enable (bool | Unset): Whether to enable non-stick roaming
    """

    fast_roaming_enable: bool
    ai_roaming_enable: bool
    dual_band_11_k_report_enable: bool | Unset = UNSET
    force_disassociation_enable: bool | Unset = UNSET
    non_stick_roaming_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fast_roaming_enable = self.fast_roaming_enable

        ai_roaming_enable = self.ai_roaming_enable

        dual_band_11_k_report_enable = self.dual_band_11_k_report_enable

        force_disassociation_enable = self.force_disassociation_enable

        non_stick_roaming_enable = self.non_stick_roaming_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fastRoamingEnable": fast_roaming_enable,
                "aiRoamingEnable": ai_roaming_enable,
            }
        )
        if dual_band_11_k_report_enable is not UNSET:
            field_dict["dualBand11kReportEnable"] = dual_band_11_k_report_enable
        if force_disassociation_enable is not UNSET:
            field_dict["forceDisassociationEnable"] = force_disassociation_enable
        if non_stick_roaming_enable is not UNSET:
            field_dict["nonStickRoamingEnable"] = non_stick_roaming_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fast_roaming_enable = d.pop("fastRoamingEnable")

        ai_roaming_enable = d.pop("aiRoamingEnable")

        dual_band_11_k_report_enable = d.pop("dualBand11kReportEnable", UNSET)

        force_disassociation_enable = d.pop("forceDisassociationEnable", UNSET)

        non_stick_roaming_enable = d.pop("nonStickRoamingEnable", UNSET)

        roaming_open_api_vo = cls(
            fast_roaming_enable=fast_roaming_enable,
            ai_roaming_enable=ai_roaming_enable,
            dual_band_11_k_report_enable=dual_band_11_k_report_enable,
            force_disassociation_enable=force_disassociation_enable,
            non_stick_roaming_enable=non_stick_roaming_enable,
        )

        roaming_open_api_vo.additional_properties = d
        return roaming_open_api_vo

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
