from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.imported_portal_page_res_open_api_vo import (
        ImportedPortalPageResOpenApiVO,
    )
    from ..models.portal_customize_res_open_api_vo import PortalCustomizeResOpenApiVO


T = TypeVar("T", bound="PortalCustomizationPageResOpenApiVO")


@_attrs_define
class PortalCustomizationPageResOpenApiVO:
    """
    Attributes:
        page_type (int | Unset): Page type, should be a value as follows: 1: Use default page, 2: use uploaded page.
            Required when portal auth type is not 4: External Portal Server
        portal_customize (PortalCustomizeResOpenApiVO | Unset): Portal customize setting, required when parameter
            [pageType] is 1
        imported_portal_page (ImportedPortalPageResOpenApiVO | Unset):
    """

    page_type: int | Unset = UNSET
    portal_customize: PortalCustomizeResOpenApiVO | Unset = UNSET
    imported_portal_page: ImportedPortalPageResOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_type = self.page_type

        portal_customize: dict[str, Any] | Unset = UNSET
        if not isinstance(self.portal_customize, Unset):
            portal_customize = self.portal_customize.to_dict()

        imported_portal_page: dict[str, Any] | Unset = UNSET
        if not isinstance(self.imported_portal_page, Unset):
            imported_portal_page = self.imported_portal_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_type is not UNSET:
            field_dict["pageType"] = page_type
        if portal_customize is not UNSET:
            field_dict["portalCustomize"] = portal_customize
        if imported_portal_page is not UNSET:
            field_dict["importedPortalPage"] = imported_portal_page

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.imported_portal_page_res_open_api_vo import (
            ImportedPortalPageResOpenApiVO,
        )
        from ..models.portal_customize_res_open_api_vo import (
            PortalCustomizeResOpenApiVO,
        )

        d = dict(src_dict)
        page_type = d.pop("pageType", UNSET)

        _portal_customize = d.pop("portalCustomize", UNSET)
        portal_customize: PortalCustomizeResOpenApiVO | Unset
        if isinstance(_portal_customize, Unset):
            portal_customize = UNSET
        else:
            portal_customize = PortalCustomizeResOpenApiVO.from_dict(_portal_customize)

        _imported_portal_page = d.pop("importedPortalPage", UNSET)
        imported_portal_page: ImportedPortalPageResOpenApiVO | Unset
        if isinstance(_imported_portal_page, Unset):
            imported_portal_page = UNSET
        else:
            imported_portal_page = ImportedPortalPageResOpenApiVO.from_dict(
                _imported_portal_page
            )

        portal_customization_page_res_open_api_vo = cls(
            page_type=page_type,
            portal_customize=portal_customize,
            imported_portal_page=imported_portal_page,
        )

        portal_customization_page_res_open_api_vo.additional_properties = d
        return portal_customization_page_res_open_api_vo

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
