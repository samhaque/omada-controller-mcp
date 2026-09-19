from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_card_data_vo import ClientCardDataVO


T = TypeVar("T", bound="ClientCardsResultOpenApiVO")


@_attrs_define
class ClientCardsResultOpenApiVO:
    """
    Attributes:
        rssi (ClientCardDataVO | Unset): SNR distribution card data. Only present when 'snr' is requested.
        snr (ClientCardDataVO | Unset): SNR distribution card data. Only present when 'snr' is requested.
    """

    rssi: ClientCardDataVO | Unset = UNSET
    snr: ClientCardDataVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rssi: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi, Unset):
            rssi = self.rssi.to_dict()

        snr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snr, Unset):
            snr = self.snr.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_card_data_vo import ClientCardDataVO

        d = dict(src_dict)
        _rssi = d.pop("rssi", UNSET)
        rssi: ClientCardDataVO | Unset
        if isinstance(_rssi, Unset):
            rssi = UNSET
        else:
            rssi = ClientCardDataVO.from_dict(_rssi)

        _snr = d.pop("snr", UNSET)
        snr: ClientCardDataVO | Unset
        if isinstance(_snr, Unset):
            snr = UNSET
        else:
            snr = ClientCardDataVO.from_dict(_snr)

        client_cards_result_open_api_vo = cls(
            rssi=rssi,
            snr=snr,
        )

        client_cards_result_open_api_vo.additional_properties = d
        return client_cards_result_open_api_vo

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
