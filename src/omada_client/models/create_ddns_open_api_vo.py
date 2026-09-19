from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ddns_interval_open_api_vo import DdnsIntervalOpenApiVO


T = TypeVar("T", bound="CreateDdnsOpenApiVO")


@_attrs_define
class CreateDdnsOpenApiVO:
    """
    Attributes:
        service (int): Dynamic DNS service type. Service should be a value as follows: 0: DynDNS, 1: NO-IP, 2:
            Peanuthull, 3: Comexe, 4: Custom, 5: TP-Link DDNS
        status (bool): Dynamic DNS enable status
        interface_port_id (str): This field represents interface Port ID
        username (str): Dynamic DNS username. Username should contain 1 to 128 characters
        password (str): Dynamic DNS password. Password should contain 1 to 128 characters
        domain_name (str | Unset): Dynamic DNS domainName, valid when parameter [service] is 0, 1 or 4
        interval (DdnsIntervalOpenApiVO | Unset): Dynamic DNS interval configuration. You can configure one of two
            intervals, when parameter [service] is 2 or 3, you can only choose [updateInterval] to configure, when parameter
            [service] is 5, you don’t need to configure interval.
        update_url (str | Unset): Dynamic DNS updateUrl, valid when parameter [service] is 4. Update URL must contain
            [USERNAME], [PASSWORD] and [DOMAIN], and Update-URL will be applied to all custom entries
    """

    service: int
    status: bool
    interface_port_id: str
    username: str
    password: str
    domain_name: str | Unset = UNSET
    interval: DdnsIntervalOpenApiVO | Unset = UNSET
    update_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        status = self.status

        interface_port_id = self.interface_port_id

        username = self.username

        password = self.password

        domain_name = self.domain_name

        interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        update_url = self.update_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service": service,
                "status": status,
                "interfacePortId": interface_port_id,
                "username": username,
                "password": password,
            }
        )
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if interval is not UNSET:
            field_dict["interval"] = interval
        if update_url is not UNSET:
            field_dict["updateUrl"] = update_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ddns_interval_open_api_vo import (
            DdnsIntervalOpenApiVO,
        )

        d = dict(src_dict)
        service = d.pop("service")

        status = d.pop("status")

        interface_port_id = d.pop("interfacePortId")

        username = d.pop("username")

        password = d.pop("password")

        domain_name = d.pop("domainName", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: DdnsIntervalOpenApiVO | Unset
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = DdnsIntervalOpenApiVO.from_dict(_interval)

        update_url = d.pop("updateUrl", UNSET)

        create_ddns_open_api_vo = cls(
            service=service,
            status=status,
            interface_port_id=interface_port_id,
            username=username,
            password=password,
            domain_name=domain_name,
            interval=interval,
            update_url=update_url,
        )

        create_ddns_open_api_vo.additional_properties = d
        return create_ddns_open_api_vo

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
