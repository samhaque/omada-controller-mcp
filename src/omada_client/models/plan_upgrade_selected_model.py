from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO


T = TypeVar("T", bound="PlanUpgradeSelectedModel")


@_attrs_define
class PlanUpgradeSelectedModel:
    """List of model selected for planned upgrade

    Attributes:
        model_type_info (ModelTypeInfoOpenApiVO): Model type information.
        current_version (list[str]): Selected model version list, software version, such as "2.5.0 Build 20190118 Rel.
            64821".
        target_version (str): Target version.
    """

    model_type_info: ModelTypeInfoOpenApiVO
    current_version: list[str]
    target_version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_type_info = self.model_type_info.to_dict()

        current_version = self.current_version

        target_version = self.target_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelTypeInfo": model_type_info,
                "currentVersion": current_version,
                "targetVersion": target_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_type_info_open_api_vo import (
            ModelTypeInfoOpenApiVO,
        )

        d = dict(src_dict)
        model_type_info = ModelTypeInfoOpenApiVO.from_dict(d.pop("modelTypeInfo"))

        current_version = cast(list[str], d.pop("currentVersion"))

        target_version = d.pop("targetVersion")

        plan_upgrade_selected_model = cls(
            model_type_info=model_type_info,
            current_version=current_version,
            target_version=target_version,
        )

        plan_upgrade_selected_model.additional_properties = d
        return plan_upgrade_selected_model

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
