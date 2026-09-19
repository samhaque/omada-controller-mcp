from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.eth_unit_1_port_dto_duplex import EthUnit1PortDTODuplex
from ..models.eth_unit_1_port_dto_duplex_link import EthUnit1PortDTODuplexLink
from ..models.eth_unit_1_port_dto_flow_control import EthUnit1PortDTOFlowControl
from ..models.eth_unit_1_port_dto_link_status import EthUnit1PortDTOLinkStatus
from ..models.eth_unit_1_port_dto_media_type import EthUnit1PortDTOMediaType
from ..models.eth_unit_1_port_dto_status import EthUnit1PortDTOStatus
from ..models.eth_unit_1_port_dto_type import EthUnit1PortDTOType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EthUnit1PortDTO")


@_attrs_define
class EthUnit1PortDTO:
    """Eth unit1 port list

    Attributes:
        port (str):
        media_type (EthUnit1PortDTOMediaType | Unset):
        description (str | Unset):
        status (EthUnit1PortDTOStatus | Unset):
        speed (int | Unset):
        duplex (EthUnit1PortDTODuplex | Unset):
        flow_control (EthUnit1PortDTOFlowControl | Unset):
        lag (str | Unset):
        speed_link (int | Unset):
        duplex_link (EthUnit1PortDTODuplexLink | Unset):
        link_status (EthUnit1PortDTOLinkStatus | Unset):
        type_ (EthUnit1PortDTOType | Unset):
        speed_max (int | Unset):
    """

    port: str
    media_type: EthUnit1PortDTOMediaType | Unset = UNSET
    description: str | Unset = UNSET
    status: EthUnit1PortDTOStatus | Unset = UNSET
    speed: int | Unset = UNSET
    duplex: EthUnit1PortDTODuplex | Unset = UNSET
    flow_control: EthUnit1PortDTOFlowControl | Unset = UNSET
    lag: str | Unset = UNSET
    speed_link: int | Unset = UNSET
    duplex_link: EthUnit1PortDTODuplexLink | Unset = UNSET
    link_status: EthUnit1PortDTOLinkStatus | Unset = UNSET
    type_: EthUnit1PortDTOType | Unset = UNSET
    speed_max: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        media_type: str | Unset = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        speed = self.speed

        duplex: str | Unset = UNSET
        if not isinstance(self.duplex, Unset):
            duplex = self.duplex.value

        flow_control: str | Unset = UNSET
        if not isinstance(self.flow_control, Unset):
            flow_control = self.flow_control.value

        lag = self.lag

        speed_link = self.speed_link

        duplex_link: str | Unset = UNSET
        if not isinstance(self.duplex_link, Unset):
            duplex_link = self.duplex_link.value

        link_status: str | Unset = UNSET
        if not isinstance(self.link_status, Unset):
            link_status = self.link_status.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        _media_type = d.pop("mediaType", UNSET)
        media_type: EthUnit1PortDTOMediaType | Unset
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = EthUnit1PortDTOMediaType(_media_type)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: EthUnit1PortDTOStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EthUnit1PortDTOStatus(_status)

        speed = d.pop("speed", UNSET)

        _duplex = d.pop("duplex", UNSET)
        duplex: EthUnit1PortDTODuplex | Unset
        if isinstance(_duplex, Unset):
            duplex = UNSET
        else:
            duplex = EthUnit1PortDTODuplex(_duplex)

        _flow_control = d.pop("flowControl", UNSET)
        flow_control: EthUnit1PortDTOFlowControl | Unset
        if isinstance(_flow_control, Unset):
            flow_control = UNSET
        else:
            flow_control = EthUnit1PortDTOFlowControl(_flow_control)

        lag = d.pop("lag", UNSET)

        speed_link = d.pop("speedLink", UNSET)

        _duplex_link = d.pop("duplexLink", UNSET)
        duplex_link: EthUnit1PortDTODuplexLink | Unset
        if isinstance(_duplex_link, Unset):
            duplex_link = UNSET
        else:
            duplex_link = EthUnit1PortDTODuplexLink(_duplex_link)

        _link_status = d.pop("linkStatus", UNSET)
        link_status: EthUnit1PortDTOLinkStatus | Unset
        if isinstance(_link_status, Unset):
            link_status = UNSET
        else:
            link_status = EthUnit1PortDTOLinkStatus(_link_status)

        _type_ = d.pop("type", UNSET)
        type_: EthUnit1PortDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EthUnit1PortDTOType(_type_)

        speed_max = d.pop("speedMax", UNSET)

        eth_unit_1_port_dto = cls(
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

        eth_unit_1_port_dto.additional_properties = d
        return eth_unit_1_port_dto

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
