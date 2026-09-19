from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_direction_entity import GatewayDirectionEntity


T = TypeVar("T", bound="MacFilteringGeneralSetting")


@_attrs_define
class MacFilteringGeneralSetting:
    """
    Attributes:
        enable (bool): Enable of the MAC filtering general setting.
        filter_mode (int | Unset): Filter mode should be a value as follows: 0: allow; 1: deny.
        direction (GatewayDirectionEntity | Unset): Only for Gateway.
    """

    enable: bool
    filter_mode: int | Unset = UNSET
    direction: GatewayDirectionEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        filter_mode = self.filter_mode

        direction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if filter_mode is not UNSET:
            field_dict["filterMode"] = filter_mode
        if direction is not UNSET:
            field_dict["direction"] = direction

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.gateway_direction_entity import (
            GatewayDirectionEntity,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        filter_mode = d.pop("filterMode", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: GatewayDirectionEntity | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = GatewayDirectionEntity.from_dict(_direction)

        mac_filtering_general_setting = cls(
            enable=enable,
            filter_mode=filter_mode,
            direction=direction,
        )

        mac_filtering_general_setting.additional_properties = d
        return mac_filtering_general_setting

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
