from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertProfileRequestOpenApiVO")


@_attrs_define
class CertProfileRequestOpenApiVO:
    """CertProfileRequestOpenApiVO

    Attributes:
        name (str): Cert profile name, name should contain 1 to 64 characters.
        type_ (int): Cert profile type, type should be a value as follows: 0: CA Cert; 1: Client Cert..
        format_ (int): Cert profile format, format should be a value as follows: 0: X509; 1: DER.
        ca_cert_file_id (str | Unset): CA Certificate file id, it's obtained from the interface 'uploadCaCertFile'; When
            type = 0, Parameter [caCertFileId] should not be null.
        client_cert_file_id (str | Unset): Client certificate file id, it's obtained from the interface
            'uploadClientCertFile'; When type = 1, Parameter [clientCertFileId] should not be null.
        private_key_file_id (str | Unset): Client private key file id, it's obtained from the interface
            'UploadClientPrivateKeyFile'; When type = 1, Parameter [privateKeyFileId] should not be null.
        private_key_password (str | Unset): Client private key password; When type = 1, Parameter [privateKeyPassword]
            is an optional input.
    """

    name: str
    type_: int
    format_: int
    ca_cert_file_id: str | Unset = UNSET
    client_cert_file_id: str | Unset = UNSET
    private_key_file_id: str | Unset = UNSET
    private_key_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        format_ = self.format_

        ca_cert_file_id = self.ca_cert_file_id

        client_cert_file_id = self.client_cert_file_id

        private_key_file_id = self.private_key_file_id

        private_key_password = self.private_key_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "format": format_,
            }
        )
        if ca_cert_file_id is not UNSET:
            field_dict["caCertFileId"] = ca_cert_file_id
        if client_cert_file_id is not UNSET:
            field_dict["clientCertFileId"] = client_cert_file_id
        if private_key_file_id is not UNSET:
            field_dict["privateKeyFileId"] = private_key_file_id
        if private_key_password is not UNSET:
            field_dict["privateKeyPassword"] = private_key_password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        format_ = d.pop("format")

        ca_cert_file_id = d.pop("caCertFileId", UNSET)

        client_cert_file_id = d.pop("clientCertFileId", UNSET)

        private_key_file_id = d.pop("privateKeyFileId", UNSET)

        private_key_password = d.pop("privateKeyPassword", UNSET)

        cert_profile_request_open_api_vo = cls(
            name=name,
            type_=type_,
            format_=format_,
            ca_cert_file_id=ca_cert_file_id,
            client_cert_file_id=client_cert_file_id,
            private_key_file_id=private_key_file_id,
            private_key_password=private_key_password,
        )

        cert_profile_request_open_api_vo.additional_properties = d
        return cert_profile_request_open_api_vo

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
