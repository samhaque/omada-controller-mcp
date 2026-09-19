from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_bridge_not_support_tdma_client_ap_open_api_vo import (
        ApBridgeNotSupportTdmaClientApOpenApiVO,
    )
    from ..models.ap_bridge_tdma_client_ap_open_api_vo import (
        ApBridgeTdmaClientApOpenApiVO,
    )


T = TypeVar("T", bound="ApBridgeTdmaSettingOpenApiVO")


@_attrs_define
class ApBridgeTdmaSettingOpenApiVO:
    """Bridge TDMA config.

    Attributes:
        status (int | Unset): Bridge TDMA Switch config status. 0: disable, 1: enable.
        clients (list[ApBridgeTdmaClientApOpenApiVO] | Unset): Bridge TDMA Client AP config.
        not_support_tdma_clients (list[ApBridgeNotSupportTdmaClientApOpenApiVO] | Unset): Bridge Not Support TDMA Client
            AP info.
    """

    status: int | Unset = UNSET
    clients: list[ApBridgeTdmaClientApOpenApiVO] | Unset = UNSET
    not_support_tdma_clients: list[ApBridgeNotSupportTdmaClientApOpenApiVO] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        not_support_tdma_clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.not_support_tdma_clients, Unset):
            not_support_tdma_clients = []
            for not_support_tdma_clients_item_data in self.not_support_tdma_clients:
                not_support_tdma_clients_item = (
                    not_support_tdma_clients_item_data.to_dict()
                )
                not_support_tdma_clients.append(not_support_tdma_clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if clients is not UNSET:
            field_dict["clients"] = clients
        if not_support_tdma_clients is not UNSET:
            field_dict["notSupportTdmaClients"] = not_support_tdma_clients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_bridge_not_support_tdma_client_ap_open_api_vo import (
            ApBridgeNotSupportTdmaClientApOpenApiVO,
        )
        from ..models.ap_bridge_tdma_client_ap_open_api_vo import (
            ApBridgeTdmaClientApOpenApiVO,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        _clients = d.pop("clients", UNSET)
        clients: list[ApBridgeTdmaClientApOpenApiVO] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = ApBridgeTdmaClientApOpenApiVO.from_dict(
                    clients_item_data
                )

                clients.append(clients_item)

        _not_support_tdma_clients = d.pop("notSupportTdmaClients", UNSET)
        not_support_tdma_clients: (
            list[ApBridgeNotSupportTdmaClientApOpenApiVO] | Unset
        ) = UNSET
        if _not_support_tdma_clients is not UNSET:
            not_support_tdma_clients = []
            for not_support_tdma_clients_item_data in _not_support_tdma_clients:
                not_support_tdma_clients_item = (
                    ApBridgeNotSupportTdmaClientApOpenApiVO.from_dict(
                        not_support_tdma_clients_item_data
                    )
                )

                not_support_tdma_clients.append(not_support_tdma_clients_item)

        ap_bridge_tdma_setting_open_api_vo = cls(
            status=status,
            clients=clients,
            not_support_tdma_clients=not_support_tdma_clients,
        )

        ap_bridge_tdma_setting_open_api_vo.additional_properties = d
        return ap_bridge_tdma_setting_open_api_vo

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
