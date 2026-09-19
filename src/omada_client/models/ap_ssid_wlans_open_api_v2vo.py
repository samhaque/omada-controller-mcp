from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssid_override_config_open_api_v2vo import (
        SsidOverrideConfigOpenApiV2VO,
    )


T = TypeVar("T", bound="ApSsidWlansOpenApiV2VO")


@_attrs_define
class ApSsidWlansOpenApiV2VO:
    """
    Attributes:
        ssid_overrides (list[SsidOverrideConfigOpenApiV2VO]): SsidOverride Config List
        ap_group_id (str | Unset): AP Group Id
        ap_group_name (str | Unset): AP Group Name
    """

    ssid_overrides: list[SsidOverrideConfigOpenApiV2VO]
    ap_group_id: str | Unset = UNSET
    ap_group_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_overrides = []
        for ssid_overrides_item_data in self.ssid_overrides:
            ssid_overrides_item = ssid_overrides_item_data.to_dict()
            ssid_overrides.append(ssid_overrides_item)

        ap_group_id = self.ap_group_id

        ap_group_name = self.ap_group_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssidOverrides": ssid_overrides,
            }
        )
        if ap_group_id is not UNSET:
            field_dict["apGroupId"] = ap_group_id
        if ap_group_name is not UNSET:
            field_dict["apGroupName"] = ap_group_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssid_override_config_open_api_v2vo import (
            SsidOverrideConfigOpenApiV2VO,
        )

        d = dict(src_dict)
        ssid_overrides = []
        _ssid_overrides = d.pop("ssidOverrides")
        for ssid_overrides_item_data in _ssid_overrides:
            ssid_overrides_item = SsidOverrideConfigOpenApiV2VO.from_dict(
                ssid_overrides_item_data
            )

            ssid_overrides.append(ssid_overrides_item)

        ap_group_id = d.pop("apGroupId", UNSET)

        ap_group_name = d.pop("apGroupName", UNSET)

        ap_ssid_wlans_open_api_v2vo = cls(
            ssid_overrides=ssid_overrides,
            ap_group_id=ap_group_id,
            ap_group_name=ap_group_name,
        )

        ap_ssid_wlans_open_api_v2vo.additional_properties = d
        return ap_ssid_wlans_open_api_v2vo

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
