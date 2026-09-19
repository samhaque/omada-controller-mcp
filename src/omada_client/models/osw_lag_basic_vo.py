from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_mlag_peer_setting_vo import OswMlagPeerSettingVO


T = TypeVar("T", bound="OswLagBasicVO")


@_attrs_define
class OswLagBasicVO:
    """Lag Setting

    Attributes:
        lag_id (int): Lag ID
        ports (list[int] | Unset): Lag ports
        lag_type (int | Unset): LagType should be a value as follows: 1: Static LAG; 2: LACP; 3: LACP-Active; 4: LACP-
            Passive
        mlag_name (str | Unset): M-LAG group Name
        mlag_enable (bool | Unset): Indicates whether M-LAG port is enabled
        mlag_peer_setting (OswMlagPeerSettingVO | Unset): M-LAG group peer device setting
    """

    lag_id: int
    ports: list[int] | Unset = UNSET
    lag_type: int | Unset = UNSET
    mlag_name: str | Unset = UNSET
    mlag_enable: bool | Unset = UNSET
    mlag_peer_setting: OswMlagPeerSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lag_id = self.lag_id

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        lag_type = self.lag_type

        mlag_name = self.mlag_name

        mlag_enable = self.mlag_enable

        mlag_peer_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_peer_setting, Unset):
            mlag_peer_setting = self.mlag_peer_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lagId": lag_id,
            }
        )
        if ports is not UNSET:
            field_dict["ports"] = ports
        if lag_type is not UNSET:
            field_dict["lagType"] = lag_type
        if mlag_name is not UNSET:
            field_dict["mlagName"] = mlag_name
        if mlag_enable is not UNSET:
            field_dict["mlagEnable"] = mlag_enable
        if mlag_peer_setting is not UNSET:
            field_dict["mlagPeerSetting"] = mlag_peer_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_mlag_peer_setting_vo import (
            OswMlagPeerSettingVO,
        )

        d = dict(src_dict)
        lag_id = d.pop("lagId")

        ports = cast(list[int], d.pop("ports", UNSET))

        lag_type = d.pop("lagType", UNSET)

        mlag_name = d.pop("mlagName", UNSET)

        mlag_enable = d.pop("mlagEnable", UNSET)

        _mlag_peer_setting = d.pop("mlagPeerSetting", UNSET)
        mlag_peer_setting: OswMlagPeerSettingVO | Unset
        if isinstance(_mlag_peer_setting, Unset):
            mlag_peer_setting = UNSET
        else:
            mlag_peer_setting = OswMlagPeerSettingVO.from_dict(_mlag_peer_setting)

        osw_lag_basic_vo = cls(
            lag_id=lag_id,
            ports=ports,
            lag_type=lag_type,
            mlag_name=mlag_name,
            mlag_enable=mlag_enable,
            mlag_peer_setting=mlag_peer_setting,
        )

        osw_lag_basic_vo.additional_properties = d
        return osw_lag_basic_vo

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
