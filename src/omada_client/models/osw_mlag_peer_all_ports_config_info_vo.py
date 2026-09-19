from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswMlagPeerAllPortsConfigInfoVO")


@_attrs_define
class OswMlagPeerAllPortsConfigInfoVO:
    """Configuration information of all M-LAG Peer ports, used to determine whether the port can be selected

    Attributes:
        all_aggregating_ports (list[int] | Unset): all aggregating ports of M-LAG Peer Switch
        all_mirroring_ports (list[int] | Unset): all mirroring ports of M-LAG Peer Switch
        all_mirrored_ports (list[int] | Unset): all mirrored ports of M-LAG Peer Switch
        all_mlag_peer_link_ports (list[int] | Unset): all M-LAG PeerLink ports of M-LAG Peer Switch
        all_mlag_dad_ports (list[int] | Unset): all M-LAG DAD ports of M-LAG Peer Switch
    """

    all_aggregating_ports: list[int] | Unset = UNSET
    all_mirroring_ports: list[int] | Unset = UNSET
    all_mirrored_ports: list[int] | Unset = UNSET
    all_mlag_peer_link_ports: list[int] | Unset = UNSET
    all_mlag_dad_ports: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_aggregating_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_aggregating_ports, Unset):
            all_aggregating_ports = self.all_aggregating_ports

        all_mirroring_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mirroring_ports, Unset):
            all_mirroring_ports = self.all_mirroring_ports

        all_mirrored_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mirrored_ports, Unset):
            all_mirrored_ports = self.all_mirrored_ports

        all_mlag_peer_link_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mlag_peer_link_ports, Unset):
            all_mlag_peer_link_ports = self.all_mlag_peer_link_ports

        all_mlag_dad_ports: list[int] | Unset = UNSET
        if not isinstance(self.all_mlag_dad_ports, Unset):
            all_mlag_dad_ports = self.all_mlag_dad_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_aggregating_ports is not UNSET:
            field_dict["allAggregatingPorts"] = all_aggregating_ports
        if all_mirroring_ports is not UNSET:
            field_dict["allMirroringPorts"] = all_mirroring_ports
        if all_mirrored_ports is not UNSET:
            field_dict["allMirroredPorts"] = all_mirrored_ports
        if all_mlag_peer_link_ports is not UNSET:
            field_dict["allMlagPeerLinkPorts"] = all_mlag_peer_link_ports
        if all_mlag_dad_ports is not UNSET:
            field_dict["allMlagDadPorts"] = all_mlag_dad_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_aggregating_ports = cast(list[int], d.pop("allAggregatingPorts", UNSET))

        all_mirroring_ports = cast(list[int], d.pop("allMirroringPorts", UNSET))

        all_mirrored_ports = cast(list[int], d.pop("allMirroredPorts", UNSET))

        all_mlag_peer_link_ports = cast(list[int], d.pop("allMlagPeerLinkPorts", UNSET))

        all_mlag_dad_ports = cast(list[int], d.pop("allMlagDadPorts", UNSET))

        osw_mlag_peer_all_ports_config_info_vo = cls(
            all_aggregating_ports=all_aggregating_ports,
            all_mirroring_ports=all_mirroring_ports,
            all_mirrored_ports=all_mirrored_ports,
            all_mlag_peer_link_ports=all_mlag_peer_link_ports,
            all_mlag_dad_ports=all_mlag_dad_ports,
        )

        osw_mlag_peer_all_ports_config_info_vo.additional_properties = d
        return osw_mlag_peer_all_ports_config_info_vo

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
