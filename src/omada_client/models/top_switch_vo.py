from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_model_base_vo import TopModelBaseVO


T = TypeVar("T", bound="TopSwitchVO")


@_attrs_define
class TopSwitchVO:
    """
    Attributes:
        top_switch_by_traffic (list[TopModelBaseVO] | Unset):
        top_switch_by_poe_power (list[TopModelBaseVO] | Unset):
    """

    top_switch_by_traffic: list[TopModelBaseVO] | Unset = UNSET
    top_switch_by_poe_power: list[TopModelBaseVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_switch_by_traffic: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_switch_by_traffic, Unset):
            top_switch_by_traffic = []
            for top_switch_by_traffic_item_data in self.top_switch_by_traffic:
                top_switch_by_traffic_item = top_switch_by_traffic_item_data.to_dict()
                top_switch_by_traffic.append(top_switch_by_traffic_item)

        top_switch_by_poe_power: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_switch_by_poe_power, Unset):
            top_switch_by_poe_power = []
            for top_switch_by_poe_power_item_data in self.top_switch_by_poe_power:
                top_switch_by_poe_power_item = (
                    top_switch_by_poe_power_item_data.to_dict()
                )
                top_switch_by_poe_power.append(top_switch_by_poe_power_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_switch_by_traffic is not UNSET:
            field_dict["topSwitchByTraffic"] = top_switch_by_traffic
        if top_switch_by_poe_power is not UNSET:
            field_dict["topSwitchByPoePower"] = top_switch_by_poe_power

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.top_model_base_vo import TopModelBaseVO

        d = dict(src_dict)
        _top_switch_by_traffic = d.pop("topSwitchByTraffic", UNSET)
        top_switch_by_traffic: list[TopModelBaseVO] | Unset = UNSET
        if _top_switch_by_traffic is not UNSET:
            top_switch_by_traffic = []
            for top_switch_by_traffic_item_data in _top_switch_by_traffic:
                top_switch_by_traffic_item = TopModelBaseVO.from_dict(
                    top_switch_by_traffic_item_data
                )

                top_switch_by_traffic.append(top_switch_by_traffic_item)

        _top_switch_by_poe_power = d.pop("topSwitchByPoePower", UNSET)
        top_switch_by_poe_power: list[TopModelBaseVO] | Unset = UNSET
        if _top_switch_by_poe_power is not UNSET:
            top_switch_by_poe_power = []
            for top_switch_by_poe_power_item_data in _top_switch_by_poe_power:
                top_switch_by_poe_power_item = TopModelBaseVO.from_dict(
                    top_switch_by_poe_power_item_data
                )

                top_switch_by_poe_power.append(top_switch_by_poe_power_item)

        top_switch_vo = cls(
            top_switch_by_traffic=top_switch_by_traffic,
            top_switch_by_poe_power=top_switch_by_poe_power,
        )

        top_switch_vo.additional_properties = d
        return top_switch_vo

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
