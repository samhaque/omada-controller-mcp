from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access_capacity_info_vo import AccessCapacityInfoVO
    from ..models.channel_inter_info_vo import ChannelInterInfoVO
    from ..models.channel_util_info_vo import ChannelUtilInfoVO
    from ..models.client_access_time_info_vo import ClientAccessTimeInfoVO
    from ..models.rssi_info_vo import RssiInfoVO


T = TypeVar("T", bound="WifiClientInfoVO")


@_attrs_define
class WifiClientInfoVO:
    """
    Attributes:
        access_time_list (list[ClientAccessTimeInfoVO] | Unset):
        channel_util_list (list[ChannelUtilInfoVO] | Unset):
        channel_interf_list (list[ChannelInterInfoVO] | Unset):
        access_capacity_list (list[AccessCapacityInfoVO] | Unset):
        rssi_list (list[RssiInfoVO] | Unset):
    """

    access_time_list: list[ClientAccessTimeInfoVO] | Unset = UNSET
    channel_util_list: list[ChannelUtilInfoVO] | Unset = UNSET
    channel_interf_list: list[ChannelInterInfoVO] | Unset = UNSET
    access_capacity_list: list[AccessCapacityInfoVO] | Unset = UNSET
    rssi_list: list[RssiInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_time_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_time_list, Unset):
            access_time_list = []
            for access_time_list_item_data in self.access_time_list:
                access_time_list_item = access_time_list_item_data.to_dict()
                access_time_list.append(access_time_list_item)

        channel_util_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_util_list, Unset):
            channel_util_list = []
            for channel_util_list_item_data in self.channel_util_list:
                channel_util_list_item = channel_util_list_item_data.to_dict()
                channel_util_list.append(channel_util_list_item)

        channel_interf_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_interf_list, Unset):
            channel_interf_list = []
            for channel_interf_list_item_data in self.channel_interf_list:
                channel_interf_list_item = channel_interf_list_item_data.to_dict()
                channel_interf_list.append(channel_interf_list_item)

        access_capacity_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_capacity_list, Unset):
            access_capacity_list = []
            for access_capacity_list_item_data in self.access_capacity_list:
                access_capacity_list_item = access_capacity_list_item_data.to_dict()
                access_capacity_list.append(access_capacity_list_item)

        rssi_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rssi_list, Unset):
            rssi_list = []
            for rssi_list_item_data in self.rssi_list:
                rssi_list_item = rssi_list_item_data.to_dict()
                rssi_list.append(rssi_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_time_list is not UNSET:
            field_dict["accessTimeList"] = access_time_list
        if channel_util_list is not UNSET:
            field_dict["channelUtilList"] = channel_util_list
        if channel_interf_list is not UNSET:
            field_dict["channelInterfList"] = channel_interf_list
        if access_capacity_list is not UNSET:
            field_dict["accessCapacityList"] = access_capacity_list
        if rssi_list is not UNSET:
            field_dict["rssiList"] = rssi_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.access_capacity_info_vo import (
            AccessCapacityInfoVO,
        )
        from ..models.channel_inter_info_vo import ChannelInterInfoVO
        from ..models.channel_util_info_vo import ChannelUtilInfoVO
        from ..models.client_access_time_info_vo import (
            ClientAccessTimeInfoVO,
        )
        from ..models.rssi_info_vo import RssiInfoVO

        d = dict(src_dict)
        _access_time_list = d.pop("accessTimeList", UNSET)
        access_time_list: list[ClientAccessTimeInfoVO] | Unset = UNSET
        if _access_time_list is not UNSET:
            access_time_list = []
            for access_time_list_item_data in _access_time_list:
                access_time_list_item = ClientAccessTimeInfoVO.from_dict(
                    access_time_list_item_data
                )

                access_time_list.append(access_time_list_item)

        _channel_util_list = d.pop("channelUtilList", UNSET)
        channel_util_list: list[ChannelUtilInfoVO] | Unset = UNSET
        if _channel_util_list is not UNSET:
            channel_util_list = []
            for channel_util_list_item_data in _channel_util_list:
                channel_util_list_item = ChannelUtilInfoVO.from_dict(
                    channel_util_list_item_data
                )

                channel_util_list.append(channel_util_list_item)

        _channel_interf_list = d.pop("channelInterfList", UNSET)
        channel_interf_list: list[ChannelInterInfoVO] | Unset = UNSET
        if _channel_interf_list is not UNSET:
            channel_interf_list = []
            for channel_interf_list_item_data in _channel_interf_list:
                channel_interf_list_item = ChannelInterInfoVO.from_dict(
                    channel_interf_list_item_data
                )

                channel_interf_list.append(channel_interf_list_item)

        _access_capacity_list = d.pop("accessCapacityList", UNSET)
        access_capacity_list: list[AccessCapacityInfoVO] | Unset = UNSET
        if _access_capacity_list is not UNSET:
            access_capacity_list = []
            for access_capacity_list_item_data in _access_capacity_list:
                access_capacity_list_item = AccessCapacityInfoVO.from_dict(
                    access_capacity_list_item_data
                )

                access_capacity_list.append(access_capacity_list_item)

        _rssi_list = d.pop("rssiList", UNSET)
        rssi_list: list[RssiInfoVO] | Unset = UNSET
        if _rssi_list is not UNSET:
            rssi_list = []
            for rssi_list_item_data in _rssi_list:
                rssi_list_item = RssiInfoVO.from_dict(rssi_list_item_data)

                rssi_list.append(rssi_list_item)

        wifi_client_info_vo = cls(
            access_time_list=access_time_list,
            channel_util_list=channel_util_list,
            channel_interf_list=channel_interf_list,
            access_capacity_list=access_capacity_list,
            rssi_list=rssi_list,
        )

        wifi_client_info_vo.additional_properties = d
        return wifi_client_info_vo

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
