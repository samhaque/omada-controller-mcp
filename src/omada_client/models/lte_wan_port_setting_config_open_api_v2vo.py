from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dialup_setting_open_api_v2vo import DialupSettingOpenApiV2VO


T = TypeVar("T", bound="LteWanPortSettingConfigOpenApiV2VO")


@_attrs_define
class LteWanPortSettingConfigOpenApiV2VO:
    """
    Attributes:
        port_uuid (str): Port Uuid
        mobile_data (bool): mobile data
        dialup_setting (DialupSettingOpenApiV2VO): Second SIM card's dial-up setting
        port_desc (str | Unset): Port description should contain 1 to 32 characters.
        sim_priority (int | Unset): Set which SIM card is used first. SIM Priority takes effect only when the device is
            powered on and the priority is changed. If only one SIM card is inserted, this card is used by default.
        dialup_setting_2 (DialupSettingOpenApiV2VO | Unset): Second SIM card's dial-up setting
    """

    port_uuid: str
    mobile_data: bool
    dialup_setting: DialupSettingOpenApiV2VO
    port_desc: str | Unset = UNSET
    sim_priority: int | Unset = UNSET
    dialup_setting_2: DialupSettingOpenApiV2VO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        mobile_data = self.mobile_data

        dialup_setting = self.dialup_setting.to_dict()

        port_desc = self.port_desc

        sim_priority = self.sim_priority

        dialup_setting_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dialup_setting_2, Unset):
            dialup_setting_2 = self.dialup_setting_2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portUuid": port_uuid,
                "mobileData": mobile_data,
                "dialupSetting": dialup_setting,
            }
        )
        if port_desc is not UNSET:
            field_dict["portDesc"] = port_desc
        if sim_priority is not UNSET:
            field_dict["simPriority"] = sim_priority
        if dialup_setting_2 is not UNSET:
            field_dict["dialupSetting2"] = dialup_setting_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dialup_setting_open_api_v2vo import (
            DialupSettingOpenApiV2VO,
        )

        d = dict(src_dict)
        port_uuid = d.pop("portUuid")

        mobile_data = d.pop("mobileData")

        dialup_setting = DialupSettingOpenApiV2VO.from_dict(d.pop("dialupSetting"))

        port_desc = d.pop("portDesc", UNSET)

        sim_priority = d.pop("simPriority", UNSET)

        _dialup_setting_2 = d.pop("dialupSetting2", UNSET)
        dialup_setting_2: DialupSettingOpenApiV2VO | Unset
        if isinstance(_dialup_setting_2, Unset):
            dialup_setting_2 = UNSET
        else:
            dialup_setting_2 = DialupSettingOpenApiV2VO.from_dict(_dialup_setting_2)

        lte_wan_port_setting_config_open_api_v2vo = cls(
            port_uuid=port_uuid,
            mobile_data=mobile_data,
            dialup_setting=dialup_setting,
            port_desc=port_desc,
            sim_priority=sim_priority,
            dialup_setting_2=dialup_setting_2,
        )

        lte_wan_port_setting_config_open_api_v2vo.additional_properties = d
        return lte_wan_port_setting_config_open_api_v2vo

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
