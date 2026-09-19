from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_band_info_open_api_vo import MultiBandInfoOpenApiVO


T = TypeVar("T", bound="CandidateParentForAdoptOpenApiVO")


@_attrs_define
class CandidateParentForAdoptOpenApiVO:
    """
    Attributes:
        mac (str | Unset): candidate parent ap mac
        name (str | Unset): candidate parent ap name
        link_status (int | Unset): 0-init; 1-linking; 2-linked; 3-link fail; 4-offline
        hop (int | Unset): The number of hops to mesh with the candidate parent AP
        childsnum (int | Unset): The number of child aps already connected to the candidate parent ap
        recommend (bool | Unset): Whether the ap is recommended by the algorithm for connection
        recommend_radio_id (int | Unset): The radio ID for mesh recommended by the algorithm
        multi_band_info (list[MultiBandInfoOpenApiVO] | Unset): multi band info of candidate parent ap
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    link_status: int | Unset = UNSET
    hop: int | Unset = UNSET
    childsnum: int | Unset = UNSET
    recommend: bool | Unset = UNSET
    recommend_radio_id: int | Unset = UNSET
    multi_band_info: list[MultiBandInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        link_status = self.link_status

        hop = self.hop

        childsnum = self.childsnum

        recommend = self.recommend

        recommend_radio_id = self.recommend_radio_id

        multi_band_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_band_info, Unset):
            multi_band_info = []
            for multi_band_info_item_data in self.multi_band_info:
                multi_band_info_item = multi_band_info_item_data.to_dict()
                multi_band_info.append(multi_band_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if hop is not UNSET:
            field_dict["hop"] = hop
        if childsnum is not UNSET:
            field_dict["childsnum"] = childsnum
        if recommend is not UNSET:
            field_dict["recommend"] = recommend
        if recommend_radio_id is not UNSET:
            field_dict["recommendRadioId"] = recommend_radio_id
        if multi_band_info is not UNSET:
            field_dict["multiBandInfo"] = multi_band_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multi_band_info_open_api_vo import (
            MultiBandInfoOpenApiVO,
        )

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        hop = d.pop("hop", UNSET)

        childsnum = d.pop("childsnum", UNSET)

        recommend = d.pop("recommend", UNSET)

        recommend_radio_id = d.pop("recommendRadioId", UNSET)

        _multi_band_info = d.pop("multiBandInfo", UNSET)
        multi_band_info: list[MultiBandInfoOpenApiVO] | Unset = UNSET
        if _multi_band_info is not UNSET:
            multi_band_info = []
            for multi_band_info_item_data in _multi_band_info:
                multi_band_info_item = MultiBandInfoOpenApiVO.from_dict(
                    multi_band_info_item_data
                )

                multi_band_info.append(multi_band_info_item)

        candidate_parent_for_adopt_open_api_vo = cls(
            mac=mac,
            name=name,
            link_status=link_status,
            hop=hop,
            childsnum=childsnum,
            recommend=recommend,
            recommend_radio_id=recommend_radio_id,
            multi_band_info=multi_band_info,
        )

        candidate_parent_for_adopt_open_api_vo.additional_properties = d
        return candidate_parent_for_adopt_open_api_vo

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
