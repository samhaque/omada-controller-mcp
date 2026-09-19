from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_query_mac_and_filter_type import ClientsQueryMacAndFilterType
    from ..models.topology_open_api_status_vo_stp_loops import (
        TopologyOpenApiStatusVOStpLoops,
    )


T = TypeVar("T", bound="TopologyOpenApiStatusVO")


@_attrs_define
class TopologyOpenApiStatusVO:
    """Topology Related Status

    Attributes:
        exist_um_vms_dev (bool | Unset): Whether Unmanaged Vms Devices Exist
        connected (int | Unset): Connected Devices Count
        disconnected (int | Unset): Disconnected Devices Count
        client2g (int | Unset): 2g Client Count
        client5g (int | Unset): 5g Client Count
        client6g (int | Unset): 6g Client Count
        wired_client (int | Unset): Wired Client Count
        directly_show_clients_device_macs (list[ClientsQueryMacAndFilterType] | Unset): Devices Macs That Show Clients
            Directly
        stp_loops (TopologyOpenApiStatusVOStpLoops | Unset): Stp Loops
    """

    exist_um_vms_dev: bool | Unset = UNSET
    connected: int | Unset = UNSET
    disconnected: int | Unset = UNSET
    client2g: int | Unset = UNSET
    client5g: int | Unset = UNSET
    client6g: int | Unset = UNSET
    wired_client: int | Unset = UNSET
    directly_show_clients_device_macs: list[ClientsQueryMacAndFilterType] | Unset = (
        UNSET
    )
    stp_loops: TopologyOpenApiStatusVOStpLoops | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exist_um_vms_dev = self.exist_um_vms_dev

        connected = self.connected

        disconnected = self.disconnected

        client2g = self.client2g

        client5g = self.client5g

        client6g = self.client6g

        wired_client = self.wired_client

        directly_show_clients_device_macs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.directly_show_clients_device_macs, Unset):
            directly_show_clients_device_macs = []
            for (
                directly_show_clients_device_macs_item_data
            ) in self.directly_show_clients_device_macs:
                directly_show_clients_device_macs_item = (
                    directly_show_clients_device_macs_item_data.to_dict()
                )
                directly_show_clients_device_macs.append(
                    directly_show_clients_device_macs_item
                )

        stp_loops: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stp_loops, Unset):
            stp_loops = self.stp_loops.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exist_um_vms_dev is not UNSET:
            field_dict["existUMVmsDev"] = exist_um_vms_dev
        if connected is not UNSET:
            field_dict["connected"] = connected
        if disconnected is not UNSET:
            field_dict["disconnected"] = disconnected
        if client2g is not UNSET:
            field_dict["client2g"] = client2g
        if client5g is not UNSET:
            field_dict["client5g"] = client5g
        if client6g is not UNSET:
            field_dict["client6g"] = client6g
        if wired_client is not UNSET:
            field_dict["wiredClient"] = wired_client
        if directly_show_clients_device_macs is not UNSET:
            field_dict["directlyShowClientsDeviceMacs"] = (
                directly_show_clients_device_macs
            )
        if stp_loops is not UNSET:
            field_dict["stpLoops"] = stp_loops

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_query_mac_and_filter_type import (
            ClientsQueryMacAndFilterType,
        )
        from ..models.topology_open_api_status_vo_stp_loops import (
            TopologyOpenApiStatusVOStpLoops,
        )

        d = dict(src_dict)
        exist_um_vms_dev = d.pop("existUMVmsDev", UNSET)

        connected = d.pop("connected", UNSET)

        disconnected = d.pop("disconnected", UNSET)

        client2g = d.pop("client2g", UNSET)

        client5g = d.pop("client5g", UNSET)

        client6g = d.pop("client6g", UNSET)

        wired_client = d.pop("wiredClient", UNSET)

        _directly_show_clients_device_macs = d.pop(
            "directlyShowClientsDeviceMacs", UNSET
        )
        directly_show_clients_device_macs: (
            list[ClientsQueryMacAndFilterType] | Unset
        ) = UNSET
        if _directly_show_clients_device_macs is not UNSET:
            directly_show_clients_device_macs = []
            for (
                directly_show_clients_device_macs_item_data
            ) in _directly_show_clients_device_macs:
                directly_show_clients_device_macs_item = (
                    ClientsQueryMacAndFilterType.from_dict(
                        directly_show_clients_device_macs_item_data
                    )
                )

                directly_show_clients_device_macs.append(
                    directly_show_clients_device_macs_item
                )

        _stp_loops = d.pop("stpLoops", UNSET)
        stp_loops: TopologyOpenApiStatusVOStpLoops | Unset
        if isinstance(_stp_loops, Unset):
            stp_loops = UNSET
        else:
            stp_loops = TopologyOpenApiStatusVOStpLoops.from_dict(_stp_loops)

        topology_open_api_status_vo = cls(
            exist_um_vms_dev=exist_um_vms_dev,
            connected=connected,
            disconnected=disconnected,
            client2g=client2g,
            client5g=client5g,
            client6g=client6g,
            wired_client=wired_client,
            directly_show_clients_device_macs=directly_show_clients_device_macs,
            stp_loops=stp_loops,
        )

        topology_open_api_status_vo.additional_properties = d
        return topology_open_api_status_vo

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
