from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApDensityItemOpenApiVO")


@_attrs_define
class ApDensityItemOpenApiVO:
    """The trend of ap density metrics displayed on the WIFI Dashboard page.

    Attributes:
        time (int | Unset): Time(unit:ms)
        dense_ap_num (int | Unset): The number of dense Ap.
        dense_ap_percent (int | Unset): The percent of dense Ap.
        moderate_ap_num (int | Unset): The number of moderate Ap.
        moderate_ap_percent (int | Unset): The percent of moderate Ap.
        sparse_ap_num (int | Unset): The number of sparse Ap.
        sparse_ap_percent (int | Unset): The percent of sparse Ap.
    """

    time: int | Unset = UNSET
    dense_ap_num: int | Unset = UNSET
    dense_ap_percent: int | Unset = UNSET
    moderate_ap_num: int | Unset = UNSET
    moderate_ap_percent: int | Unset = UNSET
    sparse_ap_num: int | Unset = UNSET
    sparse_ap_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        dense_ap_num = self.dense_ap_num

        dense_ap_percent = self.dense_ap_percent

        moderate_ap_num = self.moderate_ap_num

        moderate_ap_percent = self.moderate_ap_percent

        sparse_ap_num = self.sparse_ap_num

        sparse_ap_percent = self.sparse_ap_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if dense_ap_num is not UNSET:
            field_dict["denseApNum"] = dense_ap_num
        if dense_ap_percent is not UNSET:
            field_dict["denseApPercent"] = dense_ap_percent
        if moderate_ap_num is not UNSET:
            field_dict["moderateApNum"] = moderate_ap_num
        if moderate_ap_percent is not UNSET:
            field_dict["moderateApPercent"] = moderate_ap_percent
        if sparse_ap_num is not UNSET:
            field_dict["sparseApNum"] = sparse_ap_num
        if sparse_ap_percent is not UNSET:
            field_dict["sparseApPercent"] = sparse_ap_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        dense_ap_num = d.pop("denseApNum", UNSET)

        dense_ap_percent = d.pop("denseApPercent", UNSET)

        moderate_ap_num = d.pop("moderateApNum", UNSET)

        moderate_ap_percent = d.pop("moderateApPercent", UNSET)

        sparse_ap_num = d.pop("sparseApNum", UNSET)

        sparse_ap_percent = d.pop("sparseApPercent", UNSET)

        ap_density_item_open_api_vo = cls(
            time=time,
            dense_ap_num=dense_ap_num,
            dense_ap_percent=dense_ap_percent,
            moderate_ap_num=moderate_ap_num,
            moderate_ap_percent=moderate_ap_percent,
            sparse_ap_num=sparse_ap_num,
            sparse_ap_percent=sparse_ap_percent,
        )

        ap_density_item_open_api_vo.additional_properties = d
        return ap_density_item_open_api_vo

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
