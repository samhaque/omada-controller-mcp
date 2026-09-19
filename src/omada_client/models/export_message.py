from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportMessage")


@_attrs_define
class ExportMessage:
    """
    Attributes:
        type_ (int): Message parameter [type] should be 0 or 1. 0:inbox; 1:outbox.
        format_ (int): Message parameter [format] should be 0 or 1. 0:csv; 1:xlsx.
        start_time (int): The timeStamp of the message start time.
        end_time (int): The timeStamp of the message end time.
        sim_card (int | Unset): When the device supports Dual-SIM cardm parameter [simCard] should be 1 or 2. 1: SIM1;
            2: SIM2.
    """

    type_: int
    format_: int
    start_time: int
    end_time: int
    sim_card: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        format_ = self.format_

        start_time = self.start_time

        end_time = self.end_time

        sim_card = self.sim_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "format": format_,
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        format_ = d.pop("format")

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        sim_card = d.pop("simCard", UNSET)

        export_message = cls(
            type_=type_,
            format_=format_,
            start_time=start_time,
            end_time=end_time,
            sim_card=sim_card,
        )

        export_message.additional_properties = d
        return export_message

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
