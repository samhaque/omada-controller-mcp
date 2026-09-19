from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_info import DeviceInfo
    from ..models.osw_mlag_member_port_vo import OswMlagMemberPortVO


T = TypeVar("T", bound="OswMlagDataVODeviceInfo")


@_attrs_define
class OswMlagDataVODeviceInfo:
    """
    Attributes:
        mlag_id (str | Unset):
        mlag_name (str | Unset):
        mlag_status (int | Unset):
        mlag_members (list[OswMlagMemberPortVO] | Unset):
        member (list[DeviceInfo] | Unset):
    """

    mlag_id: str | Unset = UNSET
    mlag_name: str | Unset = UNSET
    mlag_status: int | Unset = UNSET
    mlag_members: list[OswMlagMemberPortVO] | Unset = UNSET
    member: list[DeviceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mlag_id = self.mlag_id

        mlag_name = self.mlag_name

        mlag_status = self.mlag_status

        mlag_members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mlag_members, Unset):
            mlag_members = []
            for mlag_members_item_data in self.mlag_members:
                mlag_members_item = mlag_members_item_data.to_dict()
                mlag_members.append(mlag_members_item)

        member: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = []
            for member_item_data in self.member:
                member_item = member_item_data.to_dict()
                member.append(member_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mlag_id is not UNSET:
            field_dict["mlagId"] = mlag_id
        if mlag_name is not UNSET:
            field_dict["mlagName"] = mlag_name
        if mlag_status is not UNSET:
            field_dict["mlagStatus"] = mlag_status
        if mlag_members is not UNSET:
            field_dict["mlagMembers"] = mlag_members
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_info import DeviceInfo
        from ..models.osw_mlag_member_port_vo import (
            OswMlagMemberPortVO,
        )

        d = dict(src_dict)
        mlag_id = d.pop("mlagId", UNSET)

        mlag_name = d.pop("mlagName", UNSET)

        mlag_status = d.pop("mlagStatus", UNSET)

        _mlag_members = d.pop("mlagMembers", UNSET)
        mlag_members: list[OswMlagMemberPortVO] | Unset = UNSET
        if _mlag_members is not UNSET:
            mlag_members = []
            for mlag_members_item_data in _mlag_members:
                mlag_members_item = OswMlagMemberPortVO.from_dict(
                    mlag_members_item_data
                )

                mlag_members.append(mlag_members_item)

        _member = d.pop("member", UNSET)
        member: list[DeviceInfo] | Unset = UNSET
        if _member is not UNSET:
            member = []
            for member_item_data in _member:
                member_item = DeviceInfo.from_dict(member_item_data)

                member.append(member_item)

        osw_mlag_data_vo_device_info = cls(
            mlag_id=mlag_id,
            mlag_name=mlag_name,
            mlag_status=mlag_status,
            mlag_members=mlag_members,
            member=member,
        )

        osw_mlag_data_vo_device_info.additional_properties = d
        return osw_mlag_data_vo_device_info

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
