from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FreeAuthClientPolicyOpenApiVO")


@_attrs_define
class FreeAuthClientPolicyOpenApiVO:
    """List of Free-Authentication Client Policy

    Attributes:
        type_ (int): Type of the policy. It should be a value as follows: 3: Free auth client IP, and parameter
            [clientIp] is needed. 4: Free auth client MAC, and parameter [clientMac] is needed
        id_int (int | Unset): Entry ID of the policy. Except for newly added policies, this parameter should be retained
        client_ip (str | Unset): Free auth client IP Address
        client_mac (str | Unset): Free auth client MAC Address, for example: AA-AA-AA-AA-AA-AA
        description (str | Unset): Description of Pre-Authentication Access Policy
    """

    type_: int
    id_int: int | Unset = UNSET
    client_ip: str | Unset = UNSET
    client_mac: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id_int = self.id_int

        client_ip = self.client_ip

        client_mac = self.client_mac

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if id_int is not UNSET:
            field_dict["idInt"] = id_int
        if client_ip is not UNSET:
            field_dict["clientIp"] = client_ip
        if client_mac is not UNSET:
            field_dict["clientMac"] = client_mac
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        id_int = d.pop("idInt", UNSET)

        client_ip = d.pop("clientIp", UNSET)

        client_mac = d.pop("clientMac", UNSET)

        description = d.pop("description", UNSET)

        free_auth_client_policy_open_api_vo = cls(
            type_=type_,
            id_int=id_int,
            client_ip=client_ip,
            client_mac=client_mac,
            description=description,
        )

        free_auth_client_policy_open_api_vo.additional_properties = d
        return free_auth_client_policy_open_api_vo

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
