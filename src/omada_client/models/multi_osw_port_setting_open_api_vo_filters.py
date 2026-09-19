from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.multi_osw_port_setting_open_api_vo_filters_additional_property import (
        MultiOswPortSettingOpenApiVOFiltersAdditionalProperty,
    )


T = TypeVar("T", bound="MultiOswPortSettingOpenApiVOFilters")


@_attrs_define
class MultiOswPortSettingOpenApiVOFilters:
    """Filter conditions in the form of Map.It is effected when [selectAll] is 'true', filter key is the filter field and
    the value is the filter content.Filter fields include: [connectedStatus], [networkMode], [poeDisplayType],
    [linkSpeed], [duplex],[switchMac], [switchStatusCategory], [switchSupportPoe], [nativeNetworkId],
    [networkTagsSetting], [profileId], [operation], [tagIds].

    """

    additional_properties: dict[
        str, MultiOswPortSettingOpenApiVOFiltersAdditionalProperty
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multi_osw_port_setting_open_api_vo_filters_additional_property import (
            MultiOswPortSettingOpenApiVOFiltersAdditionalProperty,
        )

        d = dict(src_dict)
        multi_osw_port_setting_open_api_vo_filters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                MultiOswPortSettingOpenApiVOFiltersAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        multi_osw_port_setting_open_api_vo_filters.additional_properties = (
            additional_properties
        )
        return multi_osw_port_setting_open_api_vo_filters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> MultiOswPortSettingOpenApiVOFiltersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: MultiOswPortSettingOpenApiVOFiltersAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
