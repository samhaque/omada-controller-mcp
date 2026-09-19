from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_mgt_ssid_vlan_custom_setting_open_api_vo import (
        ApMgtSsidVlanCustomSettingOpenApiVO,
    )


T = TypeVar("T", bound="ApMgtSsidVlanSettingOpenApiVO")


@_attrs_define
class ApMgtSsidVlanSettingOpenApiVO:
    """SSID VLAN configuration.

    Attributes:
        mode (int): should be a value as follows: 0:Default; 1:Custom.
        custom_config (ApMgtSsidVlanCustomSettingOpenApiVO | Unset): If mode=1, this field must be entered.
    """

    mode: int
    custom_config: ApMgtSsidVlanCustomSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        custom_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_config, Unset):
            custom_config = self.custom_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if custom_config is not UNSET:
            field_dict["customConfig"] = custom_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_mgt_ssid_vlan_custom_setting_open_api_vo import (
            ApMgtSsidVlanCustomSettingOpenApiVO,
        )

        d = dict(src_dict)
        mode = d.pop("mode")

        _custom_config = d.pop("customConfig", UNSET)
        custom_config: ApMgtSsidVlanCustomSettingOpenApiVO | Unset
        if isinstance(_custom_config, Unset):
            custom_config = UNSET
        else:
            custom_config = ApMgtSsidVlanCustomSettingOpenApiVO.from_dict(
                _custom_config
            )

        ap_mgt_ssid_vlan_setting_open_api_vo = cls(
            mode=mode,
            custom_config=custom_config,
        )

        ap_mgt_ssid_vlan_setting_open_api_vo.additional_properties = d
        return ap_mgt_ssid_vlan_setting_open_api_vo

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
