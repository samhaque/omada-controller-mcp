from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayCustomACLModifyEntity")


@_attrs_define
class GatewayCustomACLModifyEntity:
    """Modified Custom ACLs.

    Attributes:
        id (str): Custom ACL ID
        index (int): Custom ACL index
        status (bool): Custom ACL status
        description (str): Custom ACL description should contain 1 to 512 characters.
        direction (int): Custom ACL direction should be a value as follows: 0: LAN-LAN; 1: LAN-WAN; 2: WAN-LAN; 3: LOCAL
            IN
        policy (int): Custom ACL policy should be a value as follows: 0: Drop; 1:Allow
        protocol (int): Custom ACL protocol. For the values of protocol, refer to section 5.5 of the Open API Access
            Guide.
        source_list (list[str]): Custom ACL source list.
        destination_list (list[str]): Custom ACL destination list.
        log_status (bool): Custom ACL log status
        source_port (str | Unset): Custom ACL source port. when "protocol" is "TCP" or "UDP", port is valid.
        destination_port (str | Unset): Custom ACL destination port. when "protocol" is "TCP" or "UDP", port is valid.
    """

    id: str
    index: int
    status: bool
    description: str
    direction: int
    policy: int
    protocol: int
    source_list: list[str]
    destination_list: list[str]
    log_status: bool
    source_port: str | Unset = UNSET
    destination_port: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        index = self.index

        status = self.status

        description = self.description

        direction = self.direction

        policy = self.policy

        protocol = self.protocol

        source_list = self.source_list

        destination_list = self.destination_list

        log_status = self.log_status

        source_port = self.source_port

        destination_port = self.destination_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "index": index,
                "status": status,
                "description": description,
                "direction": direction,
                "policy": policy,
                "protocol": protocol,
                "sourceList": source_list,
                "destinationList": destination_list,
                "logStatus": log_status,
            }
        )
        if source_port is not UNSET:
            field_dict["sourcePort"] = source_port
        if destination_port is not UNSET:
            field_dict["destinationPort"] = destination_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        index = d.pop("index")

        status = d.pop("status")

        description = d.pop("description")

        direction = d.pop("direction")

        policy = d.pop("policy")

        protocol = d.pop("protocol")

        source_list = cast(list[str], d.pop("sourceList"))

        destination_list = cast(list[str], d.pop("destinationList"))

        log_status = d.pop("logStatus")

        source_port = d.pop("sourcePort", UNSET)

        destination_port = d.pop("destinationPort", UNSET)

        gateway_custom_acl_modify_entity = cls(
            id=id,
            index=index,
            status=status,
            description=description,
            direction=direction,
            policy=policy,
            protocol=protocol,
            source_list=source_list,
            destination_list=destination_list,
            log_status=log_status,
            source_port=source_port,
            destination_port=destination_port,
        )

        gateway_custom_acl_modify_entity.additional_properties = d
        return gateway_custom_acl_modify_entity

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
