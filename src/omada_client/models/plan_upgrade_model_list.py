from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO


T = TypeVar("T", bound="PlanUpgradeModelList")


@_attrs_define
class PlanUpgradeModelList:
    """
    Attributes:
        model_type_info (ModelTypeInfoOpenApiVO | Unset): Model type information.
        current_version (list[str] | Unset): Model version list, software version, such as "2.5.0 Build 20190118 Rel.
            64821"
        status (int | Unset): Model critical status should be a value as follows: 0: good; 1: critical
        upgrade_status (int | Unset): Model upgrade status should be a value as follows: 0: up-to-date; 1: new Version
            Available
    """

    model_type_info: ModelTypeInfoOpenApiVO | Unset = UNSET
    current_version: list[str] | Unset = UNSET
    status: int | Unset = UNSET
    upgrade_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_type_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_type_info, Unset):
            model_type_info = self.model_type_info.to_dict()

        current_version: list[str] | Unset = UNSET
        if not isinstance(self.current_version, Unset):
            current_version = self.current_version

        status = self.status

        upgrade_status = self.upgrade_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_type_info is not UNSET:
            field_dict["modelTypeInfo"] = model_type_info
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if status is not UNSET:
            field_dict["status"] = status
        if upgrade_status is not UNSET:
            field_dict["upgradeStatus"] = upgrade_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_type_info_open_api_vo import (
            ModelTypeInfoOpenApiVO,
        )

        d = dict(src_dict)
        _model_type_info = d.pop("modelTypeInfo", UNSET)
        model_type_info: ModelTypeInfoOpenApiVO | Unset
        if isinstance(_model_type_info, Unset):
            model_type_info = UNSET
        else:
            model_type_info = ModelTypeInfoOpenApiVO.from_dict(_model_type_info)

        current_version = cast(list[str], d.pop("currentVersion", UNSET))

        status = d.pop("status", UNSET)

        upgrade_status = d.pop("upgradeStatus", UNSET)

        plan_upgrade_model_list = cls(
            model_type_info=model_type_info,
            current_version=current_version,
            status=status,
            upgrade_status=upgrade_status,
        )

        plan_upgrade_model_list.additional_properties = d
        return plan_upgrade_model_list

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
