from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CallLogStatisticVO")


@_attrs_define
class CallLogStatisticVO:
    """
    Attributes:
        all_ (int | Unset):
        incoming (int | Unset):
        outgoing (int | Unset):
        forwarding (int | Unset):
        missed (int | Unset):
        rejected (int | Unset):
    """

    all_: int | Unset = UNSET
    incoming: int | Unset = UNSET
    outgoing: int | Unset = UNSET
    forwarding: int | Unset = UNSET
    missed: int | Unset = UNSET
    rejected: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        incoming = self.incoming

        outgoing = self.outgoing

        forwarding = self.forwarding

        missed = self.missed

        rejected = self.rejected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if incoming is not UNSET:
            field_dict["incoming"] = incoming
        if outgoing is not UNSET:
            field_dict["outgoing"] = outgoing
        if forwarding is not UNSET:
            field_dict["forwarding"] = forwarding
        if missed is not UNSET:
            field_dict["missed"] = missed
        if rejected is not UNSET:
            field_dict["rejected"] = rejected

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        incoming = d.pop("incoming", UNSET)

        outgoing = d.pop("outgoing", UNSET)

        forwarding = d.pop("forwarding", UNSET)

        missed = d.pop("missed", UNSET)

        rejected = d.pop("rejected", UNSET)

        call_log_statistic_vo = cls(
            all_=all_,
            incoming=incoming,
            outgoing=outgoing,
            forwarding=forwarding,
            missed=missed,
            rejected=rejected,
        )

        call_log_statistic_vo.additional_properties = d
        return call_log_statistic_vo

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
