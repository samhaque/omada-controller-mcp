from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireguardKeyOpenApiVO")


@_attrs_define
class WireguardKeyOpenApiVO:
    """
    Attributes:
        private_key (str | Unset): The private key of WireGuard VPN.
        public_key (str | Unset): The public key of WireGuard VPN.
    """

    private_key: str | Unset = UNSET
    public_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        private_key = self.private_key

        public_key = self.public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if private_key is not UNSET:
            field_dict["privateKey"] = private_key
        if public_key is not UNSET:
            field_dict["publicKey"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        private_key = d.pop("privateKey", UNSET)

        public_key = d.pop("publicKey", UNSET)

        wireguard_key_open_api_vo = cls(
            private_key=private_key,
            public_key=public_key,
        )

        wireguard_key_open_api_vo.additional_properties = d
        return wireguard_key_open_api_vo

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
