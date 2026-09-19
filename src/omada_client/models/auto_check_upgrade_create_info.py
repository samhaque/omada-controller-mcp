from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.model_type_info_open_api_vo import ModelTypeInfoOpenApiVO
    from ..models.upgrade_base_schedule_time_open_api_vo import (
        UpgradeBaseScheduleTimeOpenApiVO,
    )


T = TypeVar("T", bound="AutoCheckUpgradeCreateInfo")


@_attrs_define
class AutoCheckUpgradeCreateInfo:
    """
    Attributes:
        model_type_infos (list[ModelTypeInfoOpenApiVO]): List of model type selected by the user, and it should not be
            null
        site_ids (list[str]): List of sites selected by the user, and it should not be null
        occurrence (UpgradeBaseScheduleTimeOpenApiVO): Periodic execution time, and it should not be null
        channel (int): Channel should be a value as follows: 0: stable; 1: Release Candidate(RC); 2: Beta, and it should
            not be null
    """

    model_type_infos: list[ModelTypeInfoOpenApiVO]
    site_ids: list[str]
    occurrence: UpgradeBaseScheduleTimeOpenApiVO
    channel: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_type_infos = []
        for model_type_infos_item_data in self.model_type_infos:
            model_type_infos_item = model_type_infos_item_data.to_dict()
            model_type_infos.append(model_type_infos_item)

        site_ids = self.site_ids

        occurrence = self.occurrence.to_dict()

        channel = self.channel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modelTypeInfos": model_type_infos,
                "siteIds": site_ids,
                "occurrence": occurrence,
                "channel": channel,
            }
        )

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
        model_type_infos = []
        _model_type_infos = d.pop("modelTypeInfos")
        for model_type_infos_item_data in _model_type_infos:
            model_type_infos_item = ModelTypeInfoOpenApiVO.from_dict(
                model_type_infos_item_data
            )

            model_type_infos.append(model_type_infos_item)

        site_ids = cast(list[str], d.pop("siteIds"))

        occurrence = UpgradeBaseScheduleTimeOpenApiVO.from_dict(d.pop("occurrence"))

        channel = d.pop("channel")

        auto_check_upgrade_create_info = cls(
            model_type_infos=model_type_infos,
            site_ids=site_ids,
            occurrence=occurrence,
            channel=channel,
        )

        auto_check_upgrade_create_info.additional_properties = d
        return auto_check_upgrade_create_info

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
