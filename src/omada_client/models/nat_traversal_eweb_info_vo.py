from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NatTraversalEwebInfoVO")


@_attrs_define
class NatTraversalEwebInfoVO:
    """
    Attributes:
        eweb_host (str | Unset): Nat traversal tunnel eweb host
        auto_login_token (str | Unset): Nat traversal tunnel auto login token
    """

    eweb_host: str | Unset = UNSET
    auto_login_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eweb_host = self.eweb_host

        auto_login_token = self.auto_login_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eweb_host is not UNSET:
            field_dict["ewebHost"] = eweb_host
        if auto_login_token is not UNSET:
            field_dict["autoLoginToken"] = auto_login_token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        eweb_host = d.pop("ewebHost", UNSET)

        auto_login_token = d.pop("autoLoginToken", UNSET)

        nat_traversal_eweb_info_vo = cls(
            eweb_host=eweb_host,
            auto_login_token=auto_login_token,
        )

        nat_traversal_eweb_info_vo.additional_properties = d
        return nat_traversal_eweb_info_vo

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
