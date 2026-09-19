from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenApiQuerySpeedTestDateListVO")


@_attrs_define
class OpenApiQuerySpeedTestDateListVO:
    """
    Attributes:
        current_page (int): Start from 1.
        current_page_size (int): It should be within the range of 1–100.
        port_uuid (str | Unset): Port Uuid. Only one of the parameters portUuid and virtualWanId can exist
        virtual_wan_id (str | Unset): Virtual Wan Id. Only one of the parameters portUuid and virtualWanId can exist
    """

    current_page: int
    current_page_size: int
    port_uuid: str | Unset = UNSET
    virtual_wan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        current_page_size = self.current_page_size

        port_uuid = self.port_uuid

        virtual_wan_id = self.virtual_wan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentPage": current_page,
                "currentPageSize": current_page_size,
            }
        )
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        current_page = d.pop("currentPage")

        current_page_size = d.pop("currentPageSize")

        port_uuid = d.pop("portUuid", UNSET)

        virtual_wan_id = d.pop("virtualWanId", UNSET)

        open_api_query_speed_test_date_list_vo = cls(
            current_page=current_page,
            current_page_size=current_page_size,
            port_uuid=port_uuid,
            virtual_wan_id=virtual_wan_id,
        )

        open_api_query_speed_test_date_list_vo.additional_properties = d
        return open_api_query_speed_test_date_list_vo

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
