from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO


T = TypeVar("T", bound="UpgradeSiteModelInfo")


@_attrs_define
class UpgradeSiteModelInfo:
    """
    Attributes:
        model_type_infos (list[ModelTypeInfoOpenApiVO] | Unset): List of model type selected by the user
    """

    model_type_infos: list[ModelTypeInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_type_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.model_type_infos, Unset):
            model_type_infos = []
            for model_type_infos_item_data in self.model_type_infos:
                model_type_infos_item = model_type_infos_item_data.to_dict()
                model_type_infos.append(model_type_infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_type_infos is not UNSET:
            field_dict["modelTypeInfos"] = model_type_infos

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_type_info_open_api_vo import (
            ModelTypeInfoOpenApiVO,
        )

        d = dict(src_dict)
        _model_type_infos = d.pop("modelTypeInfos", UNSET)
        model_type_infos: list[ModelTypeInfoOpenApiVO] | Unset = UNSET
        if _model_type_infos is not UNSET:
            model_type_infos = []
            for model_type_infos_item_data in _model_type_infos:
                model_type_infos_item = ModelTypeInfoOpenApiVO.from_dict(
                    model_type_infos_item_data
                )

                model_type_infos.append(model_type_infos_item)

        upgrade_site_model_info = cls(
            model_type_infos=model_type_infos,
        )

        upgrade_site_model_info.additional_properties = d
        return upgrade_site_model_info

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
