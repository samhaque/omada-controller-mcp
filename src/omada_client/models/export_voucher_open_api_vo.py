from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_api_query_data_vo import OpenApiQueryDataVO


T = TypeVar("T", bound="ExportVoucherOpenApiVO")


@_attrs_define
class ExportVoucherOpenApiVO:
    """
    Attributes:
        format_ (int): Export file format, should be a value as follows: 0: csv, 1: xlsx
        type_ (int): Select type. It should be a value as follows: 0: Represents selecting all voucher groups, this
            selection does not pass parameter [groupIds]. 1: Parameter [groupIds] includes the IDs of the voucher groups to
            be selected. 2: Parameter [groupIds] includes the IDs of the voucher groups not to be selected
        query_data (OpenApiQueryDataVO | Unset):
        group_ids (list[str] | Unset): ID list of voucher groups. Voucher group can be created using 'Create Voucher
            Group' interface, and Voucher Group ID can be obtained from 'Get Voucher Group list' interface
    """

    format_: int
    type_: int
    query_data: OpenApiQueryDataVO | Unset = UNSET
    group_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        type_ = self.type_

        query_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_data, Unset):
            query_data = self.query_data.to_dict()

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "type": type_,
            }
        )
        if query_data is not UNSET:
            field_dict["queryData"] = query_data
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.open_api_query_data_vo import OpenApiQueryDataVO

        d = dict(src_dict)
        format_ = d.pop("format")

        type_ = d.pop("type")

        _query_data = d.pop("queryData", UNSET)
        query_data: OpenApiQueryDataVO | Unset
        if isinstance(_query_data, Unset):
            query_data = UNSET
        else:
            query_data = OpenApiQueryDataVO.from_dict(_query_data)

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        export_voucher_open_api_vo = cls(
            format_=format_,
            type_=type_,
            query_data=query_data,
            group_ids=group_ids,
        )

        export_voucher_open_api_vo.additional_properties = d
        return export_voucher_open_api_vo

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
