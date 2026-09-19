from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_connection_summary import ClientConnectionSummary
    from ..models.client_count_statistics_with_time import ClientCountStatisticsWithTime


T = TypeVar("T", bound="ClientConnectionTrend")


@_attrs_define
class ClientConnectionTrend:
    """Client connection trend.

    Attributes:
        client_connection_summary (ClientConnectionSummary | Unset): Summary of client count statistics.
        client_connection_trend (list[ClientCountStatisticsWithTime] | Unset): Client connection trend with time.
    """

    client_connection_summary: ClientConnectionSummary | Unset = UNSET
    client_connection_trend: list[ClientCountStatisticsWithTime] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_connection_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_connection_summary, Unset):
            client_connection_summary = self.client_connection_summary.to_dict()

        client_connection_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_connection_trend, Unset):
            client_connection_trend = []
            for client_connection_trend_item_data in self.client_connection_trend:
                client_connection_trend_item = (
                    client_connection_trend_item_data.to_dict()
                )
                client_connection_trend.append(client_connection_trend_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_connection_summary is not UNSET:
            field_dict["clientConnectionSummary"] = client_connection_summary
        if client_connection_trend is not UNSET:
            field_dict["clientConnectionTrend"] = client_connection_trend

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_connection_summary import (
            ClientConnectionSummary,
        )
        from ..models.client_count_statistics_with_time import (
            ClientCountStatisticsWithTime,
        )

        d = dict(src_dict)
        _client_connection_summary = d.pop("clientConnectionSummary", UNSET)
        client_connection_summary: ClientConnectionSummary | Unset
        if isinstance(_client_connection_summary, Unset):
            client_connection_summary = UNSET
        else:
            client_connection_summary = ClientConnectionSummary.from_dict(
                _client_connection_summary
            )

        _client_connection_trend = d.pop("clientConnectionTrend", UNSET)
        client_connection_trend: list[ClientCountStatisticsWithTime] | Unset = UNSET
        if _client_connection_trend is not UNSET:
            client_connection_trend = []
            for client_connection_trend_item_data in _client_connection_trend:
                client_connection_trend_item = ClientCountStatisticsWithTime.from_dict(
                    client_connection_trend_item_data
                )

                client_connection_trend.append(client_connection_trend_item)

        client_connection_trend = cls(
            client_connection_summary=client_connection_summary,
            client_connection_trend=client_connection_trend,
        )

        client_connection_trend.additional_properties = d
        return client_connection_trend

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
