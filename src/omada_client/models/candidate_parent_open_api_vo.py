from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_band_info_open_api_vo import MultiBandInfoOpenApiVO


T = TypeVar("T", bound="CandidateParentOpenApiVO")


@_attrs_define
class CandidateParentOpenApiVO:
    """Candidate parent ap info

    Attributes:
        priority_status (int | Unset): priority parent ap status
        mac (str | Unset): candidate parent ap mac
        name (str | Unset): candidate parent ap name
        link_status (int | Unset): 0-init; 1-linking; 2-linked; 3-link fail; 4-offline
        hop (int | Unset): The number of hops to mesh with the candidate parent AP
        childsnum (int | Unset): The number of child aps already connected to the candidate parent ap
        support_5_g_multi_band (bool | Unset): 5G support 5G1 & 5G2 multi band
        model (str | Unset): Model
        model_version (str | Unset): Model version
        multi_band_info (list[MultiBandInfoOpenApiVO] | Unset): multi band info of candidate parent ap
    """

    priority_status: int | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    link_status: int | Unset = UNSET
    hop: int | Unset = UNSET
    childsnum: int | Unset = UNSET
    support_5_g_multi_band: bool | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    multi_band_info: list[MultiBandInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority_status = self.priority_status

        mac = self.mac

        name = self.name

        link_status = self.link_status

        hop = self.hop

        childsnum = self.childsnum

        support_5_g_multi_band = self.support_5_g_multi_band

        model = self.model

        model_version = self.model_version

        multi_band_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_band_info, Unset):
            multi_band_info = []
            for multi_band_info_item_data in self.multi_band_info:
                multi_band_info_item = multi_band_info_item_data.to_dict()
                multi_band_info.append(multi_band_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority_status is not UNSET:
            field_dict["priorityStatus"] = priority_status
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
        if support_5_g_multi_band is not UNSET:
            field_dict["support5gMultiBand"] = support_5_g_multi_band
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if multi_band_info is not UNSET:
            field_dict["multiBandInfo"] = multi_band_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multi_band_info_open_api_vo import (
            MultiBandInfoOpenApiVO,
        )

        d = dict(src_dict)
        priority_status = d.pop("priorityStatus", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        hop = d.pop("hop", UNSET)

        childsnum = d.pop("childsnum", UNSET)

        support_5_g_multi_band = d.pop("support5gMultiBand", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        _multi_band_info = d.pop("multiBandInfo", UNSET)
        multi_band_info: list[MultiBandInfoOpenApiVO] | Unset = UNSET
        if _multi_band_info is not UNSET:
            multi_band_info = []
            for multi_band_info_item_data in _multi_band_info:
                multi_band_info_item = MultiBandInfoOpenApiVO.from_dict(
                    multi_band_info_item_data
                )

                multi_band_info.append(multi_band_info_item)

        candidate_parent_open_api_vo = cls(
            priority_status=priority_status,
            mac=mac,
            name=name,
            link_status=link_status,
            hop=hop,
            childsnum=childsnum,
            support_5_g_multi_band=support_5_g_multi_band,
            model=model,
            model_version=model_version,
            multi_band_info=multi_band_info,
        )

        candidate_parent_open_api_vo.additional_properties = d
        return candidate_parent_open_api_vo

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
