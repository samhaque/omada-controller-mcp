from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO
    from ..models.upgrade_base_schedule_time_open_api_vo import (
        UpgradeBaseScheduleTimeOpenApiVO,
    )


T = TypeVar("T", bound="AutoCheckUpgradeInfo")


@_attrs_define
class AutoCheckUpgradeInfo:
    """
    Attributes:
        id (str | Unset): ID
        model_type_infos (list[ModelTypeInfoOpenApiVO] | Unset): List of model type selected by the user
        site_names (list[str] | Unset): The siteNames lists selected by the user
        site_num (int | Unset): Number of sites selected by the user
        auto_check_time (str | Unset): Next execution time
        channel (int | Unset): Channel should be a value as follows: 0: stable; 1: Release Candidate(RC); 2: Beta
        occurrence (UpgradeBaseScheduleTimeOpenApiVO | Unset): Periodic execution time, and it should not be null
    """

    id: str | Unset = UNSET
    model_type_infos: list[ModelTypeInfoOpenApiVO] | Unset = UNSET
    site_names: list[str] | Unset = UNSET
    site_num: int | Unset = UNSET
    auto_check_time: str | Unset = UNSET
    channel: int | Unset = UNSET
    occurrence: UpgradeBaseScheduleTimeOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model_type_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.model_type_infos, Unset):
            model_type_infos = []
            for model_type_infos_item_data in self.model_type_infos:
                model_type_infos_item = model_type_infos_item_data.to_dict()
                model_type_infos.append(model_type_infos_item)

        site_names: list[str] | Unset = UNSET
        if not isinstance(self.site_names, Unset):
            site_names = self.site_names

        site_num = self.site_num

        auto_check_time = self.auto_check_time

        channel = self.channel

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if model_type_infos is not UNSET:
            field_dict["modelTypeInfos"] = model_type_infos
        if site_names is not UNSET:
            field_dict["siteNames"] = site_names
        if site_num is not UNSET:
            field_dict["siteNum"] = site_num
        if auto_check_time is not UNSET:
            field_dict["autoCheckTime"] = auto_check_time
        if channel is not UNSET:
            field_dict["channel"] = channel
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_type_info_open_api_vo import (
            ModelTypeInfoOpenApiVO,
        )
        from ..models.upgrade_base_schedule_time_open_api_vo import (
            UpgradeBaseScheduleTimeOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _model_type_infos = d.pop("modelTypeInfos", UNSET)
        model_type_infos: list[ModelTypeInfoOpenApiVO] | Unset = UNSET
        if _model_type_infos is not UNSET:
            model_type_infos = []
            for model_type_infos_item_data in _model_type_infos:
                model_type_infos_item = ModelTypeInfoOpenApiVO.from_dict(
                    model_type_infos_item_data
                )

                model_type_infos.append(model_type_infos_item)

        site_names = cast(list[str], d.pop("siteNames", UNSET))

        site_num = d.pop("siteNum", UNSET)

        auto_check_time = d.pop("autoCheckTime", UNSET)

        channel = d.pop("channel", UNSET)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: UpgradeBaseScheduleTimeOpenApiVO | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = UpgradeBaseScheduleTimeOpenApiVO.from_dict(_occurrence)

        auto_check_upgrade_info = cls(
            id=id,
            model_type_infos=model_type_infos,
            site_names=site_names,
            site_num=site_num,
            auto_check_time=auto_check_time,
            channel=channel,
            occurrence=occurrence,
        )

        auto_check_upgrade_info.additional_properties = d
        return auto_check_upgrade_info

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
