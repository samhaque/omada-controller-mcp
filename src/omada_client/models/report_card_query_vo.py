from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tab_card_vo import TabCardVO


T = TypeVar("T", bound="ReportCardQueryVO")


@_attrs_define
class ReportCardQueryVO:
    """
    Attributes:
        omadac_id (str | Unset): omadacId
        site_id (str | Unset): site id
        start (int | Unset): start time, unit: seconds
        end (int | Unset): end time, unit: seconds
        cards (list[TabCardVO] | Unset): card info
        request_token (str | Unset):
        token (str | Unset):
    """

    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    cards: list[TabCardVO] | Unset = UNSET
    request_token: str | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        omadac_id = self.omadac_id

        site_id = self.site_id

        start = self.start

        end = self.end

        cards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cards, Unset):
            cards = []
            for cards_item_data in self.cards:
                cards_item = cards_item_data.to_dict()
                cards.append(cards_item)

        request_token = self.request_token

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if cards is not UNSET:
            field_dict["cards"] = cards
        if request_token is not UNSET:
            field_dict["requestToken"] = request_token
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tab_card_vo import TabCardVO

        d = dict(src_dict)
        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        _cards = d.pop("cards", UNSET)
        cards: list[TabCardVO] | Unset = UNSET
        if _cards is not UNSET:
            cards = []
            for cards_item_data in _cards:
                cards_item = TabCardVO.from_dict(cards_item_data)

                cards.append(cards_item)

        request_token = d.pop("requestToken", UNSET)

        token = d.pop("token", UNSET)

        report_card_query_vo = cls(
            omadac_id=omadac_id,
            site_id=site_id,
            start=start,
            end=end,
            cards=cards,
            request_token=request_token,
            token=token,
        )

        report_card_query_vo.additional_properties = d
        return report_card_query_vo

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
