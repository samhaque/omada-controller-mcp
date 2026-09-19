from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertProfileDetailOpenApiVO")


@_attrs_define
class CertProfileDetailOpenApiVO:
    """CertProfileDetailOpenApiVO

    Attributes:
        file_name (str | Unset): Certificate authority profile file name
        type_ (int | Unset): Certificate authority profile type, such as:  0: CA Cert; 1: Client Cert.
        cert_type (str | Unset): Cert profile file type, such as: X.509.
        version (int | Unset): Cert profile file version, such as: 3.
        serial_number (str | Unset): Cert profile serial number, such as 1.
        cert_name (str | Unset): Certificate authority profile file name, such as : server_certificate
        issuer (str | Unset): Certificate authority profile file issuer, such as : L=$$$$, CN=TLSGenSelfSignedRootCA
            2024-11-01T16:54:19.242005
        subject (str | Unset): Certificate authority profile file subject, such as : O=server, CN=192.168.0.20
        issued_on (str | Unset): Certificate authority profile file issued on, such as : Fri Nov 01 16:54:19 CST 2024
        expires_on (str | Unset): Certificate authority profile file expired on, such as : Mon Oct 30 16:54:19 CST 2034
        rsa_key_size (str | Unset): Certificate authority profile file rsa Key Size, such as : 3
        signed_using (str | Unset): Certificate authority profile file signed using such as : SHA256withRSA
    """

    file_name: str | Unset = UNSET
    type_: int | Unset = UNSET
    cert_type: str | Unset = UNSET
    version: int | Unset = UNSET
    serial_number: str | Unset = UNSET
    cert_name: str | Unset = UNSET
    issuer: str | Unset = UNSET
    subject: str | Unset = UNSET
    issued_on: str | Unset = UNSET
    expires_on: str | Unset = UNSET
    rsa_key_size: str | Unset = UNSET
    signed_using: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        type_ = self.type_

        cert_type = self.cert_type

        version = self.version

        serial_number = self.serial_number

        cert_name = self.cert_name

        issuer = self.issuer

        subject = self.subject

        issued_on = self.issued_on

        expires_on = self.expires_on

        rsa_key_size = self.rsa_key_size

        signed_using = self.signed_using

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if cert_type is not UNSET:
            field_dict["certType"] = cert_type
        if version is not UNSET:
            field_dict["version"] = version
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if cert_name is not UNSET:
            field_dict["certName"] = cert_name
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if subject is not UNSET:
            field_dict["subject"] = subject
        if issued_on is not UNSET:
            field_dict["issuedOn"] = issued_on
        if expires_on is not UNSET:
            field_dict["expiresOn"] = expires_on
        if rsa_key_size is not UNSET:
            field_dict["rsaKeySize"] = rsa_key_size
        if signed_using is not UNSET:
            field_dict["signedUsing"] = signed_using

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file_name = d.pop("fileName", UNSET)

        type_ = d.pop("type", UNSET)

        cert_type = d.pop("certType", UNSET)

        version = d.pop("version", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        cert_name = d.pop("certName", UNSET)

        issuer = d.pop("issuer", UNSET)

        subject = d.pop("subject", UNSET)

        issued_on = d.pop("issuedOn", UNSET)

        expires_on = d.pop("expiresOn", UNSET)

        rsa_key_size = d.pop("rsaKeySize", UNSET)

        signed_using = d.pop("signedUsing", UNSET)

        cert_profile_detail_open_api_vo = cls(
            file_name=file_name,
            type_=type_,
            cert_type=cert_type,
            version=version,
            serial_number=serial_number,
            cert_name=cert_name,
            issuer=issuer,
            subject=subject,
            issued_on=issued_on,
            expires_on=expires_on,
            rsa_key_size=rsa_key_size,
            signed_using=signed_using,
        )

        cert_profile_detail_open_api_vo.additional_properties = d
        return cert_profile_detail_open_api_vo

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
