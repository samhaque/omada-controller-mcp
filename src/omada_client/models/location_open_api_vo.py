from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isp_open_api_vo import IspOpenApiVO


T = TypeVar("T", bound="LocationOpenApiVO")


@_attrs_define
class LocationOpenApiVO:
    """Location and ISP info, including index and name.

    Attributes:
        index (int): Location index
        name (str): Location name
        isp_info (list[IspOpenApiVO] | Unset): ISP info in the location, including index and name
    """

    index: int
    name: str
    isp_info: list[IspOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        name = self.name

        isp_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.isp_info, Unset):
            isp_info = []
            for isp_info_item_data in self.isp_info:
                isp_info_item = isp_info_item_data.to_dict()
                isp_info.append(isp_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "name": name,
            }
        )
        if isp_info is not UNSET:
            field_dict["ispInfo"] = isp_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.isp_open_api_vo import IspOpenApiVO

        d = dict(src_dict)
        index = d.pop("index")

        name = d.pop("name")

        _isp_info = d.pop("ispInfo", UNSET)
        isp_info: list[IspOpenApiVO] | Unset = UNSET
        if _isp_info is not UNSET:
            isp_info = []
            for isp_info_item_data in _isp_info:
                isp_info_item = IspOpenApiVO.from_dict(isp_info_item_data)

                isp_info.append(isp_info_item)

        location_open_api_vo = cls(
            index=index,
            name=name,
            isp_info=isp_info,
        )

        location_open_api_vo.additional_properties = d
        return location_open_api_vo

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
