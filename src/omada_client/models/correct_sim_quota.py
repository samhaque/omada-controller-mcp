from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CorrectSimQuota")


@_attrs_define
class CorrectSimQuota:
    """
    Attributes:
        data (float | Unset): The amount of data usage(KB) in current billing cycle.
        sms (int | Unset): The amount of SMS in current billing cycle, valid date should be within the range of
            0–100000.
        sim_card (int | Unset): When device supports Dual-SIM card, using parameter [simCard] to point which card to
            configure. 1: SIM1; 2:SIM2.
    """

    data: float | Unset = UNSET
    sms: int | Unset = UNSET
    sim_card: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        sms = self.sms

        sim_card = self.sim_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if sms is not UNSET:
            field_dict["sms"] = sms
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        sms = d.pop("sms", UNSET)

        sim_card = d.pop("simCard", UNSET)

        correct_sim_quota = cls(
            data=data,
            sms=sms,
            sim_card=sim_card,
        )

        correct_sim_quota.additional_properties = d
        return correct_sim_quota

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
