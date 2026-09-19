from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isp_result_open_api_vo import IspResultOpenApiVO


T = TypeVar("T", bound="IspScanResultOpenApiVO")


@_attrs_define
class IspScanResultOpenApiVO:
    """
    Attributes:
        status (int | Unset): The status of the band scan: 0 - Failed, 1 - Succeeded, 2 - Scanning.
        isp_list (list[IspResultOpenApiVO] | Unset): The list of the isp, contains the ISP name and the ID and the state
            of the ISP.
    """

    status: int | Unset = UNSET
    isp_list: list[IspResultOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        isp_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.isp_list, Unset):
            isp_list = []
            for isp_list_item_data in self.isp_list:
                isp_list_item = isp_list_item_data.to_dict()
                isp_list.append(isp_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if isp_list is not UNSET:
            field_dict["ispList"] = isp_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.isp_result_open_api_vo import IspResultOpenApiVO

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        _isp_list = d.pop("ispList", UNSET)
        isp_list: list[IspResultOpenApiVO] | Unset = UNSET
        if _isp_list is not UNSET:
            isp_list = []
            for isp_list_item_data in _isp_list:
                isp_list_item = IspResultOpenApiVO.from_dict(isp_list_item_data)

                isp_list.append(isp_list_item)

        isp_scan_result_open_api_vo = cls(
            status=status,
            isp_list=isp_list,
        )

        isp_scan_result_open_api_vo.additional_properties = d
        return isp_scan_result_open_api_vo

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
