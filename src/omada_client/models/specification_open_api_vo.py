from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpecificationOpenApiVO")


@_attrs_define
class SpecificationOpenApiVO:
    """
    Attributes:
        interface_num (int | Unset): The number of interfaces supported by the site.
        url_filtering_num (int | Unset): The number of urlFilteringNum supported by the sitey.
        mac_group_address_num (int | Unset): The number of macGroupAddressNum supported by the site.
    """

    interface_num: int | Unset = UNSET
    url_filtering_num: int | Unset = UNSET
    mac_group_address_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_num = self.interface_num

        url_filtering_num = self.url_filtering_num

        mac_group_address_num = self.mac_group_address_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface_num is not UNSET:
            field_dict["interfaceNum"] = interface_num
        if url_filtering_num is not UNSET:
            field_dict["urlFilteringNum"] = url_filtering_num
        if mac_group_address_num is not UNSET:
            field_dict["macGroupAddressNum"] = mac_group_address_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interface_num = d.pop("interfaceNum", UNSET)

        url_filtering_num = d.pop("urlFilteringNum", UNSET)

        mac_group_address_num = d.pop("macGroupAddressNum", UNSET)

        specification_open_api_vo = cls(
            interface_num=interface_num,
            url_filtering_num=url_filtering_num,
            mac_group_address_num=mac_group_address_num,
        )

        specification_open_api_vo.additional_properties = d
        return specification_open_api_vo

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
