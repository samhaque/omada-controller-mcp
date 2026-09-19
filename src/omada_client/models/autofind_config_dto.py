from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.autofind_config_dto_aging_time_status import (
    AutofindConfigDTOAgingTimeStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutofindConfigDTO")


@_attrs_define
class AutofindConfigDTO:
    """
    Attributes:
        aging_time_status (AutofindConfigDTOAgingTimeStatus): Configure the DDM (Digital Diagnostic Monitoring) feature
            enable status for the optical port.AgingTimeStatus should be a value as follows:TIMEOUT,NO_AGING
        autofind_interval (int): Auto find interval should be within the range of 1 to 10s
        pon_port (str | Unset): Pon port collection.e.g.,'GPON 1/1/1'、'GPON 1/1/1-3'、'GPON 1/1/1-3,GPON 1/1/5,GPON
            1/1/7-8'
        aging_time (int | Unset): Configure the actions corresponding to received DDM messages on the optical port.If
            aging time status is 'No-Aging',AgingTime should be null;If aging time status is 'Timeout',AgingTime should not
            be null and should be within the range of 100 to 300s.
    """

    aging_time_status: AutofindConfigDTOAgingTimeStatus
    autofind_interval: int
    pon_port: str | Unset = UNSET
    aging_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aging_time_status = self.aging_time_status.value

        autofind_interval = self.autofind_interval

        pon_port = self.pon_port

        aging_time = self.aging_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agingTimeStatus": aging_time_status,
                "autofindInterval": autofind_interval,
            }
        )
        if pon_port is not UNSET:
            field_dict["ponPort"] = pon_port
        if aging_time is not UNSET:
            field_dict["agingTime"] = aging_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        aging_time_status = AutofindConfigDTOAgingTimeStatus(d.pop("agingTimeStatus"))

        autofind_interval = d.pop("autofindInterval")

        pon_port = d.pop("ponPort", UNSET)

        aging_time = d.pop("agingTime", UNSET)

        autofind_config_dto = cls(
            aging_time_status=aging_time_status,
            autofind_interval=autofind_interval,
            pon_port=pon_port,
            aging_time=aging_time,
        )

        autofind_config_dto.additional_properties = d
        return autofind_config_dto

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
