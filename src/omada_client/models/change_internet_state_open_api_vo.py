from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangeInternetStateOpenApiVO")


@_attrs_define
class ChangeInternetStateOpenApiVO:
    """
    Attributes:
        port_id (int | Unset): port ID
        operation (int | Unset): operation, 1 for open, and 0 for close
        virtual_wan_id (str | Unset): If operating virtualWan, should give virtualWanId
    """

    port_id: int | Unset = UNSET
    operation: int | Unset = UNSET
    virtual_wan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        operation = self.operation

        virtual_wan_id = self.virtual_wan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        operation = d.pop("operation", UNSET)

        virtual_wan_id = d.pop("virtualWanId", UNSET)

        change_internet_state_open_api_vo = cls(
            port_id=port_id,
            operation=operation,
            virtual_wan_id=virtual_wan_id,
        )

        change_internet_state_open_api_vo.additional_properties = d
        return change_internet_state_open_api_vo

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
