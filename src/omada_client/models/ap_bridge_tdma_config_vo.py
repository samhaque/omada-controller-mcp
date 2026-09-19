from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_client_ap_config_vo import BridgeClientApConfigVO


T = TypeVar("T", bound="ApBridgeTdmaConfigVO")


@_attrs_define
class ApBridgeTdmaConfigVO:
    """Bridge TDMA config.

    Attributes:
        status (int): Bridge TDMA config status. 0: disable, 1: enable.
        clients (list[BridgeClientApConfigVO] | Unset): Bridge TDMA Client config.
    """

    status: int
    clients: list[BridgeClientApConfigVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if clients is not UNSET:
            field_dict["clients"] = clients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bridge_client_ap_config_vo import (
            BridgeClientApConfigVO,
        )

        d = dict(src_dict)
        status = d.pop("status")

        _clients = d.pop("clients", UNSET)
        clients: list[BridgeClientApConfigVO] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = BridgeClientApConfigVO.from_dict(clients_item_data)

                clients.append(clients_item)

        ap_bridge_tdma_config_vo = cls(
            status=status,
            clients=clients,
        )

        ap_bridge_tdma_config_vo.additional_properties = d
        return ap_bridge_tdma_config_vo

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
