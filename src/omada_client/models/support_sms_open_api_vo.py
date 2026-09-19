from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportSmsOpenApiVO")


@_attrs_define
class SupportSmsOpenApiVO:
    """
    Attributes:
        support_sms (bool | Unset): Whether the using SIM card supports SMS.
        support_lte (bool | Unset): Whether the device supports LTE.
        support_dual_sms (int | Unset): Whether two SIM cards support SMS. 0: SIM1 and SIM2 not support; 1: SIM1
            supports, SIM2 not supports; 2: SIM1 not supports, SIM2 supports; 3: SIM1 and SIM2 support.
        support_dual_sim (int | Unset): Whether the device supports Dual-SIM card.
    """

    support_sms: bool | Unset = UNSET
    support_lte: bool | Unset = UNSET
    support_dual_sms: int | Unset = UNSET
    support_dual_sim: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_sms = self.support_sms

        support_lte = self.support_lte

        support_dual_sms = self.support_dual_sms

        support_dual_sim = self.support_dual_sim

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support_sms is not UNSET:
            field_dict["supportSms"] = support_sms
        if support_lte is not UNSET:
            field_dict["supportLte"] = support_lte
        if support_dual_sms is not UNSET:
            field_dict["supportDualSms"] = support_dual_sms
        if support_dual_sim is not UNSET:
            field_dict["supportDualSim"] = support_dual_sim

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support_sms = d.pop("supportSms", UNSET)

        support_lte = d.pop("supportLte", UNSET)

        support_dual_sms = d.pop("supportDualSms", UNSET)

        support_dual_sim = d.pop("supportDualSim", UNSET)

        support_sms_open_api_vo = cls(
            support_sms=support_sms,
            support_lte=support_lte,
            support_dual_sms=support_dual_sms,
            support_dual_sim=support_dual_sim,
        )

        support_sms_open_api_vo.additional_properties = d
        return support_sms_open_api_vo

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
