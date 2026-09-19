from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.speed_test_v2_result_item_vo import SpeedTestV2ResultItemVO


T = TypeVar("T", bound="SpeedTestV2ResultVO")


@_attrs_define
class SpeedTestV2ResultVO:
    """
    Attributes:
        status (int | Unset):
        port_speed_results (list[SpeedTestV2ResultItemVO] | Unset):
    """

    status: int | Unset = UNSET
    port_speed_results: list[SpeedTestV2ResultItemVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        port_speed_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_speed_results, Unset):
            port_speed_results = []
            for port_speed_results_item_data in self.port_speed_results:
                port_speed_results_item = port_speed_results_item_data.to_dict()
                port_speed_results.append(port_speed_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if port_speed_results is not UNSET:
            field_dict["portSpeedResults"] = port_speed_results

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.speed_test_v2_result_item_vo import (
            SpeedTestV2ResultItemVO,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        _port_speed_results = d.pop("portSpeedResults", UNSET)
        port_speed_results: list[SpeedTestV2ResultItemVO] | Unset = UNSET
        if _port_speed_results is not UNSET:
            port_speed_results = []
            for port_speed_results_item_data in _port_speed_results:
                port_speed_results_item = SpeedTestV2ResultItemVO.from_dict(
                    port_speed_results_item_data
                )

                port_speed_results.append(port_speed_results_item)

        speed_test_v2_result_vo = cls(
            status=status,
            port_speed_results=port_speed_results,
        )

        speed_test_v2_result_vo.additional_properties = d
        return speed_test_v2_result_vo

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
