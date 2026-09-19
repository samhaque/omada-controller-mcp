from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_bind_open_api_vo import DeviceBindOpenApiVO


T = TypeVar("T", bound="BindSiteOpenApiVO")


@_attrs_define
class BindSiteOpenApiVO:
    """
    Attributes:
        site_id (str): Site ID to bind.
        switches (list[DeviceBindOpenApiVO] | Unset): Switch choose for binding device template.
    """

    site_id: str
    switches: list[DeviceBindOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        switches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switches, Unset):
            switches = []
            for switches_item_data in self.switches:
                switches_item = switches_item_data.to_dict()
                switches.append(switches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteId": site_id,
            }
        )
        if switches is not UNSET:
            field_dict["switches"] = switches

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_bind_open_api_vo import (
            DeviceBindOpenApiVO,
        )

        d = dict(src_dict)
        site_id = d.pop("siteId")

        _switches = d.pop("switches", UNSET)
        switches: list[DeviceBindOpenApiVO] | Unset = UNSET
        if _switches is not UNSET:
            switches = []
            for switches_item_data in _switches:
                switches_item = DeviceBindOpenApiVO.from_dict(switches_item_data)

                switches.append(switches_item)

        bind_site_open_api_vo = cls(
            site_id=site_id,
            switches=switches,
        )

        bind_site_open_api_vo.additional_properties = d
        return bind_site_open_api_vo

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
