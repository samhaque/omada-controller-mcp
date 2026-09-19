from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IptvPortOpenApiVO")


@_attrs_define
class IptvPortOpenApiVO:
    """Config the port mode of the LAN ports to determine which port is used to support Internet service, IPTV service, or
    IP Phone service.

        Attributes:
            port_id (str): This field represents Port ID.
            type_ (int): Type should be a value as follows: 1: Internet; 2:IPTV; 3:IP-Phone
            name (str | Unset): This field represents Port's Name.
    """

    port_id: str
    type_: int
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        type_ = self.type_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId")

        type_ = d.pop("type")

        name = d.pop("name", UNSET)

        iptv_port_open_api_vo = cls(
            port_id=port_id,
            type_=type_,
            name=name,
        )

        iptv_port_open_api_vo.additional_properties = d
        return iptv_port_open_api_vo

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
