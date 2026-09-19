from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortSettingVO")


@_attrs_define
class PortSettingVO:
    """Parameter [portSettings] should not be null when parameter [provider] is 6.

    Attributes:
        registrar_port (int | Unset): When parameter [provider] is 0, parameter [registrarPort] has a default value of
            [5060]. In other cases, parameter [registrarPort] is always 5060.
        sip_proxy (str | Unset): Parameter [sipProxy] should not be null when parameter [provider] is 6. When parameter
            [provider] is 0, parameter [sipProxy] has a default value of [0.0.0.0]. In other cases, parameter [sipProxy] is
            always [0.0.0.0].
        sip_proxy_port (int | Unset): When parameter [provider] is 0, parameter [sipProxyPort] has a default value of
            [5060]. In other cases, parameter [sipProxyPort] is always 5060.
        outbound_proxy (str | Unset): When parameter [provider] is 0, parameter [outboundProxy] has a default value of
            [0.0.0.0]. In other cases, parameter [outboundProxy] is always [0.0.0.0].
        outbound_proxy_port (int | Unset): When parameter [provider] is 0, parameter [outboundProxyPort] has a default
            value of [5060]. In other cases, parameter [outboundProxyPort] is always 5060.
        via_outbound_proxy (bool | Unset): When parameter [provider] is 0, parameter [viaOutboundProxy] has a default
            value of [true]. In other cases, parameter [viaOutboundProxy] is always true.
    """

    registrar_port: int | Unset = UNSET
    sip_proxy: str | Unset = UNSET
    sip_proxy_port: int | Unset = UNSET
    outbound_proxy: str | Unset = UNSET
    outbound_proxy_port: int | Unset = UNSET
    via_outbound_proxy: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        registrar_port = self.registrar_port

        sip_proxy = self.sip_proxy

        sip_proxy_port = self.sip_proxy_port

        outbound_proxy = self.outbound_proxy

        outbound_proxy_port = self.outbound_proxy_port

        via_outbound_proxy = self.via_outbound_proxy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if registrar_port is not UNSET:
            field_dict["registrarPort"] = registrar_port
        if sip_proxy is not UNSET:
            field_dict["sipProxy"] = sip_proxy
        if sip_proxy_port is not UNSET:
            field_dict["sipProxyPort"] = sip_proxy_port
        if outbound_proxy is not UNSET:
            field_dict["outboundProxy"] = outbound_proxy
        if outbound_proxy_port is not UNSET:
            field_dict["outboundProxyPort"] = outbound_proxy_port
        if via_outbound_proxy is not UNSET:
            field_dict["viaOutboundProxy"] = via_outbound_proxy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        registrar_port = d.pop("registrarPort", UNSET)

        sip_proxy = d.pop("sipProxy", UNSET)

        sip_proxy_port = d.pop("sipProxyPort", UNSET)

        outbound_proxy = d.pop("outboundProxy", UNSET)

        outbound_proxy_port = d.pop("outboundProxyPort", UNSET)

        via_outbound_proxy = d.pop("viaOutboundProxy", UNSET)

        port_setting_vo = cls(
            registrar_port=registrar_port,
            sip_proxy=sip_proxy,
            sip_proxy_port=sip_proxy_port,
            outbound_proxy=outbound_proxy,
            outbound_proxy_port=outbound_proxy_port,
            via_outbound_proxy=via_outbound_proxy,
        )

        port_setting_vo.additional_properties = d
        return port_setting_vo

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
