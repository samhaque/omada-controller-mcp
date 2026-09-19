from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_link_entry_dto import MultiLinkEntryDTO


T = TypeVar("T", bound="VigiWirelessUpInfoDTO")


@_attrs_define
class VigiWirelessUpInfoDTO:
    """Wireless Vigi UpLink Info

    Attributes:
        channel (int | Unset): Wireless Vigi Channel
        ssid (str | Unset): Wireless Vigi Ssid
        radio (int | Unset): Wireless Vigi Radio
        support5g2 (bool | Unset): Whether The Vigi Supports 5g2 Or Not
        multi_link (list[MultiLinkEntryDTO] | Unset): Vigi MultiLink In MLO Mode
    """

    channel: int | Unset = UNSET
    ssid: str | Unset = UNSET
    radio: int | Unset = UNSET
    support5g2: bool | Unset = UNSET
    multi_link: list[MultiLinkEntryDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ssid = self.ssid

        radio = self.radio

        support5g2 = self.support5g2

        multi_link: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_link, Unset):
            multi_link = []
            for multi_link_item_data in self.multi_link:
                multi_link_item = multi_link_item_data.to_dict()
                multi_link.append(multi_link_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if radio is not UNSET:
            field_dict["radio"] = radio
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if multi_link is not UNSET:
            field_dict["multiLink"] = multi_link

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multi_link_entry_dto import MultiLinkEntryDTO

        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        ssid = d.pop("ssid", UNSET)

        radio = d.pop("radio", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        _multi_link = d.pop("multiLink", UNSET)
        multi_link: list[MultiLinkEntryDTO] | Unset = UNSET
        if _multi_link is not UNSET:
            multi_link = []
            for multi_link_item_data in _multi_link:
                multi_link_item = MultiLinkEntryDTO.from_dict(multi_link_item_data)

                multi_link.append(multi_link_item)

        vigi_wireless_up_info_dto = cls(
            channel=channel,
            ssid=ssid,
            radio=radio,
            support5g2=support5g2,
            multi_link=multi_link,
        )

        vigi_wireless_up_info_dto.additional_properties = d
        return vigi_wireless_up_info_dto

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
