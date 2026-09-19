from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_port_group_vo import OswStackPortGroupVO


T = TypeVar("T", bound="StackMsgVO")


@_attrs_define
class StackMsgVO:
    """Stack Message

    Attributes:
        stack_id (str | Unset): Stack ID
        stack_name (str | Unset): Stack name
        unit (int | Unset): Stack unit ID
        priority (int | Unset): Stack priority
        master_mac (str | Unset): Stack masterMac
        stack_status (int | Unset): StackStatus should be a value as follows: 0: normal; 1: abnormal; 2: stack not ready
        abnormal_reason (int | Unset): Causes of abnormal
        stack_ports (list[OswStackPortGroupVO] | Unset): The stack port that has been configured on the current unit
        account_vrf_id (str | Unset): The VRF ID for account traffic
        auth_vrf_id (str | Unset): The VRF ID for auth traffic
    """

    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    unit: int | Unset = UNSET
    priority: int | Unset = UNSET
    master_mac: str | Unset = UNSET
    stack_status: int | Unset = UNSET
    abnormal_reason: int | Unset = UNSET
    stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
    account_vrf_id: str | Unset = UNSET
    auth_vrf_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        stack_name = self.stack_name

        unit = self.unit

        priority = self.priority

        master_mac = self.master_mac

        stack_status = self.stack_status

        abnormal_reason = self.abnormal_reason

        stack_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_ports, Unset):
            stack_ports = []
            for stack_ports_item_data in self.stack_ports:
                stack_ports_item = stack_ports_item_data.to_dict()
                stack_ports.append(stack_ports_item)

        account_vrf_id = self.account_vrf_id

        auth_vrf_id = self.auth_vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if unit is not UNSET:
            field_dict["unit"] = unit
        if priority is not UNSET:
            field_dict["priority"] = priority
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac
        if stack_status is not UNSET:
            field_dict["stackStatus"] = stack_status
        if abnormal_reason is not UNSET:
            field_dict["abnormalReason"] = abnormal_reason
        if stack_ports is not UNSET:
            field_dict["stackPorts"] = stack_ports
        if account_vrf_id is not UNSET:
            field_dict["accountVrfId"] = account_vrf_id
        if auth_vrf_id is not UNSET:
            field_dict["authVrfId"] = auth_vrf_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_port_group_vo import (
            OswStackPortGroupVO,
        )

        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        unit = d.pop("unit", UNSET)

        priority = d.pop("priority", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        stack_status = d.pop("stackStatus", UNSET)

        abnormal_reason = d.pop("abnormalReason", UNSET)

        _stack_ports = d.pop("stackPorts", UNSET)
        stack_ports: list[OswStackPortGroupVO] | Unset = UNSET
        if _stack_ports is not UNSET:
            stack_ports = []
            for stack_ports_item_data in _stack_ports:
                stack_ports_item = OswStackPortGroupVO.from_dict(stack_ports_item_data)

                stack_ports.append(stack_ports_item)

        account_vrf_id = d.pop("accountVrfId", UNSET)

        auth_vrf_id = d.pop("authVrfId", UNSET)

        stack_msg_vo = cls(
            stack_id=stack_id,
            stack_name=stack_name,
            unit=unit,
            priority=priority,
            master_mac=master_mac,
            stack_status=stack_status,
            abnormal_reason=abnormal_reason,
            stack_ports=stack_ports,
            account_vrf_id=account_vrf_id,
            auth_vrf_id=auth_vrf_id,
        )

        stack_msg_vo.additional_properties = d
        return stack_msg_vo

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
