from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voucher_summary_open_api_vo import VoucherSummaryOpenApiVO
    from ..models.voucher_usage_open_api_vo import VoucherUsageOpenApiVO


T = TypeVar("T", bound="VoucherStatisticsHistoryOpenApiVO")


@_attrs_define
class VoucherStatisticsHistoryOpenApiVO:
    """
    Attributes:
        summary (VoucherSummaryOpenApiVO | Unset): Summary of all created vouchers, including deleted vouchers
        usage (list[VoucherUsageOpenApiVO] | Unset): Data points of vouchers
    """

    summary: VoucherSummaryOpenApiVO | Unset = UNSET
    usage: list[VoucherUsageOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        usage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = []
            for usage_item_data in self.usage:
                usage_item = usage_item_data.to_dict()
                usage.append(usage_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.voucher_summary_open_api_vo import (
            VoucherSummaryOpenApiVO,
        )
        from ..models.voucher_usage_open_api_vo import (
            VoucherUsageOpenApiVO,
        )

        d = dict(src_dict)
        _summary = d.pop("summary", UNSET)
        summary: VoucherSummaryOpenApiVO | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = VoucherSummaryOpenApiVO.from_dict(_summary)

        _usage = d.pop("usage", UNSET)
        usage: list[VoucherUsageOpenApiVO] | Unset = UNSET
        if _usage is not UNSET:
            usage = []
            for usage_item_data in _usage:
                usage_item = VoucherUsageOpenApiVO.from_dict(usage_item_data)

                usage.append(usage_item)

        voucher_statistics_history_open_api_vo = cls(
            summary=summary,
            usage=usage,
        )

        voucher_statistics_history_open_api_vo.additional_properties = d
        return voucher_statistics_history_open_api_vo

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
