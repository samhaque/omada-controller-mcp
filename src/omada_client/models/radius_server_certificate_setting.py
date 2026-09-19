from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RADIUSServerCertificateSetting")


@_attrs_define
class RADIUSServerCertificateSetting:
    """RADIUS server certificate

    Attributes:
        cer_id (str | Unset): Certificate ID
        cer_name (str | Unset): Certificate name
        key_id (str | Unset): Secrect key ID
        key_name (str | Unset): Secrect key name
        key_password (str | Unset): Keystore password
        cer_type (str | Unset): Certificate type: JKS/PFX/PEM
    """

    cer_id: str | Unset = UNSET
    cer_name: str | Unset = UNSET
    key_id: str | Unset = UNSET
    key_name: str | Unset = UNSET
    key_password: str | Unset = UNSET
    cer_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cer_id = self.cer_id

        cer_name = self.cer_name

        key_id = self.key_id

        key_name = self.key_name

        key_password = self.key_password

        cer_type = self.cer_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cer_id is not UNSET:
            field_dict["cerId"] = cer_id
        if cer_name is not UNSET:
            field_dict["cerName"] = cer_name
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if key_name is not UNSET:
            field_dict["keyName"] = key_name
        if key_password is not UNSET:
            field_dict["keyPassword"] = key_password
        if cer_type is not UNSET:
            field_dict["cerType"] = cer_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cer_id = d.pop("cerId", UNSET)

        cer_name = d.pop("cerName", UNSET)

        key_id = d.pop("keyId", UNSET)

        key_name = d.pop("keyName", UNSET)

        key_password = d.pop("keyPassword", UNSET)

        cer_type = d.pop("cerType", UNSET)

        radius_server_certificate_setting = cls(
            cer_id=cer_id,
            cer_name=cer_name,
            key_id=key_id,
            key_name=key_name,
            key_password=key_password,
            cer_type=cer_type,
        )

        radius_server_certificate_setting.additional_properties = d
        return radius_server_certificate_setting

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
