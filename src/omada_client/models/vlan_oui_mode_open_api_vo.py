from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="VlanOuiModeOpenApiVO")


@_attrs_define
class VlanOuiModeOpenApiVO:
    """Basic vlan-oui-priority configuration of oui based rule. Cannot be empty.

    Attributes:
        vlan_id (int): Selected vlan, valid range is 1 to 4094.
        priority (int): Selected priority, valid range is 0 to 7.
        oui_profile_id (str): Oui profile ID.
    """

    vlan_id: int
    priority: int
    oui_profile_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan_id = self.vlan_id

        priority = self.priority

        oui_profile_id = self.oui_profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vlanId": vlan_id,
                "priority": priority,
                "ouiProfileId": oui_profile_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vlan_id = d.pop("vlanId")

        priority = d.pop("priority")

        oui_profile_id = d.pop("ouiProfileId")

        vlan_oui_mode_open_api_vo = cls(
            vlan_id=vlan_id,
            priority=priority,
            oui_profile_id=oui_profile_id,
        )

        vlan_oui_mode_open_api_vo.additional_properties = d
        return vlan_oui_mode_open_api_vo

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
