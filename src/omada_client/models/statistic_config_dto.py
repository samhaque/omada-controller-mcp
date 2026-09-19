from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.statistic_config_dto_auto_refresh import StatisticConfigDTOAutoRefresh
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatisticConfigDTO")


@_attrs_define
class StatisticConfigDTO:
    """
    Attributes:
        auto_refresh (StatisticConfigDTOAutoRefresh | Unset): AutoRefresh should be a value as follows:DISABLE,ENABLE
        refresh_interval (int | Unset): RefreshInterval should be within the range of 3 to 300
    """

    auto_refresh: StatisticConfigDTOAutoRefresh | Unset = UNSET
    refresh_interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_refresh: str | Unset = UNSET
        if not isinstance(self.auto_refresh, Unset):
            auto_refresh = self.auto_refresh.value

        refresh_interval = self.refresh_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_refresh is not UNSET:
            field_dict["autoRefresh"] = auto_refresh
        if refresh_interval is not UNSET:
            field_dict["refreshInterval"] = refresh_interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _auto_refresh = d.pop("autoRefresh", UNSET)
        auto_refresh: StatisticConfigDTOAutoRefresh | Unset
        if isinstance(_auto_refresh, Unset):
            auto_refresh = UNSET
        else:
            auto_refresh = StatisticConfigDTOAutoRefresh(_auto_refresh)

        refresh_interval = d.pop("refreshInterval", UNSET)

        statistic_config_dto = cls(
            auto_refresh=auto_refresh,
            refresh_interval=refresh_interval,
        )

        statistic_config_dto.additional_properties = d
        return statistic_config_dto

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
