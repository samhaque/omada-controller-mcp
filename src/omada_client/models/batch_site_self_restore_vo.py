from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.self_site_restore_vo import SelfSiteRestoreVO


T = TypeVar("T", bound="BatchSiteSelfRestoreVO")


@_attrs_define
class BatchSiteSelfRestoreVO:
    """
    Attributes:
        site_restore_infos (list[SelfSiteRestoreVO]): Site restore info list to restore. Up to 300 entries are allowed
            for the site restore info list.
    """

    site_restore_infos: list[SelfSiteRestoreVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_restore_infos = []
        for site_restore_infos_item_data in self.site_restore_infos:
            site_restore_infos_item = site_restore_infos_item_data.to_dict()
            site_restore_infos.append(site_restore_infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteRestoreInfos": site_restore_infos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.self_site_restore_vo import SelfSiteRestoreVO

        d = dict(src_dict)
        site_restore_infos = []
        _site_restore_infos = d.pop("siteRestoreInfos")
        for site_restore_infos_item_data in _site_restore_infos:
            site_restore_infos_item = SelfSiteRestoreVO.from_dict(
                site_restore_infos_item_data
            )

            site_restore_infos.append(site_restore_infos_item)

        batch_site_self_restore_vo = cls(
            site_restore_infos=site_restore_infos,
        )

        batch_site_self_restore_vo.additional_properties = d
        return batch_site_self_restore_vo

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
