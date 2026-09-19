from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpecifiedOptionOpenApiVO")


@_attrs_define
class SpecifiedOptionOpenApiVO:
    """Specified option of the attack defense setting.

    Attributes:
        security_option_enable (bool | Unset): Security Option of the attack defense setting.
        record_route_enable (bool | Unset): Record Route Option of the attack defense setting.
        stream_enable (bool | Unset): Stream Option of the attack defense setting.
        timestamp_enable (bool | Unset): Timestamp Option of the attack defense setting.
        no_operation_enable (bool | Unset): No Operation Option of the attack defense setting.
    """

    security_option_enable: bool | Unset = UNSET
    record_route_enable: bool | Unset = UNSET
    stream_enable: bool | Unset = UNSET
    timestamp_enable: bool | Unset = UNSET
    no_operation_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        security_option_enable = self.security_option_enable

        record_route_enable = self.record_route_enable

        stream_enable = self.stream_enable

        timestamp_enable = self.timestamp_enable

        no_operation_enable = self.no_operation_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if security_option_enable is not UNSET:
            field_dict["securityOptionEnable"] = security_option_enable
        if record_route_enable is not UNSET:
            field_dict["recordRouteEnable"] = record_route_enable
        if stream_enable is not UNSET:
            field_dict["streamEnable"] = stream_enable
        if timestamp_enable is not UNSET:
            field_dict["timestampEnable"] = timestamp_enable
        if no_operation_enable is not UNSET:
            field_dict["noOperationEnable"] = no_operation_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        security_option_enable = d.pop("securityOptionEnable", UNSET)

        record_route_enable = d.pop("recordRouteEnable", UNSET)

        stream_enable = d.pop("streamEnable", UNSET)

        timestamp_enable = d.pop("timestampEnable", UNSET)

        no_operation_enable = d.pop("noOperationEnable", UNSET)

        specified_option_open_api_vo = cls(
            security_option_enable=security_option_enable,
            record_route_enable=record_route_enable,
            stream_enable=stream_enable,
            timestamp_enable=timestamp_enable,
            no_operation_enable=no_operation_enable,
        )

        specified_option_open_api_vo.additional_properties = d
        return specified_option_open_api_vo

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
