from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_site_client_export_open_api_vo_clients_display_override import (
        MultiSiteClientExportOpenApiVOClientsDisplayOverride,
    )


T = TypeVar("T", bound="MultiSiteClientExportOpenApiVO")


@_attrs_define
class MultiSiteClientExportOpenApiVO:
    """
    Attributes:
        format_ (int): Format should be a value as follows: 0: csv; 1: xlsx.
        mode (int): Export columns mode. 0：All Columns  1: CurrentDisplayColumns.
        select_type (str): Select type of the sites of clients to export. include: include selected sites, exclude: all
            but exclude selected sites, all: include all sites.
        site_ids (list[str]): List of site id to export. SiteIds should contains at least 1 element when [selectType] is
            "include".
        clients_display (list[str] | Unset): The information of client list for export.
        clients_display_override (MultiSiteClientExportOpenApiVOClientsDisplayOverride | Unset): Override the export
            columns for given siteIds.
    """

    format_: int
    mode: int
    select_type: str
    site_ids: list[str]
    clients_display: list[str] | Unset = UNSET
    clients_display_override: (
        MultiSiteClientExportOpenApiVOClientsDisplayOverride | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        mode = self.mode

        select_type = self.select_type

        site_ids = self.site_ids

        clients_display: list[str] | Unset = UNSET
        if not isinstance(self.clients_display, Unset):
            clients_display = self.clients_display

        clients_display_override: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clients_display_override, Unset):
            clients_display_override = self.clients_display_override.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "mode": mode,
                "selectType": select_type,
                "siteIds": site_ids,
            }
        )
        if clients_display is not UNSET:
            field_dict["clientsDisplay"] = clients_display
        if clients_display_override is not UNSET:
            field_dict["clientsDisplayOverride"] = clients_display_override

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multi_site_client_export_open_api_vo_clients_display_override import (
            MultiSiteClientExportOpenApiVOClientsDisplayOverride,
        )

        d = dict(src_dict)
        format_ = d.pop("format")

        mode = d.pop("mode")

        select_type = d.pop("selectType")

        site_ids = cast(list[str], d.pop("siteIds"))

        clients_display = cast(list[str], d.pop("clientsDisplay", UNSET))

        _clients_display_override = d.pop("clientsDisplayOverride", UNSET)
        clients_display_override: (
            MultiSiteClientExportOpenApiVOClientsDisplayOverride | Unset
        )
        if isinstance(_clients_display_override, Unset):
            clients_display_override = UNSET
        else:
            clients_display_override = (
                MultiSiteClientExportOpenApiVOClientsDisplayOverride.from_dict(
                    _clients_display_override
                )
            )

        multi_site_client_export_open_api_vo = cls(
            format_=format_,
            mode=mode,
            select_type=select_type,
            site_ids=site_ids,
            clients_display=clients_display,
            clients_display_override=clients_display_override,
        )

        multi_site_client_export_open_api_vo.additional_properties = d
        return multi_site_client_export_open_api_vo

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
