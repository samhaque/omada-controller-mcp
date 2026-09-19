from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditVoucherGroupPatternOpenApiVO")


@_attrs_define
class EditVoucherGroupPatternOpenApiVO:
    """
    Attributes:
        pattern_type (int | Unset): 0: Logo, 1: Title, 2: Disable
        position (int | Unset): 0: Left, 1: Right, 2: Middle
        logo_picture_id (str | Unset): Logo picture ID
        logo_size (int | Unset): Logo size. It should be within the range of 50-175
        title (str | Unset): Voucher title
        title_size (int | Unset): Voucher title size. It should be within the range of 12-18
        ssid_networkenable (bool | Unset): Whether to print SSIDs and networks on the pattern of the voucher
        ssid_list (list[str] | Unset): SSID list on the pattern of the voucher
        network_list (list[str] | Unset): Network list on the pattern of the voucher
        duration_enable (bool | Unset): Whether to print duration of the voucher
        limit_enable (bool | Unset): Whether to print limit information of the voucher
        print_comments (str | Unset): Comments to print on the voucher
    """

    pattern_type: int | Unset = UNSET
    position: int | Unset = UNSET
    logo_picture_id: str | Unset = UNSET
    logo_size: int | Unset = UNSET
    title: str | Unset = UNSET
    title_size: int | Unset = UNSET
    ssid_networkenable: bool | Unset = UNSET
    ssid_list: list[str] | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    duration_enable: bool | Unset = UNSET
    limit_enable: bool | Unset = UNSET
    print_comments: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern_type = self.pattern_type

        position = self.position

        logo_picture_id = self.logo_picture_id

        logo_size = self.logo_size

        title = self.title

        title_size = self.title_size

        ssid_networkenable = self.ssid_networkenable

        ssid_list: list[str] | Unset = UNSET
        if not isinstance(self.ssid_list, Unset):
            ssid_list = self.ssid_list

        network_list: list[str] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        duration_enable = self.duration_enable

        limit_enable = self.limit_enable

        print_comments = self.print_comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pattern_type is not UNSET:
            field_dict["patternType"] = pattern_type
        if position is not UNSET:
            field_dict["position"] = position
        if logo_picture_id is not UNSET:
            field_dict["logoPictureId"] = logo_picture_id
        if logo_size is not UNSET:
            field_dict["logoSize"] = logo_size
        if title is not UNSET:
            field_dict["title"] = title
        if title_size is not UNSET:
            field_dict["titleSize"] = title_size
        if ssid_networkenable is not UNSET:
            field_dict["ssidNetworkenable"] = ssid_networkenable
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pattern_type = d.pop("patternType", UNSET)

        position = d.pop("position", UNSET)

        logo_picture_id = d.pop("logoPictureId", UNSET)

        logo_size = d.pop("logoSize", UNSET)

        title = d.pop("title", UNSET)

        title_size = d.pop("titleSize", UNSET)

        ssid_networkenable = d.pop("ssidNetworkenable", UNSET)

        ssid_list = cast(list[str], d.pop("ssidList", UNSET))

        network_list = cast(list[str], d.pop("networkList", UNSET))

        duration_enable = d.pop("durationEnable", UNSET)

        limit_enable = d.pop("limitEnable", UNSET)

        print_comments = d.pop("printComments", UNSET)

        edit_voucher_group_pattern_open_api_vo = cls(
            pattern_type=pattern_type,
            position=position,
            logo_picture_id=logo_picture_id,
            logo_size=logo_size,
            title=title,
            title_size=title_size,
            ssid_networkenable=ssid_networkenable,
            ssid_list=ssid_list,
            network_list=network_list,
            duration_enable=duration_enable,
            limit_enable=limit_enable,
            print_comments=print_comments,
        )

        edit_voucher_group_pattern_open_api_vo.additional_properties = d
        return edit_voucher_group_pattern_open_api_vo

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
