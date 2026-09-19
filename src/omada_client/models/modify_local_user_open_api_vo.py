from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO


T = TypeVar("T", bound="ModifyLocalUserOpenApiVO")


@_attrs_define
class ModifyLocalUserOpenApiVO:
    """
    Attributes:
        password (str): Password should contain 1 to 128 characters.
        enable (bool): Whether to enable.
        expiration_time (int): Expiration timestamp. Unit:ms.
        binding_type (int): MAC binding type should be a value as follows: 0: no binding; 1: static binding; 2: dynamic
            binding.
        max_users (int): The maximum number of users online at the same time when the MAC binding type is No Binding. It
            cannot be modified after initialization. MaxUsers should be within the range of 1–2048.
        rate_limit (RateLimitOpenApiVO): When configuring rate limit, can only configure one of rateLimitProfileId or
            customRateLimit
        traffic_limit_enable (bool): Whether to enable traffic limit.
        portals (list[str]): Bound portal ID list. Portal can be created using 'Add portal' interface, and portal ID can
            be obtained from 'Get portal list in a site' interface
        mac_address (str | Unset): Mac address,the value is only available when the macType is static binding or dynamic
            binding.
        name (str | Unset): Name should contain 1 to 128 characters, with no spaces at the beginning and end, and spaces
            in the middle
        phone (str | Unset): Phone number should contain 1 to 20 characters.
        traffic_limit (int | Unset): Traffic limit in MB. It should be within the range of 1–10485760.
        traffic_limit_frequency (int | Unset): Frequency of traffic limit should be a value as follows: 0: total; 1:
            daily; 2: weekly; 3: monthly.
        logout (bool | Unset): local user logout. enable local user logout
        apply_to_all_portals (bool | Unset): Is the localuser effective for all portals, including all newly created
            portals
    """

    password: str
    enable: bool
    expiration_time: int
    binding_type: int
    max_users: int
    rate_limit: RateLimitOpenApiVO
    traffic_limit_enable: bool
    portals: list[str]
    mac_address: str | Unset = UNSET
    name: str | Unset = UNSET
    phone: str | Unset = UNSET
    traffic_limit: int | Unset = UNSET
    traffic_limit_frequency: int | Unset = UNSET
    logout: bool | Unset = UNSET
    apply_to_all_portals: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        enable = self.enable

        expiration_time = self.expiration_time

        binding_type = self.binding_type

        max_users = self.max_users

        rate_limit = self.rate_limit.to_dict()

        traffic_limit_enable = self.traffic_limit_enable

        portals = self.portals

        mac_address = self.mac_address

        name = self.name

        phone = self.phone

        traffic_limit = self.traffic_limit

        traffic_limit_frequency = self.traffic_limit_frequency

        logout = self.logout

        apply_to_all_portals = self.apply_to_all_portals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "enable": enable,
                "expirationTime": expiration_time,
                "bindingType": binding_type,
                "maxUsers": max_users,
                "rateLimit": rate_limit,
                "trafficLimitEnable": traffic_limit_enable,
                "portals": portals,
            }
        )
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency
        if logout is not UNSET:
            field_dict["logout"] = logout
        if apply_to_all_portals is not UNSET:
            field_dict["applyToAllPortals"] = apply_to_all_portals

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO

        d = dict(src_dict)
        password = d.pop("password")

        enable = d.pop("enable")

        expiration_time = d.pop("expirationTime")

        binding_type = d.pop("bindingType")

        max_users = d.pop("maxUsers")

        rate_limit = RateLimitOpenApiVO.from_dict(d.pop("rateLimit"))

        traffic_limit_enable = d.pop("trafficLimitEnable")

        portals = cast(list[str], d.pop("portals"))

        mac_address = d.pop("macAddress", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        logout = d.pop("logout", UNSET)

        apply_to_all_portals = d.pop("applyToAllPortals", UNSET)

        modify_local_user_open_api_vo = cls(
            password=password,
            enable=enable,
            expiration_time=expiration_time,
            binding_type=binding_type,
            max_users=max_users,
            rate_limit=rate_limit,
            traffic_limit_enable=traffic_limit_enable,
            portals=portals,
            mac_address=mac_address,
            name=name,
            phone=phone,
            traffic_limit=traffic_limit,
            traffic_limit_frequency=traffic_limit_frequency,
            logout=logout,
            apply_to_all_portals=apply_to_all_portals,
        )

        modify_local_user_open_api_vo.additional_properties = d
        return modify_local_user_open_api_vo

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
