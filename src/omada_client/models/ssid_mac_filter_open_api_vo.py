from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidMacFilterOpenApiVO")


@_attrs_define
class SsidMacFilterOpenApiVO:
    """SSID MAC Filter config.

    Attributes:
        mac_filter_enable (bool | Unset): SSID MAC Filter global config status. True: enable, false: disable.
        policy (int | Unset): SSID MAC Filter policy config mode; It should be a value as follows: 0: Deny List, 1:
            Allow List.
        mac_filter_id (str | Unset): This field represents MAC Group Profile ID. MAC Group Profile can be created using
            Create a new group profile interface, and MAC Group Profile ID can be obtained from Get group profile list by
            type interface.
        oui_profile_id_list (list[str] | Unset): This field represents OUI Profile ID list. OUI Profile can be created
            using Create OUI profile interface, and OUI Profile ID can be obtained from Get OUI profile summary list
            interface.
    """

    mac_filter_enable: bool | Unset = UNSET
    policy: int | Unset = UNSET
    mac_filter_id: str | Unset = UNSET
    oui_profile_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac_filter_enable = self.mac_filter_enable

        policy = self.policy

        mac_filter_id = self.mac_filter_id

        oui_profile_id_list: list[str] | Unset = UNSET
        if not isinstance(self.oui_profile_id_list, Unset):
            oui_profile_id_list = self.oui_profile_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac_filter_enable is not UNSET:
            field_dict["macFilterEnable"] = mac_filter_enable
        if policy is not UNSET:
            field_dict["policy"] = policy
        if mac_filter_id is not UNSET:
            field_dict["macFilterId"] = mac_filter_id
        if oui_profile_id_list is not UNSET:
            field_dict["ouiProfileIdList"] = oui_profile_id_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac_filter_enable = d.pop("macFilterEnable", UNSET)

        policy = d.pop("policy", UNSET)

        mac_filter_id = d.pop("macFilterId", UNSET)

        oui_profile_id_list = cast(list[str], d.pop("ouiProfileIdList", UNSET))

        ssid_mac_filter_open_api_vo = cls(
            mac_filter_enable=mac_filter_enable,
            policy=policy,
            mac_filter_id=mac_filter_id,
            oui_profile_id_list=oui_profile_id_list,
        )

        ssid_mac_filter_open_api_vo.additional_properties = d
        return ssid_mac_filter_open_api_vo

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
