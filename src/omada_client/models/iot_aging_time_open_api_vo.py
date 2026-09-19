from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="IotAgingTimeOpenApiVO")


@_attrs_define
class IotAgingTimeOpenApiVO:
    """
    Attributes:
        aging_time_iot_aging_time (int): The system automatically removes a device's registry entry if no data reports
            are received within a predefined aging period.<br/>When format = 0, The parameter aging time should be within
            the range of 30-86400.<br/>When format = 1, The parameter aging time should be within the range of
            1-1440.<br/>When format = 2, The parameter aging time should be within the range of 1-24.<br/>
        format_iot_aging_time (int): The parameter [format] should be a value as follows: [0:second 1:minute; 2:hour]
    """

    aging_time_iot_aging_time: int
    format_iot_aging_time: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aging_time_iot_aging_time = self.aging_time_iot_aging_time

        format_iot_aging_time = self.format_iot_aging_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agingTime_iotAgingTime": aging_time_iot_aging_time,
                "format_iotAgingTime": format_iot_aging_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        aging_time_iot_aging_time = d.pop("agingTime_iotAgingTime")

        format_iot_aging_time = d.pop("format_iotAgingTime")

        iot_aging_time_open_api_vo = cls(
            aging_time_iot_aging_time=aging_time_iot_aging_time,
            format_iot_aging_time=format_iot_aging_time,
        )

        iot_aging_time_open_api_vo.additional_properties = d
        return iot_aging_time_open_api_vo

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
