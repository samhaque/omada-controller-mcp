from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_event_setting_open_api_vo_params import (
        AnomalyEventSettingOpenApiVOParams,
    )


T = TypeVar("T", bound="AnomalyEventSettingOpenApiVO")


@_attrs_define
class AnomalyEventSettingOpenApiVO:
    """
    Attributes:
        anomaly_code (str | Unset): For the values of Anomaly event code, refer to section 5.7.2.1 of the Open API
            Access Example: 01001001.
        category (int | Unset): Anomaly event category, it should be a value as follows:11:Access, 12:Authentication,
            13:Roaming, 14:Wireless Network, 15:Wired Network, 16:Link, 17:WAN and Services, 18:Device Status, 19:Security,
            example: 11 Or 12,13,14 Example: 11.
        enable (bool | Unset): Whether to detect anomaly events Example: False.
        level (int | Unset): Anomaly event level, it should be a value as follows: 0:Critical, 1:Error, 2:Warning, 3:
            Info Example: 1.
        params (AnomalyEventSettingOpenApiVOParams | Unset): For the values of Anomaly event params, refer to section
            5.7.2.1 of the Open API Access Example: {'offlineCount': 2}.
        object_type (str | Unset): Device type Example: gateway.
    """

    anomaly_code: str | Unset = UNSET
    category: int | Unset = UNSET
    enable: bool | Unset = UNSET
    level: int | Unset = UNSET
    params: AnomalyEventSettingOpenApiVOParams | Unset = UNSET
    object_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly_code = self.anomaly_code

        category = self.category

        enable = self.enable

        level = self.level

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        object_type = self.object_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly_code is not UNSET:
            field_dict["anomalyCode"] = anomaly_code
        if category is not UNSET:
            field_dict["category"] = category
        if enable is not UNSET:
            field_dict["enable"] = enable
        if level is not UNSET:
            field_dict["level"] = level
        if params is not UNSET:
            field_dict["params"] = params
        if object_type is not UNSET:
            field_dict["objectType"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_event_setting_open_api_vo_params import (
            AnomalyEventSettingOpenApiVOParams,
        )

        d = dict(src_dict)
        anomaly_code = d.pop("anomalyCode", UNSET)

        category = d.pop("category", UNSET)

        enable = d.pop("enable", UNSET)

        level = d.pop("level", UNSET)

        _params = d.pop("params", UNSET)
        params: AnomalyEventSettingOpenApiVOParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = AnomalyEventSettingOpenApiVOParams.from_dict(_params)

        object_type = d.pop("objectType", UNSET)

        anomaly_event_setting_open_api_vo = cls(
            anomaly_code=anomaly_code,
            category=category,
            enable=enable,
            level=level,
            params=params,
            object_type=object_type,
        )

        anomaly_event_setting_open_api_vo.additional_properties = d
        return anomaly_event_setting_open_api_vo

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
