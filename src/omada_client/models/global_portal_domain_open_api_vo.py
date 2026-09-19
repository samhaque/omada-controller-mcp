from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalPortalDomainOpenApiVO")


@_attrs_define
class GlobalPortalDomainOpenApiVO:
    """
    Attributes:
        auto_refresh (bool | Unset): Whether Portal URL enable Auto Refresh
        url (str | Unset): Portal URL, valid when parameter [autoRefresh] is false
    """

    auto_refresh: bool | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_refresh = self.auto_refresh

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_refresh is not UNSET:
            field_dict["autoRefresh"] = auto_refresh
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        auto_refresh = d.pop("autoRefresh", UNSET)

        url = d.pop("url", UNSET)

        global_portal_domain_open_api_vo = cls(
            auto_refresh=auto_refresh,
            url=url,
        )

        global_portal_domain_open_api_vo.additional_properties = d
        return global_portal_domain_open_api_vo

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
