from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgIptvVO")


@_attrs_define
class OsgIptvVO:
    """
    Attributes:
        igmp_enable (bool | Unset):
        igmp_version (str | Unset):
    """

    igmp_enable: bool | Unset = UNSET
    igmp_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        igmp_enable = self.igmp_enable

        igmp_version = self.igmp_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if igmp_enable is not UNSET:
            field_dict["igmpEnable"] = igmp_enable
        if igmp_version is not UNSET:
            field_dict["igmpVersion"] = igmp_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        igmp_enable = d.pop("igmpEnable", UNSET)

        igmp_version = d.pop("igmpVersion", UNSET)

        osg_iptv_vo = cls(
            igmp_enable=igmp_enable,
            igmp_version=igmp_version,
        )

        osg_iptv_vo.additional_properties = d
        return osg_iptv_vo

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
