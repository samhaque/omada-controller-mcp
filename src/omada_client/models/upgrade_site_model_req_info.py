from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpgradeSiteModelReqInfo")


@_attrs_define
class UpgradeSiteModelReqInfo:
    """
    Attributes:
        site_ids (list[str] | Unset): List collection of siteID
    """

    site_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_ids: list[str] | Unset = UNSET
        if not isinstance(self.site_ids, Unset):
            site_ids = self.site_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_ids is not UNSET:
            field_dict["siteIds"] = site_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_ids = cast(list[str], d.pop("siteIds", UNSET))

        upgrade_site_model_req_info = cls(
            site_ids=site_ids,
        )

        upgrade_site_model_req_info.additional_properties = d
        return upgrade_site_model_req_info

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
