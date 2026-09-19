from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voucher_summary_open_api_vo import VoucherSummaryOpenApiVO


T = TypeVar("T", bound="AllTimeVoucherSummaryOpenApiVO")


@_attrs_define
class AllTimeVoucherSummaryOpenApiVO:
    """
    Attributes:
        current (VoucherSummaryOpenApiVO | Unset): Summary of all created vouchers, including deleted vouchers
        inuse (VoucherSummaryOpenApiVO | Unset): Summary of all created vouchers, including deleted vouchers
        expired (VoucherSummaryOpenApiVO | Unset): Summary of all created vouchers, including deleted vouchers
        unused (VoucherSummaryOpenApiVO | Unset): Summary of all created vouchers, including deleted vouchers
        created (VoucherSummaryOpenApiVO | Unset): Summary of all created vouchers, including deleted vouchers
        support_voucher_traffic_stat (bool | Unset): Whether the controller support voucher traffic statistics
    """

    current: VoucherSummaryOpenApiVO | Unset = UNSET
    inuse: VoucherSummaryOpenApiVO | Unset = UNSET
    expired: VoucherSummaryOpenApiVO | Unset = UNSET
    unused: VoucherSummaryOpenApiVO | Unset = UNSET
    created: VoucherSummaryOpenApiVO | Unset = UNSET
    support_voucher_traffic_stat: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current, Unset):
            current = self.current.to_dict()

        inuse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inuse, Unset):
            inuse = self.inuse.to_dict()

        expired: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expired, Unset):
            expired = self.expired.to_dict()

        unused: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unused, Unset):
            unused = self.unused.to_dict()

        created: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.to_dict()

        support_voucher_traffic_stat = self.support_voucher_traffic_stat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current is not UNSET:
            field_dict["current"] = current
        if inuse is not UNSET:
            field_dict["inuse"] = inuse
        if expired is not UNSET:
            field_dict["expired"] = expired
        if unused is not UNSET:
            field_dict["unused"] = unused
        if created is not UNSET:
            field_dict["created"] = created
        if support_voucher_traffic_stat is not UNSET:
            field_dict["supportVoucherTrafficStat"] = support_voucher_traffic_stat

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.voucher_summary_open_api_vo import (
            VoucherSummaryOpenApiVO,
        )

        d = dict(src_dict)
        _current = d.pop("current", UNSET)
        current: VoucherSummaryOpenApiVO | Unset
        if isinstance(_current, Unset):
            current = UNSET
        else:
            current = VoucherSummaryOpenApiVO.from_dict(_current)

        _inuse = d.pop("inuse", UNSET)
        inuse: VoucherSummaryOpenApiVO | Unset
        if isinstance(_inuse, Unset):
            inuse = UNSET
        else:
            inuse = VoucherSummaryOpenApiVO.from_dict(_inuse)

        _expired = d.pop("expired", UNSET)
        expired: VoucherSummaryOpenApiVO | Unset
        if isinstance(_expired, Unset):
            expired = UNSET
        else:
            expired = VoucherSummaryOpenApiVO.from_dict(_expired)

        _unused = d.pop("unused", UNSET)
        unused: VoucherSummaryOpenApiVO | Unset
        if isinstance(_unused, Unset):
            unused = UNSET
        else:
            unused = VoucherSummaryOpenApiVO.from_dict(_unused)

        _created = d.pop("created", UNSET)
        created: VoucherSummaryOpenApiVO | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = VoucherSummaryOpenApiVO.from_dict(_created)

        support_voucher_traffic_stat = d.pop("supportVoucherTrafficStat", UNSET)

        all_time_voucher_summary_open_api_vo = cls(
            current=current,
            inuse=inuse,
            expired=expired,
            unused=unused,
            created=created,
            support_voucher_traffic_stat=support_voucher_traffic_stat,
        )

        all_time_voucher_summary_open_api_vo.additional_properties = d
        return all_time_voucher_summary_open_api_vo

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
