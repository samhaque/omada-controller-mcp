from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_client_vo import OswClientVO
    from ..models.osw_port_and_lag_network_vo import OswPortAndLagNetworkVO
    from ..models.osw_stack_detail_vo import OswStackDetailVO
    from ..models.osw_stack_member_lag_vo import OswStackMemberLagVO


T = TypeVar("T", bound="VlanNetworkAffectingStackDetailVO")


@_attrs_define
class VlanNetworkAffectingStackDetailVO:
    """Stack info, only valid when type is switch and stackId is not empty.

    Attributes:
        affected_ports (OswPortAndLagNetworkVO | Unset): OswPortAndLagNetworkVO
        clients (list[OswClientVO] | Unset): Switch downlink clients.
        support_layout (bool | Unset): Whether the device supports reporting port layout information.
        stack_detail (OswStackDetailVO | Unset): Stack detail
        stack_lags (list[OswStackMemberLagVO] | Unset): Stack lags
    """

    affected_ports: OswPortAndLagNetworkVO | Unset = UNSET
    clients: list[OswClientVO] | Unset = UNSET
    support_layout: bool | Unset = UNSET
    stack_detail: OswStackDetailVO | Unset = UNSET
    stack_lags: list[OswStackMemberLagVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affected_ports, Unset):
            affected_ports = self.affected_ports.to_dict()

        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        support_layout = self.support_layout

        stack_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_detail, Unset):
            stack_detail = self.stack_detail.to_dict()

        stack_lags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_lags, Unset):
            stack_lags = []
            for stack_lags_item_data in self.stack_lags:
                stack_lags_item = stack_lags_item_data.to_dict()
                stack_lags.append(stack_lags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_ports is not UNSET:
            field_dict["affectedPorts"] = affected_ports
        if clients is not UNSET:
            field_dict["clients"] = clients
        if support_layout is not UNSET:
            field_dict["supportLayout"] = support_layout
        if stack_detail is not UNSET:
            field_dict["stackDetail"] = stack_detail
        if stack_lags is not UNSET:
            field_dict["stackLags"] = stack_lags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_client_vo import OswClientVO
        from ..models.osw_port_and_lag_network_vo import (
            OswPortAndLagNetworkVO,
        )
        from ..models.osw_stack_detail_vo import OswStackDetailVO
        from ..models.osw_stack_member_lag_vo import (
            OswStackMemberLagVO,
        )

        d = dict(src_dict)
        _affected_ports = d.pop("affectedPorts", UNSET)
        affected_ports: OswPortAndLagNetworkVO | Unset
        if isinstance(_affected_ports, Unset):
            affected_ports = UNSET
        else:
            affected_ports = OswPortAndLagNetworkVO.from_dict(_affected_ports)

        _clients = d.pop("clients", UNSET)
        clients: list[OswClientVO] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = OswClientVO.from_dict(clients_item_data)

                clients.append(clients_item)

        support_layout = d.pop("supportLayout", UNSET)

        _stack_detail = d.pop("stackDetail", UNSET)
        stack_detail: OswStackDetailVO | Unset
        if isinstance(_stack_detail, Unset):
            stack_detail = UNSET
        else:
            stack_detail = OswStackDetailVO.from_dict(_stack_detail)

        _stack_lags = d.pop("stackLags", UNSET)
        stack_lags: list[OswStackMemberLagVO] | Unset = UNSET
        if _stack_lags is not UNSET:
            stack_lags = []
            for stack_lags_item_data in _stack_lags:
                stack_lags_item = OswStackMemberLagVO.from_dict(stack_lags_item_data)

                stack_lags.append(stack_lags_item)

        vlan_network_affecting_stack_detail_vo = cls(
            affected_ports=affected_ports,
            clients=clients,
            support_layout=support_layout,
            stack_detail=stack_detail,
            stack_lags=stack_lags,
        )

        vlan_network_affecting_stack_detail_vo.additional_properties = d
        return vlan_network_affecting_stack_detail_vo

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
