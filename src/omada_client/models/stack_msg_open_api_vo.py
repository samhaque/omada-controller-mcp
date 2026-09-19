from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StackMsgOpenApiVO")


@_attrs_define
class StackMsgOpenApiVO:
    """The information of the stack to which it belongs.

    Attributes:
        stack_id (str | Unset): Stack Id.
        stack_name (str | Unset): Stack Name.
        master_mac (str | Unset): Stack MasterMac.
    """

    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    master_mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        stack_name = self.stack_name

        master_mac = self.master_mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        stack_msg_open_api_vo = cls(
            stack_id=stack_id,
            stack_name=stack_name,
            master_mac=master_mac,
        )

        stack_msg_open_api_vo.additional_properties = d
        return stack_msg_open_api_vo

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
