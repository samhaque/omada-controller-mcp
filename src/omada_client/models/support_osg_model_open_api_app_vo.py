from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.osg_model_open_api_info_vo import OsgModelOpenApiInfoVO


T = TypeVar("T", bound="SupportOsgModelOpenApiAppVO")


@_attrs_define
class SupportOsgModelOpenApiAppVO:
    """
    Attributes:
        support_models (list[OsgModelOpenApiInfoVO]): Model ID and name
    """

    support_models: list[OsgModelOpenApiInfoVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_models = []
        for support_models_item_data in self.support_models:
            support_models_item = support_models_item_data.to_dict()
            support_models.append(support_models_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "supportModels": support_models,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_model_open_api_info_vo import (
            OsgModelOpenApiInfoVO,
        )

        d = dict(src_dict)
        support_models = []
        _support_models = d.pop("supportModels")
        for support_models_item_data in _support_models:
            support_models_item = OsgModelOpenApiInfoVO.from_dict(
                support_models_item_data
            )

            support_models.append(support_models_item)

        support_osg_model_open_api_app_vo = cls(
            support_models=support_models,
        )

        support_osg_model_open_api_app_vo.additional_properties = d
        return support_osg_model_open_api_app_vo

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
