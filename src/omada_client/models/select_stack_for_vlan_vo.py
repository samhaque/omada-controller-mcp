from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.select_stack_lag_for_vlan_vo import SelectStackLagForVlanVO
    from ..models.select_stack_member_for_vlan_vo import SelectStackMemberForVlanVO


T = TypeVar("T", bound="SelectStackForVlanVO")


@_attrs_define
class SelectStackForVlanVO:
    """Affected stack list

    Attributes:
        stack_id (str | Unset): Stack ID
        stack_name (str | Unset): Stack Name
        master_mac (str | Unset): Master mac
        status (int | Unset): Stack Status should be a value as follows: 0: normal; 1: abnormal; 2: stack not ready
        members (list[SelectStackMemberForVlanVO] | Unset): Stack Members
        lags (list[SelectStackLagForVlanVO] | Unset): Lags
        manually_select (bool | Unset): Whether the stack is manually selected.
        replaced_device (bool | Unset): It indicates whether the stack is the dhcp server device that is replaced in the
            first step
    """

    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    master_mac: str | Unset = UNSET
    status: int | Unset = UNSET
    members: list[SelectStackMemberForVlanVO] | Unset = UNSET
    lags: list[SelectStackLagForVlanVO] | Unset = UNSET
    manually_select: bool | Unset = UNSET
    replaced_device: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        stack_name = self.stack_name

        master_mac = self.master_mac

        status = self.status

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lags, Unset):
            lags = []
            for lags_item_data in self.lags:
                lags_item = lags_item_data.to_dict()
                lags.append(lags_item)

        manually_select = self.manually_select

        replaced_device = self.replaced_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac
        if status is not UNSET:
            field_dict["status"] = status
        if members is not UNSET:
            field_dict["members"] = members
        if lags is not UNSET:
            field_dict["lags"] = lags
        if manually_select is not UNSET:
            field_dict["manuallySelect"] = manually_select
        if replaced_device is not UNSET:
            field_dict["replacedDevice"] = replaced_device

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.select_stack_lag_for_vlan_vo import (
            SelectStackLagForVlanVO,
        )
        from ..models.select_stack_member_for_vlan_vo import (
            SelectStackMemberForVlanVO,
        )

        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        status = d.pop("status", UNSET)

        _members = d.pop("members", UNSET)
        members: list[SelectStackMemberForVlanVO] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = SelectStackMemberForVlanVO.from_dict(members_item_data)

                members.append(members_item)

        _lags = d.pop("lags", UNSET)
        lags: list[SelectStackLagForVlanVO] | Unset = UNSET
        if _lags is not UNSET:
            lags = []
            for lags_item_data in _lags:
                lags_item = SelectStackLagForVlanVO.from_dict(lags_item_data)

                lags.append(lags_item)

        manually_select = d.pop("manuallySelect", UNSET)

        replaced_device = d.pop("replacedDevice", UNSET)

        select_stack_for_vlan_vo = cls(
            stack_id=stack_id,
            stack_name=stack_name,
            master_mac=master_mac,
            status=status,
            members=members,
            lags=lags,
            manually_select=manually_select,
            replaced_device=replaced_device,
        )

        select_stack_for_vlan_vo.additional_properties = d
        return select_stack_for_vlan_vo

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
