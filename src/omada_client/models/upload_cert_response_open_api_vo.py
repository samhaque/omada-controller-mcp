from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadCertResponseOpenApiVO")


@_attrs_define
class UploadCertResponseOpenApiVO:
    """UploadCertResponseOpenApiVO

    Attributes:
        ca_cert_file_id (str | Unset): CA certificate profile file id.
        client_cert_file_id (str | Unset): Client certificate profile file id.
        private_key_file_id (str | Unset): Client Private key file id.
    """

    ca_cert_file_id: str | Unset = UNSET
    client_cert_file_id: str | Unset = UNSET
    private_key_file_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ca_cert_file_id = self.ca_cert_file_id

        client_cert_file_id = self.client_cert_file_id

        private_key_file_id = self.private_key_file_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ca_cert_file_id is not UNSET:
            field_dict["caCertFileId"] = ca_cert_file_id
        if client_cert_file_id is not UNSET:
            field_dict["clientCertFileId"] = client_cert_file_id
        if private_key_file_id is not UNSET:
            field_dict["privateKeyFileId"] = private_key_file_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ca_cert_file_id = d.pop("caCertFileId", UNSET)

        client_cert_file_id = d.pop("clientCertFileId", UNSET)

        private_key_file_id = d.pop("privateKeyFileId", UNSET)

        upload_cert_response_open_api_vo = cls(
            ca_cert_file_id=ca_cert_file_id,
            client_cert_file_id=client_cert_file_id,
            private_key_file_id=private_key_file_id,
        )

        upload_cert_response_open_api_vo.additional_properties = d
        return upload_cert_response_open_api_vo

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
