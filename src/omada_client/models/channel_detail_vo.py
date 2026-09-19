from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelDetailVO")


@_attrs_define
class ChannelDetailVO:
    """
    Attributes:
        freq (int | Unset):
        channel_name (str | Unset):
        value (int | Unset):
        max_pow (int | Unset):
        width_flag (int | Unset):
        dfs (int | Unset):
        limit (int | Unset):
        channel_value (int | Unset):
        max_pow_id (int | Unset):
        width_flag_id (int | Unset):
        max_pow_od (int | Unset):
        width_flag_od (int | Unset):
        min_pow_ant (int | Unset):
        max_pow_ant (int | Unset):
    """

    freq: int | Unset = UNSET
    channel_name: str | Unset = UNSET
    value: int | Unset = UNSET
    max_pow: int | Unset = UNSET
    width_flag: int | Unset = UNSET
    dfs: int | Unset = UNSET
    limit: int | Unset = UNSET
    channel_value: int | Unset = UNSET
    max_pow_id: int | Unset = UNSET
    width_flag_id: int | Unset = UNSET
    max_pow_od: int | Unset = UNSET
    width_flag_od: int | Unset = UNSET
    min_pow_ant: int | Unset = UNSET
    max_pow_ant: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        freq = self.freq

        channel_name = self.channel_name

        value = self.value

        max_pow = self.max_pow

        width_flag = self.width_flag

        dfs = self.dfs

        limit = self.limit

        channel_value = self.channel_value

        max_pow_id = self.max_pow_id

        width_flag_id = self.width_flag_id

        max_pow_od = self.max_pow_od

        width_flag_od = self.width_flag_od

        min_pow_ant = self.min_pow_ant

        max_pow_ant = self.max_pow_ant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if freq is not UNSET:
            field_dict["freq"] = freq
        if channel_name is not UNSET:
            field_dict["channelName"] = channel_name
        if value is not UNSET:
            field_dict["value"] = value
        if max_pow is not UNSET:
            field_dict["maxPow"] = max_pow
        if width_flag is not UNSET:
            field_dict["widthFlag"] = width_flag
        if dfs is not UNSET:
            field_dict["dfs"] = dfs
        if limit is not UNSET:
            field_dict["limit"] = limit
        if channel_value is not UNSET:
            field_dict["channelValue"] = channel_value
        if max_pow_id is not UNSET:
            field_dict["maxPowId"] = max_pow_id
        if width_flag_id is not UNSET:
            field_dict["widthFlagId"] = width_flag_id
        if max_pow_od is not UNSET:
            field_dict["maxPowOd"] = max_pow_od
        if width_flag_od is not UNSET:
            field_dict["widthFlagOd"] = width_flag_od
        if min_pow_ant is not UNSET:
            field_dict["minPowAnt"] = min_pow_ant
        if max_pow_ant is not UNSET:
            field_dict["maxPowAnt"] = max_pow_ant

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        freq = d.pop("freq", UNSET)

        channel_name = d.pop("channelName", UNSET)

        value = d.pop("value", UNSET)

        max_pow = d.pop("maxPow", UNSET)

        width_flag = d.pop("widthFlag", UNSET)

        dfs = d.pop("dfs", UNSET)

        limit = d.pop("limit", UNSET)

        channel_value = d.pop("channelValue", UNSET)

        max_pow_id = d.pop("maxPowId", UNSET)

        width_flag_id = d.pop("widthFlagId", UNSET)

        max_pow_od = d.pop("maxPowOd", UNSET)

        width_flag_od = d.pop("widthFlagOd", UNSET)

        min_pow_ant = d.pop("minPowAnt", UNSET)

        max_pow_ant = d.pop("maxPowAnt", UNSET)

        channel_detail_vo = cls(
            freq=freq,
            channel_name=channel_name,
            value=value,
            max_pow=max_pow,
            width_flag=width_flag,
            dfs=dfs,
            limit=limit,
            channel_value=channel_value,
            max_pow_id=max_pow_id,
            width_flag_id=width_flag_id,
            max_pow_od=max_pow_od,
            width_flag_od=width_flag_od,
            min_pow_ant=min_pow_ant,
            max_pow_ant=max_pow_ant,
        )

        channel_detail_vo.additional_properties = d
        return channel_detail_vo

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
