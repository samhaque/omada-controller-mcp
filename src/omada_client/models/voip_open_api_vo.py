from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoipOpenApiVO")


@_attrs_define
class VoipOpenApiVO:
    """
    Attributes:
        enable (bool): The status of First Priority for VoIP SIP/RTP, valid value is true or false.
        sip_udp_port (int | Unset): The SIP UDP Port should be within the range of 0-65535 when parameter [enable] is
            true.
    """

    enable: bool
    sip_udp_port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        sip_udp_port = self.sip_udp_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if sip_udp_port is not UNSET:
            field_dict["sipUdpPort"] = sip_udp_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        sip_udp_port = d.pop("sipUdpPort", UNSET)

        voip_open_api_vo = cls(
            enable=enable,
            sip_udp_port=sip_udp_port,
        )

        voip_open_api_vo.additional_properties = d
        return voip_open_api_vo

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
