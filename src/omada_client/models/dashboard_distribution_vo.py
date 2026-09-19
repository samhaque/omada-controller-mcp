from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eap_distribution_vo import EapDistributionVO
    from ..models.switch_distribution_vo import SwitchDistributionVO


T = TypeVar("T", bound="DashboardDistributionVO")


@_attrs_define
class DashboardDistributionVO:
    """
    Attributes:
        eap_distribution (EapDistributionVO | Unset):
        switch_distribution (SwitchDistributionVO | Unset):
    """

    eap_distribution: EapDistributionVO | Unset = UNSET
    switch_distribution: SwitchDistributionVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eap_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eap_distribution, Unset):
            eap_distribution = self.eap_distribution.to_dict()

        switch_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_distribution, Unset):
            switch_distribution = self.switch_distribution.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eap_distribution is not UNSET:
            field_dict["eapDistribution"] = eap_distribution
        if switch_distribution is not UNSET:
            field_dict["switchDistribution"] = switch_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eap_distribution_vo import EapDistributionVO
        from ..models.switch_distribution_vo import (
            SwitchDistributionVO,
        )

        d = dict(src_dict)
        _eap_distribution = d.pop("eapDistribution", UNSET)
        eap_distribution: EapDistributionVO | Unset
        if isinstance(_eap_distribution, Unset):
            eap_distribution = UNSET
        else:
            eap_distribution = EapDistributionVO.from_dict(_eap_distribution)

        _switch_distribution = d.pop("switchDistribution", UNSET)
        switch_distribution: SwitchDistributionVO | Unset
        if isinstance(_switch_distribution, Unset):
            switch_distribution = UNSET
        else:
            switch_distribution = SwitchDistributionVO.from_dict(_switch_distribution)

        dashboard_distribution_vo = cls(
            eap_distribution=eap_distribution,
            switch_distribution=switch_distribution,
        )

        dashboard_distribution_vo.additional_properties = d
        return dashboard_distribution_vo

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
