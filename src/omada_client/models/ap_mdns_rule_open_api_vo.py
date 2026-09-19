from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ApMdnsRuleOpenApiVO")


@_attrs_define
class ApMdnsRuleOpenApiVO:
    """MDNS rule by VLAN ID config, valid when parameter [type] is 0

    Attributes:
        service_vlan (str): Services Network VLAN. ServiceVlan should be within the range of 1 to 4094. Enter only one
            VLAN. This configuration is used for MDNS Rules where the band VLAN type is "By VLAN ID".
        client_vlan (str): Client Network VLAN. ClientVlan should be within the range of 1 to 4094. Enter one or
            multiple VLANs. For example: 1,2-100. This configuration is used for MDNS Rules where the band VLAN type is "By
            VLAN ID".
    """

    service_vlan: str
    client_vlan: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_vlan = self.service_vlan

        client_vlan = self.client_vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceVlan": service_vlan,
                "clientVlan": client_vlan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_vlan = d.pop("serviceVlan")

        client_vlan = d.pop("clientVlan")

        ap_mdns_rule_open_api_vo = cls(
            service_vlan=service_vlan,
            client_vlan=client_vlan,
        )

        ap_mdns_rule_open_api_vo.additional_properties = d
        return ap_mdns_rule_open_api_vo

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
