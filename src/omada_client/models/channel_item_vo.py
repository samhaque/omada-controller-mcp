from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.afc_6g_power_detail_vo import Afc6GPowerDetailVO
    from ..models.channel_detail_vo import ChannelDetailVO


T = TypeVar("T", bound="ChannelItemVO")


@_attrs_define
class ChannelItemVO:
    """Ap channel item list.

    Attributes:
        radio_id (int | Unset):
        band (str | Unset):
        channel_list (list[ChannelDetailVO] | Unset):
        afc_6_g_power_list (list[Afc6GPowerDetailVO] | Unset):
        disable_6_g_reason (int | Unset):
        min_pow_ant (int | Unset):
        max_pow_ant (int | Unset):
    """

    radio_id: int | Unset = UNSET
    band: str | Unset = UNSET
    channel_list: list[ChannelDetailVO] | Unset = UNSET
    afc_6_g_power_list: list[Afc6GPowerDetailVO] | Unset = UNSET
    disable_6_g_reason: int | Unset = UNSET
    min_pow_ant: int | Unset = UNSET
    max_pow_ant: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        band = self.band

        channel_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_list, Unset):
            channel_list = []
            for channel_list_item_data in self.channel_list:
                channel_list_item = channel_list_item_data.to_dict()
                channel_list.append(channel_list_item)

        afc_6_g_power_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.afc_6_g_power_list, Unset):
            afc_6_g_power_list = []
            for afc_6_g_power_list_item_data in self.afc_6_g_power_list:
                afc_6_g_power_list_item = afc_6_g_power_list_item_data.to_dict()
                afc_6_g_power_list.append(afc_6_g_power_list_item)

        disable_6_g_reason = self.disable_6_g_reason

        min_pow_ant = self.min_pow_ant

        max_pow_ant = self.max_pow_ant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if band is not UNSET:
            field_dict["band"] = band
        if channel_list is not UNSET:
            field_dict["channelList"] = channel_list
        if afc_6_g_power_list is not UNSET:
            field_dict["afc6gPowerList"] = afc_6_g_power_list
        if disable_6_g_reason is not UNSET:
            field_dict["disable6gReason"] = disable_6_g_reason
        if min_pow_ant is not UNSET:
            field_dict["minPowAnt"] = min_pow_ant
        if max_pow_ant is not UNSET:
            field_dict["maxPowAnt"] = max_pow_ant

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.afc_6g_power_detail_vo import Afc6GPowerDetailVO
        from ..models.channel_detail_vo import ChannelDetailVO

        d = dict(src_dict)
        radio_id = d.pop("radioId", UNSET)

        band = d.pop("band", UNSET)

        _channel_list = d.pop("channelList", UNSET)
        channel_list: list[ChannelDetailVO] | Unset = UNSET
        if _channel_list is not UNSET:
            channel_list = []
            for channel_list_item_data in _channel_list:
                channel_list_item = ChannelDetailVO.from_dict(channel_list_item_data)

                channel_list.append(channel_list_item)

        _afc_6_g_power_list = d.pop("afc6gPowerList", UNSET)
        afc_6_g_power_list: list[Afc6GPowerDetailVO] | Unset = UNSET
        if _afc_6_g_power_list is not UNSET:
            afc_6_g_power_list = []
            for afc_6_g_power_list_item_data in _afc_6_g_power_list:
                afc_6_g_power_list_item = Afc6GPowerDetailVO.from_dict(
                    afc_6_g_power_list_item_data
                )

                afc_6_g_power_list.append(afc_6_g_power_list_item)

        disable_6_g_reason = d.pop("disable6gReason", UNSET)

        min_pow_ant = d.pop("minPowAnt", UNSET)

        max_pow_ant = d.pop("maxPowAnt", UNSET)

        channel_item_vo = cls(
            radio_id=radio_id,
            band=band,
            channel_list=channel_list,
            afc_6_g_power_list=afc_6_g_power_list,
            disable_6_g_reason=disable_6_g_reason,
            min_pow_ant=min_pow_ant,
            max_pow_ant=max_pow_ant,
        )

        channel_item_vo.additional_properties = d
        return channel_item_vo

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
