from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_osw_health_open_api_vo import ActiveOswHealthOpenApiVO
    from ..models.top_cpu_usage_health_open_api_vo import TopCpuUsageHealthOpenApiVO
    from ..models.top_mem_usage_health_open_api_vo import TopMemUsageHealthOpenApiVO
    from ..models.top_osw_error_packet_open_api_vo import TopOswErrorPacketOpenApiVO
    from ..models.top_osw_packet_loss_open_api_vo import TopOswPacketLossOpenApiVO


T = TypeVar("T", bound="OswRankingCardsOpenApiVO")


@_attrs_define
class OswRankingCardsOpenApiVO:
    """
    Attributes:
        top_active_switches (list[ActiveOswHealthOpenApiVO] | Unset): Active switches information list
        top_cpu (list[TopCpuUsageHealthOpenApiVO] | Unset): Cpu information list
        top_mem (list[TopMemUsageHealthOpenApiVO] | Unset): Memory information list
        top_packets_loss (list[TopOswPacketLossOpenApiVO] | Unset): Packet loss information list
        top_packets_error (list[TopOswErrorPacketOpenApiVO] | Unset): Packet error information list
    """

    top_active_switches: list[ActiveOswHealthOpenApiVO] | Unset = UNSET
    top_cpu: list[TopCpuUsageHealthOpenApiVO] | Unset = UNSET
    top_mem: list[TopMemUsageHealthOpenApiVO] | Unset = UNSET
    top_packets_loss: list[TopOswPacketLossOpenApiVO] | Unset = UNSET
    top_packets_error: list[TopOswErrorPacketOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_active_switches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_active_switches, Unset):
            top_active_switches = []
            for top_active_switches_item_data in self.top_active_switches:
                top_active_switches_item = top_active_switches_item_data.to_dict()
                top_active_switches.append(top_active_switches_item)

        top_cpu: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_cpu, Unset):
            top_cpu = []
            for top_cpu_item_data in self.top_cpu:
                top_cpu_item = top_cpu_item_data.to_dict()
                top_cpu.append(top_cpu_item)

        top_mem: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_mem, Unset):
            top_mem = []
            for top_mem_item_data in self.top_mem:
                top_mem_item = top_mem_item_data.to_dict()
                top_mem.append(top_mem_item)

        top_packets_loss: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_packets_loss, Unset):
            top_packets_loss = []
            for top_packets_loss_item_data in self.top_packets_loss:
                top_packets_loss_item = top_packets_loss_item_data.to_dict()
                top_packets_loss.append(top_packets_loss_item)

        top_packets_error: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_packets_error, Unset):
            top_packets_error = []
            for top_packets_error_item_data in self.top_packets_error:
                top_packets_error_item = top_packets_error_item_data.to_dict()
                top_packets_error.append(top_packets_error_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_active_switches is not UNSET:
            field_dict["topActiveSwitches"] = top_active_switches
        if top_cpu is not UNSET:
            field_dict["topCpu"] = top_cpu
        if top_mem is not UNSET:
            field_dict["topMem"] = top_mem
        if top_packets_loss is not UNSET:
            field_dict["topPacketsLoss"] = top_packets_loss
        if top_packets_error is not UNSET:
            field_dict["topPacketsError"] = top_packets_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.active_osw_health_open_api_vo import (
            ActiveOswHealthOpenApiVO,
        )
        from ..models.top_cpu_usage_health_open_api_vo import (
            TopCpuUsageHealthOpenApiVO,
        )
        from ..models.top_mem_usage_health_open_api_vo import (
            TopMemUsageHealthOpenApiVO,
        )
        from ..models.top_osw_error_packet_open_api_vo import (
            TopOswErrorPacketOpenApiVO,
        )
        from ..models.top_osw_packet_loss_open_api_vo import (
            TopOswPacketLossOpenApiVO,
        )

        d = dict(src_dict)
        _top_active_switches = d.pop("topActiveSwitches", UNSET)
        top_active_switches: list[ActiveOswHealthOpenApiVO] | Unset = UNSET
        if _top_active_switches is not UNSET:
            top_active_switches = []
            for top_active_switches_item_data in _top_active_switches:
                top_active_switches_item = ActiveOswHealthOpenApiVO.from_dict(
                    top_active_switches_item_data
                )

                top_active_switches.append(top_active_switches_item)

        _top_cpu = d.pop("topCpu", UNSET)
        top_cpu: list[TopCpuUsageHealthOpenApiVO] | Unset = UNSET
        if _top_cpu is not UNSET:
            top_cpu = []
            for top_cpu_item_data in _top_cpu:
                top_cpu_item = TopCpuUsageHealthOpenApiVO.from_dict(top_cpu_item_data)

                top_cpu.append(top_cpu_item)

        _top_mem = d.pop("topMem", UNSET)
        top_mem: list[TopMemUsageHealthOpenApiVO] | Unset = UNSET
        if _top_mem is not UNSET:
            top_mem = []
            for top_mem_item_data in _top_mem:
                top_mem_item = TopMemUsageHealthOpenApiVO.from_dict(top_mem_item_data)

                top_mem.append(top_mem_item)

        _top_packets_loss = d.pop("topPacketsLoss", UNSET)
        top_packets_loss: list[TopOswPacketLossOpenApiVO] | Unset = UNSET
        if _top_packets_loss is not UNSET:
            top_packets_loss = []
            for top_packets_loss_item_data in _top_packets_loss:
                top_packets_loss_item = TopOswPacketLossOpenApiVO.from_dict(
                    top_packets_loss_item_data
                )

                top_packets_loss.append(top_packets_loss_item)

        _top_packets_error = d.pop("topPacketsError", UNSET)
        top_packets_error: list[TopOswErrorPacketOpenApiVO] | Unset = UNSET
        if _top_packets_error is not UNSET:
            top_packets_error = []
            for top_packets_error_item_data in _top_packets_error:
                top_packets_error_item = TopOswErrorPacketOpenApiVO.from_dict(
                    top_packets_error_item_data
                )

                top_packets_error.append(top_packets_error_item)

        osw_ranking_cards_open_api_vo = cls(
            top_active_switches=top_active_switches,
            top_cpu=top_cpu,
            top_mem=top_mem,
            top_packets_loss=top_packets_loss,
            top_packets_error=top_packets_error,
        )

        osw_ranking_cards_open_api_vo.additional_properties = d
        return osw_ranking_cards_open_api_vo

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
