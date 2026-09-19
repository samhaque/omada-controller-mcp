from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_admin_status_edit_dto_admin_status import (
    OnuAdminStatusEditDTOAdminStatus,
)

T = TypeVar("T", bound="OnuAdminStatusEditDTO")


@_attrs_define
class OnuAdminStatusEditDTO:
    """
    Attributes:
        admin_status (OnuAdminStatusEditDTOAdminStatus): Admin status should be a value as follows:ACTIVATE,DEACTIVATE
        keys (list[str]): Entry identifier list
    """

    admin_status: OnuAdminStatusEditDTOAdminStatus
    keys: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin_status = self.admin_status.value

        keys = self.keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adminStatus": admin_status,
                "keys": keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        admin_status = OnuAdminStatusEditDTOAdminStatus(d.pop("adminStatus"))

        keys = cast(list[str], d.pop("keys"))

        onu_admin_status_edit_dto = cls(
            admin_status=admin_status,
            keys=keys,
        )

        onu_admin_status_edit_dto.additional_properties = d
        return onu_admin_status_edit_dto

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
