from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="IptvPortConfigOpenApiVO")


@_attrs_define
class IptvPortConfigOpenApiVO:
    """All available ports need to be configured. The list of port ID is the same as that returned by "Get IPTV setting"

    Attributes:
        port_id (str): Port ID can be obtained from 'Get internet basic info' interface.
        type_ (int): Type should be a value as follows: 1: Internet; 2:IPTV; 3:IP-Phone, 3 is valid only IPTV mode is
            custom.
    """

    port_id: str
    type_: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId")

        type_ = d.pop("type")

        iptv_port_config_open_api_vo = cls(
            port_id=port_id,
            type_=type_,
        )

        iptv_port_config_open_api_vo.additional_properties = d
        return iptv_port_config_open_api_vo

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
