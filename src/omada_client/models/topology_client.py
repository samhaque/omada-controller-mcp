from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_client_uplink_ap_info import TopologyClientUplinkApInfo
    from ..models.topology_client_uplink_gateway_info import (
        TopologyClientUplinkGatewayInfo,
    )
    from ..models.topology_client_uplink_switch_info import (
        TopologyClientUplinkSwitchInfo,
    )


T = TypeVar("T", bound="TopologyClient")


@_attrs_define
class TopologyClient:
    """Client In Topology.

    Attributes:
        mac (str | Unset): Client MAC address, like AA-BB-CC-DD-EE-FF.
        name (str | Unset): Client name.
        wireless (bool | Unset): Whether the client is wireless.
        uplink_switch_info (TopologyClientUplinkSwitchInfo | Unset): Uplink Information while Uplink Device is Switch.
        uplink_ap_info (TopologyClientUplinkApInfo | Unset): Uplink Information while Uplink Device is Ap.
        uplink_gateway_info (TopologyClientUplinkGatewayInfo | Unset): Uplink Information while Uplink Device is
            Gateway.
        guest (bool | Unset): Whether the client is a guest.
        type_ (str | Unset): Client Type.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    uplink_switch_info: TopologyClientUplinkSwitchInfo | Unset = UNSET
    uplink_ap_info: TopologyClientUplinkApInfo | Unset = UNSET
    uplink_gateway_info: TopologyClientUplinkGatewayInfo | Unset = UNSET
    guest: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        wireless = self.wireless

        uplink_switch_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink_switch_info, Unset):
            uplink_switch_info = self.uplink_switch_info.to_dict()

        uplink_ap_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink_ap_info, Unset):
            uplink_ap_info = self.uplink_ap_info.to_dict()

        uplink_gateway_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink_gateway_info, Unset):
            uplink_gateway_info = self.uplink_gateway_info.to_dict()

        guest = self.guest

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if uplink_switch_info is not UNSET:
            field_dict["uplinkSwitchInfo"] = uplink_switch_info
        if uplink_ap_info is not UNSET:
            field_dict["uplinkApInfo"] = uplink_ap_info
        if uplink_gateway_info is not UNSET:
            field_dict["uplinkGatewayInfo"] = uplink_gateway_info
        if guest is not UNSET:
            field_dict["guest"] = guest
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_client_uplink_ap_info import (
            TopologyClientUplinkApInfo,
        )
        from ..models.topology_client_uplink_gateway_info import (
            TopologyClientUplinkGatewayInfo,
        )
        from ..models.topology_client_uplink_switch_info import (
            TopologyClientUplinkSwitchInfo,
        )

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        wireless = d.pop("wireless", UNSET)

        _uplink_switch_info = d.pop("uplinkSwitchInfo", UNSET)
        uplink_switch_info: TopologyClientUplinkSwitchInfo | Unset
        if isinstance(_uplink_switch_info, Unset):
            uplink_switch_info = UNSET
        else:
            uplink_switch_info = TopologyClientUplinkSwitchInfo.from_dict(
                _uplink_switch_info
            )

        _uplink_ap_info = d.pop("uplinkApInfo", UNSET)
        uplink_ap_info: TopologyClientUplinkApInfo | Unset
        if isinstance(_uplink_ap_info, Unset):
            uplink_ap_info = UNSET
        else:
            uplink_ap_info = TopologyClientUplinkApInfo.from_dict(_uplink_ap_info)

        _uplink_gateway_info = d.pop("uplinkGatewayInfo", UNSET)
        uplink_gateway_info: TopologyClientUplinkGatewayInfo | Unset
        if isinstance(_uplink_gateway_info, Unset):
            uplink_gateway_info = UNSET
        else:
            uplink_gateway_info = TopologyClientUplinkGatewayInfo.from_dict(
                _uplink_gateway_info
            )

        guest = d.pop("guest", UNSET)

        type_ = d.pop("type", UNSET)

        topology_client = cls(
            mac=mac,
            name=name,
            wireless=wireless,
            uplink_switch_info=uplink_switch_info,
            uplink_ap_info=uplink_ap_info,
            uplink_gateway_info=uplink_gateway_info,
            guest=guest,
            type_=type_,
        )

        topology_client.additional_properties = d
        return topology_client

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
