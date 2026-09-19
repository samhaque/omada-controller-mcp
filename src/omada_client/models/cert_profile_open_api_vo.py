from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertProfileOpenApiVO")


@_attrs_define
class CertProfileOpenApiVO:
    """CertProfileOpenApiVO

    Attributes:
        id (str | Unset): Certificate authority profile entry id.
        name (str | Unset): Certificate authority profile name
        file_name (str | Unset): Certificate authority profile file name
        type_ (int | Unset): Certificate authority profile type, such as:  0: CA Cert; 1: Client Cert.
        format_ (int | Unset): Cert profile format, format should be a value as follows: 0: X509; 1: DER.
        status (int | Unset): Cert profile status, status should be a value as follows: 0: Normal 1: Expired Soon 2:
            Expired.
        expired_on (int | Unset): Cert profile expired time, expired timestamp, in seconds, such as 1682000000.
        ca_cert_file_id (str | Unset): CA Certificate file id, it's obtained from the interface 'uploadCaCertFile'; When
            type = 0, Parameter [caCertFileId] should not be null.
        client_cert_file_id (str | Unset): Client certificate file id, it's obtained from the interface
            'uploadClientCertFile'; When type = 1, Parameter [clientCertFileId] should not be null.
        cert_file_md_5 (str | Unset): Client certificate file MD5.
        private_key_file_id (str | Unset): Client private key file id, it's obtained from the interface
            'UploadClientPrivateKeyFile'; When type = 1, Parameter [privateKeyFileId] should not be null.
        private_key_file_name (str | Unset): Client private key file name.
        private_key_file_md_5 (str | Unset): Client private key file MD5.
        private_key_password (str | Unset): Certificate authority profile privateKey Password should contain 1 to 64
            characters, spaces, comma, single quotation marks and double quotation marks are not allowed.
        resource (int | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    file_name: str | Unset = UNSET
    type_: int | Unset = UNSET
    format_: int | Unset = UNSET
    status: int | Unset = UNSET
    expired_on: int | Unset = UNSET
    ca_cert_file_id: str | Unset = UNSET
    client_cert_file_id: str | Unset = UNSET
    cert_file_md_5: str | Unset = UNSET
    private_key_file_id: str | Unset = UNSET
    private_key_file_name: str | Unset = UNSET
    private_key_file_md_5: str | Unset = UNSET
    private_key_password: str | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        file_name = self.file_name

        type_ = self.type_

        format_ = self.format_

        status = self.status

        expired_on = self.expired_on

        ca_cert_file_id = self.ca_cert_file_id

        client_cert_file_id = self.client_cert_file_id

        cert_file_md_5 = self.cert_file_md_5

        private_key_file_id = self.private_key_file_id

        private_key_file_name = self.private_key_file_name

        private_key_file_md_5 = self.private_key_file_md_5

        private_key_password = self.private_key_password

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if format_ is not UNSET:
            field_dict["format"] = format_
        if status is not UNSET:
            field_dict["status"] = status
        if expired_on is not UNSET:
            field_dict["expiredOn"] = expired_on
        if ca_cert_file_id is not UNSET:
            field_dict["caCertFileId"] = ca_cert_file_id
        if client_cert_file_id is not UNSET:
            field_dict["clientCertFileId"] = client_cert_file_id
        if cert_file_md_5 is not UNSET:
            field_dict["certFileMd5"] = cert_file_md_5
        if private_key_file_id is not UNSET:
            field_dict["privateKeyFileId"] = private_key_file_id
        if private_key_file_name is not UNSET:
            field_dict["privateKeyFileName"] = private_key_file_name
        if private_key_file_md_5 is not UNSET:
            field_dict["privateKeyFileMd5"] = private_key_file_md_5
        if private_key_password is not UNSET:
            field_dict["privateKeyPassword"] = private_key_password
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        file_name = d.pop("fileName", UNSET)

        type_ = d.pop("type", UNSET)

        format_ = d.pop("format", UNSET)

        status = d.pop("status", UNSET)

        expired_on = d.pop("expiredOn", UNSET)

        ca_cert_file_id = d.pop("caCertFileId", UNSET)

        client_cert_file_id = d.pop("clientCertFileId", UNSET)

        cert_file_md_5 = d.pop("certFileMd5", UNSET)

        private_key_file_id = d.pop("privateKeyFileId", UNSET)

        private_key_file_name = d.pop("privateKeyFileName", UNSET)

        private_key_file_md_5 = d.pop("privateKeyFileMd5", UNSET)

        private_key_password = d.pop("privateKeyPassword", UNSET)

        resource = d.pop("resource", UNSET)

        cert_profile_open_api_vo = cls(
            id=id,
            name=name,
            file_name=file_name,
            type_=type_,
            format_=format_,
            status=status,
            expired_on=expired_on,
            ca_cert_file_id=ca_cert_file_id,
            client_cert_file_id=client_cert_file_id,
            cert_file_md_5=cert_file_md_5,
            private_key_file_id=private_key_file_id,
            private_key_file_name=private_key_file_name,
            private_key_file_md_5=private_key_file_md_5,
            private_key_password=private_key_password,
            resource=resource,
        )

        cert_profile_open_api_vo.additional_properties = d
        return cert_profile_open_api_vo

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
