from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherBriefOpenApiVO")


@_attrs_define
class VoucherBriefOpenApiVO:
    """
    Attributes:
        code (str | Unset): Voucher code
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
        unit_price (str | Unset): Price of single voucher. It should be within the range of 1–999999999
        currency (str | Unset): Currency Short Code of voucher. For the values of Currency Short Code, refer to section
            5.4.2 of the Open API Access Guide.
        validity (str | Unset): The validity period information of the voucher
        print_comments (str | Unset): Print comments of the voucher
        ssid_name_list (list[str] | Unset): Ssid name for voucher
        network_name_list (list[str] | Unset): Network name for voucher
        pattern_type (int | Unset): Voucher pattern type. 0: Logo, 1: Title, 3: Disabled
        pic_id (str | Unset): Voucher logo picture ID
        title (str | Unset): Title for voucher
        position (int | Unset): Position for logo or title
        logo_size (int | Unset): Size of logo on the pattern of the voucher. It should be within the range of 12-18.
        title_size (int | Unset): Size of title on the pattern of the voucher. It should be within the range of 50-175
    """

    code: str | Unset = UNSET
    limit_type: int | Unset = UNSET
    limit_num: int | Unset = UNSET
    duration_type: int | Unset = UNSET
    duration: int | Unset = UNSET
    unit_price: str | Unset = UNSET
    currency: str | Unset = UNSET
    validity: str | Unset = UNSET
    print_comments: str | Unset = UNSET
    ssid_name_list: list[str] | Unset = UNSET
    network_name_list: list[str] | Unset = UNSET
    pattern_type: int | Unset = UNSET
    pic_id: str | Unset = UNSET
    title: str | Unset = UNSET
    position: int | Unset = UNSET
    logo_size: int | Unset = UNSET
    title_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        limit_type = self.limit_type

        limit_num = self.limit_num

        duration_type = self.duration_type

        duration = self.duration

        unit_price = self.unit_price

        currency = self.currency

        validity = self.validity

        print_comments = self.print_comments

        ssid_name_list: list[str] | Unset = UNSET
        if not isinstance(self.ssid_name_list, Unset):
            ssid_name_list = self.ssid_name_list

        network_name_list: list[str] | Unset = UNSET
        if not isinstance(self.network_name_list, Unset):
            network_name_list = self.network_name_list

        pattern_type = self.pattern_type

        pic_id = self.pic_id

        title = self.title

        position = self.position

        logo_size = self.logo_size

        title_size = self.title_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if limit_type is not UNSET:
            field_dict["limitType"] = limit_type
        if limit_num is not UNSET:
            field_dict["limitNum"] = limit_num
        if duration_type is not UNSET:
            field_dict["durationType"] = duration_type
        if duration is not UNSET:
            field_dict["duration"] = duration
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if validity is not UNSET:
            field_dict["validity"] = validity
        if print_comments is not UNSET:
            field_dict["printComments"] = print_comments
        if ssid_name_list is not UNSET:
            field_dict["ssidNameList"] = ssid_name_list
        if network_name_list is not UNSET:
            field_dict["networkNameList"] = network_name_list
        if pattern_type is not UNSET:
            field_dict["patternType"] = pattern_type
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
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        limit_type = d.pop("limitType", UNSET)

        limit_num = d.pop("limitNum", UNSET)

        duration_type = d.pop("durationType", UNSET)

        duration = d.pop("duration", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        currency = d.pop("currency", UNSET)

        validity = d.pop("validity", UNSET)

        print_comments = d.pop("printComments", UNSET)

        ssid_name_list = cast(list[str], d.pop("ssidNameList", UNSET))

        network_name_list = cast(list[str], d.pop("networkNameList", UNSET))

        pattern_type = d.pop("patternType", UNSET)

        pic_id = d.pop("picId", UNSET)

        title = d.pop("title", UNSET)

        position = d.pop("position", UNSET)

        logo_size = d.pop("logoSize", UNSET)

        title_size = d.pop("titleSize", UNSET)

        voucher_brief_open_api_vo = cls(
            code=code,
            limit_type=limit_type,
            limit_num=limit_num,
            duration_type=duration_type,
            duration=duration,
            unit_price=unit_price,
            currency=currency,
            validity=validity,
            print_comments=print_comments,
            ssid_name_list=ssid_name_list,
            network_name_list=network_name_list,
            pattern_type=pattern_type,
            pic_id=pic_id,
            title=title,
            position=position,
            logo_size=logo_size,
            title_size=title_size,
        )

        voucher_brief_open_api_vo.additional_properties = d
        return voucher_brief_open_api_vo

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
