from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO
    from ..models.voucher_schedule_open_api_vo import VoucherScheduleOpenApiVO


T = TypeVar("T", bound="CreateVoucherGroupOpenApiVO")


@_attrs_define
class CreateVoucherGroupOpenApiVO:
    """
    Attributes:
        name (str): Voucher group name. It should contain 1-32 characters
        amount (int): The amount of vouchers created. It should be within the range of 1-5000
        code_length (int): The length of voucher code. It should be within the range of 6–10.
        code_form (list[int]): The character types contained in the voucher code. It should be a value as follows: 0:
            Number, 1: Letter. For example, [0] indicates that the code only contains numbers; [0, 1] indicates that the
            code contains numbers and letters
        limit_type (int): The limitations of the voucher. It should be a value as follows: 0: Limited Usage Counts, 1:
            Limited Online Users, 2: Unlimited
        duration_type (int): The duration type of the voucher. It should be a value as follows: 0: Client duration, each
            client expires after the duration is used. 1: Voucher duration, after reaching the voucher duration, clients
            using the voucher will expire
        duration (int): Duration of one use, unit: minute. It should be within the range of 1–14400000.
        timing_type (int): The timing type of the voucher. It should be a value as follows: 0: Timing by time, clients
            can use vouchers for specified time duration. 1: Timing by usage, clients can use vouchers for the duration of
            actual usage
        rate_limit (RateLimitOpenApiVO): When configuring rate limit, can only configure one of rateLimitProfileId or
            customRateLimit
        traffic_limit_enable (bool): Whether to enable traffic limit
        apply_to_all_portals (bool): Is the voucher effective for all portals, including all newly created portals
        limit_num (int | Unset): The number of limitations. It should be within the range of 1–999. If Parameter
            [limitType] is 0 or 1, [limitNum] should not be null.When Parameter [limitType] is 0, [limitNum] represents the
            maximum number of times this voucher can be used.When Parameter [limitType] is 1, [limitNum] represents the
            maximum number of users this voucher can be used at the same time.
        traffic_limit (int | Unset): Traffic limit in MB. It should be within the range of 1–10485760
        traffic_limit_frequency (int | Unset): Frequency of traffic limit should be a value as follows: 0: total; 1:
            daily; 2: weekly; 3: monthly.
        unit_price (int | Unset): Price of single voucher. It should be within the range of 1–999999999
        currency (str | Unset): Currency Short Code of voucher. For the values of Currency Short Code, refer to section
            5.4.2 of the Open API Access Guide.
        portals (list[str] | Unset): Bound portal ID list. Portal can be created using 'Add portal' interface, and
            portal ID can be obtained from 'Get portal list in a site' interface
        expiration_time (int | Unset): The timestamp of the expiration of the voucher, unit: millisecond. When parameter
            [validityType] is 1, parameter [expirationTime] is required
        effective_time (int | Unset): The timestamp when the voucher takes effect, unit: millisecond. When parameter
            [validityType] is 1, parameter [effectiveTime] is required
        logout (bool | Unset): Whether the voucher support portal logout functionality
        description (str | Unset): Description of the voucher group
        print_comments (str | Unset): Print comments of the voucher group
        validity_type (int | Unset): The validity type of the voucher. It should be a value as follows: 0: Voucher can
            be used at any time, parameter [effectiveTime], [expirationTime] and [schedule] should be null. 1: Voucher can
            be used between the effective time and expiration time, parameter [effectiveTime] and [expirationTime] should
            not be null, parameter [schedule] should be null. 2: Voucher can be used within a specified time period by
            schedule, parameter [effectiveTime] and [expirationTime] should be null, parameter [schedule] should not be null
        schedule (VoucherScheduleOpenApiVO | Unset): Specified time period that voucher can be used. When parameter
            [validityType] is 2, parameter [schedule] is required
    """

    name: str
    amount: int
    code_length: int
    code_form: list[int]
    limit_type: int
    duration_type: int
    duration: int
    timing_type: int
    rate_limit: RateLimitOpenApiVO
    traffic_limit_enable: bool
    apply_to_all_portals: bool
    limit_num: int | Unset = UNSET
    traffic_limit: int | Unset = UNSET
    traffic_limit_frequency: int | Unset = UNSET
    unit_price: int | Unset = UNSET
    currency: str | Unset = UNSET
    portals: list[str] | Unset = UNSET
    expiration_time: int | Unset = UNSET
    effective_time: int | Unset = UNSET
    logout: bool | Unset = UNSET
    description: str | Unset = UNSET
    print_comments: str | Unset = UNSET
    validity_type: int | Unset = UNSET
    schedule: VoucherScheduleOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        amount = self.amount

        code_length = self.code_length

        code_form = self.code_form

        limit_type = self.limit_type

        duration_type = self.duration_type

        duration = self.duration

        timing_type = self.timing_type

        rate_limit = self.rate_limit.to_dict()

        traffic_limit_enable = self.traffic_limit_enable

        apply_to_all_portals = self.apply_to_all_portals

        limit_num = self.limit_num

        traffic_limit = self.traffic_limit

        traffic_limit_frequency = self.traffic_limit_frequency

        unit_price = self.unit_price

        currency = self.currency

        portals: list[str] | Unset = UNSET
        if not isinstance(self.portals, Unset):
            portals = self.portals

        expiration_time = self.expiration_time

        effective_time = self.effective_time

        logout = self.logout

        description = self.description

        print_comments = self.print_comments

        validity_type = self.validity_type

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "amount": amount,
                "codeLength": code_length,
                "codeForm": code_form,
                "limitType": limit_type,
                "durationType": duration_type,
                "duration": duration,
                "timingType": timing_type,
                "rateLimit": rate_limit,
                "trafficLimitEnable": traffic_limit_enable,
                "applyToAllPortals": apply_to_all_portals,
            }
        )
        if limit_num is not UNSET:
            field_dict["limitNum"] = limit_num
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if portals is not UNSET:
            field_dict["portals"] = portals
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if effective_time is not UNSET:
            field_dict["effectiveTime"] = effective_time
        if logout is not UNSET:
            field_dict["logout"] = logout
        if description is not UNSET:
            field_dict["description"] = description
        if print_comments is not UNSET:
            field_dict["printComments"] = print_comments
        if validity_type is not UNSET:
            field_dict["validityType"] = validity_type
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO
        from ..models.voucher_schedule_open_api_vo import (
            VoucherScheduleOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        amount = d.pop("amount")

        code_length = d.pop("codeLength")

        code_form = cast(list[int], d.pop("codeForm"))

        limit_type = d.pop("limitType")

        duration_type = d.pop("durationType")

        duration = d.pop("duration")

        timing_type = d.pop("timingType")

        rate_limit = RateLimitOpenApiVO.from_dict(d.pop("rateLimit"))

        traffic_limit_enable = d.pop("trafficLimitEnable")

        apply_to_all_portals = d.pop("applyToAllPortals")

        limit_num = d.pop("limitNum", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        currency = d.pop("currency", UNSET)

        portals = cast(list[str], d.pop("portals", UNSET))

        expiration_time = d.pop("expirationTime", UNSET)

        effective_time = d.pop("effectiveTime", UNSET)

        logout = d.pop("logout", UNSET)

        description = d.pop("description", UNSET)

        print_comments = d.pop("printComments", UNSET)

        validity_type = d.pop("validityType", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: VoucherScheduleOpenApiVO | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = VoucherScheduleOpenApiVO.from_dict(_schedule)

        create_voucher_group_open_api_vo = cls(
            name=name,
            amount=amount,
            code_length=code_length,
            code_form=code_form,
            limit_type=limit_type,
            duration_type=duration_type,
            duration=duration,
            timing_type=timing_type,
            rate_limit=rate_limit,
            traffic_limit_enable=traffic_limit_enable,
            apply_to_all_portals=apply_to_all_portals,
            limit_num=limit_num,
            traffic_limit=traffic_limit,
            traffic_limit_frequency=traffic_limit_frequency,
            unit_price=unit_price,
            currency=currency,
            portals=portals,
            expiration_time=expiration_time,
            effective_time=effective_time,
            logout=logout,
            description=description,
            print_comments=print_comments,
            validity_type=validity_type,
            schedule=schedule,
        )

        create_voucher_group_open_api_vo.additional_properties = d
        return create_voucher_group_open_api_vo

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
