from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_speed_cap_vo import PortSpeedCapVO


T = TypeVar("T", bound="OswPortSpeedCapVO")


@_attrs_define
class OswPortSpeedCapVO:
    """Port Speed Capability

    Attributes:
        link_speed (PortSpeedCapVO | Unset): Duplex
        duplex (PortSpeedCapVO | Unset): Duplex
    """

    link_speed: PortSpeedCapVO | Unset = UNSET
    duplex: PortSpeedCapVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link_speed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_speed, Unset):
            link_speed = self.link_speed.to_dict()

        duplex: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duplex, Unset):
            duplex = self.duplex.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_speed is not UNSET:
            field_dict["Link Speed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_speed_cap_vo import PortSpeedCapVO

        d = dict(src_dict)
        _link_speed = d.pop("Link Speed", UNSET)
        link_speed: PortSpeedCapVO | Unset
        if isinstance(_link_speed, Unset):
            link_speed = UNSET
        else:
            link_speed = PortSpeedCapVO.from_dict(_link_speed)

        _duplex = d.pop("duplex", UNSET)
        duplex: PortSpeedCapVO | Unset
        if isinstance(_duplex, Unset):
            duplex = UNSET
        else:
            duplex = PortSpeedCapVO.from_dict(_duplex)

        osw_port_speed_cap_vo = cls(
            link_speed=link_speed,
            duplex=duplex,
        )

        osw_port_speed_cap_vo.additional_properties = d
        return osw_port_speed_cap_vo

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
