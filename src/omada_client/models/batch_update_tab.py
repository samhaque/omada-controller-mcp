from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchUpdateTab")


@_attrs_define
class BatchUpdateTab:
    """Edit Tab Parameters

    Attributes:
        id (str | Unset): A unique identifier
        cards (list[int] | Unset): Card list displayed in Tab. Each number indicates a type of card. card should be a
            value as follows:  0: Controller Snapshot, 101: Alerts, 102: ISP Load, 103: L2TP/PPTP VPN, 104: Channel
            Distribution and Usage, 105: Most Active EAPs, 106: Most Active Switches, 108: WiFi/Switching Summary, 109:
            Traffic Distribution, 110: Traffic Activities, 111: Clients Distribution, 112: Retry Rate/Dropped Rate, 117: Top
            Device CPU/Memory Usage, 118: IPSEC VPN, 119: OPEN VPN, 120: SSL VPN, 200: Most Active Clients, 201: Longest
            client uptime, 202: Clients Freq Distribution, 203: Clients Activities, 204: Clients Association Activities,
            205: Association Failures, 206: Clients Association Time Distribution, 207: Clients SSID Distribution, 208:
            Clients RSSI Distribution
    """

    id: str | Unset = UNSET
    cards: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        cards: list[int] | Unset = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if cards is not UNSET:
            field_dict["cards"] = cards

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        cards = cast(list[int], d.pop("cards", UNSET))

        batch_update_tab = cls(
            id=id,
            cards=cards,
        )

        batch_update_tab.additional_properties = d
        return batch_update_tab

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
