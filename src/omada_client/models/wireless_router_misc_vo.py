from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessRouterMiscVO")


@_attrs_define
class WirelessRouterMiscVO:
    """
    Attributes:
        support2g (bool | Unset):
        support5g (bool | Unset):
        support5g2 (bool | Unset):
        support6g (bool | Unset):
        support11ac (bool | Unset):
        support_lag (bool | Unset):
        support_mesh (int | Unset):
        customize_region (int | Unset):
        min_power_2g (int | Unset):
        max_power_2g (int | Unset):
        min_power_5g (int | Unset):
        max_power_5g (int | Unset):
        min_power_5g2 (int | Unset):
        max_power_5g2 (int | Unset):
        min_power_6g (int | Unset):
        max_power_6g (int | Unset):
        support_channel_limit (bool | Unset):
        channel_limit_mode (int | Unset):
        support_dfs (int | Unset):
        support_roaming (int | Unset):
    """

    support2g: bool | Unset = UNSET
    support5g: bool | Unset = UNSET
    support5g2: bool | Unset = UNSET
    support6g: bool | Unset = UNSET
    support11ac: bool | Unset = UNSET
    support_lag: bool | Unset = UNSET
    support_mesh: int | Unset = UNSET
    customize_region: int | Unset = UNSET
    min_power_2g: int | Unset = UNSET
    max_power_2g: int | Unset = UNSET
    min_power_5g: int | Unset = UNSET
    max_power_5g: int | Unset = UNSET
    min_power_5g2: int | Unset = UNSET
    max_power_5g2: int | Unset = UNSET
    min_power_6g: int | Unset = UNSET
    max_power_6g: int | Unset = UNSET
    support_channel_limit: bool | Unset = UNSET
    channel_limit_mode: int | Unset = UNSET
    support_dfs: int | Unset = UNSET
    support_roaming: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support2g = self.support2g

        support5g = self.support5g

        support5g2 = self.support5g2

        support6g = self.support6g

        support11ac = self.support11ac

        support_lag = self.support_lag

        support_mesh = self.support_mesh

        customize_region = self.customize_region

        min_power_2g = self.min_power_2g

        max_power_2g = self.max_power_2g

        min_power_5g = self.min_power_5g

        max_power_5g = self.max_power_5g

        min_power_5g2 = self.min_power_5g2

        max_power_5g2 = self.max_power_5g2

        min_power_6g = self.min_power_6g

        max_power_6g = self.max_power_6g

        support_channel_limit = self.support_channel_limit

        channel_limit_mode = self.channel_limit_mode

        support_dfs = self.support_dfs

        support_roaming = self.support_roaming

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support2g is not UNSET:
            field_dict["support2g"] = support2g
        if support5g is not UNSET:
            field_dict["support5g"] = support5g
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if support6g is not UNSET:
            field_dict["support6g"] = support6g
        if support11ac is not UNSET:
            field_dict["support11ac"] = support11ac
        if support_lag is not UNSET:
            field_dict["supportLag"] = support_lag
        if support_mesh is not UNSET:
            field_dict["supportMesh"] = support_mesh
        if customize_region is not UNSET:
            field_dict["customizeRegion"] = customize_region
        if min_power_2g is not UNSET:
            field_dict["minPower2G"] = min_power_2g
        if max_power_2g is not UNSET:
            field_dict["maxPower2G"] = max_power_2g
        if min_power_5g is not UNSET:
            field_dict["minPower5G"] = min_power_5g
        if max_power_5g is not UNSET:
            field_dict["maxPower5G"] = max_power_5g
        if min_power_5g2 is not UNSET:
            field_dict["minPower5G2"] = min_power_5g2
        if max_power_5g2 is not UNSET:
            field_dict["maxPower5G2"] = max_power_5g2
        if min_power_6g is not UNSET:
            field_dict["minPower6G"] = min_power_6g
        if max_power_6g is not UNSET:
            field_dict["maxPower6G"] = max_power_6g
        if support_channel_limit is not UNSET:
            field_dict["supportChannelLimit"] = support_channel_limit
        if channel_limit_mode is not UNSET:
            field_dict["channelLimitMode"] = channel_limit_mode
        if support_dfs is not UNSET:
            field_dict["supportDfs"] = support_dfs
        if support_roaming is not UNSET:
            field_dict["supportRoaming"] = support_roaming

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support2g = d.pop("support2g", UNSET)

        support5g = d.pop("support5g", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        support6g = d.pop("support6g", UNSET)

        support11ac = d.pop("support11ac", UNSET)

        support_lag = d.pop("supportLag", UNSET)

        support_mesh = d.pop("supportMesh", UNSET)

        customize_region = d.pop("customizeRegion", UNSET)

        min_power_2g = d.pop("minPower2G", UNSET)

        max_power_2g = d.pop("maxPower2G", UNSET)

        min_power_5g = d.pop("minPower5G", UNSET)

        max_power_5g = d.pop("maxPower5G", UNSET)

        min_power_5g2 = d.pop("minPower5G2", UNSET)

        max_power_5g2 = d.pop("maxPower5G2", UNSET)

        min_power_6g = d.pop("minPower6G", UNSET)

        max_power_6g = d.pop("maxPower6G", UNSET)

        support_channel_limit = d.pop("supportChannelLimit", UNSET)

        channel_limit_mode = d.pop("channelLimitMode", UNSET)

        support_dfs = d.pop("supportDfs", UNSET)

        support_roaming = d.pop("supportRoaming", UNSET)

        wireless_router_misc_vo = cls(
            support2g=support2g,
            support5g=support5g,
            support5g2=support5g2,
            support6g=support6g,
            support11ac=support11ac,
            support_lag=support_lag,
            support_mesh=support_mesh,
            customize_region=customize_region,
            min_power_2g=min_power_2g,
            max_power_2g=max_power_2g,
            min_power_5g=min_power_5g,
            max_power_5g=max_power_5g,
            min_power_5g2=min_power_5g2,
            max_power_5g2=max_power_5g2,
            min_power_6g=min_power_6g,
            max_power_6g=max_power_6g,
            support_channel_limit=support_channel_limit,
            channel_limit_mode=channel_limit_mode,
            support_dfs=support_dfs,
            support_roaming=support_roaming,
        )

        wireless_router_misc_vo.additional_properties = d
        return wireless_router_misc_vo

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
