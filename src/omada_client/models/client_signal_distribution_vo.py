from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_distribution_vo import ClientDistributionVO


T = TypeVar("T", bound="ClientSignalDistributionVO")


@_attrs_define
class ClientSignalDistributionVO:
    """
    Attributes:
        poor_signal (ClientDistributionVO | Unset):
        weak_signal (ClientDistributionVO | Unset):
        average_signal (ClientDistributionVO | Unset):
        stable_signal (ClientDistributionVO | Unset):
        strong_signal (ClientDistributionVO | Unset):
    """

    poor_signal: ClientDistributionVO | Unset = UNSET
    weak_signal: ClientDistributionVO | Unset = UNSET
    average_signal: ClientDistributionVO | Unset = UNSET
    stable_signal: ClientDistributionVO | Unset = UNSET
    strong_signal: ClientDistributionVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        poor_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poor_signal, Unset):
            poor_signal = self.poor_signal.to_dict()

        weak_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weak_signal, Unset):
            weak_signal = self.weak_signal.to_dict()

        average_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.average_signal, Unset):
            average_signal = self.average_signal.to_dict()

        stable_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stable_signal, Unset):
            stable_signal = self.stable_signal.to_dict()

        strong_signal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strong_signal, Unset):
            strong_signal = self.strong_signal.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if poor_signal is not UNSET:
            field_dict["poorSignal"] = poor_signal
        if weak_signal is not UNSET:
            field_dict["weakSignal"] = weak_signal
        if average_signal is not UNSET:
            field_dict["averageSignal"] = average_signal
        if stable_signal is not UNSET:
            field_dict["stableSignal"] = stable_signal
        if strong_signal is not UNSET:
            field_dict["strongSignal"] = strong_signal

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_distribution_vo import (
            ClientDistributionVO,
        )

        d = dict(src_dict)
        _poor_signal = d.pop("poorSignal", UNSET)
        poor_signal: ClientDistributionVO | Unset
        if isinstance(_poor_signal, Unset):
            poor_signal = UNSET
        else:
            poor_signal = ClientDistributionVO.from_dict(_poor_signal)

        _weak_signal = d.pop("weakSignal", UNSET)
        weak_signal: ClientDistributionVO | Unset
        if isinstance(_weak_signal, Unset):
            weak_signal = UNSET
        else:
            weak_signal = ClientDistributionVO.from_dict(_weak_signal)

        _average_signal = d.pop("averageSignal", UNSET)
        average_signal: ClientDistributionVO | Unset
        if isinstance(_average_signal, Unset):
            average_signal = UNSET
        else:
            average_signal = ClientDistributionVO.from_dict(_average_signal)

        _stable_signal = d.pop("stableSignal", UNSET)
        stable_signal: ClientDistributionVO | Unset
        if isinstance(_stable_signal, Unset):
            stable_signal = UNSET
        else:
            stable_signal = ClientDistributionVO.from_dict(_stable_signal)

        _strong_signal = d.pop("strongSignal", UNSET)
        strong_signal: ClientDistributionVO | Unset
        if isinstance(_strong_signal, Unset):
            strong_signal = UNSET
        else:
            strong_signal = ClientDistributionVO.from_dict(_strong_signal)

        client_signal_distribution_vo = cls(
            poor_signal=poor_signal,
            weak_signal=weak_signal,
            average_signal=average_signal,
            stable_signal=stable_signal,
            strong_signal=strong_signal,
        )

        client_signal_distribution_vo.additional_properties = d
        return client_signal_distribution_vo

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
