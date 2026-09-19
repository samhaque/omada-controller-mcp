from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalCandidatesOpenApiVO")


@_attrs_define
class PortalCandidatesOpenApiVO:
    """
    Attributes:
        all_portal (bool): Whether portal privilege is true
        portal_ids (list[str] | Unset): Portal IDs of the requested SSIDs and networks.
    """

    all_portal: bool
    portal_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_portal = self.all_portal

        portal_ids: list[str] | Unset = UNSET
        if not isinstance(self.portal_ids, Unset):
            portal_ids = self.portal_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allPortal": all_portal,
            }
        )
        if portal_ids is not UNSET:
            field_dict["portalIds"] = portal_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_portal = d.pop("allPortal")

        portal_ids = cast(list[str], d.pop("portalIds", UNSET))

        portal_candidates_open_api_vo = cls(
            all_portal=all_portal,
            portal_ids=portal_ids,
        )

        portal_candidates_open_api_vo.additional_properties = d
        return portal_candidates_open_api_vo

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
