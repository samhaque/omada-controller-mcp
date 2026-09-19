from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_rssi_distribution_vo import ClientsRssiDistributionVO


T = TypeVar("T", bound="ClientRssiChannelDistributionVO")


@_attrs_define
class ClientRssiChannelDistributionVO:
    """
    Attributes:
        less_than_72 (int | Unset):
        from_71_to_65 (int | Unset):
        from_65_to_55 (int | Unset):
        from_55_to_45 (int | Unset):
        more_than_45 (int | Unset):
        distribution_2g (ClientsRssiDistributionVO | Unset):
        distribution_5g (ClientsRssiDistributionVO | Unset):
        distribution_6g (ClientsRssiDistributionVO | Unset):
    """

    less_than_72: int | Unset = UNSET
    from_71_to_65: int | Unset = UNSET
    from_65_to_55: int | Unset = UNSET
    from_55_to_45: int | Unset = UNSET
    more_than_45: int | Unset = UNSET
    distribution_2g: ClientsRssiDistributionVO | Unset = UNSET
    distribution_5g: ClientsRssiDistributionVO | Unset = UNSET
    distribution_6g: ClientsRssiDistributionVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        less_than_72 = self.less_than_72

        from_71_to_65 = self.from_71_to_65

        from_65_to_55 = self.from_65_to_55

        from_55_to_45 = self.from_55_to_45

        more_than_45 = self.more_than_45

        distribution_2g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution_2g, Unset):
            distribution_2g = self.distribution_2g.to_dict()

        distribution_5g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution_5g, Unset):
            distribution_5g = self.distribution_5g.to_dict()

        distribution_6g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution_6g, Unset):
            distribution_6g = self.distribution_6g.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if less_than_72 is not UNSET:
            field_dict["lessThan72"] = less_than_72
        if from_71_to_65 is not UNSET:
            field_dict["from71To65"] = from_71_to_65
        if from_65_to_55 is not UNSET:
            field_dict["from65To55"] = from_65_to_55
        if from_55_to_45 is not UNSET:
            field_dict["from55To45"] = from_55_to_45
        if more_than_45 is not UNSET:
            field_dict["moreThan45"] = more_than_45
        if distribution_2g is not UNSET:
            field_dict["distribution2G"] = distribution_2g
        if distribution_5g is not UNSET:
            field_dict["distribution5G"] = distribution_5g
        if distribution_6g is not UNSET:
            field_dict["distribution6G"] = distribution_6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_rssi_distribution_vo import (
            ClientsRssiDistributionVO,
        )

        d = dict(src_dict)
        less_than_72 = d.pop("lessThan72", UNSET)

        from_71_to_65 = d.pop("from71To65", UNSET)

        from_65_to_55 = d.pop("from65To55", UNSET)

        from_55_to_45 = d.pop("from55To45", UNSET)

        more_than_45 = d.pop("moreThan45", UNSET)

        _distribution_2g = d.pop("distribution2G", UNSET)
        distribution_2g: ClientsRssiDistributionVO | Unset
        if isinstance(_distribution_2g, Unset):
            distribution_2g = UNSET
        else:
            distribution_2g = ClientsRssiDistributionVO.from_dict(_distribution_2g)

        _distribution_5g = d.pop("distribution5G", UNSET)
        distribution_5g: ClientsRssiDistributionVO | Unset
        if isinstance(_distribution_5g, Unset):
            distribution_5g = UNSET
        else:
            distribution_5g = ClientsRssiDistributionVO.from_dict(_distribution_5g)

        _distribution_6g = d.pop("distribution6G", UNSET)
        distribution_6g: ClientsRssiDistributionVO | Unset
        if isinstance(_distribution_6g, Unset):
            distribution_6g = UNSET
        else:
            distribution_6g = ClientsRssiDistributionVO.from_dict(_distribution_6g)

        client_rssi_channel_distribution_vo = cls(
            less_than_72=less_than_72,
            from_71_to_65=from_71_to_65,
            from_65_to_55=from_65_to_55,
            from_55_to_45=from_55_to_45,
            more_than_45=more_than_45,
            distribution_2g=distribution_2g,
            distribution_5g=distribution_5g,
            distribution_6g=distribution_6g,
        )

        client_rssi_channel_distribution_vo.additional_properties = d
        return client_rssi_channel_distribution_vo

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
