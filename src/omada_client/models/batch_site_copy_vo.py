from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="BatchSiteCopyVO")


@_attrs_define
class BatchSiteCopyVO:
    """
    Attributes:
        source_site_id (str): Source site ID to be copied.
        target_site_num (int): Site num to be created should between 1 and 300.
        site_name_prefix (str): Site name prefix, new sites name will use this prefix. Parameter [siteNamePrefix] should
            be 1 - 128 ASCII characters.
    """

    source_site_id: str
    target_site_num: int
    site_name_prefix: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_site_id = self.source_site_id

        target_site_num = self.target_site_num

        site_name_prefix = self.site_name_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceSiteId": source_site_id,
                "targetSiteNum": target_site_num,
                "siteNamePrefix": site_name_prefix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        source_site_id = d.pop("sourceSiteId")

        target_site_num = d.pop("targetSiteNum")

        site_name_prefix = d.pop("siteNamePrefix")

        batch_site_copy_vo = cls(
            source_site_id=source_site_id,
            target_site_num=target_site_num,
            site_name_prefix=site_name_prefix,
        )

        batch_site_copy_vo.additional_properties = d
        return batch_site_copy_vo

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
