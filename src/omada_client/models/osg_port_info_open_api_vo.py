from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wan_lan_port_setting_open_api_vo import WanLanPortSettingOpenApiVO


T = TypeVar("T", bound="OsgPortInfoOpenApiVO")


@_attrs_define
class OsgPortInfoOpenApiVO:
    """Gateway port info.

    Attributes:
        real_osg_model (str | Unset): real gateway model
        pre_osg_model (int | Unset): preconfigured gateway model
        pre_osg_model_name (str | Unset): preconfigured gateway model name
        target_models (list[int] | Unset): target gateway models when gateway change
        wan_port_num (int | Unset): custom wan port num
        wan_lan_port_settings (list[WanLanPortSettingOpenApiVO] | Unset):
    """

    real_osg_model: str | Unset = UNSET
    pre_osg_model: int | Unset = UNSET
    pre_osg_model_name: str | Unset = UNSET
    target_models: list[int] | Unset = UNSET
    wan_port_num: int | Unset = UNSET
    wan_lan_port_settings: list[WanLanPortSettingOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        real_osg_model = self.real_osg_model

        pre_osg_model = self.pre_osg_model

        pre_osg_model_name = self.pre_osg_model_name

        target_models: list[int] | Unset = UNSET
        if not isinstance(self.target_models, Unset):
            target_models = self.target_models

        wan_port_num = self.wan_port_num

        wan_lan_port_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_lan_port_settings, Unset):
            wan_lan_port_settings = []
            for wan_lan_port_settings_item_data in self.wan_lan_port_settings:
                wan_lan_port_settings_item = wan_lan_port_settings_item_data.to_dict()
                wan_lan_port_settings.append(wan_lan_port_settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if real_osg_model is not UNSET:
            field_dict["realOsgModel"] = real_osg_model
        if pre_osg_model is not UNSET:
            field_dict["preOsgModel"] = pre_osg_model
        if pre_osg_model_name is not UNSET:
            field_dict["preOsgModelName"] = pre_osg_model_name
        if target_models is not UNSET:
            field_dict["targetModels"] = target_models
        if wan_port_num is not UNSET:
            field_dict["wanPortNum"] = wan_port_num
        if wan_lan_port_settings is not UNSET:
            field_dict["wanLanPortSettings"] = wan_lan_port_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wan_lan_port_setting_open_api_vo import (
            WanLanPortSettingOpenApiVO,
        )

        d = dict(src_dict)
        real_osg_model = d.pop("realOsgModel", UNSET)

        pre_osg_model = d.pop("preOsgModel", UNSET)

        pre_osg_model_name = d.pop("preOsgModelName", UNSET)

        target_models = cast(list[int], d.pop("targetModels", UNSET))

        wan_port_num = d.pop("wanPortNum", UNSET)

        _wan_lan_port_settings = d.pop("wanLanPortSettings", UNSET)
        wan_lan_port_settings: list[WanLanPortSettingOpenApiVO] | Unset = UNSET
        if _wan_lan_port_settings is not UNSET:
            wan_lan_port_settings = []
            for wan_lan_port_settings_item_data in _wan_lan_port_settings:
                wan_lan_port_settings_item = WanLanPortSettingOpenApiVO.from_dict(
                    wan_lan_port_settings_item_data
                )

                wan_lan_port_settings.append(wan_lan_port_settings_item)

        osg_port_info_open_api_vo = cls(
            real_osg_model=real_osg_model,
            pre_osg_model=pre_osg_model,
            pre_osg_model_name=pre_osg_model_name,
            target_models=target_models,
            wan_port_num=wan_port_num,
            wan_lan_port_settings=wan_lan_port_settings,
        )

        osg_port_info_open_api_vo.additional_properties = d
        return osg_port_info_open_api_vo

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
