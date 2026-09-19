from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_server_range_vo import DhcpServerRangeVO


T = TypeVar("T", bound="DhcpServerForVlanVO")


@_attrs_define
class DhcpServerForVlanVO:
    """
    Attributes:
        ranges (list[DhcpServerRangeVO] | Unset): Dhcp Server Ranges
    """

    ranges: list[DhcpServerRangeVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_server_range_vo import DhcpServerRangeVO

        d = dict(src_dict)
        _ranges = d.pop("ranges", UNSET)
        ranges: list[DhcpServerRangeVO] | Unset = UNSET
        if _ranges is not UNSET:
            ranges = []
            for ranges_item_data in _ranges:
                ranges_item = DhcpServerRangeVO.from_dict(ranges_item_data)

                ranges.append(ranges_item)

        dhcp_server_for_vlan_vo = cls(
            ranges=ranges,
        )

        dhcp_server_for_vlan_vo.additional_properties = d
        return dhcp_server_for_vlan_vo

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
