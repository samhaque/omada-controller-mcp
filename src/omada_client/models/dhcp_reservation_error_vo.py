from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_reservation_error_vo_error_map import (
        DhcpReservationErrorVOErrorMap,
    )


T = TypeVar("T", bound="DhcpReservationErrorVO")


@_attrs_define
class DhcpReservationErrorVO:
    """
    Attributes:
        error_map (DhcpReservationErrorVOErrorMap | Unset): Error details when importing some entries fails: 0: The
            imported MAC entries conflict; 1: The server device's user list has reached its limit.
    """

    error_map: DhcpReservationErrorVOErrorMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_map, Unset):
            error_map = self.error_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_map is not UNSET:
            field_dict["errorMap"] = error_map

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_reservation_error_vo_error_map import (
            DhcpReservationErrorVOErrorMap,
        )

        d = dict(src_dict)
        _error_map = d.pop("errorMap", UNSET)
        error_map: DhcpReservationErrorVOErrorMap | Unset
        if isinstance(_error_map, Unset):
            error_map = UNSET
        else:
            error_map = DhcpReservationErrorVOErrorMap.from_dict(_error_map)

        dhcp_reservation_error_vo = cls(
            error_map=error_map,
        )

        dhcp_reservation_error_vo.additional_properties = d
        return dhcp_reservation_error_vo

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
