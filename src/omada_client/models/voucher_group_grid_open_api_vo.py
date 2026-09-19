from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO
    from ..models.simple_voucher_open_api_vo import SimpleVoucherOpenApiVO
    from ..models.statistics_count_open_api_vo import StatisticsCountOpenApiVO
    from ..models.voucher_pattern_open_api_vo import VoucherPatternOpenApiVO
    from ..models.voucher_schedule_open_api_vo import VoucherScheduleOpenApiVO


T = TypeVar("T", bound="VoucherGroupGridOpenApiVO")


@_attrs_define
class VoucherGroupGridOpenApiVO:
    """
    Attributes:
        id (str | Unset): Voucher group ID
        name (str | Unset): Voucher group ID
        created_time (int | Unset): Create timestamp for the voucher group, unit: millisecond
        creator_name (str | Unset): Role of the creator of the voucher group
        limit_type (int | Unset): The limitations of the voucher. It should be a value as follows: 0: Limited Usage
            Counts, 1: Limited Online Users, 2: Unlimited
        limit_num (int | Unset): The number of limitations. It should be within the range of 1–999. If Parameter
            [limitType] is 0 or 1, [limitNum] should not be null.When Parameter [limitType] is 0, [limitNum] represents the
            maximum number of times this voucher can be used.When Parameter [limitType] is 1, [limitNum] represents the
            maximum number of users this voucher can be used at the same time.
        duration_type (int | Unset): The duration type of the voucher. It should be a value as follows: 0: Client
            duration, each client expires after the duration is used. 1: Voucher duration, after reaching the voucher
            duration, clients using the voucher will expire
        duration (int | Unset): Duration of one use, unit: minute. It should be within the range of 1–14400000.
        timing_type (int | Unset): The timing type of the voucher. It should be a value as follows: 0: Timing by time,
            clients can use vouchers for specified time duration. 1: Timing by usage, clients can use vouchers for the
            duration of actual usage
        rate_limit (RateLimitOpenApiVO | Unset): When configuring rate limit, can only configure one of
            rateLimitProfileId or customRateLimit
        traffic_limit_enable (bool | Unset): Whether to enable traffic limit
        traffic_limit (int | Unset): Traffic limit in MB. It should be within the range of 1–10485760
        traffic_limit_frequency (int | Unset): Frequency of traffic limit should be a value as follows: 0: total; 1:
            daily; 2: weekly; 3: monthly.
        unit_price (str | Unset): Price of single voucher. It should be within the range of 1–999999999
        currency (str | Unset): Currency Short Code of voucher. For the values of Currency Short Code, refer to section
            5.4.2 of the Open API Access Guide.
        portal_names (list[str] | Unset): Bound portal name list
        apply_to_all_portals (bool | Unset): Is the voucher effective for all portals, including all newly created
            portals
        expiration_time (int | Unset): The timestamp of the expiration of the voucher, unit: millisecond
        effective_time (int | Unset): The timestamp when the voucher takes effect, unit: millisecond
        validity_type (int | Unset): The validity type of the voucher. It should be a value as follows: 0: Voucher can
            be used at any time, parameter [effectiveTime], [expirationTime] and [schedule] should be null. 1: Voucher can
            be used between the effective time and expiration time, parameter [effectiveTime] and [expirationTime] should
            not be null, parameter [schedule] should be null. 2: Voucher can be used within a specified time period by
            schedule, parameter [effectiveTime] and [expirationTime] should be null, parameter [schedule] should not be null
        schedule (VoucherScheduleOpenApiVO | Unset): Specified time period that voucher can be used. When parameter
            [validityType] is 2, parameter [schedule] is required
        logout (bool | Unset): Whether the voucher support portal logout functionality
        description (str | Unset): Description of the voucher group
        print_comments (str | Unset): Print comments of the voucher group
        voucher_pattern (VoucherPatternOpenApiVO | Unset): Voucher pattern
        unused_count (int | Unset): Unused voucher counts of the voucher group, affected by search
        used_count (int | Unset): Used voucher counts of the voucher group, affected by search
        in_use_count (int | Unset): In use voucher counts of the voucher group, affected by search
        expired_count (int | Unset): Expired voucher counts of the voucher group, affected by search
        total_count (int | Unset): Total voucher counts of the voucher group, affected by search
        unused_amount (str | Unset): Unused voucher amount of the voucher group, unaffected by search
        used_amount (str | Unset): Used voucher amount of the voucher group, unaffected by search
        total_amount (str | Unset): Total voucher amount of the voucher group, unaffected by search
        statistics_count (StatisticsCountOpenApiVO | Unset): Represents the quantity of statistics for the voucher
            group, unaffected by search
        total_rows (int | Unset): Total rows of vouchers in the voucher group, affected by search
        current_page (int | Unset): Current page number
        current_size (int | Unset): Number of entries per page
        data (list[SimpleVoucherOpenApiVO] | Unset): Voucher pagination data of the voucher group
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    created_time: int | Unset = UNSET
    creator_name: str | Unset = UNSET
    limit_type: int | Unset = UNSET
    limit_num: int | Unset = UNSET
    duration_type: int | Unset = UNSET
    duration: int | Unset = UNSET
    timing_type: int | Unset = UNSET
    rate_limit: RateLimitOpenApiVO | Unset = UNSET
    traffic_limit_enable: bool | Unset = UNSET
    traffic_limit: int | Unset = UNSET
    traffic_limit_frequency: int | Unset = UNSET
    unit_price: str | Unset = UNSET
    currency: str | Unset = UNSET
    portal_names: list[str] | Unset = UNSET
    apply_to_all_portals: bool | Unset = UNSET
    expiration_time: int | Unset = UNSET
    effective_time: int | Unset = UNSET
    validity_type: int | Unset = UNSET
    schedule: VoucherScheduleOpenApiVO | Unset = UNSET
    logout: bool | Unset = UNSET
    description: str | Unset = UNSET
    print_comments: str | Unset = UNSET
    voucher_pattern: VoucherPatternOpenApiVO | Unset = UNSET
    unused_count: int | Unset = UNSET
    used_count: int | Unset = UNSET
    in_use_count: int | Unset = UNSET
    expired_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    unused_amount: str | Unset = UNSET
    used_amount: str | Unset = UNSET
    total_amount: str | Unset = UNSET
    statistics_count: StatisticsCountOpenApiVO | Unset = UNSET
    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[SimpleVoucherOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_time = self.created_time

        creator_name = self.creator_name

        limit_type = self.limit_type

        limit_num = self.limit_num

        duration_type = self.duration_type

        duration = self.duration

        timing_type = self.timing_type

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        traffic_limit_enable = self.traffic_limit_enable

        traffic_limit = self.traffic_limit

        traffic_limit_frequency = self.traffic_limit_frequency

        unit_price = self.unit_price

        currency = self.currency

        portal_names: list[str] | Unset = UNSET
        if not isinstance(self.portal_names, Unset):
            portal_names = self.portal_names

        apply_to_all_portals = self.apply_to_all_portals

        expiration_time = self.expiration_time

        effective_time = self.effective_time

        validity_type = self.validity_type

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        logout = self.logout

        description = self.description

        print_comments = self.print_comments

        voucher_pattern: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voucher_pattern, Unset):
            voucher_pattern = self.voucher_pattern.to_dict()

        unused_count = self.unused_count

        used_count = self.used_count

        in_use_count = self.in_use_count

        expired_count = self.expired_count

        total_count = self.total_count

        unused_amount = self.unused_amount

        used_amount = self.used_amount

        total_amount = self.total_amount

        statistics_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics_count, Unset):
            statistics_count = self.statistics_count.to_dict()

        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if creator_name is not UNSET:
            field_dict["creatorName"] = creator_name
        if limit_type is not UNSET:
            field_dict["limitType"] = limit_type
        if limit_num is not UNSET:
            field_dict["limitNum"] = limit_num
        if duration_type is not UNSET:
            field_dict["durationType"] = duration_type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if timing_type is not UNSET:
            field_dict["timingType"] = timing_type
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if traffic_limit_enable is not UNSET:
            field_dict["trafficLimitEnable"] = traffic_limit_enable
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if portal_names is not UNSET:
            field_dict["portalNames"] = portal_names
        if apply_to_all_portals is not UNSET:
            field_dict["applyToAllPortals"] = apply_to_all_portals
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if effective_time is not UNSET:
            field_dict["effectiveTime"] = effective_time
        if validity_type is not UNSET:
            field_dict["validityType"] = validity_type
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if logout is not UNSET:
            field_dict["logout"] = logout
        if description is not UNSET:
            field_dict["description"] = description
        if print_comments is not UNSET:
            field_dict["printComments"] = print_comments
        if voucher_pattern is not UNSET:
            field_dict["voucherPattern"] = voucher_pattern
        if unused_count is not UNSET:
            field_dict["unusedCount"] = unused_count
        if used_count is not UNSET:
            field_dict["usedCount"] = used_count
        if in_use_count is not UNSET:
            field_dict["inUseCount"] = in_use_count
        if expired_count is not UNSET:
            field_dict["expiredCount"] = expired_count
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if unused_amount is not UNSET:
            field_dict["unusedAmount"] = unused_amount
        if used_amount is not UNSET:
            field_dict["usedAmount"] = used_amount
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if statistics_count is not UNSET:
            field_dict["statisticsCount"] = statistics_count
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO
        from ..models.simple_voucher_open_api_vo import (
            SimpleVoucherOpenApiVO,
        )
        from ..models.statistics_count_open_api_vo import (
            StatisticsCountOpenApiVO,
        )
        from ..models.voucher_pattern_open_api_vo import (
            VoucherPatternOpenApiVO,
        )
        from ..models.voucher_schedule_open_api_vo import (
            VoucherScheduleOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        created_time = d.pop("createdTime", UNSET)

        creator_name = d.pop("creatorName", UNSET)

        limit_type = d.pop("limitType", UNSET)

        limit_num = d.pop("limitNum", UNSET)

        duration_type = d.pop("durationType", UNSET)

        duration = d.pop("duration", UNSET)

        timing_type = d.pop("timingType", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: RateLimitOpenApiVO | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = RateLimitOpenApiVO.from_dict(_rate_limit)

        traffic_limit_enable = d.pop("trafficLimitEnable", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        currency = d.pop("currency", UNSET)

        portal_names = cast(list[str], d.pop("portalNames", UNSET))

        apply_to_all_portals = d.pop("applyToAllPortals", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        effective_time = d.pop("effectiveTime", UNSET)

        validity_type = d.pop("validityType", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: VoucherScheduleOpenApiVO | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = VoucherScheduleOpenApiVO.from_dict(_schedule)

        logout = d.pop("logout", UNSET)

        description = d.pop("description", UNSET)

        print_comments = d.pop("printComments", UNSET)

        _voucher_pattern = d.pop("voucherPattern", UNSET)
        voucher_pattern: VoucherPatternOpenApiVO | Unset
        if isinstance(_voucher_pattern, Unset):
            voucher_pattern = UNSET
        else:
            voucher_pattern = VoucherPatternOpenApiVO.from_dict(_voucher_pattern)

        unused_count = d.pop("unusedCount", UNSET)

        used_count = d.pop("usedCount", UNSET)

        in_use_count = d.pop("inUseCount", UNSET)

        expired_count = d.pop("expiredCount", UNSET)

        total_count = d.pop("totalCount", UNSET)

        unused_amount = d.pop("unusedAmount", UNSET)

        used_amount = d.pop("usedAmount", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        _statistics_count = d.pop("statisticsCount", UNSET)
        statistics_count: StatisticsCountOpenApiVO | Unset
        if isinstance(_statistics_count, Unset):
            statistics_count = UNSET
        else:
            statistics_count = StatisticsCountOpenApiVO.from_dict(_statistics_count)

        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[SimpleVoucherOpenApiVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = SimpleVoucherOpenApiVO.from_dict(data_item_data)

                data.append(data_item)

        voucher_group_grid_open_api_vo = cls(
            id=id,
            name=name,
            created_time=created_time,
            creator_name=creator_name,
            limit_type=limit_type,
            limit_num=limit_num,
            duration_type=duration_type,
            duration=duration,
            timing_type=timing_type,
            rate_limit=rate_limit,
            traffic_limit_enable=traffic_limit_enable,
            traffic_limit=traffic_limit,
            traffic_limit_frequency=traffic_limit_frequency,
            unit_price=unit_price,
            currency=currency,
            portal_names=portal_names,
            apply_to_all_portals=apply_to_all_portals,
            expiration_time=expiration_time,
            effective_time=effective_time,
            validity_type=validity_type,
            schedule=schedule,
            logout=logout,
            description=description,
            print_comments=print_comments,
            voucher_pattern=voucher_pattern,
            unused_count=unused_count,
            used_count=used_count,
            in_use_count=in_use_count,
            expired_count=expired_count,
            total_count=total_count,
            unused_amount=unused_amount,
            used_amount=used_amount,
            total_amount=total_amount,
            statistics_count=statistics_count,
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
        )

        voucher_group_grid_open_api_vo.additional_properties = d
        return voucher_group_grid_open_api_vo

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
