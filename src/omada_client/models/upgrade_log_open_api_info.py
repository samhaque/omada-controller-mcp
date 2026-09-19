from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO


T = TypeVar("T", bound="UpgradeLogOpenApiInfo")


@_attrs_define
class UpgradeLogOpenApiInfo:
    """
    Attributes:
        id (str | Unset): Upgrade log ID.
        model_type_info (ModelTypeInfoOpenApiVO | Unset): Model type information.
        site_names (list[str] | Unset): The siteName lists where the model belongs.
        site_num (int | Unset): Number of sites where the model belongs.
        current_version (list[str] | Unset): Model firmware version list before upgrade ,such as "[2.5.0 Build 20190118
            Rel. 64821, 2.4.8 Build 20190118 Rel. 64821]". This field is the same as "PREVIOUS VERSION" in Controller
            Upgrade Logs
        target_version (str | Unset): Model firmware version after device upgrade, such as "2.5.1 Build 20190118 Rel.
            64821". This field is the same as "CURRENT VERSION" in Controller Upgrade Logs
        upgrade_time (str | Unset): The time when the upgrade is complete.
        operator (str | Unset): Operator.
        rollbacked (bool | Unset): Whether the log is rolled back or not. The logs that are rolled back cannot be rolled
            back repeatedly.
        failed_device_num (int | Unset): The number of devices that failed to upgrade in this upgrade plan.
    """

    id: str | Unset = UNSET
    model_type_info: ModelTypeInfoOpenApiVO | Unset = UNSET
    site_names: list[str] | Unset = UNSET
    site_num: int | Unset = UNSET
    current_version: list[str] | Unset = UNSET
    target_version: str | Unset = UNSET
    upgrade_time: str | Unset = UNSET
    operator: str | Unset = UNSET
    rollbacked: bool | Unset = UNSET
    failed_device_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_type_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_type_info, Unset):
            model_type_info = self.model_type_info.to_dict()

        site_names: list[str] | Unset = UNSET
        if not isinstance(self.site_names, Unset):
            site_names = self.site_names

        site_num = self.site_num

        current_version: list[str] | Unset = UNSET
        if not isinstance(self.current_version, Unset):
            current_version = self.current_version

        target_version = self.target_version

        upgrade_time = self.upgrade_time

        operator = self.operator

        rollbacked = self.rollbacked

        failed_device_num = self.failed_device_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if model_type_info is not UNSET:
            field_dict["modelTypeInfo"] = model_type_info
        if site_names is not UNSET:
            field_dict["siteNames"] = site_names
        if site_num is not UNSET:
            field_dict["siteNum"] = site_num
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if target_version is not UNSET:
            field_dict["targetVersion"] = target_version
        if upgrade_time is not UNSET:
            field_dict["upgradeTime"] = upgrade_time
        if operator is not UNSET:
            field_dict["operator"] = operator
        if rollbacked is not UNSET:
            field_dict["rollbacked"] = rollbacked
        if failed_device_num is not UNSET:
            field_dict["failedDeviceNum"] = failed_device_num

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

        site_names = cast(list[str], d.pop("siteNames", UNSET))

        site_num = d.pop("siteNum", UNSET)

        current_version = cast(list[str], d.pop("currentVersion", UNSET))

        target_version = d.pop("targetVersion", UNSET)

        upgrade_time = d.pop("upgradeTime", UNSET)

        operator = d.pop("operator", UNSET)

        rollbacked = d.pop("rollbacked", UNSET)

        failed_device_num = d.pop("failedDeviceNum", UNSET)

        upgrade_log_open_api_info = cls(
            id=id,
            model_type_info=model_type_info,
            site_names=site_names,
            site_num=site_num,
            current_version=current_version,
            target_version=target_version,
            upgrade_time=upgrade_time,
            operator=operator,
            rollbacked=rollbacked,
            failed_device_num=failed_device_num,
        )

        upgrade_log_open_api_info.additional_properties = d
        return upgrade_log_open_api_info

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
