from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_ranking_band_item_vo import IncidentRankingBandItemVO
    from ..models.incident_ranking_client_item_vo import IncidentRankingClientItemVO
    from ..models.incident_ranking_device_item_vo import IncidentRankingDeviceItemVO
    from ..models.incident_ranking_ssid_item_vo import IncidentRankingSsidItemVO


T = TypeVar("T", bound="IncidentRankingResultVO")


@_attrs_define
class IncidentRankingResultVO:
    """
    Attributes:
        client_list (list[IncidentRankingClientItemVO] | Unset): Top clients ranked by incident count
        device_list (list[IncidentRankingDeviceItemVO] | Unset): Top devices ranked by incident count
        ssid_list (list[IncidentRankingSsidItemVO] | Unset): Top SSIDs ranked by incident count
        band_list (list[IncidentRankingBandItemVO] | Unset): Top frequency bands ranked by incident count (e.g.
            0=2.4GHz, 1=5GHz, 2=5GHz-2, 3=6GHz)
    """

    client_list: list[IncidentRankingClientItemVO] | Unset = UNSET
    device_list: list[IncidentRankingDeviceItemVO] | Unset = UNSET
    ssid_list: list[IncidentRankingSsidItemVO] | Unset = UNSET
    band_list: list[IncidentRankingBandItemVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_list, Unset):
            client_list = []
            for client_list_item_data in self.client_list:
                client_list_item = client_list_item_data.to_dict()
                client_list.append(client_list_item)

        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        ssid_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssid_list, Unset):
            ssid_list = []
            for ssid_list_item_data in self.ssid_list:
                ssid_list_item = ssid_list_item_data.to_dict()
                ssid_list.append(ssid_list_item)

        band_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.band_list, Unset):
            band_list = []
            for band_list_item_data in self.band_list:
                band_list_item = band_list_item_data.to_dict()
                band_list.append(band_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_list is not UNSET:
            field_dict["clientList"] = client_list
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list
        if ssid_list is not UNSET:
            field_dict["ssidList"] = ssid_list
        if band_list is not UNSET:
            field_dict["bandList"] = band_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_ranking_band_item_vo import (
            IncidentRankingBandItemVO,
        )
        from ..models.incident_ranking_client_item_vo import (
            IncidentRankingClientItemVO,
        )
        from ..models.incident_ranking_device_item_vo import (
            IncidentRankingDeviceItemVO,
        )
        from ..models.incident_ranking_ssid_item_vo import (
            IncidentRankingSsidItemVO,
        )

        d = dict(src_dict)
        _client_list = d.pop("clientList", UNSET)
        client_list: list[IncidentRankingClientItemVO] | Unset = UNSET
        if _client_list is not UNSET:
            client_list = []
            for client_list_item_data in _client_list:
                client_list_item = IncidentRankingClientItemVO.from_dict(
                    client_list_item_data
                )

                client_list.append(client_list_item)

        _device_list = d.pop("deviceList", UNSET)
        device_list: list[IncidentRankingDeviceItemVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = IncidentRankingDeviceItemVO.from_dict(
                    device_list_item_data
                )

                device_list.append(device_list_item)

        _ssid_list = d.pop("ssidList", UNSET)
        ssid_list: list[IncidentRankingSsidItemVO] | Unset = UNSET
        if _ssid_list is not UNSET:
            ssid_list = []
            for ssid_list_item_data in _ssid_list:
                ssid_list_item = IncidentRankingSsidItemVO.from_dict(
                    ssid_list_item_data
                )

                ssid_list.append(ssid_list_item)

        _band_list = d.pop("bandList", UNSET)
        band_list: list[IncidentRankingBandItemVO] | Unset = UNSET
        if _band_list is not UNSET:
            band_list = []
            for band_list_item_data in _band_list:
                band_list_item = IncidentRankingBandItemVO.from_dict(
                    band_list_item_data
                )

                band_list.append(band_list_item)

        incident_ranking_result_vo = cls(
            client_list=client_list,
            device_list=device_list,
            ssid_list=ssid_list,
            band_list=band_list,
        )

        incident_ranking_result_vo.additional_properties = d
        return incident_ranking_result_vo

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
