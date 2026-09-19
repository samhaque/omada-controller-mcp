from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_mac_address_open_api_vo import CreateMacAddressOpenApiVO
    from ..models.domain_open_api_vo import DomainOpenApiVO
    from ..models.i_pv_6_subnets_open_api_vo import IPv6SubnetsOpenApiVO
    from ..models.ip_subnets_open_api_vo import IPSubnetsOpenApiVO
    from ..models.port_mask_open_api_vo import PortMaskOpenApiVO


T = TypeVar("T", bound="CreateGroupOpenApiVO")


@_attrs_define
class CreateGroupOpenApiVO:
    """
    Attributes:
        name (str): Group profile name. Name should contain 1 to 64 characters
        type_ (int): Type of group profile, type should be a value as follows: 0: IP Group; 1: IP Port Group; 2: MAC
            Group; 3: IPv6 Group; 4: IPv6 Port Group; 5: Country Group; 7: Domain Group;
        ip_list (list[IPSubnetsOpenApiVO] | Unset): IP subnet info list. [type] value of 0 or 1 is required
        ipv_6_list (list[IPv6SubnetsOpenApiVO] | Unset): IPv6 subnet info list. [type] value of 3 or 4 is required
        port_type (int | Unset): Port type, portType should be a value as follows: 0: port range 1: port mask. [type]
            value of 1 or 4 is required
        port_list (list[str] | Unset): Port list. [portType] value of 0 is required. PortList should be within the range
            of 0-65535, e.g. 80 or 80-100
        port_mask_list (list[PortMaskOpenApiVO] | Unset): Port mask list. [portType] value of 1 is required
        mac_address_list (list[CreateMacAddressOpenApiVO] | Unset): MAC address list. [type] value of 2 is required
        country_list (list[str] | Unset): Country list. [type] value of 5 is required. For the values of countryList,
            refer to 'Country Name' section 5.4.1 of the Open API Access Guide
        description (str | Unset): Description should contain 1 to 256 characters. [type] value of 5 is required
        domain_name_port (list[DomainOpenApiVO] | Unset): Domain info. Handle situations where there are ports, [type]
            value of 7 is required
    """

    name: str
    type_: int
    ip_list: list[IPSubnetsOpenApiVO] | Unset = UNSET
    ipv_6_list: list[IPv6SubnetsOpenApiVO] | Unset = UNSET
    port_type: int | Unset = UNSET
    port_list: list[str] | Unset = UNSET
    port_mask_list: list[PortMaskOpenApiVO] | Unset = UNSET
    mac_address_list: list[CreateMacAddressOpenApiVO] | Unset = UNSET
    country_list: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    domain_name_port: list[DomainOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        ip_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip_list, Unset):
            ip_list = []
            for ip_list_item_data in self.ip_list:
                ip_list_item = ip_list_item_data.to_dict()
                ip_list.append(ip_list_item)

        ipv_6_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = []
            for ipv_6_list_item_data in self.ipv_6_list:
                ipv_6_list_item = ipv_6_list_item_data.to_dict()
                ipv_6_list.append(ipv_6_list_item)

        port_type = self.port_type

        port_list: list[str] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        port_mask_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_mask_list, Unset):
            port_mask_list = []
            for port_mask_list_item_data in self.port_mask_list:
                port_mask_list_item = port_mask_list_item_data.to_dict()
                port_mask_list.append(port_mask_list_item)

        mac_address_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mac_address_list, Unset):
            mac_address_list = []
            for mac_address_list_item_data in self.mac_address_list:
                mac_address_list_item = mac_address_list_item_data.to_dict()
                mac_address_list.append(mac_address_list_item)

        country_list: list[str] | Unset = UNSET
        if not isinstance(self.country_list, Unset):
            country_list = self.country_list

        description = self.description

        domain_name_port: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domain_name_port, Unset):
            domain_name_port = []
            for domain_name_port_item_data in self.domain_name_port:
                domain_name_port_item = domain_name_port_item_data.to_dict()
                domain_name_port.append(domain_name_port_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if ip_list is not UNSET:
            field_dict["ipList"] = ip_list
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if port_type is not UNSET:
            field_dict["portType"] = port_type
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if port_mask_list is not UNSET:
            field_dict["portMaskList"] = port_mask_list
        if mac_address_list is not UNSET:
            field_dict["macAddressList"] = mac_address_list
        if country_list is not UNSET:
            field_dict["countryList"] = country_list
        if description is not UNSET:
            field_dict["description"] = description
        if domain_name_port is not UNSET:
            field_dict["domainNamePort"] = domain_name_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_mac_address_open_api_vo import (
            CreateMacAddressOpenApiVO,
        )
        from ..models.domain_open_api_vo import DomainOpenApiVO
        from ..models.i_pv_6_subnets_open_api_vo import (
            IPv6SubnetsOpenApiVO,
        )
        from ..models.ip_subnets_open_api_vo import IPSubnetsOpenApiVO
        from ..models.port_mask_open_api_vo import PortMaskOpenApiVO

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        _ip_list = d.pop("ipList", UNSET)
        ip_list: list[IPSubnetsOpenApiVO] | Unset = UNSET
        if _ip_list is not UNSET:
            ip_list = []
            for ip_list_item_data in _ip_list:
                ip_list_item = IPSubnetsOpenApiVO.from_dict(ip_list_item_data)

                ip_list.append(ip_list_item)

        _ipv_6_list = d.pop("ipv6List", UNSET)
        ipv_6_list: list[IPv6SubnetsOpenApiVO] | Unset = UNSET
        if _ipv_6_list is not UNSET:
            ipv_6_list = []
            for ipv_6_list_item_data in _ipv_6_list:
                ipv_6_list_item = IPv6SubnetsOpenApiVO.from_dict(ipv_6_list_item_data)

                ipv_6_list.append(ipv_6_list_item)

        port_type = d.pop("portType", UNSET)

        port_list = cast(list[str], d.pop("portList", UNSET))

        _port_mask_list = d.pop("portMaskList", UNSET)
        port_mask_list: list[PortMaskOpenApiVO] | Unset = UNSET
        if _port_mask_list is not UNSET:
            port_mask_list = []
            for port_mask_list_item_data in _port_mask_list:
                port_mask_list_item = PortMaskOpenApiVO.from_dict(
                    port_mask_list_item_data
                )

                port_mask_list.append(port_mask_list_item)

        _mac_address_list = d.pop("macAddressList", UNSET)
        mac_address_list: list[CreateMacAddressOpenApiVO] | Unset = UNSET
        if _mac_address_list is not UNSET:
            mac_address_list = []
            for mac_address_list_item_data in _mac_address_list:
                mac_address_list_item = CreateMacAddressOpenApiVO.from_dict(
                    mac_address_list_item_data
                )

                mac_address_list.append(mac_address_list_item)

        country_list = cast(list[str], d.pop("countryList", UNSET))

        description = d.pop("description", UNSET)

        _domain_name_port = d.pop("domainNamePort", UNSET)
        domain_name_port: list[DomainOpenApiVO] | Unset = UNSET
        if _domain_name_port is not UNSET:
            domain_name_port = []
            for domain_name_port_item_data in _domain_name_port:
                domain_name_port_item = DomainOpenApiVO.from_dict(
                    domain_name_port_item_data
                )

                domain_name_port.append(domain_name_port_item)

        create_group_open_api_vo = cls(
            name=name,
            type_=type_,
            ip_list=ip_list,
            ipv_6_list=ipv_6_list,
            port_type=port_type,
            port_list=port_list,
            port_mask_list=port_mask_list,
            mac_address_list=mac_address_list,
            country_list=country_list,
            description=description,
            domain_name_port=domain_name_port,
        )

        create_group_open_api_vo.additional_properties = d
        return create_group_open_api_vo

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
