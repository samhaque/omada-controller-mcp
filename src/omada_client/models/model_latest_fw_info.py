from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO


T = TypeVar("T", bound="ModelLatestFwInfo")


@_attrs_define
class ModelLatestFwInfo:
    """
    Attributes:
        id (str | Unset): ID
        model_type_info (ModelTypeInfoOpenApiVO | Unset): Model type information.
        latest_version (str | Unset): Latest version
        release_time (int | Unset): Latest version release time, timestamp ms
    """

    id: str | Unset = UNSET
    model_type_info: ModelTypeInfoOpenApiVO | Unset = UNSET
    latest_version: str | Unset = UNSET
    release_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_type_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_type_info, Unset):
            model_type_info = self.model_type_info.to_dict()

        latest_version = self.latest_version

        release_time = self.release_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if model_type_info is not UNSET:
            field_dict["modelTypeInfo"] = model_type_info
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if release_time is not UNSET:
            field_dict["releaseTime"] = release_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_type_info_open_api_vo import (
            ModelTypeInfoOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _model_type_info = d.pop("modelTypeInfo", UNSET)
        model_type_info: ModelTypeInfoOpenApiVO | Unset
        if isinstance(_model_type_info, Unset):
            model_type_info = UNSET
        else:
            model_type_info = ModelTypeInfoOpenApiVO.from_dict(_model_type_info)

        latest_version = d.pop("latestVersion", UNSET)

        release_time = d.pop("releaseTime", UNSET)

        model_latest_fw_info = cls(
            id=id,
            model_type_info=model_type_info,
            latest_version=latest_version,
            release_time=release_time,
        )

        model_latest_fw_info.additional_properties = d
        return model_latest_fw_info

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
