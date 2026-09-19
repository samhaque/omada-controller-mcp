from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="OptimizationStrategy")


@_attrs_define
class OptimizationStrategy:
    """
    Attributes:
        optimization_strategy (int): Strategy of WLAN Optimization. 0: Global Optimization. 1: Optimization Adjustment,
            when WLAN Optimization is performed for the first time, that is, when API [get RF Planning Deploy History]
            returns ‘true’, this option is equivalent to Global Optimization.
    """

    optimization_strategy: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        optimization_strategy = self.optimization_strategy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "optimizationStrategy": optimization_strategy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        optimization_strategy = d.pop("optimizationStrategy")

        optimization_strategy = cls(
            optimization_strategy=optimization_strategy,
        )

        optimization_strategy.additional_properties = d
        return optimization_strategy

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
