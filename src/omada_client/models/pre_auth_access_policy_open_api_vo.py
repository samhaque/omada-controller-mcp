from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreAuthAccessPolicyOpenApiVO")


@_attrs_define
class PreAuthAccessPolicyOpenApiVO:
    """List of Pre-Authentication Access Policy

    Attributes:
        type_ (int): Type of the policy. It should be a value as follows: 1: Destination IP Range, and parameter [ip]
            and [subnetMask] is needed. 2: URL, and parameter [url] is needed
        id_int (int | Unset): Entry ID of the policy. Except for newly added policies, this parameter should be retained
        ip (str | Unset): IP Address of Pre-Authentication Access
        subnet_mask (int | Unset): Subnet mask of Pre-Authentication Access. It should be within the range of 1-32
        url (str | Unset): URL of Pre-Authentication Access
        description (str | Unset): Description of Pre-Authentication Access Policy
    """

    type_: int
    id_int: int | Unset = UNSET
    ip: str | Unset = UNSET
    subnet_mask: int | Unset = UNSET
    url: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id_int = self.id_int

        ip = self.ip

        subnet_mask = self.subnet_mask

        url = self.url

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
        if ip is not UNSET:
            field_dict["ip"] = ip
        if subnet_mask is not UNSET:
            field_dict["subnetMask"] = subnet_mask
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        id_int = d.pop("idInt", UNSET)

        ip = d.pop("ip", UNSET)

        subnet_mask = d.pop("subnetMask", UNSET)

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        pre_auth_access_policy_open_api_vo = cls(
            type_=type_,
            id_int=id_int,
            ip=ip,
            subnet_mask=subnet_mask,
            url=url,
            description=description,
        )

        pre_auth_access_policy_open_api_vo.additional_properties = d
        return pre_auth_access_policy_open_api_vo

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
