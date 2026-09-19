from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="OswStpInstanceConfigOpenApiVO")


@_attrs_define
class OswStpInstanceConfigOpenApiVO:
    """Instances

    Attributes:
        id (int): ID
        priority (int): Priority
        vlan (str): Parameter [vlan] should be between 1 and 4094.
    """

    id: int
    priority: int
    vlan: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        priority = self.priority

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "priority": priority,
                "vlan": vlan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        priority = d.pop("priority")

        vlan = d.pop("vlan")

        osw_stp_instance_config_open_api_vo = cls(
            id=id,
            priority=priority,
            vlan=vlan,
        )

        osw_stp_instance_config_open_api_vo.additional_properties = d
        return osw_stp_instance_config_open_api_vo

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
