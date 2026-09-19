from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO


T = TypeVar("T", bound="VoucherOpenApiVO")


@_attrs_define
class VoucherOpenApiVO:
    """
    Attributes:
        id (str | Unset): Voucher ID
        code (str | Unset): Voucher code
        created_time (int | Unset): Create timestamp for the voucher, unit: millisecond
        limit_type (int | Unset): The limitations of the voucher. It should be a value as follows: 0: Limited Usage
            Counts, 1: Limited Online Users, 2: Unlimited
        limit_num (int | Unset): The number of limitations. It should be within the range of 1–999. If Parameter
            [limitType] is 0 or 1, [limitNum] should not be null.When Parameter [limitType] is 0, [limitNum] represents the
            maximum number of times this voucher can be used.When Parameter [limitType] is 1, [limitNum] represents the
            maximum number of users this voucher can be used at the same time.
        used (int | Unset): The number of times the voucher is used
        duration_type (int | Unset): The duration type of the voucher. It should be a value as follows: 0: Client
            duration, each client expires after the duration is used. 1: Voucher duration, after reaching the voucher
            duration, clients using the voucher will expire
        duration (int | Unset): Duration of one use, unit: minute. It should be within the range of 1–14400000.
        timing_type (int | Unset): The timing type of the voucher. It should be a value as follows: 0: Timing by time,
            clients can use vouchers for specified time duration. 1: Timing by usage, clients can use vouchers for the
            duration of actual usage
        expiration_time (int | Unset): The timestamp of the expiration of the voucher, unit: millisecond
        effective_time (int | Unset): The timestamp when the voucher takes effect, unit: millisecond
        description (str | Unset): Description of the voucher
        rate_limit (RateLimitOpenApiVO | Unset): When configuring rate limit, can only configure one of
            rateLimitProfileId or customRateLimit
        traffic_limit_enable (bool | Unset): Whether to enable traffic limit
        traffic_limit (int | Unset): Traffic limit in MB. It should be within the range of 1–10485760
        traffic_limit_frequency (int | Unset): Frequency of traffic limit should be a value as follows: 0: total; 1:
            daily; 2: weekly; 3: monthly.
        traffic_left (bool | Unset): Is there remaining traffic of traffic for the voucher
        start_time (int | Unset): The time when the voucher was first used, 0 represents it hasn't started using yet
        end_time (int | Unset): The expiration date of the voucher
        valid (bool | Unset): Can the voucher still be used
        traffic_used (int | Unset): Used traffic of the voucher, unit: Byte
        unit_price (str | Unset): Price of single voucher. It should be within the range of 1–999999999
        currency (str | Unset): Currency Short Code of voucher. For the values of Currency Short Code, refer to section
            5.4.2 of the Open API Access Guide.
        portal_names (list[str] | Unset): Bound portal name list
        logout (bool | Unset): Whether the voucher support portal logout functionality
        validity (str | Unset): Information on the validity period of the voucher
        print_comments (str | Unset): Customized print information for voters
        ssid_name_list (list[str] | Unset): SSIDs for voucher
        network_name_list (list[str] | Unset): Networks for voucher
        pic_id (str | Unset): Voucher logo picture ID
        title (str | Unset): Title for voucher
        position (int | Unset): Position for logo or title
        logo_size (int | Unset): Size of logo on the pattern of the voucher. It should be within the range of 12-18.
        title_size (int | Unset): Size of title on the pattern of the voucher. It should be within the range of 50-175
    """

    id: str | Unset = UNSET
    code: str | Unset = UNSET
    created_time: int | Unset = UNSET
    limit_type: int | Unset = UNSET
    limit_num: int | Unset = UNSET
    used: int | Unset = UNSET
    duration_type: int | Unset = UNSET
    duration: int | Unset = UNSET
    timing_type: int | Unset = UNSET
    expiration_time: int | Unset = UNSET
    effective_time: int | Unset = UNSET
    description: str | Unset = UNSET
    rate_limit: RateLimitOpenApiVO | Unset = UNSET
    traffic_limit_enable: bool | Unset = UNSET
    traffic_limit: int | Unset = UNSET
    traffic_limit_frequency: int | Unset = UNSET
    traffic_left: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    valid: bool | Unset = UNSET
    traffic_used: int | Unset = UNSET
    unit_price: str | Unset = UNSET
    currency: str | Unset = UNSET
    portal_names: list[str] | Unset = UNSET
    logout: bool | Unset = UNSET
    validity: str | Unset = UNSET
    print_comments: str | Unset = UNSET
    ssid_name_list: list[str] | Unset = UNSET
    network_name_list: list[str] | Unset = UNSET
    pic_id: str | Unset = UNSET
    title: str | Unset = UNSET
    position: int | Unset = UNSET
    logo_size: int | Unset = UNSET
    title_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        code = self.code

        created_time = self.created_time

        limit_type = self.limit_type

        limit_num = self.limit_num

        used = self.used

        duration_type = self.duration_type

        duration = self.duration

        timing_type = self.timing_type

        expiration_time = self.expiration_time

        effective_time = self.effective_time

        description = self.description

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        traffic_limit_enable = self.traffic_limit_enable

        traffic_limit = self.traffic_limit

        traffic_limit_frequency = self.traffic_limit_frequency

        traffic_left = self.traffic_left

        start_time = self.start_time

        end_time = self.end_time

        valid = self.valid

        traffic_used = self.traffic_used

        unit_price = self.unit_price

        currency = self.currency

        portal_names: list[str] | Unset = UNSET
        if not isinstance(self.portal_names, Unset):
            portal_names = self.portal_names

        logout = self.logout

        validity = self.validity

        print_comments = self.print_comments

        ssid_name_list: list[str] | Unset = UNSET
        if not isinstance(self.ssid_name_list, Unset):
            ssid_name_list = self.ssid_name_list

        network_name_list: list[str] | Unset = UNSET
        if not isinstance(self.network_name_list, Unset):
            network_name_list = self.network_name_list

        pic_id = self.pic_id

        title = self.title

        position = self.position

        logo_size = self.logo_size

        title_size = self.title_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if code is not UNSET:
            field_dict["code"] = code
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if limit_type is not UNSET:
            field_dict["limitType"] = limit_type
        if limit_num is not UNSET:
            field_dict["limitNum"] = limit_num
        if used is not UNSET:
            field_dict["used"] = used
        if duration_type is not UNSET:
            field_dict["durationType"] = duration_type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if timing_type is not UNSET:
            field_dict["timingType"] = timing_type
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if effective_time is not UNSET:
            field_dict["effectiveTime"] = effective_time
        if description is not UNSET:
            field_dict["description"] = description
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if traffic_limit_enable is not UNSET:
            field_dict["trafficLimitEnable"] = traffic_limit_enable
        if traffic_limit is not UNSET:
            field_dict["trafficLimit"] = traffic_limit
        if traffic_limit_frequency is not UNSET:
            field_dict["trafficLimitFrequency"] = traffic_limit_frequency
        if traffic_left is not UNSET:
            field_dict["trafficLeft"] = traffic_left
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if valid is not UNSET:
            field_dict["valid"] = valid
        if traffic_used is not UNSET:
            field_dict["trafficUsed"] = traffic_used
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if portal_names is not UNSET:
            field_dict["portalNames"] = portal_names
        if logout is not UNSET:
            field_dict["logout"] = logout
        if validity is not UNSET:
            field_dict["validity"] = validity
        if print_comments is not UNSET:
            field_dict["printComments"] = print_comments
        if ssid_name_list is not UNSET:
            field_dict["ssidNameList"] = ssid_name_list
        if network_name_list is not UNSET:
            field_dict["networkNameList"] = network_name_list
        if pic_id is not UNSET:
            field_dict["picId"] = pic_id
        if title is not UNSET:
            field_dict["title"] = title
        if position is not UNSET:
            field_dict["position"] = position
        if logo_size is not UNSET:
            field_dict["logoSize"] = logo_size
        if title_size is not UNSET:
            field_dict["titleSize"] = title_size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rate_limit_open_api_vo import RateLimitOpenApiVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        code = d.pop("code", UNSET)

        created_time = d.pop("createdTime", UNSET)

        limit_type = d.pop("limitType", UNSET)

        limit_num = d.pop("limitNum", UNSET)

        used = d.pop("used", UNSET)

        duration_type = d.pop("durationType", UNSET)

        duration = d.pop("duration", UNSET)

        timing_type = d.pop("timingType", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        effective_time = d.pop("effectiveTime", UNSET)

        description = d.pop("description", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: RateLimitOpenApiVO | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = RateLimitOpenApiVO.from_dict(_rate_limit)

        traffic_limit_enable = d.pop("trafficLimitEnable", UNSET)

        traffic_limit = d.pop("trafficLimit", UNSET)

        traffic_limit_frequency = d.pop("trafficLimitFrequency", UNSET)

        traffic_left = d.pop("trafficLeft", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        valid = d.pop("valid", UNSET)

        traffic_used = d.pop("trafficUsed", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        currency = d.pop("currency", UNSET)

        portal_names = cast(list[str], d.pop("portalNames", UNSET))

        logout = d.pop("logout", UNSET)

        validity = d.pop("validity", UNSET)

        print_comments = d.pop("printComments", UNSET)

        ssid_name_list = cast(list[str], d.pop("ssidNameList", UNSET))

        network_name_list = cast(list[str], d.pop("networkNameList", UNSET))

        pic_id = d.pop("picId", UNSET)

        title = d.pop("title", UNSET)

        position = d.pop("position", UNSET)

        logo_size = d.pop("logoSize", UNSET)

        title_size = d.pop("titleSize", UNSET)

        voucher_open_api_vo = cls(
            id=id,
            code=code,
            created_time=created_time,
            limit_type=limit_type,
            limit_num=limit_num,
            used=used,
            duration_type=duration_type,
            duration=duration,
            timing_type=timing_type,
            expiration_time=expiration_time,
            effective_time=effective_time,
            description=description,
            rate_limit=rate_limit,
            traffic_limit_enable=traffic_limit_enable,
            traffic_limit=traffic_limit,
            traffic_limit_frequency=traffic_limit_frequency,
            traffic_left=traffic_left,
            start_time=start_time,
            end_time=end_time,
            valid=valid,
            traffic_used=traffic_used,
            unit_price=unit_price,
            currency=currency,
            portal_names=portal_names,
            logout=logout,
            validity=validity,
            print_comments=print_comments,
            ssid_name_list=ssid_name_list,
            network_name_list=network_name_list,
            pic_id=pic_id,
            title=title,
            position=position,
            logo_size=logo_size,
            title_size=title_size,
        )

        voucher_open_api_vo.additional_properties = d
        return voucher_open_api_vo

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
