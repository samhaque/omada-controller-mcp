from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TabCardVO")


@_attrs_define
class TabCardVO:
    """card info

    Attributes:
        type_ (str | Unset): card type enum: overviewSummary,clientConnectionTrend,internet,network,alertSummary,gateway
            Summary,ispLoad,switchStatus,switchAlertReboot,topSwitchCpuMemory,topSwitchByTrafficAndPoePower,poePowerTrend,wi
            relessTraffic,apStatus,topApByTrafficAndClient,topApByInterference,topApByRtAndDrop,topApByCpuAndMemory,topSsidB
            yTraffic,clientsOverview,
            clientsAssociationActivities,clientsWithOnboardingTimes,topClient,appCategories,topApplicationByTraffic Example:
            overviewSummary.
        top_k (int | Unset): topK: 5, 10, 20 Example: 5.
    """

    type_: str | Unset = UNSET
    top_k: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if top_k is not UNSET:
            field_dict["topK"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        top_k = d.pop("topK", UNSET)

        tab_card_vo = cls(
            type_=type_,
            top_k=top_k,
        )

        tab_card_vo.additional_properties = d
        return tab_card_vo

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
