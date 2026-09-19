from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_osw_port_select_vo_filters import MultiOswPortSelectVOFilters
    from ..models.osw_port_lag_list_vo import OswPortLagListVO


T = TypeVar("T", bound="MultiOswPortSelectVO")


@_attrs_define
class MultiOswPortSelectVO:
    """
    Attributes:
        switch_list (list[OswPortLagListVO]): Switches Port And Lag List
        select_all (bool): Indicates whether select all switch ports.false: include selected switch ports and lags in
            Parameter [switchList], true: all switch ports and lags but exclude selected switch ports and lags in Parameter
            [switchList].
        search_key (str | Unset): The keywords of the searchIt is effected when [selectAll] is 'true'.
        filters (MultiOswPortSelectVOFilters | Unset): Filter conditions in the form of Map.It is effected when
            [selectAll] is 'true', filter key is the filter field and the value is the filter content.Filter fields include:
            [connectedStatus], [networkMode], [poeDisplayType], [linkSpeed], [duplex],[switchMac], [switchStatusCategory],
            [switchSupportPoe], [nativeNetworkId], [networkTagsSetting], [profileId], [operation], [tagIds].
    """

    switch_list: list[OswPortLagListVO]
    select_all: bool
    search_key: str | Unset = UNSET
    filters: MultiOswPortSelectVOFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        switch_list = []
        for switch_list_item_data in self.switch_list:
            switch_list_item = switch_list_item_data.to_dict()
            switch_list.append(switch_list_item)

        select_all = self.select_all

        search_key = self.search_key

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "switchList": switch_list,
                "selectAll": select_all,
            }
        )
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multi_osw_port_select_vo_filters import (
            MultiOswPortSelectVOFilters,
        )
        from ..models.osw_port_lag_list_vo import OswPortLagListVO

        d = dict(src_dict)
        switch_list = []
        _switch_list = d.pop("switchList")
        for switch_list_item_data in _switch_list:
            switch_list_item = OswPortLagListVO.from_dict(switch_list_item_data)

            switch_list.append(switch_list_item)

        select_all = d.pop("selectAll")

        search_key = d.pop("searchKey", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: MultiOswPortSelectVOFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = MultiOswPortSelectVOFilters.from_dict(_filters)

        multi_osw_port_select_vo = cls(
            switch_list=switch_list,
            select_all=select_all,
            search_key=search_key,
            filters=filters,
        )

        multi_osw_port_select_vo.additional_properties = d
        return multi_osw_port_select_vo

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
