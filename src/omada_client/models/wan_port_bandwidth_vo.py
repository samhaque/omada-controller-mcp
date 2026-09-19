from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_bandwidth_vo import PortBandwidthVO


T = TypeVar("T", bound="WanPortBandwidthVO")


@_attrs_define
class WanPortBandwidthVO:
    """
    Attributes:
        bandwidths (list[PortBandwidthVO] | Unset): Set port bandwidth info list.
    """

    bandwidths: list[PortBandwidthVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bandwidths: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bandwidths, Unset):
            bandwidths = []
            for bandwidths_item_data in self.bandwidths:
                bandwidths_item = bandwidths_item_data.to_dict()
                bandwidths.append(bandwidths_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bandwidths is not UNSET:
            field_dict["bandwidths"] = bandwidths

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_bandwidth_vo import PortBandwidthVO

        d = dict(src_dict)
        _bandwidths = d.pop("bandwidths", UNSET)
        bandwidths: list[PortBandwidthVO] | Unset = UNSET
        if _bandwidths is not UNSET:
            bandwidths = []
            for bandwidths_item_data in _bandwidths:
                bandwidths_item = PortBandwidthVO.from_dict(bandwidths_item_data)

                bandwidths.append(bandwidths_item)

        wan_port_bandwidth_vo = cls(
            bandwidths=bandwidths,
        )

        wan_port_bandwidth_vo.additional_properties = d
        return wan_port_bandwidth_vo

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
