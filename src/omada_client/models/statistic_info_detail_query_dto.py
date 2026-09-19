from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="StatisticInfoDetailQueryDTO")


@_attrs_define
class StatisticInfoDetailQueryDTO:
    """
    Attributes:
        service_port_index (int): ID of service port.ServicePortIndex should be within the range of 1 to 8100
    """

    service_port_index: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_port_index = self.service_port_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "servicePortIndex": service_port_index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_port_index = d.pop("servicePortIndex")

        statistic_info_detail_query_dto = cls(
            service_port_index=service_port_index,
        )

        statistic_info_detail_query_dto.additional_properties = d
        return statistic_info_detail_query_dto

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
