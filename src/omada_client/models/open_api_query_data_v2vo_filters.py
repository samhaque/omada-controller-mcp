from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.open_api_query_data_v2vo_filters_additional_property import (
        OpenApiQueryDataV2VOFiltersAdditionalProperty,
    )


T = TypeVar("T", bound="OpenApiQueryDataV2VOFilters")


@_attrs_define
class OpenApiQueryDataV2VOFilters:
    additional_properties: dict[str, OpenApiQueryDataV2VOFiltersAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.open_api_query_data_v2vo_filters_additional_property import (
            OpenApiQueryDataV2VOFiltersAdditionalProperty,
        )

        d = dict(src_dict)
        open_api_query_data_v2vo_filters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                OpenApiQueryDataV2VOFiltersAdditionalProperty.from_dict(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        open_api_query_data_v2vo_filters.additional_properties = additional_properties
        return open_api_query_data_v2vo_filters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> OpenApiQueryDataV2VOFiltersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: OpenApiQueryDataV2VOFiltersAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
