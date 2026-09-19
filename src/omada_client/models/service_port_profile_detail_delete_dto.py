from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicePortProfileDetailDeleteDTO")


@_attrs_define
class ServicePortProfileDetailDeleteDTO:
    """
    Attributes:
        service_port_id (list[str] | Unset): Service port ID List. It can be obtained from"Get service port profile
            detail list" interface. Up to 50 entries are allowed for the ids list.
        service_port_profile_id (str | Unset): Service port profile ID. The servicePortProfileId should be within the
            range of 1 to 127. It can be obtained from "Get service port profile detail".
    """

    service_port_id: list[str] | Unset = UNSET
    service_port_profile_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_port_id: list[str] | Unset = UNSET
        if not isinstance(self.service_port_id, Unset):
            service_port_id = self.service_port_id

        service_port_profile_id = self.service_port_profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_port_id is not UNSET:
            field_dict["servicePortId"] = service_port_id
        if service_port_profile_id is not UNSET:
            field_dict["servicePortProfileId"] = service_port_profile_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        service_port_id = cast(list[str], d.pop("servicePortId", UNSET))

        service_port_profile_id = d.pop("servicePortProfileId", UNSET)

        service_port_profile_detail_delete_dto = cls(
            service_port_id=service_port_id,
            service_port_profile_id=service_port_profile_id,
        )

        service_port_profile_detail_delete_dto.additional_properties = d
        return service_port_profile_detail_delete_dto

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
