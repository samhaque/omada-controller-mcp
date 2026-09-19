from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="OsgMdnsRuleOpenApiVO")


@_attrs_define
class OsgMdnsRuleOpenApiVO:
    """MDNS rule by network config, valid when parameter [type] is 1

    Attributes:
        service_networks (list[str]): LAN Network ID list of selected service networks. This configuration is used for
            MDNS Rules where the band VLAN type is "By Network". LAN Network can be created using 'Create LAN network'
            interface, and LAN Network ID can be obtained from 'Get LAN network list' interface
        client_networks (list[str]): LAN Network ID list of selected client networks.  This configuration is used for
            MDNS Rules where the band VLAN type is "By Network". LAN Network can be created using 'Create LAN network'
            interface, and LAN Network ID can be obtained from 'Get LAN network list' interface
    """

    service_networks: list[str]
    client_networks: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_networks = self.service_networks

        client_networks = self.client_networks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceNetworks": service_networks,
                "clientNetworks": client_networks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_networks = cast(list[str], d.pop("serviceNetworks"))

        client_networks = cast(list[str], d.pop("clientNetworks"))

        osg_mdns_rule_open_api_vo = cls(
            service_networks=service_networks,
            client_networks=client_networks,
        )

        osg_mdns_rule_open_api_vo.additional_properties = d
        return osg_mdns_rule_open_api_vo

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
