from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wired_port_dto import WiredPortDTO


T = TypeVar("T", bound="OswUpInfo")


@_attrs_define
class OswUpInfo:
    """Upper Info of Switch

    Attributes:
        port (WiredPortDTO | Unset): UpLink Device's Port
        up_link_port (WiredPortDTO | Unset): UpLink Device's Port
        link_speed (int | Unset): LinkSpeed
        duplex (int | Unset): Duplex
    """

    port: WiredPortDTO | Unset = UNSET
    up_link_port: WiredPortDTO | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        up_link_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.up_link_port, Unset):
            up_link_port = self.up_link_port.to_dict()

        link_speed = self.link_speed

        duplex = self.duplex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if up_link_port is not UNSET:
            field_dict["upLinkPort"] = up_link_port
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wired_port_dto import WiredPortDTO

        d = dict(src_dict)
        _port = d.pop("port", UNSET)
        port: WiredPortDTO | Unset
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = WiredPortDTO.from_dict(_port)

        _up_link_port = d.pop("upLinkPort", UNSET)
        up_link_port: WiredPortDTO | Unset
        if isinstance(_up_link_port, Unset):
            up_link_port = UNSET
        else:
            up_link_port = WiredPortDTO.from_dict(_up_link_port)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        osw_up_info = cls(
            port=port,
            up_link_port=up_link_port,
            link_speed=link_speed,
            duplex=duplex,
        )

        osw_up_info.additional_properties = d
        return osw_up_info

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
