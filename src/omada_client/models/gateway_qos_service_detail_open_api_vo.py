from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayQosServiceDetailOpenApiVO")


@_attrs_define
class GatewayQosServiceDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): The ID of Gateway QoS Service.
        default_profile (bool | Unset): Indicating that the profile is the default which cannot be modified.
        name (str | Unset): The name of Gateway QoS Service should contain 1 to 64 characters.
        protocol (int | Unset): The protocol of Gateway QoS Service should be a value as follows: 0: TCP, 1: UDP, 2:
            TCP/UDP, 3: ICMP, 4: Other.
        source_start_port (int | Unset): The start port of Source Port Range. It must be less than the end port. It
            should be within the range of 0-65535 when protocol is 0(TCP), 1(UDP) or 2(TCP/UDP).
        source_end_port (int | Unset): The end port of Source Port Range. It must be more than the start port. It should
            be within the range of 0-65535 when protocol is 0(TCP), 1(UDP) or 2(TCP/UDP).
        dest_start_port (int | Unset): The start port of Destination Port Range. It must be less than the end port. It
            should be within the range of 0-65535 when protocol is 0(TCP), 1(UDP) or 2(TCP/UDP).
        dest_end_port (int | Unset): The end port of Destination Port Range. It must be more than the start port. It
            should be within the range of 0-65535 when protocol is 0(TCP), 1(UDP) or 2(TCP/UDP).
        type_ (int | Unset): The type cannot be null and should be within the range of 0-255 when protocol is 3(ICMP).
        code (int | Unset): The code cannot be null and should be within the range of 0-255 when protocol is 3(ICMP).
        proto_num (int | Unset): The protoNum cannot be null and should be within the range of 1-255 when protocol is
            4(Other).
        description (str | Unset): The description of Gateway QoS Service should contain 0 to 128 characters.
    """

    id: str | Unset = UNSET
    default_profile: bool | Unset = UNSET
    name: str | Unset = UNSET
    protocol: int | Unset = UNSET
    source_start_port: int | Unset = UNSET
    source_end_port: int | Unset = UNSET
    dest_start_port: int | Unset = UNSET
    dest_end_port: int | Unset = UNSET
    type_: int | Unset = UNSET
    code: int | Unset = UNSET
    proto_num: int | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        default_profile = self.default_profile

        name = self.name

        protocol = self.protocol

        source_start_port = self.source_start_port

        source_end_port = self.source_end_port

        dest_start_port = self.dest_start_port

        dest_end_port = self.dest_end_port

        type_ = self.type_

        code = self.code

        proto_num = self.proto_num

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if default_profile is not UNSET:
            field_dict["defaultProfile"] = default_profile
        if name is not UNSET:
            field_dict["name"] = name
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if source_start_port is not UNSET:
            field_dict["sourceStartPort"] = source_start_port
        if source_end_port is not UNSET:
            field_dict["sourceEndPort"] = source_end_port
        if dest_start_port is not UNSET:
            field_dict["destStartPort"] = dest_start_port
        if dest_end_port is not UNSET:
            field_dict["destEndPort"] = dest_end_port
        if type_ is not UNSET:
            field_dict["type"] = type_
        if code is not UNSET:
            field_dict["code"] = code
        if proto_num is not UNSET:
            field_dict["protoNum"] = proto_num
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        default_profile = d.pop("defaultProfile", UNSET)

        name = d.pop("name", UNSET)

        protocol = d.pop("protocol", UNSET)

        source_start_port = d.pop("sourceStartPort", UNSET)

        source_end_port = d.pop("sourceEndPort", UNSET)

        dest_start_port = d.pop("destStartPort", UNSET)

        dest_end_port = d.pop("destEndPort", UNSET)

        type_ = d.pop("type", UNSET)

        code = d.pop("code", UNSET)

        proto_num = d.pop("protoNum", UNSET)

        description = d.pop("description", UNSET)

        gateway_qos_service_detail_open_api_vo = cls(
            id=id,
            default_profile=default_profile,
            name=name,
            protocol=protocol,
            source_start_port=source_start_port,
            source_end_port=source_end_port,
            dest_start_port=dest_start_port,
            dest_end_port=dest_end_port,
            type_=type_,
            code=code,
            proto_num=proto_num,
            description=description,
        )

        gateway_qos_service_detail_open_api_vo.additional_properties = d
        return gateway_qos_service_detail_open_api_vo

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
