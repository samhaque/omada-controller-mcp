from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswStackPortGroupVO")


@_attrs_define
class OswStackPortGroupVO:
    """Stack port list

    Attributes:
        id (int): The ID of the stack port aggregation group
        name (str | Unset): Name of the stacking port aggregation group
        ports (list[OswStandPortVO] | Unset): Stack port aggregation group member port
        group_speed (int | Unset): Stack port aggregation group link speed config
    """

    id: int
    name: str | Unset = UNSET
    ports: list[OswStandPortVO] | Unset = UNSET
    group_speed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        group_speed = self.group_speed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ID": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if ports is not UNSET:
            field_dict["ports"] = ports
        if group_speed is not UNSET:
            field_dict["groupSpeed"] = group_speed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        id = d.pop("ID")

        name = d.pop("name", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[OswStandPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswStandPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        group_speed = d.pop("groupSpeed", UNSET)

        osw_stack_port_group_vo = cls(
            id=id,
            name=name,
            ports=ports,
            group_speed=group_speed,
        )

        osw_stack_port_group_vo.additional_properties = d
        return osw_stack_port_group_vo

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
