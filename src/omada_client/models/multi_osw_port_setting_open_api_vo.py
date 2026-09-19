from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_osw_port_setting_open_api_vo_filters import (
        MultiOswPortSettingOpenApiVOFilters,
    )
    from ..models.multi_osw_port_setting_open_api_vo_tag_bridge_vlan_map import (
        MultiOswPortSettingOpenApiVOTagBridgeVlanMap,
    )
    from ..models.multi_osw_port_setting_open_api_vo_untag_bridge_vlan_map import (
        MultiOswPortSettingOpenApiVOUntagBridgeVlanMap,
    )
    from ..models.osw_port_lag_list_vo import OswPortLagListVO


T = TypeVar("T", bound="MultiOswPortSettingOpenApiVO")


@_attrs_define
class MultiOswPortSettingOpenApiVO:
    """
    Attributes:
        switch_list (list[OswPortLagListVO]): Switch List with port and LAG info
        select_all (bool): Indicates whether select all switch ports.false: include selected switch ports and lags in
            Parameter [switchList], true: all switch ports and lags but exclude selected switch ports and lags in Parameter
            [switchList].
        search_key (str | Unset): The keywords of the searchIt is effected when [selectAll] is 'true'.
        filters (MultiOswPortSettingOpenApiVOFilters | Unset): Filter conditions in the form of Map.It is effected when
            [selectAll] is 'true', filter key is the filter field and the value is the filter content.Filter fields include:
            [connectedStatus], [networkMode], [poeDisplayType], [linkSpeed], [duplex],[switchMac], [switchStatusCategory],
            [switchSupportPoe], [nativeNetworkId], [networkTagsSetting], [profileId], [operation], [tagIds].
        tag_ids (list[str] | Unset): Tag ID List
        native_network_id (str | Unset): Native Network ID, Native Network cannot be selected from Tagged Networks or
            Untagged Networks.
        native_bridge_vlan (int | Unset): Native Network Bridge Vlan.
        network_tags_setting (int | Unset): Network Tags Setting should be a value as follows: 0: Allow All; 1: Block
            All; 2: Custom
        tag_network_ids (list[str] | Unset): Tag Network IDs
        tag_bridge_vlan_map (MultiOswPortSettingOpenApiVOTagBridgeVlanMap | Unset): Tag Network Bridge Vlan Map
        untag_network_ids (list[str] | Unset): Untag Network IDs
        untag_bridge_vlan_map (MultiOswPortSettingOpenApiVOUntagBridgeVlanMap | Unset): Untag Network Bridge Vlan Map
        voice_network_enable (bool | Unset): Indicates whether voice network is enabled
        voice_network_id (str | Unset): Voice Network ID
        voice_bridge_vlan (int | Unset): Voice Network Bridge Vlan
        profile_id (str | Unset): Profile ID
        profile_override_enable (bool | Unset): Indicates whether to enable Profile Override before v6.2.10; Indicates
            the fill mode of port configuration after v6.2.10: true: custom; false: follow profile
        profile_vlan_override_enable (bool | Unset): Indicates the fill mode of vlan configuration: true: custom; false:
            follow profile
    """

    switch_list: list[OswPortLagListVO]
    select_all: bool
    search_key: str | Unset = UNSET
    filters: MultiOswPortSettingOpenApiVOFilters | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    native_network_id: str | Unset = UNSET
    native_bridge_vlan: int | Unset = UNSET
    network_tags_setting: int | Unset = UNSET
    tag_network_ids: list[str] | Unset = UNSET
    tag_bridge_vlan_map: MultiOswPortSettingOpenApiVOTagBridgeVlanMap | Unset = UNSET
    untag_network_ids: list[str] | Unset = UNSET
    untag_bridge_vlan_map: MultiOswPortSettingOpenApiVOUntagBridgeVlanMap | Unset = (
        UNSET
    )
    voice_network_enable: bool | Unset = UNSET
    voice_network_id: str | Unset = UNSET
    voice_bridge_vlan: int | Unset = UNSET
    profile_id: str | Unset = UNSET
    profile_override_enable: bool | Unset = UNSET
    profile_vlan_override_enable: bool | Unset = UNSET
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

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        native_network_id = self.native_network_id

        native_bridge_vlan = self.native_bridge_vlan

        network_tags_setting = self.network_tags_setting

        tag_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_network_ids, Unset):
            tag_network_ids = self.tag_network_ids

        tag_bridge_vlan_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tag_bridge_vlan_map, Unset):
            tag_bridge_vlan_map = self.tag_bridge_vlan_map.to_dict()

        untag_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.untag_network_ids, Unset):
            untag_network_ids = self.untag_network_ids

        untag_bridge_vlan_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.untag_bridge_vlan_map, Unset):
            untag_bridge_vlan_map = self.untag_bridge_vlan_map.to_dict()

        voice_network_enable = self.voice_network_enable

        voice_network_id = self.voice_network_id

        voice_bridge_vlan = self.voice_bridge_vlan

        profile_id = self.profile_id

        profile_override_enable = self.profile_override_enable

        profile_vlan_override_enable = self.profile_vlan_override_enable

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
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if native_network_id is not UNSET:
            field_dict["nativeNetworkId"] = native_network_id
        if native_bridge_vlan is not UNSET:
            field_dict["nativeBridgeVlan"] = native_bridge_vlan
        if network_tags_setting is not UNSET:
            field_dict["networkTagsSetting"] = network_tags_setting
        if tag_network_ids is not UNSET:
            field_dict["tagNetworkIds"] = tag_network_ids
        if tag_bridge_vlan_map is not UNSET:
            field_dict["tagBridgeVlanMap"] = tag_bridge_vlan_map
        if untag_network_ids is not UNSET:
            field_dict["untagNetworkIds"] = untag_network_ids
        if untag_bridge_vlan_map is not UNSET:
            field_dict["untagBridgeVlanMap"] = untag_bridge_vlan_map
        if voice_network_enable is not UNSET:
            field_dict["voiceNetworkEnable"] = voice_network_enable
        if voice_network_id is not UNSET:
            field_dict["voiceNetworkId"] = voice_network_id
        if voice_bridge_vlan is not UNSET:
            field_dict["voiceBridgeVlan"] = voice_bridge_vlan
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if profile_override_enable is not UNSET:
            field_dict["profileOverrideEnable"] = profile_override_enable
        if profile_vlan_override_enable is not UNSET:
            field_dict["profileVlanOverrideEnable"] = profile_vlan_override_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multi_osw_port_setting_open_api_vo_filters import (
            MultiOswPortSettingOpenApiVOFilters,
        )
        from ..models.multi_osw_port_setting_open_api_vo_tag_bridge_vlan_map import (
            MultiOswPortSettingOpenApiVOTagBridgeVlanMap,
        )
        from ..models.multi_osw_port_setting_open_api_vo_untag_bridge_vlan_map import (
            MultiOswPortSettingOpenApiVOUntagBridgeVlanMap,
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
        filters: MultiOswPortSettingOpenApiVOFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = MultiOswPortSettingOpenApiVOFilters.from_dict(_filters)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        native_network_id = d.pop("nativeNetworkId", UNSET)

        native_bridge_vlan = d.pop("nativeBridgeVlan", UNSET)

        network_tags_setting = d.pop("networkTagsSetting", UNSET)

        tag_network_ids = cast(list[str], d.pop("tagNetworkIds", UNSET))

        _tag_bridge_vlan_map = d.pop("tagBridgeVlanMap", UNSET)
        tag_bridge_vlan_map: MultiOswPortSettingOpenApiVOTagBridgeVlanMap | Unset
        if isinstance(_tag_bridge_vlan_map, Unset):
            tag_bridge_vlan_map = UNSET
        else:
            tag_bridge_vlan_map = (
                MultiOswPortSettingOpenApiVOTagBridgeVlanMap.from_dict(
                    _tag_bridge_vlan_map
                )
            )

        untag_network_ids = cast(list[str], d.pop("untagNetworkIds", UNSET))

        _untag_bridge_vlan_map = d.pop("untagBridgeVlanMap", UNSET)
        untag_bridge_vlan_map: MultiOswPortSettingOpenApiVOUntagBridgeVlanMap | Unset
        if isinstance(_untag_bridge_vlan_map, Unset):
            untag_bridge_vlan_map = UNSET
        else:
            untag_bridge_vlan_map = (
                MultiOswPortSettingOpenApiVOUntagBridgeVlanMap.from_dict(
                    _untag_bridge_vlan_map
                )
            )

        voice_network_enable = d.pop("voiceNetworkEnable", UNSET)

        voice_network_id = d.pop("voiceNetworkId", UNSET)

        voice_bridge_vlan = d.pop("voiceBridgeVlan", UNSET)

        profile_id = d.pop("profileId", UNSET)

        profile_override_enable = d.pop("profileOverrideEnable", UNSET)

        profile_vlan_override_enable = d.pop("profileVlanOverrideEnable", UNSET)

        multi_osw_port_setting_open_api_vo = cls(
            switch_list=switch_list,
            select_all=select_all,
            search_key=search_key,
            filters=filters,
            tag_ids=tag_ids,
            native_network_id=native_network_id,
            native_bridge_vlan=native_bridge_vlan,
            network_tags_setting=network_tags_setting,
            tag_network_ids=tag_network_ids,
            tag_bridge_vlan_map=tag_bridge_vlan_map,
            untag_network_ids=untag_network_ids,
            untag_bridge_vlan_map=untag_bridge_vlan_map,
            voice_network_enable=voice_network_enable,
            voice_network_id=voice_network_id,
            voice_bridge_vlan=voice_bridge_vlan,
            profile_id=profile_id,
            profile_override_enable=profile_override_enable,
            profile_vlan_override_enable=profile_vlan_override_enable,
        )

        multi_osw_port_setting_open_api_vo.additional_properties = d
        return multi_osw_port_setting_open_api_vo

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
