from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.reboot_schedule_time_open_api_vo import RebootScheduleTimeOpenApiVO


T = TypeVar("T", bound="RebootScheduleTemplateOpenApiVO")


@_attrs_define
class RebootScheduleTemplateOpenApiVO:
    """
    Attributes:
        name (str): Reboot Schedule name should contain 1 to 128 characters.
        status (bool): Reboot Schedule status.
        time (RebootScheduleTimeOpenApiVO): Execution time setting.
    """

    name: str
    status: bool
    time: RebootScheduleTimeOpenApiVO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        time = self.time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "time": time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.reboot_schedule_time_open_api_vo import (
            RebootScheduleTimeOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        time = RebootScheduleTimeOpenApiVO.from_dict(d.pop("time"))

        reboot_schedule_template_open_api_vo = cls(
            name=name,
            status=status,
            time=time,
        )

        reboot_schedule_template_open_api_vo.additional_properties = d
        return reboot_schedule_template_open_api_vo

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
