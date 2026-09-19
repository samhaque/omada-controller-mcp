from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveToSite")


@_attrs_define
class MoveToSite:
    """
    Attributes:
        site (str): Target site key
        device_macs (list[str] | Unset): Device mac list
        stack_ids (list[str] | Unset): Stack id list
    """

    site: str
    device_macs: list[str] | Unset = UNSET
    stack_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site = self.site

        device_macs: list[str] | Unset = UNSET
        if not isinstance(self.device_macs, Unset):
            device_macs = self.device_macs

        stack_ids: list[str] | Unset = UNSET
        if not isinstance(self.stack_ids, Unset):
            stack_ids = self.stack_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "site": site,
            }
        )
        if device_macs is not UNSET:
            field_dict["deviceMacs"] = device_macs
        if stack_ids is not UNSET:
            field_dict["stackIds"] = stack_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site = d.pop("site")

        device_macs = cast(list[str], d.pop("deviceMacs", UNSET))

        stack_ids = cast(list[str], d.pop("stackIds", UNSET))

        move_to_site = cls(
            site=site,
            device_macs=device_macs,
            stack_ids=stack_ids,
        )

        move_to_site.additional_properties = d
        return move_to_site

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
