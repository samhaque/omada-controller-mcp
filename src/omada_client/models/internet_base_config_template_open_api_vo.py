from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternetBaseConfigTemplateOpenApiVO")


@_attrs_define
class InternetBaseConfigTemplateOpenApiVO:
    """
    Attributes:
        wan_port_list (list[str]): List of enabled WAN port IDs, the valid port IDs can be obtained from "Get site
            template internet basic info".
        interval (int | Unset): Online detection interval(second). 0 means disable. It should be within the range of
            0–3600.
    """

    wan_port_list: list[str]
    interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_port_list = self.wan_port_list

        interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wanPortList": wan_port_list,
            }
        )
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wan_port_list = cast(list[str], d.pop("wanPortList"))

        interval = d.pop("interval", UNSET)

        internet_base_config_template_open_api_vo = cls(
            wan_port_list=wan_port_list,
            interval=interval,
        )

        internet_base_config_template_open_api_vo.additional_properties = d
        return internet_base_config_template_open_api_vo

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
