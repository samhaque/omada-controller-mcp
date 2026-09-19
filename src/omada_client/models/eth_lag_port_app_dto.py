from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EthLagPortAppDTO")


@_attrs_define
class EthLagPortAppDTO:
    """
    Attributes:
        lag (str): ID of LAG
        description (str | Unset): Description of port
        status (int | Unset): Port switch status.Status should be a value as follows:0:DISABLE;1:ENABLE
        speed (int | Unset): Port speed negotiation mode. speed should be a value as follows: 0;10;100;1000;2500;10000.0
            represents Auto, and all other values are in Mbps.
        duplex (int | Unset): Port duplex negotiation mode.Duplex should be a value as follows: 2:FULL,0:AUTO
        flow_control (int | Unset): Port flow control function switch.FlowControl should be a value as follows:
            0:DISABLE;1:ENABLE
    """

    lag: str
    description: str | Unset = UNSET
    status: int | Unset = UNSET
    speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    flow_control: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lag = self.lag

        description = self.description

        status = self.status

        speed = self.speed

        duplex = self.duplex

        flow_control = self.flow_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lag": lag,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if speed is not UNSET:
            field_dict["speed"] = speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if flow_control is not UNSET:
            field_dict["flowControl"] = flow_control

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lag = d.pop("lag")

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        speed = d.pop("speed", UNSET)

        duplex = d.pop("duplex", UNSET)

        flow_control = d.pop("flowControl", UNSET)

        eth_lag_port_app_dto = cls(
            lag=lag,
            description=description,
            status=status,
            speed=speed,
            duplex=duplex,
            flow_control=flow_control,
        )

        eth_lag_port_app_dto.additional_properties = d
        return eth_lag_port_app_dto

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
