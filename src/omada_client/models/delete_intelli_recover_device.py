from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteIntelliRecoverDevice")


@_attrs_define
class DeleteIntelliRecoverDevice:
    """
    Attributes:
        delete_macs (list[str] | Unset): The device macs to be deleted from intelli recover device list.
    """

    delete_macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delete_macs: list[str] | Unset = UNSET
        if not isinstance(self.delete_macs, Unset):
            delete_macs = self.delete_macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_macs is not UNSET:
            field_dict["deleteMacs"] = delete_macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delete_macs = cast(list[str], d.pop("deleteMacs", UNSET))

        delete_intelli_recover_device = cls(
            delete_macs=delete_macs,
        )

        delete_intelli_recover_device.additional_properties = d
        return delete_intelli_recover_device

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
