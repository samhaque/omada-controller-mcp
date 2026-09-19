from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wired_port_v3dto import WiredPortV3DTO


T = TypeVar("T", bound="VrrpLinkDTO")


@_attrs_define
class VrrpLinkDTO:
    """Vrrp members internal link

    Attributes:
        up_link (WiredPortV3DTO | Unset): Downlink Port
        down_link (WiredPortV3DTO | Unset): Downlink Port
        link_speed (int | Unset): LinkSpeed
        duplex (int | Unset): Duplex
        blocked (bool | Unset): Whether The Link Is Blocked By STP Or Not
    """

    up_link: WiredPortV3DTO | Unset = UNSET
    down_link: WiredPortV3DTO | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    blocked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.up_link, Unset):
            up_link = self.up_link.to_dict()

        down_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.down_link, Unset):
            down_link = self.down_link.to_dict()

        link_speed = self.link_speed

        duplex = self.duplex

        blocked = self.blocked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if up_link is not UNSET:
            field_dict["upLink"] = up_link
        if down_link is not UNSET:
            field_dict["downLink"] = down_link
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if blocked is not UNSET:
            field_dict["blocked"] = blocked

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wired_port_v3dto import WiredPortV3DTO

        d = dict(src_dict)
        _up_link = d.pop("upLink", UNSET)
        up_link: WiredPortV3DTO | Unset
        if isinstance(_up_link, Unset):
            up_link = UNSET
        else:
            up_link = WiredPortV3DTO.from_dict(_up_link)

        _down_link = d.pop("downLink", UNSET)
        down_link: WiredPortV3DTO | Unset
        if isinstance(_down_link, Unset):
            down_link = UNSET
        else:
            down_link = WiredPortV3DTO.from_dict(_down_link)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        blocked = d.pop("blocked", UNSET)

        vrrp_link_dto = cls(
            up_link=up_link,
            down_link=down_link,
            link_speed=link_speed,
            duplex=duplex,
            blocked=blocked,
        )

        vrrp_link_dto.additional_properties = d
        return vrrp_link_dto

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
