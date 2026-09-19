from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.upload_voucher_group_logo_open_api_vo import (
        UploadVoucherGroupLogoOpenApiVO,
    )


T = TypeVar("T", bound="UploadVoucherLogoBody")


@_attrs_define
class UploadVoucherLogoBody:
    """
    Attributes:
        data (UploadVoucherGroupLogoOpenApiVO): File name,,need to specify Content-Type of this form part as
            application/json.
        file (File): At least one of the file or md5 parameters needs to be passed
    """

    data: UploadVoucherGroupLogoOpenApiVO
    file: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(
            (
                "data",
                (None, json.dumps(self.data.to_dict()).encode(), "application/json"),
            )
        )

        files.append(("file", self.file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.upload_voucher_group_logo_open_api_vo import (
            UploadVoucherGroupLogoOpenApiVO,
        )

        d = dict(src_dict)
        data = UploadVoucherGroupLogoOpenApiVO.from_dict(d.pop("data"))

        file = File(payload=BytesIO(d.pop("file")))

        upload_voucher_logo_body = cls(
            data=data,
            file=file,
        )

        upload_voucher_logo_body.additional_properties = d
        return upload_voucher_logo_body

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
