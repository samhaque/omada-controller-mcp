from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="EapACLInfo")


@_attrs_define
class EapACLInfo:
    """
    Attributes:
        id (str): ACL ID
        index (int): Index
        description (str): ACL rule description, description should contain 1 to 512 characters.
        status (bool): Status should be a value as follows: 0: disable; 1: enable
        policy (int): Policy should be a value as follows: 0: drop; 1: allow;
        protocols (list[int]): For the values of protocols, refer to section 5.5 of the Open API Access Guide.
        source_ids (list[str]): Source IDs, which depends on sourceType, for example: if sourceType is network,
            sourceIds should be LAN network ID. LAN Network can be created using 'Create LAN network' interface, and LAN
            Network ID can be obtained from 'Get LAN network list' interface.
        destination_ids (list[str]): Destination IDs, which depends on destinationType, for example: if destinationType
            is network, destinationIds should be LAN network ID. LAN Network can be created using 'Create LAN network'
            interface, and LAN Network ID can be obtained from 'Get LAN network list' interface.
        source_type (int): SourceType should be a value as follows: 0: network; 1: IP Group; 2: IP-Port Group; 4: SSID;
            6: IPv6 Group; 7: IPv6-Port Group.
        destination_type (int): DestinationType should be a value as follows: 0: network; 1: IP Group; 2: IP-Port Group;
            6: IPv6 Group; 7: IPv6-Port Group
    """

    id: str
    index: int
    description: str
    status: bool
    policy: int
    protocols: list[int]
    source_ids: list[str]
    destination_ids: list[str]
    source_type: int
    destination_type: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        index = self.index

        description = self.description

        status = self.status

        policy = self.policy

        protocols = self.protocols

        source_ids = self.source_ids

        destination_ids = self.destination_ids

        source_type = self.source_type

        destination_type = self.destination_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "index": index,
                "description": description,
                "status": status,
                "policy": policy,
                "protocols": protocols,
                "sourceIds": source_ids,
                "destinationIds": destination_ids,
                "sourceType": source_type,
                "destinationType": destination_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        index = d.pop("index")

        description = d.pop("description")

        status = d.pop("status")

        policy = d.pop("policy")

        protocols = cast(list[int], d.pop("protocols"))

        source_ids = cast(list[str], d.pop("sourceIds"))

        destination_ids = cast(list[str], d.pop("destinationIds"))

        source_type = d.pop("sourceType")

        destination_type = d.pop("destinationType")

        eap_acl_info = cls(
            id=id,
            index=index,
            description=description,
            status=status,
            policy=policy,
            protocols=protocols,
            source_ids=source_ids,
            destination_ids=destination_ids,
            source_type=source_type,
            destination_type=destination_type,
        )

        eap_acl_info.additional_properties = d
        return eap_acl_info

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
