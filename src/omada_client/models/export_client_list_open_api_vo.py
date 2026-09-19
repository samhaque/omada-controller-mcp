from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_api_query_data_vo import OpenApiQueryDataVO


T = TypeVar("T", bound="ExportClientListOpenApiVO")


@_attrs_define
class ExportClientListOpenApiVO:
    """
    Attributes:
        site_ids (list[str]): IDs of the site of the data to be exported.
        mode (int): Export columns mode. 0：All Columns  1: CurrentDisplayColumns.
        format_ (int): Format of file exported.0: CSV 1: XLSX
        clients_display (list[str] | Unset): The information of client list for export.
        query_data_vo (OpenApiQueryDataVO | Unset):
    """

    site_ids: list[str]
    mode: int
    format_: int
    clients_display: list[str] | Unset = UNSET
    query_data_vo: OpenApiQueryDataVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_ids = self.site_ids

        mode = self.mode

        format_ = self.format_

        clients_display: list[str] | Unset = UNSET
        if not isinstance(self.clients_display, Unset):
            clients_display = self.clients_display

        query_data_vo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_data_vo, Unset):
            query_data_vo = self.query_data_vo.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteIds": site_ids,
                "mode": mode,
                "format": format_,
            }
        )
        if clients_display is not UNSET:
            field_dict["clientsDisplay"] = clients_display
        if query_data_vo is not UNSET:
            field_dict["queryDataVO"] = query_data_vo

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.open_api_query_data_vo import OpenApiQueryDataVO

        d = dict(src_dict)
        site_ids = cast(list[str], d.pop("siteIds"))

        mode = d.pop("mode")

        format_ = d.pop("format")

        clients_display = cast(list[str], d.pop("clientsDisplay", UNSET))

        _query_data_vo = d.pop("queryDataVO", UNSET)
        query_data_vo: OpenApiQueryDataVO | Unset
        if isinstance(_query_data_vo, Unset):
            query_data_vo = UNSET
        else:
            query_data_vo = OpenApiQueryDataVO.from_dict(_query_data_vo)

        export_client_list_open_api_vo = cls(
            site_ids=site_ids,
            mode=mode,
            format_=format_,
            clients_display=clients_display,
            query_data_vo=query_data_vo,
        )

        export_client_list_open_api_vo.additional_properties = d
        return export_client_list_open_api_vo

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
