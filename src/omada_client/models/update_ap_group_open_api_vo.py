from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApGroupOpenApiVO")


@_attrs_define
class UpdateApGroupOpenApiVO:
    """
    Attributes:
        name (str): AP group name should contain 1 to 128 characters.
        add_ap_macs (list[str] | Unset): List of AP device MAC addresses to be added to this AP group. Can be empty.
        remove_ap_macs (list[str] | Unset): List of AP device MAC addresses to be removed from this AP group. Can be
            empty.
    """

    name: str
    add_ap_macs: list[str] | Unset = UNSET
    remove_ap_macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        add_ap_macs: list[str] | Unset = UNSET
        if not isinstance(self.add_ap_macs, Unset):
            add_ap_macs = self.add_ap_macs

        remove_ap_macs: list[str] | Unset = UNSET
        if not isinstance(self.remove_ap_macs, Unset):
            remove_ap_macs = self.remove_ap_macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if add_ap_macs is not UNSET:
            field_dict["addApMacs"] = add_ap_macs
        if remove_ap_macs is not UNSET:
            field_dict["removeApMacs"] = remove_ap_macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        add_ap_macs = cast(list[str], d.pop("addApMacs", UNSET))

        remove_ap_macs = cast(list[str], d.pop("removeApMacs", UNSET))

        update_ap_group_open_api_vo = cls(
            name=name,
            add_ap_macs=add_ap_macs,
            remove_ap_macs=remove_ap_macs,
        )

        update_ap_group_open_api_vo.additional_properties = d
        return update_ap_group_open_api_vo

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
