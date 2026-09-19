from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.auto_authentication_config_dto_auto_authentication_status import (
    AutoAuthenticationConfigDTOAutoAuthenticationStatus,
)

T = TypeVar("T", bound="AutoAuthenticationConfigDTO")


@_attrs_define
class AutoAuthenticationConfigDTO:
    """
    Attributes:
        auto_authentication_status (AutoAuthenticationConfigDTOAutoAuthenticationStatus): Auto authentication status
            should be a value as follows:ENABLE,DISABLE
    """

    auto_authentication_status: AutoAuthenticationConfigDTOAutoAuthenticationStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_authentication_status = self.auto_authentication_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoAuthenticationStatus": auto_authentication_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        auto_authentication_status = (
            AutoAuthenticationConfigDTOAutoAuthenticationStatus(
                d.pop("autoAuthenticationStatus")
            )
        )

        auto_authentication_config_dto = cls(
            auto_authentication_status=auto_authentication_status,
        )

        auto_authentication_config_dto.additional_properties = d
        return auto_authentication_config_dto

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
