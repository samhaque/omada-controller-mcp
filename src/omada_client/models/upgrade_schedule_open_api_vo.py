from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_schedule_time_open_api_vo import BaseScheduleTimeOpenApiVO


T = TypeVar("T", bound="UpgradeScheduleOpenApiVO")


@_attrs_define
class UpgradeScheduleOpenApiVO:
    """
    Attributes:
        name (str): Upgrade schedule name should contain 1 to 128 characters.
        status (bool): Upgrade schedule status.
        type_ (int): Type should be a value as follows: 0: execute only once; 1: repeat
        device_macs (list[str]): MAC address of the selected devices. E.g. AA-BB-CC-DD-11-22
        next_execute_time (int | Unset): Execution timeStamp(ms). Required when type is 0.
        occurrence_time (BaseScheduleTimeOpenApiVO | Unset): Execution occurrence setting. Required when type is 1.
    """

    name: str
    status: bool
    type_: int
    device_macs: list[str]
    next_execute_time: int | Unset = UNSET
    occurrence_time: BaseScheduleTimeOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        type_ = self.type_

        device_macs = self.device_macs

        next_execute_time = self.next_execute_time

        occurrence_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence_time, Unset):
            occurrence_time = self.occurrence_time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "type": type_,
                "deviceMacs": device_macs,
            }
        )
        if next_execute_time is not UNSET:
            field_dict["nextExecuteTime"] = next_execute_time
        if occurrence_time is not UNSET:
            field_dict["occurrenceTime"] = occurrence_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_schedule_time_open_api_vo import (
            BaseScheduleTimeOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        type_ = d.pop("type")

        device_macs = cast(list[str], d.pop("deviceMacs"))

        next_execute_time = d.pop("nextExecuteTime", UNSET)

        _occurrence_time = d.pop("occurrenceTime", UNSET)
        occurrence_time: BaseScheduleTimeOpenApiVO | Unset
        if isinstance(_occurrence_time, Unset):
            occurrence_time = UNSET
        else:
            occurrence_time = BaseScheduleTimeOpenApiVO.from_dict(_occurrence_time)

        upgrade_schedule_open_api_vo = cls(
            name=name,
            status=status,
            type_=type_,
            device_macs=device_macs,
            next_execute_time=next_execute_time,
            occurrence_time=occurrence_time,
        )

        upgrade_schedule_open_api_vo.additional_properties = d
        return upgrade_schedule_open_api_vo

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
