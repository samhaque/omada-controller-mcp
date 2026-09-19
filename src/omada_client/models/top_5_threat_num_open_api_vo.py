from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_open_api_vo import ClassificationOpenApiVO
    from ..models.geo_open_api_vo import GeoOpenApiVO


T = TypeVar("T", bound="Top5ThreatNumOpenApiVO")


@_attrs_define
class Top5ThreatNumOpenApiVO:
    """
    Attributes:
        geo (list[GeoOpenApiVO] | Unset): Geo List.
        classification (list[ClassificationOpenApiVO] | Unset): Classification List.
    """

    geo: list[GeoOpenApiVO] | Unset = UNSET
    classification: list[ClassificationOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        geo: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geo, Unset):
            geo = []
            for geo_item_data in self.geo:
                geo_item = geo_item_data.to_dict()
                geo.append(geo_item)

        classification: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.classification, Unset):
            classification = []
            for classification_item_data in self.classification:
                classification_item = classification_item_data.to_dict()
                classification.append(classification_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geo is not UNSET:
            field_dict["geo"] = geo
        if classification is not UNSET:
            field_dict["classification"] = classification

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.classification_open_api_vo import (
            ClassificationOpenApiVO,
        )
        from ..models.geo_open_api_vo import GeoOpenApiVO

        d = dict(src_dict)
        _geo = d.pop("geo", UNSET)
        geo: list[GeoOpenApiVO] | Unset = UNSET
        if _geo is not UNSET:
            geo = []
            for geo_item_data in _geo:
                geo_item = GeoOpenApiVO.from_dict(geo_item_data)

                geo.append(geo_item)

        _classification = d.pop("classification", UNSET)
        classification: list[ClassificationOpenApiVO] | Unset = UNSET
        if _classification is not UNSET:
            classification = []
            for classification_item_data in _classification:
                classification_item = ClassificationOpenApiVO.from_dict(
                    classification_item_data
                )

                classification.append(classification_item)

        top_5_threat_num_open_api_vo = cls(
            geo=geo,
            classification=classification,
        )

        top_5_threat_num_open_api_vo.additional_properties = d
        return top_5_threat_num_open_api_vo

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
