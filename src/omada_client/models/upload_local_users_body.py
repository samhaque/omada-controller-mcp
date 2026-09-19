from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import File

if TYPE_CHECKING:
    from ..models.hotspot_portals_open_api_vo import HotspotPortalsOpenApiVO


T = TypeVar("T", bound="UploadLocalUsersBody")


@_attrs_define
class UploadLocalUsersBody:
    """
    Attributes:
        config (HotspotPortalsOpenApiVO): Bound portal ID list,need to specify Content-Type of this form part as
            application/json.
        file (File):
    """

    config: HotspotPortalsOpenApiVO
    file: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hotspot_portals_open_api_vo import (
            HotspotPortalsOpenApiVO,
        )

        d = dict(src_dict)
        config = HotspotPortalsOpenApiVO.from_dict(d.pop("config"))

        file = File(payload=BytesIO(d.pop("file")))

        upload_local_users_body = cls(
            config=config,
            file=file,
        )

        upload_local_users_body.additional_properties = d
        return upload_local_users_body

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
