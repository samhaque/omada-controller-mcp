from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_detail_int_property_dto import OswStackDetailIntPropertyDTO
    from ..models.osw_stack_detail_long_property_dto import (
        OswStackDetailLongPropertyDTO,
    )


T = TypeVar("T", bound="OswStackDetailStatVO")


@_attrs_define
class OswStackDetailStatVO:
    """
    Attributes:
        time (int | Unset): Time
        cpu (list[OswStackDetailIntPropertyDTO] | Unset): Cpu Utilization information
        mem (list[OswStackDetailIntPropertyDTO] | Unset): Memory Utilization information
        drop_pkts (list[OswStackDetailLongPropertyDTO] | Unset): Drop Packets information
        tx_err_pkts (list[OswStackDetailLongPropertyDTO] | Unset): Transmit error packets information
        rx_err_pkts (list[OswStackDetailLongPropertyDTO] | Unset): Receive error packets information
    """

    time: int | Unset = UNSET
    cpu: list[OswStackDetailIntPropertyDTO] | Unset = UNSET
    mem: list[OswStackDetailIntPropertyDTO] | Unset = UNSET
    drop_pkts: list[OswStackDetailLongPropertyDTO] | Unset = UNSET
    tx_err_pkts: list[OswStackDetailLongPropertyDTO] | Unset = UNSET
    rx_err_pkts: list[OswStackDetailLongPropertyDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        cpu: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cpu, Unset):
            cpu = []
            for cpu_item_data in self.cpu:
                cpu_item = cpu_item_data.to_dict()
                cpu.append(cpu_item)

        mem: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mem, Unset):
            mem = []
            for mem_item_data in self.mem:
                mem_item = mem_item_data.to_dict()
                mem.append(mem_item)

        drop_pkts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drop_pkts, Unset):
            drop_pkts = []
            for drop_pkts_item_data in self.drop_pkts:
                drop_pkts_item = drop_pkts_item_data.to_dict()
                drop_pkts.append(drop_pkts_item)

        tx_err_pkts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tx_err_pkts, Unset):
            tx_err_pkts = []
            for tx_err_pkts_item_data in self.tx_err_pkts:
                tx_err_pkts_item = tx_err_pkts_item_data.to_dict()
                tx_err_pkts.append(tx_err_pkts_item)

        rx_err_pkts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rx_err_pkts, Unset):
            rx_err_pkts = []
            for rx_err_pkts_item_data in self.rx_err_pkts:
                rx_err_pkts_item = rx_err_pkts_item_data.to_dict()
                rx_err_pkts.append(rx_err_pkts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if mem is not UNSET:
            field_dict["mem"] = mem
        if drop_pkts is not UNSET:
            field_dict["dropPkts"] = drop_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_detail_int_property_dto import (
            OswStackDetailIntPropertyDTO,
        )
        from ..models.osw_stack_detail_long_property_dto import (
            OswStackDetailLongPropertyDTO,
        )

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        _cpu = d.pop("cpu", UNSET)
        cpu: list[OswStackDetailIntPropertyDTO] | Unset = UNSET
        if _cpu is not UNSET:
            cpu = []
            for cpu_item_data in _cpu:
                cpu_item = OswStackDetailIntPropertyDTO.from_dict(cpu_item_data)

                cpu.append(cpu_item)

        _mem = d.pop("mem", UNSET)
        mem: list[OswStackDetailIntPropertyDTO] | Unset = UNSET
        if _mem is not UNSET:
            mem = []
            for mem_item_data in _mem:
                mem_item = OswStackDetailIntPropertyDTO.from_dict(mem_item_data)

                mem.append(mem_item)

        _drop_pkts = d.pop("dropPkts", UNSET)
        drop_pkts: list[OswStackDetailLongPropertyDTO] | Unset = UNSET
        if _drop_pkts is not UNSET:
            drop_pkts = []
            for drop_pkts_item_data in _drop_pkts:
                drop_pkts_item = OswStackDetailLongPropertyDTO.from_dict(
                    drop_pkts_item_data
                )

                drop_pkts.append(drop_pkts_item)

        _tx_err_pkts = d.pop("txErrPkts", UNSET)
        tx_err_pkts: list[OswStackDetailLongPropertyDTO] | Unset = UNSET
        if _tx_err_pkts is not UNSET:
            tx_err_pkts = []
            for tx_err_pkts_item_data in _tx_err_pkts:
                tx_err_pkts_item = OswStackDetailLongPropertyDTO.from_dict(
                    tx_err_pkts_item_data
                )

                tx_err_pkts.append(tx_err_pkts_item)

        _rx_err_pkts = d.pop("rxErrPkts", UNSET)
        rx_err_pkts: list[OswStackDetailLongPropertyDTO] | Unset = UNSET
        if _rx_err_pkts is not UNSET:
            rx_err_pkts = []
            for rx_err_pkts_item_data in _rx_err_pkts:
                rx_err_pkts_item = OswStackDetailLongPropertyDTO.from_dict(
                    rx_err_pkts_item_data
                )

                rx_err_pkts.append(rx_err_pkts_item)

        osw_stack_detail_stat_vo = cls(
            time=time,
            cpu=cpu,
            mem=mem,
            drop_pkts=drop_pkts,
            tx_err_pkts=tx_err_pkts,
            rx_err_pkts=rx_err_pkts,
        )

        osw_stack_detail_stat_vo.additional_properties = d
        return osw_stack_detail_stat_vo

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
