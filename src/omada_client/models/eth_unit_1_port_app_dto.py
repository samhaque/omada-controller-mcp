from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EthUnit1PortAppDTO")


@_attrs_define
class EthUnit1PortAppDTO:
    """
    Attributes:
        port (str): OLT physical port
        media_type (int | Unset): Port media type
        description (str | Unset): Display the configured port description.Description should contain 1-32 bits numbers,
            Upper and lower letters, -@_:/. .
        status (int | Unset): Port switch status.Status should be a value as follows:0:DISABLE;1:ENABLE
        speed (int | Unset): Port speed negotiation mode.Speed should be a value as follows:0;10;100;1000;2500;10000.0
            represents Auto, and all other values are in Mbps.
        duplex (int | Unset): Port duplex negotiation mode.Duplex should be a value as follows: 2:FULL,0:AUTO
        flow_control (int | Unset): Port flow control function switch.FlowControl should be a value as follows:
            0:DISABLE;1:ENABLE
        lag (str | Unset): The LAG to which the port belongs.
        speed_link (int | Unset): Port speed negotiation mode: 0 represents Auto, and all other values are in Mbps.
        duplex_link (int | Unset): Actual port duplex mode.DuplexLink should be a value as follows: 0:DISABLE;1:ENABLE
        link_status (int | Unset): Connection status of the PON port. LinkStatus should be a value as
            follows:0:LINK_DOWN;1:LINK_UP
        type_ (int | Unset): Port type.Type should be null.Type is a value as
            follows:0:COPPER;1:COMBO;2:SFP;3:SFP+;4:RJ45
        speed_max (int | Unset): The maximum rate that this port can achieve, in Mbps.SpeedMax should be null
    """

    port: str
    media_type: int | Unset = UNSET
    description: str | Unset = UNSET
    status: int | Unset = UNSET
    speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    flow_control: int | Unset = UNSET
    lag: str | Unset = UNSET
    speed_link: int | Unset = UNSET
    duplex_link: int | Unset = UNSET
    link_status: int | Unset = UNSET
    type_: int | Unset = UNSET
    speed_max: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        media_type = self.media_type

        description = self.description

        status = self.status

        speed = self.speed

        duplex = self.duplex

        flow_control = self.flow_control

        lag = self.lag

        speed_link = self.speed_link

        duplex_link = self.duplex_link

        link_status = self.link_status

        type_ = self.type_

        speed_max = self.speed_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "port": port,
            }
        )
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
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
        if lag is not UNSET:
            field_dict["lag"] = lag
        if speed_link is not UNSET:
            field_dict["speedLink"] = speed_link
        if duplex_link is not UNSET:
            field_dict["duplexLink"] = duplex_link
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if speed_max is not UNSET:
            field_dict["speedMax"] = speed_max

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port")

        media_type = d.pop("mediaType", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        speed = d.pop("speed", UNSET)

        duplex = d.pop("duplex", UNSET)

        flow_control = d.pop("flowControl", UNSET)

        lag = d.pop("lag", UNSET)

        speed_link = d.pop("speedLink", UNSET)

        duplex_link = d.pop("duplexLink", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        type_ = d.pop("type", UNSET)

        speed_max = d.pop("speedMax", UNSET)

        eth_unit_1_port_app_dto = cls(
            port=port,
            media_type=media_type,
            description=description,
            status=status,
            speed=speed,
            duplex=duplex,
            flow_control=flow_control,
            lag=lag,
            speed_link=speed_link,
            duplex_link=duplex_link,
            link_status=link_status,
            type_=type_,
            speed_max=speed_max,
        )

        eth_unit_1_port_app_dto.additional_properties = d
        return eth_unit_1_port_app_dto

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
