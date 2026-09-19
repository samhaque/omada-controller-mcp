from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_copy_result_vo import SiteCopyResultVO


T = TypeVar("T", bound="CopySiteTemplateOpenApiResultVO")


@_attrs_define
class CopySiteTemplateOpenApiResultVO:
    """
    Attributes:
        success_num (int | Unset): Number of successful copies.
        fail_num (int | Unset): Number of failed copies.
        error_customers (list[SiteCopyResultVO] | Unset): Copy failed customer related information.
    """

    success_num: int | Unset = UNSET
    fail_num: int | Unset = UNSET
    error_customers: list[SiteCopyResultVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_num = self.success_num

        fail_num = self.fail_num

        error_customers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.error_customers, Unset):
            error_customers = []
            for error_customers_item_data in self.error_customers:
                error_customers_item = error_customers_item_data.to_dict()
                error_customers.append(error_customers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_num is not UNSET:
            field_dict["successNum"] = success_num
        if fail_num is not UNSET:
            field_dict["failNum"] = fail_num
        if error_customers is not UNSET:
            field_dict["errorCustomers"] = error_customers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_copy_result_vo import SiteCopyResultVO

        d = dict(src_dict)
        success_num = d.pop("successNum", UNSET)

        fail_num = d.pop("failNum", UNSET)

        _error_customers = d.pop("errorCustomers", UNSET)
        error_customers: list[SiteCopyResultVO] | Unset = UNSET
        if _error_customers is not UNSET:
            error_customers = []
            for error_customers_item_data in _error_customers:
                error_customers_item = SiteCopyResultVO.from_dict(
                    error_customers_item_data
                )

                error_customers.append(error_customers_item)

        copy_site_template_open_api_result_vo = cls(
            success_num=success_num,
            fail_num=fail_num,
            error_customers=error_customers,
        )

        copy_site_template_open_api_result_vo.additional_properties = d
        return copy_site_template_open_api_result_vo

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
