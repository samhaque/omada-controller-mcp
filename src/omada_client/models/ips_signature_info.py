from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsSignatureInfo")


@_attrs_define
class IpsSignatureInfo:
    """IPS signature Info entity

    Attributes:
        id (str): The unique identity of the signature suppresses.
        classification (str): Attack service concrete classification. Example: misc-attack.
        category (int): Attack service wide category. Example: 2.
        signature (str): Attack service signature.
        sid (int): IPS signature rule SID which is from device. Example: 240201.
        service (str): Attack service service, the same as parameter[signature]
        type_ (int): Type should be a value as follow: 0: all traffic; 1: packet tracking Example: 1.
        direction (int | Unset): Direction should be a value as follow: 0: both direction; 1: source direction; 2:
            destination direction Example: 1.
        traffic_type (int | Unset): TrafficType should be a value as follow: 0: ip address; 1: subnet Example: 0.
        traffic_source (str | Unset): IPS signature traffic Source. If parameter [trafficType] is 0, parameter
            [trafficSource] should be IPV4 address. If parameter [trafficType] is 1, parameter [trafficSource] should be
            subnet address. Example: 192.168.0.1.
    """

    id: str
    classification: str
    category: int
    signature: str
    sid: int
    service: str
    type_: int
    direction: int | Unset = UNSET
    traffic_type: int | Unset = UNSET
    traffic_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        classification = self.classification

        category = self.category

        signature = self.signature

        sid = self.sid

        service = self.service

        type_ = self.type_

        direction = self.direction

        traffic_type = self.traffic_type

        traffic_source = self.traffic_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "classification": classification,
                "category": category,
                "signature": signature,
                "sid": sid,
                "service": service,
                "type": type_,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if traffic_type is not UNSET:
            field_dict["trafficType"] = traffic_type
        if traffic_source is not UNSET:
            field_dict["trafficSource"] = traffic_source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        classification = d.pop("classification")

        category = d.pop("category")

        signature = d.pop("signature")

        sid = d.pop("sid")

        service = d.pop("service")

        type_ = d.pop("type")

        direction = d.pop("direction", UNSET)

        traffic_type = d.pop("trafficType", UNSET)

        traffic_source = d.pop("trafficSource", UNSET)

        ips_signature_info = cls(
            id=id,
            classification=classification,
            category=category,
            signature=signature,
            sid=sid,
            service=service,
            type_=type_,
            direction=direction,
            traffic_type=traffic_type,
            traffic_source=traffic_source,
        )

        ips_signature_info.additional_properties = d
        return ips_signature_info

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
