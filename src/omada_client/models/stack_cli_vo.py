from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stack_cli_vo_variable_map import StackCliVOVariableMap


T = TypeVar("T", bound="StackCliVO")


@_attrs_define
class StackCliVO:
    """List of stacks bound to the CLI configuration, only device CLI has this field.

    Attributes:
        stack_id (str | Unset): Stack ID
        stack_name (str | Unset): Stack name
        master_mac (str | Unset): Master mac
        variable_map (StackCliVOVariableMap | Unset): The values of different user-defined variables.
    """

    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    master_mac: str | Unset = UNSET
    variable_map: StackCliVOVariableMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        stack_name = self.stack_name

        master_mac = self.master_mac

        variable_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variable_map, Unset):
            variable_map = self.variable_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if master_mac is not UNSET:
            field_dict["masterMac"] = master_mac
        if variable_map is not UNSET:
            field_dict["variableMap"] = variable_map

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.stack_cli_vo_variable_map import (
            StackCliVOVariableMap,
        )

        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        master_mac = d.pop("masterMac", UNSET)

        _variable_map = d.pop("variableMap", UNSET)
        variable_map: StackCliVOVariableMap | Unset
        if isinstance(_variable_map, Unset):
            variable_map = UNSET
        else:
            variable_map = StackCliVOVariableMap.from_dict(_variable_map)

        stack_cli_vo = cls(
            stack_id=stack_id,
            stack_name=stack_name,
            master_mac=master_mac,
            variable_map=variable_map,
        )

        stack_cli_vo.additional_properties = d
        return stack_cli_vo

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
