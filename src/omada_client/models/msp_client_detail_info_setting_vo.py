from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspClientDetailInfoSettingVO")


@_attrs_define
class MspClientDetailInfoSettingVO:
    """
    Attributes:
        client_health_enable (bool | Unset): Whether client health is enabled. When enabled, client health data will be
            recorded, which may consume a significant amount of storage space.
        client_history_enable (bool | Unset): Whether client history is enabled. When enabled, client history, client
            logs will be recorded. This will occupy much storage space.
        client_data_trend_enable (bool | Unset): Whether client data trend record is enabled. When enabled, client trend
            statistics and charts will be retained, which will take up lots of storage space.
    """

    client_health_enable: bool | Unset = UNSET
    client_history_enable: bool | Unset = UNSET
    client_data_trend_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_health_enable = self.client_health_enable

        client_history_enable = self.client_history_enable

        client_data_trend_enable = self.client_data_trend_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_health_enable is not UNSET:
            field_dict["clientHealthEnable"] = client_health_enable
        if client_history_enable is not UNSET:
            field_dict["clientHistoryEnable"] = client_history_enable
        if client_data_trend_enable is not UNSET:
            field_dict["clientDataTrendEnable"] = client_data_trend_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_health_enable = d.pop("clientHealthEnable", UNSET)

        client_history_enable = d.pop("clientHistoryEnable", UNSET)

        client_data_trend_enable = d.pop("clientDataTrendEnable", UNSET)

        msp_client_detail_info_setting_vo = cls(
            client_health_enable=client_health_enable,
            client_history_enable=client_history_enable,
            client_data_trend_enable=client_data_trend_enable,
        )

        msp_client_detail_info_setting_vo.additional_properties = d
        return msp_client_detail_info_setting_vo

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
