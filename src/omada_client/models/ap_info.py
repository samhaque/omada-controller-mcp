from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wired_up_link_info import WiredUpLinkInfo
    from ..models.wireless_up_link_info import WirelessUpLinkInfo


T = TypeVar("T", bound="APInfo")


@_attrs_define
class APInfo:
    """AP info, exists when deviceType is 0.

    Attributes:
        wired_up_link (WiredUpLinkInfo | Unset): Exists when connected to upper level device via wired connection
        wireless_up_link (WirelessUpLinkInfo | Unset): Exists when connected to upper level device via wireless
            connection
    """

    wired_up_link: WiredUpLinkInfo | Unset = UNSET
    wireless_up_link: WirelessUpLinkInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wired_up_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wired_up_link, Unset):
            wired_up_link = self.wired_up_link.to_dict()

        wireless_up_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_up_link, Unset):
            wireless_up_link = self.wireless_up_link.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wired_up_link is not UNSET:
            field_dict["wiredUpLink"] = wired_up_link
        if wireless_up_link is not UNSET:
            field_dict["wirelessUpLink"] = wireless_up_link

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wired_up_link_info import WiredUpLinkInfo
        from ..models.wireless_up_link_info import WirelessUpLinkInfo

        d = dict(src_dict)
        _wired_up_link = d.pop("wiredUpLink", UNSET)
        wired_up_link: WiredUpLinkInfo | Unset
        if isinstance(_wired_up_link, Unset):
            wired_up_link = UNSET
        else:
            wired_up_link = WiredUpLinkInfo.from_dict(_wired_up_link)

        _wireless_up_link = d.pop("wirelessUpLink", UNSET)
        wireless_up_link: WirelessUpLinkInfo | Unset
        if isinstance(_wireless_up_link, Unset):
            wireless_up_link = UNSET
        else:
            wireless_up_link = WirelessUpLinkInfo.from_dict(_wireless_up_link)

        ap_info = cls(
            wired_up_link=wired_up_link,
            wireless_up_link=wireless_up_link,
        )

        ap_info.additional_properties = d
        return ap_info

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
