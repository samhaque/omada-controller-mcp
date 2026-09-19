from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthInfoOpenApiVO")


@_attrs_define
class AuthInfoOpenApiVO:
    """Client portal authentication information

    Attributes:
        auth_type (int | Unset): Auth type should be a value as follows: 0: No Auth; 1: Simple Password; 2: External
            Radius; 3: Voucher; 4: External Portal Server; 5: Local User; 6: SMS; 7: Facebook; 8: Hotspot Radius; 9: Mac
            Auth (with fail over); 10: Admin auth; 12: Form auth; 15: LDAP
        info (str | Unset): Auth brief information
    """

    auth_type: int | Unset = UNSET
    info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type

        info = self.info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        auth_type = d.pop("authType", UNSET)

        info = d.pop("info", UNSET)

        auth_info_open_api_vo = cls(
            auth_type=auth_type,
            info=info,
        )

        auth_info_open_api_vo.additional_properties = d
        return auth_info_open_api_vo

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
