from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO
    from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO


T = TypeVar("T", bound="LocalUserOpenApiVO")


@_attrs_define
class LocalUserOpenApiVO:
    """
    Attributes:
        id (str | Unset): Local user ID
        user_name (str | Unset): User name should contain 1 to 128 characters
        password (str | Unset): Password should contain 1 to 128 characters
        enable (bool | Unset): Local user enable status
        expiration_time (int | Unset): Expiration time, unit: ms
        binding_type (int | Unset): MAC binding type should be a value as follows: 0: no binding; 1: static binding; 2:
            dynamic binding.
        mac_address (str | Unset): Mac address,the value is only available when the macType is static binding or dynamic
            binding.
        max_users (int | Unset): The maximum number of users online at the same time when the MAC binding type is No
            Binding. It cannot be modified after initialization. Value of Maximum Users should be within the range of
            1-2048.
        name (str | Unset): Name
        phone (str | Unset): Phone number should contain 1 to 20 characters.
        rate_limit (RateLimitOpenApiVO | Unset): When configuring rate limit, can only configure one of
            rateLimitProfileId or customRateLimit
        traffic_limit_enable (bool | Unset): Whether to enable traffic limit.
        traffic_limit (int | Unset): Traffic limit in MB. The value should be within the range of 1–10485760.
        traffic_left (bool | Unset): Is there any remaining traffic.
        traffic_used (int | Unset): Used traffic(MB).
        traffic_limit_frequency (int | Unset): Frequency of traffic limit should be a value as follows: 0: total; 1:
            daily; 2: weekly; 3: monthly.
        used (int | Unset): Used quantity.
        overtime (bool | Unset): Whether the current time has exceeded the expirationTime
        portals (list[str] | Unset): Bound portal names.
        logout (bool | Unset): local user logout. enable local user logout.
        apply_to_all_portals (bool | Unset): Is the localuser effective for all portals, including all newly created
            portals
        daily_limit_enable (bool | Unset): Whether to enable localuser daily time limit
        daily_limit (AuthTimeOpenApiVO | Unset): Authentication timeout time. Display when enabled, otherwise no
            display.
        daily_limit_ms (int | Unset): Daily time limit, unit is ms, required when parameter [dailyLimitEnable] is true
        daily_limit_left_ms (int | Unset): Daily time left, unit is ms, required when parameter [dailyLimitEnable] is
            true
    """

    id: str | Unset = UNSET
    user_name: str | Unset = UNSET
    password: str | Unset = UNSET
    enable: bool | Unset = UNSET
    expiration_time: int | Unset = UNSET
    binding_type: int | Unset = UNSET
    mac_address: str | Unset = UNSET
    max_users: int | Unset = UNSET
    name: str | Unset = UNSET
    phone: str | Unset = UNSET
    rate_limit: RateLimitOpenApiVO | Unset = UNSET
    traffic_limit_enable: bool | Unset = UNSET
    traffic_limit: int | Unset = UNSET
    traffic_left: bool | Unset = UNSET
    traffic_used: int | Unset = UNSET
    traffic_limit_frequency: int | Unset = UNSET
    used: int | Unset = UNSET
    overtime: bool | Unset = UNSET
    portals: list[str] | Unset = UNSET
    logout: bool | Unset = UNSET
    apply_to_all_portals: bool | Unset = UNSET
    daily_limit_enable: bool | Unset = UNSET
    daily_limit: AuthTimeOpenApiVO | Unset = UNSET
    daily_limit_ms: int | Unset = UNSET
    daily_limit_left_ms: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_name = self.user_name

        password = self.password

        enable = self.enable

        expiration_time = self.expiration_time

        binding_type = self.binding_type

        mac_address = self.mac_address

        max_users = self.max_users

        name = self.name

        phone = self.phone

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        traffic_limit_enable = self.traffic_limit_enable

        traffic_limit = self.traffic_limit

        traffic_left = self.traffic_left

        traffic_used = self.traffic_used

        traffic_limit_frequency = self.traffic_limit_frequency

        used = self.used

        overtime = self.overtime

        portals: list[str] | Unset = UNSET
        if not isinstance(self.portals, Unset):
            portals = self.portals

        logout = self.logout

        apply_to_all_portals = self.apply_to_all_portals

        daily_limit_enable = self.daily_limit_enable

        daily_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_limit, Unset):
            daily_limit = self.daily_limit.to_dict()

        daily_limit_ms = self.daily_limit_ms

        daily_limit_left_ms = self.daily_limit_left_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if password is not UNSET:
            field_dict["password"] = password
        if enable is not UNSET:
            field_dict["enable"] = enable
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if binding_type is not UNSET:
            field_dict["bindingType"] = binding_type
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if max_users is not UNSET:
            field_dict["maxUsers"] = max_users
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if traffic_limit_enable is not UNSET:
            field_dict["trafficLimitEnable"] = traffic_limit_enable
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_left is not UNSET:
            field_dict["trafficLeft"] = traffic_left
        if traffic_used is not UNSET:
            field_dict["trafficUsed"] = traffic_used
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency
        if used is not UNSET:
            field_dict["used"] = used
        if overtime is not UNSET:
            field_dict["overtime"] = overtime
        if portals is not UNSET:
            field_dict["portals"] = portals
        if logout is not UNSET:
            field_dict["logout"] = logout
        if apply_to_all_portals is not UNSET:
            field_dict["applyToAllPortals"] = apply_to_all_portals
        if daily_limit_enable is not UNSET:
            field_dict["dailyLimitEnable"] = daily_limit_enable
        if daily_limit is not UNSET:
            field_dict["dailyLimit"] = daily_limit
        if daily_limit_ms is not UNSET:
            field_dict["dailyLimitMs"] = daily_limit_ms
        if daily_limit_left_ms is not UNSET:
            field_dict["dailyLimitLeftMs"] = daily_limit_left_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO
        from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_name = d.pop("userName", UNSET)

        password = d.pop("password", UNSET)

        enable = d.pop("enable", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        binding_type = d.pop("bindingType", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        max_users = d.pop("maxUsers", UNSET)

        name = d.pop("name", UNSET)

        phone = d.pop("phone", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: RateLimitOpenApiVO | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = RateLimitOpenApiVO.from_dict(_rate_limit)

        traffic_limit_enable = d.pop("trafficLimitEnable", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_left = d.pop("trafficLeft", UNSET)

        traffic_used = d.pop("trafficUsed", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        used = d.pop("used", UNSET)

        overtime = d.pop("overtime", UNSET)

        portals = cast(list[str], d.pop("portals", UNSET))

        logout = d.pop("logout", UNSET)

        apply_to_all_portals = d.pop("applyToAllPortals", UNSET)

        daily_limit_enable = d.pop("dailyLimitEnable", UNSET)

        _daily_limit = d.pop("dailyLimit", UNSET)
        daily_limit: AuthTimeOpenApiVO | Unset
        if isinstance(_daily_limit, Unset):
            daily_limit = UNSET
        else:
            daily_limit = AuthTimeOpenApiVO.from_dict(_daily_limit)

        daily_limit_ms = d.pop("dailyLimitMs", UNSET)

        daily_limit_left_ms = d.pop("dailyLimitLeftMs", UNSET)

        local_user_open_api_vo = cls(
            id=id,
            user_name=user_name,
            password=password,
            enable=enable,
            expiration_time=expiration_time,
            binding_type=binding_type,
            mac_address=mac_address,
            max_users=max_users,
            name=name,
            phone=phone,
            rate_limit=rate_limit,
            traffic_limit_enable=traffic_limit_enable,
            traffic_limit=traffic_limit,
            traffic_left=traffic_left,
            traffic_used=traffic_used,
            traffic_limit_frequency=traffic_limit_frequency,
            used=used,
            overtime=overtime,
            portals=portals,
            logout=logout,
            apply_to_all_portals=apply_to_all_portals,
            daily_limit_enable=daily_limit_enable,
            daily_limit=daily_limit,
            daily_limit_ms=daily_limit_ms,
            daily_limit_left_ms=daily_limit_left_ms,
        )

        local_user_open_api_vo.additional_properties = d
        return local_user_open_api_vo

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
