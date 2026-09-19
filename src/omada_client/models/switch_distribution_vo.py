from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_client_vo import DeviceClientVO


T = TypeVar("T", bound="SwitchDistributionVO")


@_attrs_define
class SwitchDistributionVO:
    """
    Attributes:
        switches (list[DeviceClientVO] | Unset):
        others (DeviceClientVO | Unset):
        total_switch_clients (int | Unset):
        total_switch_distribution (float | Unset):
    """

    switches: list[DeviceClientVO] | Unset = UNSET
    others: DeviceClientVO | Unset = UNSET
    total_switch_clients: int | Unset = UNSET
    total_switch_distribution: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        switches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switches, Unset):
            switches = []
            for switches_item_data in self.switches:
                switches_item = switches_item_data.to_dict()
                switches.append(switches_item)

        others: dict[str, Any] | Unset = UNSET
        if not isinstance(self.others, Unset):
            others = self.others.to_dict()

        total_switch_clients = self.total_switch_clients

        total_switch_distribution = self.total_switch_distribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if switches is not UNSET:
            field_dict["switches"] = switches
        if others is not UNSET:
            field_dict["others"] = others
        if total_switch_clients is not UNSET:
            field_dict["totalSwitchClients"] = total_switch_clients
        if total_switch_distribution is not UNSET:
            field_dict["totalSwitchDistribution"] = total_switch_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_client_vo import DeviceClientVO

        d = dict(src_dict)
        _switches = d.pop("switches", UNSET)
        switches: list[DeviceClientVO] | Unset = UNSET
        if _switches is not UNSET:
            switches = []
            for switches_item_data in _switches:
                switches_item = DeviceClientVO.from_dict(switches_item_data)

                switches.append(switches_item)

        _others = d.pop("others", UNSET)
        others: DeviceClientVO | Unset
        if isinstance(_others, Unset):
            others = UNSET
        else:
            others = DeviceClientVO.from_dict(_others)

        total_switch_clients = d.pop("totalSwitchClients", UNSET)

        total_switch_distribution = d.pop("totalSwitchDistribution", UNSET)

        switch_distribution_vo = cls(
            switches=switches,
            others=others,
            total_switch_clients=total_switch_clients,
            total_switch_distribution=total_switch_distribution,
        )

        switch_distribution_vo.additional_properties = d
        return switch_distribution_vo

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
