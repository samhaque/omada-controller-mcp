from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_model_base_vo import TopModelBaseVO


T = TypeVar("T", bound="TopApByTrafficAndClientVO")


@_attrs_define
class TopApByTrafficAndClientVO:
    """
    Attributes:
        top_ap_by_traffic_max (list[TopModelBaseVO] | Unset):
        top_ap_by_traffic_min (list[TopModelBaseVO] | Unset):
        top_ap_by_client_max (list[TopModelBaseVO] | Unset):
        top_ap_by_client_min (list[TopModelBaseVO] | Unset):
    """

    top_ap_by_traffic_max: list[TopModelBaseVO] | Unset = UNSET
    top_ap_by_traffic_min: list[TopModelBaseVO] | Unset = UNSET
    top_ap_by_client_max: list[TopModelBaseVO] | Unset = UNSET
    top_ap_by_client_min: list[TopModelBaseVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_ap_by_traffic_max: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_traffic_max, Unset):
            top_ap_by_traffic_max = []
            for top_ap_by_traffic_max_item_data in self.top_ap_by_traffic_max:
                top_ap_by_traffic_max_item = top_ap_by_traffic_max_item_data.to_dict()
                top_ap_by_traffic_max.append(top_ap_by_traffic_max_item)

        top_ap_by_traffic_min: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_traffic_min, Unset):
            top_ap_by_traffic_min = []
            for top_ap_by_traffic_min_item_data in self.top_ap_by_traffic_min:
                top_ap_by_traffic_min_item = top_ap_by_traffic_min_item_data.to_dict()
                top_ap_by_traffic_min.append(top_ap_by_traffic_min_item)

        top_ap_by_client_max: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_client_max, Unset):
            top_ap_by_client_max = []
            for top_ap_by_client_max_item_data in self.top_ap_by_client_max:
                top_ap_by_client_max_item = top_ap_by_client_max_item_data.to_dict()
                top_ap_by_client_max.append(top_ap_by_client_max_item)

        top_ap_by_client_min: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_client_min, Unset):
            top_ap_by_client_min = []
            for top_ap_by_client_min_item_data in self.top_ap_by_client_min:
                top_ap_by_client_min_item = top_ap_by_client_min_item_data.to_dict()
                top_ap_by_client_min.append(top_ap_by_client_min_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_ap_by_traffic_max is not UNSET:
            field_dict["topApByTrafficMax"] = top_ap_by_traffic_max
        if top_ap_by_traffic_min is not UNSET:
            field_dict["topApByTrafficMin"] = top_ap_by_traffic_min
        if top_ap_by_client_max is not UNSET:
            field_dict["topApByClientMax"] = top_ap_by_client_max
        if top_ap_by_client_min is not UNSET:
            field_dict["topApByClientMin"] = top_ap_by_client_min

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.top_model_base_vo import TopModelBaseVO

        d = dict(src_dict)
        _top_ap_by_traffic_max = d.pop("topApByTrafficMax", UNSET)
        top_ap_by_traffic_max: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_traffic_max is not UNSET:
            top_ap_by_traffic_max = []
            for top_ap_by_traffic_max_item_data in _top_ap_by_traffic_max:
                top_ap_by_traffic_max_item = TopModelBaseVO.from_dict(
                    top_ap_by_traffic_max_item_data
                )

                top_ap_by_traffic_max.append(top_ap_by_traffic_max_item)

        _top_ap_by_traffic_min = d.pop("topApByTrafficMin", UNSET)
        top_ap_by_traffic_min: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_traffic_min is not UNSET:
            top_ap_by_traffic_min = []
            for top_ap_by_traffic_min_item_data in _top_ap_by_traffic_min:
                top_ap_by_traffic_min_item = TopModelBaseVO.from_dict(
                    top_ap_by_traffic_min_item_data
                )

                top_ap_by_traffic_min.append(top_ap_by_traffic_min_item)

        _top_ap_by_client_max = d.pop("topApByClientMax", UNSET)
        top_ap_by_client_max: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_client_max is not UNSET:
            top_ap_by_client_max = []
            for top_ap_by_client_max_item_data in _top_ap_by_client_max:
                top_ap_by_client_max_item = TopModelBaseVO.from_dict(
                    top_ap_by_client_max_item_data
                )

                top_ap_by_client_max.append(top_ap_by_client_max_item)

        _top_ap_by_client_min = d.pop("topApByClientMin", UNSET)
        top_ap_by_client_min: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_client_min is not UNSET:
            top_ap_by_client_min = []
            for top_ap_by_client_min_item_data in _top_ap_by_client_min:
                top_ap_by_client_min_item = TopModelBaseVO.from_dict(
                    top_ap_by_client_min_item_data
                )

                top_ap_by_client_min.append(top_ap_by_client_min_item)

        top_ap_by_traffic_and_client_vo = cls(
            top_ap_by_traffic_max=top_ap_by_traffic_max,
            top_ap_by_traffic_min=top_ap_by_traffic_min,
            top_ap_by_client_max=top_ap_by_client_max,
            top_ap_by_client_min=top_ap_by_client_min,
        )

        top_ap_by_traffic_and_client_vo.additional_properties = d
        return top_ap_by_traffic_and_client_vo

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
