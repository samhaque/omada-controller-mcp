from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_mlag_member_vo import OswMlagMemberVO


T = TypeVar("T", bound="OswMlagVO")


@_attrs_define
class OswMlagVO:
    """
    Attributes:
        id (str | Unset): M-LAG ID
        group_id (str | Unset): M-LAG group ID
        name (str | Unset): M-LAG group Name
        status (int | Unset): M-LAG group status should be a value as follows: 0: NORMAL; 1: PEER ERROR; 2: DAD ERROR;
            3: ABNORMAL; 4: CONFIGURATION UNSYNCHRONIZED; 5: MLAG MEMBERS INCOMPATIBLE; 6: MLAG MEMBERS MISMATCH.
        devices_num (int | Unset): Number of devices
        version (str | Unset): Version
        locate_enable (bool | Unset): Indicates whether the locate function is enabled
        members (list[OswMlagMemberVO] | Unset): M-LAG Group member list
    """

    id: str | Unset = UNSET
    group_id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: int | Unset = UNSET
    devices_num: int | Unset = UNSET
    version: str | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    members: list[OswMlagMemberVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        group_id = self.group_id

        name = self.name

        status = self.status

        devices_num = self.devices_num

        version = self.version

        locate_enable = self.locate_enable

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if devices_num is not UNSET:
            field_dict["devicesNum"] = devices_num
        if version is not UNSET:
            field_dict["version"] = version
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_mlag_member_vo import OswMlagMemberVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        group_id = d.pop("groupId", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        devices_num = d.pop("devicesNum", UNSET)

        version = d.pop("version", UNSET)

        locate_enable = d.pop("locateEnable", UNSET)

        _members = d.pop("members", UNSET)
        members: list[OswMlagMemberVO] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = OswMlagMemberVO.from_dict(members_item_data)

                members.append(members_item)

        osw_mlag_vo = cls(
            id=id,
            group_id=group_id,
            name=name,
            status=status,
            devices_num=devices_num,
            version=version,
            locate_enable=locate_enable,
            members=members,
        )

        osw_mlag_vo.additional_properties = d
        return osw_mlag_vo

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
