from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Certificate")


@_attrs_define
class Certificate:
    """
    Attributes:
        cer_id (str): Certificate ID
        cer_name (str | Unset): Certificate name
        key_name (str | Unset): Certificate key name
        key_id (str | Unset): Certificate key ID
        enable (bool | Unset): Certificate enable status
        key_password (str | Unset): Certificate key password
        trust_password (str | Unset): Certificate trust password
        cer_type (str | Unset): Certificate type
    """

    cer_id: str
    cer_name: str | Unset = UNSET
    key_name: str | Unset = UNSET
    key_id: str | Unset = UNSET
    enable: bool | Unset = UNSET
    key_password: str | Unset = UNSET
    trust_password: str | Unset = UNSET
    cer_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cer_id = self.cer_id

        cer_name = self.cer_name

        key_name = self.key_name

        key_id = self.key_id

        enable = self.enable

        key_password = self.key_password

        trust_password = self.trust_password

        cer_type = self.cer_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cerId": cer_id,
            }
        )
        if cer_name is not UNSET:
            field_dict["cerName"] = cer_name
        if key_name is not UNSET:
            field_dict["keyName"] = key_name
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if key_password is not UNSET:
            field_dict["keyPassword"] = key_password
        if trust_password is not UNSET:
            field_dict["trustPassword"] = trust_password
        if cer_type is not UNSET:
            field_dict["cerType"] = cer_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cer_id = d.pop("cerId")

        cer_name = d.pop("cerName", UNSET)

        key_name = d.pop("keyName", UNSET)

        key_id = d.pop("keyId", UNSET)

        enable = d.pop("enable", UNSET)

        key_password = d.pop("keyPassword", UNSET)

        trust_password = d.pop("trustPassword", UNSET)

        cer_type = d.pop("cerType", UNSET)

        certificate = cls(
            cer_id=cer_id,
            cer_name=cer_name,
            key_name=key_name,
            key_id=key_id,
            enable=enable,
            key_password=key_password,
            trust_password=trust_password,
            cer_type=cer_type,
        )

        certificate.additional_properties = d
        return certificate

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
