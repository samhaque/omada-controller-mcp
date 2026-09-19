from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eap_client_vo import EapClientVO


T = TypeVar("T", bound="EapDistributionVO")


@_attrs_define
class EapDistributionVO:
    """
    Attributes:
        eaps (list[EapClientVO] | Unset):
        others (EapClientVO | Unset):
        total_eap_clients (int | Unset):
        total_eap_distribution (float | Unset):
    """

    eaps: list[EapClientVO] | Unset = UNSET
    others: EapClientVO | Unset = UNSET
    total_eap_clients: int | Unset = UNSET
    total_eap_distribution: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eaps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eaps, Unset):
            eaps = []
            for eaps_item_data in self.eaps:
                eaps_item = eaps_item_data.to_dict()
                eaps.append(eaps_item)

        others: dict[str, Any] | Unset = UNSET
        if not isinstance(self.others, Unset):
            others = self.others.to_dict()

        total_eap_clients = self.total_eap_clients

        total_eap_distribution = self.total_eap_distribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eaps is not UNSET:
            field_dict["eaps"] = eaps
        if others is not UNSET:
            field_dict["others"] = others
        if total_eap_clients is not UNSET:
            field_dict["totalEapClients"] = total_eap_clients
        if total_eap_distribution is not UNSET:
            field_dict["totalEapDistribution"] = total_eap_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eap_client_vo import EapClientVO

        d = dict(src_dict)
        _eaps = d.pop("eaps", UNSET)
        eaps: list[EapClientVO] | Unset = UNSET
        if _eaps is not UNSET:
            eaps = []
            for eaps_item_data in _eaps:
                eaps_item = EapClientVO.from_dict(eaps_item_data)

                eaps.append(eaps_item)

        _others = d.pop("others", UNSET)
        others: EapClientVO | Unset
        if isinstance(_others, Unset):
            others = UNSET
        else:
            others = EapClientVO.from_dict(_others)

        total_eap_clients = d.pop("totalEapClients", UNSET)

        total_eap_distribution = d.pop("totalEapDistribution", UNSET)

        eap_distribution_vo = cls(
            eaps=eaps,
            others=others,
            total_eap_clients=total_eap_clients,
            total_eap_distribution=total_eap_distribution,
        )

        eap_distribution_vo.additional_properties = d
        return eap_distribution_vo

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
