from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_open_api_vo import LocationOpenApiVO


T = TypeVar("T", bound="LocationAndIspInfoOpenApiVO")


@_attrs_define
class LocationAndIspInfoOpenApiVO:
    """
    Attributes:
        location_and_isp (list[LocationOpenApiVO] | Unset): Location and ISP info, including index and name.
    """

    location_and_isp: list[LocationOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_and_isp: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.location_and_isp, Unset):
            location_and_isp = []
            for location_and_isp_item_data in self.location_and_isp:
                location_and_isp_item = location_and_isp_item_data.to_dict()
                location_and_isp.append(location_and_isp_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_and_isp is not UNSET:
            field_dict["locationAndIsp"] = location_and_isp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.location_open_api_vo import LocationOpenApiVO

        d = dict(src_dict)
        _location_and_isp = d.pop("locationAndIsp", UNSET)
        location_and_isp: list[LocationOpenApiVO] | Unset = UNSET
        if _location_and_isp is not UNSET:
            location_and_isp = []
            for location_and_isp_item_data in _location_and_isp:
                location_and_isp_item = LocationOpenApiVO.from_dict(
                    location_and_isp_item_data
                )

                location_and_isp.append(location_and_isp_item)

        location_and_isp_info_open_api_vo = cls(
            location_and_isp=location_and_isp,
        )

        location_and_isp_info_open_api_vo.additional_properties = d
        return location_and_isp_info_open_api_vo

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
