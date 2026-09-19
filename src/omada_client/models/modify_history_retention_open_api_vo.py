from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyHistoryRetentionOpenApiVO")


@_attrs_define
class ModifyHistoryRetentionOpenApiVO:
    """
    Attributes:
        clients_data_enable (bool): Whether the clients' history data is recorded.
        override (bool | Unset): Whether the customer overrides the retention configuration of MSP. This configuration
            applies to the customer in MSP mode only. If true, customer retention configuration will be used (excluding
            daily, clientHistory, log and widsData).
        client_data_trend_enable (bool | Unset): Whether the client data trend records is recorded.
        client_recognition_enable (bool | Unset): Whether client recognition is enabled. With the feature enabled,
            network devices will report client information in real time to ensure the accuracy of client recognition. Cloud
            Access is required for client recognition.
        client_health_enable (bool | Unset): Whether client health is enabled. When enabled, client health data will be
            recorded, which may consume a significant amount of storage space.
        known_client (int | Unset): Retention configuration of known client Data, knownClient should be a value as
            follows: -1: Disabled; 0: All Time(Windows, Linux Only); 1: 1day; 7: 7days; 31: 31days; 90: 90days; 180:
            180days; 365: 365days.
        client_history (int | Unset): Retention configuration of client History(only effective in local controller),
            clientHistory should be a value as follows: -1: Disabled; 0: All Time(Windows, Linux Only); 7: 7days; 31:
            31days; 90: 90days; 180: 180days; 365: 365days.
        daily (int | Unset): Retention configuration of time series with daily granularity, daily should be a value as
            follows: 90: 90days; 180: 180days; 365: 365days(Fixed value in Cloud Based Controller as 365 days).
        weekly (int | Unset): Retention configuration of time series with weekly granularity, weekly should be a value
            as follows: 31: 31days; 90: 90days; 180: 180days; 365: 365days.
        portal_auth (int | Unset): Retention configuration of portal authentication records, portalAuth should be a
            value as follows: 0: All Time(Windows, Linux Only); 7: 7days; 31: 31days; 90: 90days; 180: 180days; 365:
            365days.
        log (int | Unset): Retention Configuration of log data(only effective in local controller), log should be a
            value as follows: 0: All Time(Windows, Linux Only); 31: 31days; 90: 90days; 180: 180days; 365: 365days.
        rogue_ap (int | Unset): Retention Configuration of rogue ap data, rogueAp should be a value as follows: 0: All
            Time(Windows, Linux Only); 31: 31days; 90: 90days; 180: 180days; 365: 365days.
        wids_data (int | Unset): Retention Configuration of wids data(only effective in local pro controller), widsData
            should be a value as follows: 0: All Time(Windows, Linux Only); 90: 90days; 180: 180days; 365: 365days.
        client_data_trend_daily (int | Unset): Retention Configuration of client data trend records(only effective in
            local controller), clientDataTrendDaily should be a value as follows: 1: 1day; 7: 7days; 31: 31days; 60: 60days,
            90: 90days.
    """

    clients_data_enable: bool
    override: bool | Unset = UNSET
    client_data_trend_enable: bool | Unset = UNSET
    client_recognition_enable: bool | Unset = UNSET
    client_health_enable: bool | Unset = UNSET
    known_client: int | Unset = UNSET
    client_history: int | Unset = UNSET
    daily: int | Unset = UNSET
    weekly: int | Unset = UNSET
    portal_auth: int | Unset = UNSET
    log: int | Unset = UNSET
    rogue_ap: int | Unset = UNSET
    wids_data: int | Unset = UNSET
    client_data_trend_daily: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clients_data_enable = self.clients_data_enable

        override = self.override

        client_data_trend_enable = self.client_data_trend_enable

        client_recognition_enable = self.client_recognition_enable

        client_health_enable = self.client_health_enable

        known_client = self.known_client

        client_history = self.client_history

        daily = self.daily

        weekly = self.weekly

        portal_auth = self.portal_auth

        log = self.log

        rogue_ap = self.rogue_ap

        wids_data = self.wids_data

        client_data_trend_daily = self.client_data_trend_daily

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientsDataEnable": clients_data_enable,
            }
        )
        if override is not UNSET:
            field_dict["override"] = override
        if client_data_trend_enable is not UNSET:
            field_dict["clientDataTrendEnable"] = client_data_trend_enable
        if client_recognition_enable is not UNSET:
            field_dict["clientRecognitionEnable"] = client_recognition_enable
        if client_health_enable is not UNSET:
            field_dict["clientHealthEnable"] = client_health_enable
        if known_client is not UNSET:
            field_dict["knownClient"] = known_client
        if client_history is not UNSET:
            field_dict["clientHistory"] = client_history
        if daily is not UNSET:
            field_dict["daily"] = daily
        if weekly is not UNSET:
            field_dict["weekly"] = weekly
        if portal_auth is not UNSET:
            field_dict["portalAuth"] = portal_auth
        if log is not UNSET:
            field_dict["log"] = log
        if rogue_ap is not UNSET:
            field_dict["rogueAp"] = rogue_ap
        if wids_data is not UNSET:
            field_dict["widsData"] = wids_data
        if client_data_trend_daily is not UNSET:
            field_dict["clientDataTrendDaily"] = client_data_trend_daily

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        clients_data_enable = d.pop("clientsDataEnable")

        override = d.pop("override", UNSET)

        client_data_trend_enable = d.pop("clientDataTrendEnable", UNSET)

        client_recognition_enable = d.pop("clientRecognitionEnable", UNSET)

        client_health_enable = d.pop("clientHealthEnable", UNSET)

        known_client = d.pop("knownClient", UNSET)

        client_history = d.pop("clientHistory", UNSET)

        daily = d.pop("daily", UNSET)

        weekly = d.pop("weekly", UNSET)

        portal_auth = d.pop("portalAuth", UNSET)

        log = d.pop("log", UNSET)

        rogue_ap = d.pop("rogueAp", UNSET)

        wids_data = d.pop("widsData", UNSET)

        client_data_trend_daily = d.pop("clientDataTrendDaily", UNSET)

        modify_history_retention_open_api_vo = cls(
            clients_data_enable=clients_data_enable,
            override=override,
            client_data_trend_enable=client_data_trend_enable,
            client_recognition_enable=client_recognition_enable,
            client_health_enable=client_health_enable,
            known_client=known_client,
            client_history=client_history,
            daily=daily,
            weekly=weekly,
            portal_auth=portal_auth,
            log=log,
            rogue_ap=rogue_ap,
            wids_data=wids_data,
            client_data_trend_daily=client_data_trend_daily,
        )

        modify_history_retention_open_api_vo.additional_properties = d
        return modify_history_retention_open_api_vo

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
