from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_health_category_vo import ClientHealthCategoryVO


T = TypeVar("T", bound="ClientHealthTrendVO")


@_attrs_define
class ClientHealthTrendVO:
    """
    Attributes:
        time (int | Unset): Timestamp
        total (int | Unset): Total client count
        good (int | Unset): Good health count
        average (int | Unset): Fair health count
        poor (int | Unset): Poor health count
        no_data (int | Unset): No data count
        wireless (ClientHealthCategoryVO | Unset): Wired client health
        wired (ClientHealthCategoryVO | Unset): Wired client health
    """

    time: int | Unset = UNSET
    total: int | Unset = UNSET
    good: int | Unset = UNSET
    average: int | Unset = UNSET
    poor: int | Unset = UNSET
    no_data: int | Unset = UNSET
    wireless: ClientHealthCategoryVO | Unset = UNSET
    wired: ClientHealthCategoryVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        total = self.total

        good = self.good

        average = self.average

        poor = self.poor

        no_data = self.no_data

        wireless: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless, Unset):
            wireless = self.wireless.to_dict()

        wired: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wired, Unset):
            wired = self.wired.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if total is not UNSET:
            field_dict["total"] = total
        if good is not UNSET:
            field_dict["good"] = good
        if average is not UNSET:
            field_dict["average"] = average
        if poor is not UNSET:
            field_dict["poor"] = poor
        if no_data is not UNSET:
            field_dict["noData"] = no_data
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if wired is not UNSET:
            field_dict["wired"] = wired

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_health_category_vo import (
            ClientHealthCategoryVO,
        )

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        total = d.pop("total", UNSET)

        good = d.pop("good", UNSET)

        average = d.pop("average", UNSET)

        poor = d.pop("poor", UNSET)

        no_data = d.pop("noData", UNSET)

        _wireless = d.pop("wireless", UNSET)
        wireless: ClientHealthCategoryVO | Unset
        if isinstance(_wireless, Unset):
            wireless = UNSET
        else:
            wireless = ClientHealthCategoryVO.from_dict(_wireless)

        _wired = d.pop("wired", UNSET)
        wired: ClientHealthCategoryVO | Unset
        if isinstance(_wired, Unset):
            wired = UNSET
        else:
            wired = ClientHealthCategoryVO.from_dict(_wired)

        client_health_trend_vo = cls(
            time=time,
            total=total,
            good=good,
            average=average,
            poor=poor,
            no_data=no_data,
            wireless=wireless,
            wired=wired,
        )

        client_health_trend_vo.additional_properties = d
        return client_health_trend_vo

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
