from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenApiSpeedTestSelectPortsVO")


@_attrs_define
class OpenApiSpeedTestSelectPortsVO:
    """
    Attributes:
        port_uuid_list (list[str] | Unset): The uuid of selected wan ports for speed test.
        virtual_wan_id_list (list[str] | Unset): The id of selected virtual wan ports for speed test.
    """

    port_uuid_list: list[str] | Unset = UNSET
    virtual_wan_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid_list: list[str] | Unset = UNSET
        if not isinstance(self.port_uuid_list, Unset):
            port_uuid_list = self.port_uuid_list

        virtual_wan_id_list: list[str] | Unset = UNSET
        if not isinstance(self.virtual_wan_id_list, Unset):
            virtual_wan_id_list = self.virtual_wan_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_uuid_list is not UNSET:
            field_dict["portUuidList"] = port_uuid_list
        if virtual_wan_id_list is not UNSET:
            field_dict["virtualWanIdList"] = virtual_wan_id_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_uuid_list = cast(list[str], d.pop("portUuidList", UNSET))

        virtual_wan_id_list = cast(list[str], d.pop("virtualWanIdList", UNSET))

        open_api_speed_test_select_ports_vo = cls(
            port_uuid_list=port_uuid_list,
            virtual_wan_id_list=virtual_wan_id_list,
        )

        open_api_speed_test_select_ports_vo.additional_properties = d
        return open_api_speed_test_select_ports_vo

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
