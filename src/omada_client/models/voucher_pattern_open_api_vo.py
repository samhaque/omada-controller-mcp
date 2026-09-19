from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voucher_logo_vo import VoucherLogoVO


T = TypeVar("T", bound="VoucherPatternOpenApiVO")


@_attrs_define
class VoucherPatternOpenApiVO:
    """Voucher pattern

    Attributes:
        pattern_type (int | Unset): 0: Logo, 1: Title, 2: Disable
        pattern_code (str | Unset): Voucher code of the previewed voucher pattern
        position (int | Unset): 0: Left, 1: Right, 2: Middle
        logo_picture (VoucherLogoVO | Unset): Logo info of the voucher pattern, used when pattern type is 0
        logo_size (int | Unset): Logo size of the voucher pattern, used when pattern type is 0
        title (str | Unset): Title of the voucher pattern, used when pattern type is 1
        title_size (int | Unset): Title size of the voucher pattern, used when pattern type is 1
        ssid_network_enable (bool | Unset): Whether to print SSIDs and networks on the pattern of the voucher
        ssid_network_name_list (list[str] | Unset): SSID and network name list on the pattern of the voucher
        ssid_list (list[str] | Unset): IDs of the SSIDs on the pattern of the voucher
        network_list (list[str] | Unset): IDs of the networks on the pattern of the voucher
        duration_enable (bool | Unset): Whether to print duration of the voucher
        limit_enable (bool | Unset): Whether to print limit info of the voucher. Limit info is limited usage count or
            limited online user number depending on the setting of the voucher group.
        print_comments (str | Unset): Comments to print on the voucher
        validity (str | Unset): Validity information to print on the voucher
    """

    pattern_type: int | Unset = UNSET
    pattern_code: str | Unset = UNSET
    position: int | Unset = UNSET
    logo_picture: VoucherLogoVO | Unset = UNSET
    logo_size: int | Unset = UNSET
    title: str | Unset = UNSET
    title_size: int | Unset = UNSET
    ssid_network_enable: bool | Unset = UNSET
    ssid_network_name_list: list[str] | Unset = UNSET
    ssid_list: list[str] | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    duration_enable: bool | Unset = UNSET
    limit_enable: bool | Unset = UNSET
    print_comments: str | Unset = UNSET
    validity: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern_type = self.pattern_type

        pattern_code = self.pattern_code

        position = self.position

        logo_picture: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logo_picture, Unset):
            logo_picture = self.logo_picture.to_dict()

        logo_size = self.logo_size

        title = self.title

        title_size = self.title_size

        ssid_network_enable = self.ssid_network_enable

        ssid_network_name_list: list[str] | Unset = UNSET
        if not isinstance(self.ssid_network_name_list, Unset):
            ssid_network_name_list = self.ssid_network_name_list

        ssid_list: list[str] | Unset = UNSET
        if not isinstance(self.ssid_list, Unset):
            ssid_list = self.ssid_list

        network_list: list[str] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        duration_enable = self.duration_enable

        limit_enable = self.limit_enable

        print_comments = self.print_comments

        validity = self.validity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pattern_type is not UNSET:
            field_dict["patternType"] = pattern_type
        if pattern_code is not UNSET:
            field_dict["patternCode"] = pattern_code
        if position is not UNSET:
            field_dict["position"] = position
        if logo_picture is not UNSET:
            field_dict["logoPicture"] = logo_picture
        if logo_size is not UNSET:
            field_dict["logoSize"] = logo_size
        if title is not UNSET:
            field_dict["title"] = title
        if title_size is not UNSET:
            field_dict["titleSize"] = title_size
        if ssid_network_enable is not UNSET:
            field_dict["ssidNetworkEnable"] = ssid_network_enable
        if ssid_network_name_list is not UNSET:
            field_dict["ssidNetworkNameList"] = ssid_network_name_list
        if ssid_list is not UNSET:
            field_dict["ssidList"] = ssid_list
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if duration_enable is not UNSET:
            field_dict["durationEnable"] = duration_enable
        if limit_enable is not UNSET:
            field_dict["limitEnable"] = limit_enable
        if print_comments is not UNSET:
            field_dict["printComments"] = print_comments
        if validity is not UNSET:
            field_dict["validity"] = validity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.voucher_logo_vo import VoucherLogoVO

        d = dict(src_dict)
        pattern_type = d.pop("patternType", UNSET)

        pattern_code = d.pop("patternCode", UNSET)

        position = d.pop("position", UNSET)

        _logo_picture = d.pop("logoPicture", UNSET)
        logo_picture: VoucherLogoVO | Unset
        if isinstance(_logo_picture, Unset):
            logo_picture = UNSET
        else:
            logo_picture = VoucherLogoVO.from_dict(_logo_picture)

        logo_size = d.pop("logoSize", UNSET)

        title = d.pop("title", UNSET)

        title_size = d.pop("titleSize", UNSET)

        ssid_network_enable = d.pop("ssidNetworkEnable", UNSET)

        ssid_network_name_list = cast(list[str], d.pop("ssidNetworkNameList", UNSET))

        ssid_list = cast(list[str], d.pop("ssidList", UNSET))

        network_list = cast(list[str], d.pop("networkList", UNSET))

        duration_enable = d.pop("durationEnable", UNSET)

        limit_enable = d.pop("limitEnable", UNSET)

        print_comments = d.pop("printComments", UNSET)

        validity = d.pop("validity", UNSET)

        voucher_pattern_open_api_vo = cls(
            pattern_type=pattern_type,
            pattern_code=pattern_code,
            position=position,
            logo_picture=logo_picture,
            logo_size=logo_size,
            title=title,
            title_size=title_size,
            ssid_network_enable=ssid_network_enable,
            ssid_network_name_list=ssid_network_name_list,
            ssid_list=ssid_list,
            network_list=network_list,
            duration_enable=duration_enable,
            limit_enable=limit_enable,
            print_comments=print_comments,
            validity=validity,
        )

        voucher_pattern_open_api_vo.additional_properties = d
        return voucher_pattern_open_api_vo

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
