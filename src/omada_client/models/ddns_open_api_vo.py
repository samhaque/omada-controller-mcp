from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DdnsOpenApiVO")


@_attrs_define
class DdnsOpenApiVO:
    """
    Attributes:
        id (str | Unset): Dynamic DNS ID
        service (int | Unset): Dynamic DNS service type, 0: DynDNS, 1: NO-IP, 2: Peanuthull, 3: Comexe, 4: Custom, 5:
            TP-Link DDNS
        status (bool | Unset): Dynamic DNS enable status
        interface_port_id (str | Unset): Port ID of interface
        username (str | Unset): Dynamic DNS username
        password (str | Unset): Dynamic DNS password
        domain_name (str | Unset): Dynamic DNS domainName
        update_interval (int | Unset): Dynamic DNS update interval, unit: hour
        custom_interval (int | Unset): Dynamic DNS custom interval, valid when parameter [server] is 0, 1 or 4, unit:
            minute
        update_url (str | Unset): Dynamic DNS updateUrl, valid when parameter [server] is 4
        exist_custom_ddns (bool | Unset): Whether Custom Service Provider has been configured in the current Dynamic
            DNS.
        exist_custom_interval (bool | Unset): Whether Custom Update Interval has been configured in the current Dynamic
            DNS.
        exist_tp_linkddns (bool | Unset): Whether TP-Link has been configured as Service Provider in the current Dynamic
            DNS.
    """

    id: str | Unset = UNSET
    service: int | Unset = UNSET
    status: bool | Unset = UNSET
    interface_port_id: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    domain_name: str | Unset = UNSET
    update_interval: int | Unset = UNSET
    custom_interval: int | Unset = UNSET
    update_url: str | Unset = UNSET
    exist_custom_ddns: bool | Unset = UNSET
    exist_custom_interval: bool | Unset = UNSET
    exist_tp_linkddns: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        service = self.service

        status = self.status

        interface_port_id = self.interface_port_id

        username = self.username

        password = self.password

        domain_name = self.domain_name

        update_interval = self.update_interval

        custom_interval = self.custom_interval

        update_url = self.update_url

        exist_custom_ddns = self.exist_custom_ddns

        exist_custom_interval = self.exist_custom_interval

        exist_tp_linkddns = self.exist_tp_linkddns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if service is not UNSET:
            field_dict["service"] = service
        if status is not UNSET:
            field_dict["status"] = status
        if interface_port_id is not UNSET:
            field_dict["interfacePortId"] = interface_port_id
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if update_interval is not UNSET:
            field_dict["updateInterval"] = update_interval
        if custom_interval is not UNSET:
            field_dict["customInterval"] = custom_interval
        if update_url is not UNSET:
            field_dict["updateUrl"] = update_url
        if exist_custom_ddns is not UNSET:
            field_dict["existCustomDdns"] = exist_custom_ddns
        if exist_custom_interval is not UNSET:
            field_dict["existCustomInterval"] = exist_custom_interval
        if exist_tp_linkddns is not UNSET:
            field_dict["existTpLinkddns"] = exist_tp_linkddns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        service = d.pop("service", UNSET)

        status = d.pop("status", UNSET)

        interface_port_id = d.pop("interfacePortId", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        domain_name = d.pop("domainName", UNSET)

        update_interval = d.pop("updateInterval", UNSET)

        custom_interval = d.pop("customInterval", UNSET)

        update_url = d.pop("updateUrl", UNSET)

        exist_custom_ddns = d.pop("existCustomDdns", UNSET)

        exist_custom_interval = d.pop("existCustomInterval", UNSET)

        exist_tp_linkddns = d.pop("existTpLinkddns", UNSET)

        ddns_open_api_vo = cls(
            id=id,
            service=service,
            status=status,
            interface_port_id=interface_port_id,
            username=username,
            password=password,
            domain_name=domain_name,
            update_interval=update_interval,
            custom_interval=custom_interval,
            update_url=update_url,
            exist_custom_ddns=exist_custom_ddns,
            exist_custom_interval=exist_custom_interval,
            exist_tp_linkddns=exist_tp_linkddns,
        )

        ddns_open_api_vo.additional_properties = d
        return ddns_open_api_vo

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
