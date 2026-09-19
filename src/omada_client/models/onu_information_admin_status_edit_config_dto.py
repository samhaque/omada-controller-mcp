from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_information_admin_status_edit_config_dto_admin_status import (
    OnuInformationAdminStatusEditConfigDTOAdminStatus,
)

T = TypeVar("T", bound="OnuInformationAdminStatusEditConfigDTO")


@_attrs_define
class OnuInformationAdminStatusEditConfigDTO:
    """
    Attributes:
        keys (list[str]): ONU identifier list
        admin_status (OnuInformationAdminStatusEditConfigDTOAdminStatus): Admin status should be a value as
            follows:ACTIVATE,DEACTIVATE
    """

    keys: list[str]
    admin_status: OnuInformationAdminStatusEditConfigDTOAdminStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys = self.keys

        admin_status = self.admin_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keys": keys,
                "adminStatus": admin_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        keys = cast(list[str], d.pop("keys"))

        admin_status = OnuInformationAdminStatusEditConfigDTOAdminStatus(
            d.pop("adminStatus")
        )

        onu_information_admin_status_edit_config_dto = cls(
            keys=keys,
            admin_status=admin_status,
        )

        onu_information_admin_status_edit_config_dto.additional_properties = d
        return onu_information_admin_status_edit_config_dto

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
