from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_model_base_vo import TopModelBaseVO


T = TypeVar("T", bound="TopApByRtDropVO")


@_attrs_define
class TopApByRtDropVO:
    """
    Attributes:
        top_ap_by_rt (list[TopModelBaseVO] | Unset):
        top_ap_by_drop (list[TopModelBaseVO] | Unset):
    """

    top_ap_by_rt: list[TopModelBaseVO] | Unset = UNSET
    top_ap_by_drop: list[TopModelBaseVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_ap_by_rt: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_rt, Unset):
            top_ap_by_rt = []
            for top_ap_by_rt_item_data in self.top_ap_by_rt:
                top_ap_by_rt_item = top_ap_by_rt_item_data.to_dict()
                top_ap_by_rt.append(top_ap_by_rt_item)

        top_ap_by_drop: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_by_drop, Unset):
            top_ap_by_drop = []
            for top_ap_by_drop_item_data in self.top_ap_by_drop:
                top_ap_by_drop_item = top_ap_by_drop_item_data.to_dict()
                top_ap_by_drop.append(top_ap_by_drop_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_ap_by_rt is not UNSET:
            field_dict["topApByRt"] = top_ap_by_rt
        if top_ap_by_drop is not UNSET:
            field_dict["topApByDrop"] = top_ap_by_drop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.top_model_base_vo import TopModelBaseVO

        d = dict(src_dict)
        _top_ap_by_rt = d.pop("topApByRt", UNSET)
        top_ap_by_rt: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_rt is not UNSET:
            top_ap_by_rt = []
            for top_ap_by_rt_item_data in _top_ap_by_rt:
                top_ap_by_rt_item = TopModelBaseVO.from_dict(top_ap_by_rt_item_data)

                top_ap_by_rt.append(top_ap_by_rt_item)

        _top_ap_by_drop = d.pop("topApByDrop", UNSET)
        top_ap_by_drop: list[TopModelBaseVO] | Unset = UNSET
        if _top_ap_by_drop is not UNSET:
            top_ap_by_drop = []
            for top_ap_by_drop_item_data in _top_ap_by_drop:
                top_ap_by_drop_item = TopModelBaseVO.from_dict(top_ap_by_drop_item_data)

                top_ap_by_drop.append(top_ap_by_drop_item)

        top_ap_by_rt_drop_vo = cls(
            top_ap_by_rt=top_ap_by_rt,
            top_ap_by_drop=top_ap_by_drop,
        )

        top_ap_by_rt_drop_vo.additional_properties = d
        return top_ap_by_rt_drop_vo

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
