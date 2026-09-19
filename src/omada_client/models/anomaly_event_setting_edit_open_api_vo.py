from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_event_setting_edit_open_api_vo_params import (
        AnomalyEventSettingEditOpenApiVOParams,
    )


T = TypeVar("T", bound="AnomalyEventSettingEditOpenApiVO")


@_attrs_define
class AnomalyEventSettingEditOpenApiVO:
    """
    Attributes:
        anomaly_code (str): For the values of Anomaly event code, refer to section 5.7.2.1 of the Open API Access
            Example: 01001001.
        enable (bool | Unset): Whether to detect anomaly events Example: False.
        level (int | Unset): Anomaly event level, it should be a value as follows: 0:Critical, 1:Error, 2:Warning, 3:
            Info Example: 1.
        params (AnomalyEventSettingEditOpenApiVOParams | Unset): For the values of Anomaly event params, refer to
            section 5.7.2.1 of the Open API Access Example: {'offlineCount': 2}.
    """

    anomaly_code: str
    enable: bool | Unset = UNSET
    level: int | Unset = UNSET
    params: AnomalyEventSettingEditOpenApiVOParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly_code = self.anomaly_code

        enable = self.enable

        level = self.level

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anomalyCode": anomaly_code,
            }
        )
        if enable is not UNSET:
            field_dict["enable"] = enable
        if level is not UNSET:
            field_dict["level"] = level
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_event_setting_edit_open_api_vo_params import (
            AnomalyEventSettingEditOpenApiVOParams,
        )

        d = dict(src_dict)
        anomaly_code = d.pop("anomalyCode")

        enable = d.pop("enable", UNSET)

        level = d.pop("level", UNSET)

        _params = d.pop("params", UNSET)
        params: AnomalyEventSettingEditOpenApiVOParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = AnomalyEventSettingEditOpenApiVOParams.from_dict(_params)

        anomaly_event_setting_edit_open_api_vo = cls(
            anomaly_code=anomaly_code,
            enable=enable,
            level=level,
            params=params,
        )

        anomaly_event_setting_edit_open_api_vo.additional_properties = d
        return anomaly_event_setting_edit_open_api_vo

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
