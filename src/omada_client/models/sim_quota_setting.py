from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quota_data_setting_open_api_vo import QuotaDataSettingOpenApiVO
    from ..models.quota_sms_setting_open_api_vo import QuotaSmsSettingOpenApiVO


T = TypeVar("T", bound="SimQuotaSetting")


@_attrs_define
class SimQuotaSetting:
    """When parameter [type] is 0, parameter [content] should not be null.

    Attributes:
        data_setting (QuotaDataSettingOpenApiVO | Unset): Data quota setting.
        sms_setting (QuotaSmsSettingOpenApiVO | Unset): SMS quota setting.
        sim_card (int | Unset): When device supports Dual-SIM card, using parameter [simCard] to point which card to
            configure. 1: SIM1; 2:SIM2.
        card_status (int | Unset): Sim card status.
        resource (int | Unset): Sim quota setting creation resource,such as: 0: new created, 1: from template, 2:
            override.
    """

    data_setting: QuotaDataSettingOpenApiVO | Unset = UNSET
    sms_setting: QuotaSmsSettingOpenApiVO | Unset = UNSET
    sim_card: int | Unset = UNSET
    card_status: int | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_setting, Unset):
            data_setting = self.data_setting.to_dict()

        sms_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sms_setting, Unset):
            sms_setting = self.sms_setting.to_dict()

        sim_card = self.sim_card

        card_status = self.card_status

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_setting is not UNSET:
            field_dict["dataSetting"] = data_setting
        if sms_setting is not UNSET:
            field_dict["smsSetting"] = sms_setting
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card
        if card_status is not UNSET:
            field_dict["cardStatus"] = card_status
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.quota_data_setting_open_api_vo import (
            QuotaDataSettingOpenApiVO,
        )
        from ..models.quota_sms_setting_open_api_vo import (
            QuotaSmsSettingOpenApiVO,
        )

        d = dict(src_dict)
        _data_setting = d.pop("dataSetting", UNSET)
        data_setting: QuotaDataSettingOpenApiVO | Unset
        if isinstance(_data_setting, Unset):
            data_setting = UNSET
        else:
            data_setting = QuotaDataSettingOpenApiVO.from_dict(_data_setting)

        _sms_setting = d.pop("smsSetting", UNSET)
        sms_setting: QuotaSmsSettingOpenApiVO | Unset
        if isinstance(_sms_setting, Unset):
            sms_setting = UNSET
        else:
            sms_setting = QuotaSmsSettingOpenApiVO.from_dict(_sms_setting)

        sim_card = d.pop("simCard", UNSET)

        card_status = d.pop("cardStatus", UNSET)

        resource = d.pop("resource", UNSET)

        sim_quota_setting = cls(
            data_setting=data_setting,
            sms_setting=sms_setting,
            sim_card=sim_card,
            card_status=card_status,
            resource=resource,
        )

        sim_quota_setting.additional_properties = d
        return sim_quota_setting

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
