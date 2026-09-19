from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswStackPortCapVO")


@_attrs_define
class OswStackPortCapVO:
    """Ports capability that support configuration as stack port

    Attributes:
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
        group_speed_cap (list[int] | Unset): Stack port aggregation group link speed capability
    """

    standard_port: OswStandPortVO | Unset = UNSET
    group_speed_cap: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        group_speed_cap: list[int] | Unset = UNSET
        if not isinstance(self.group_speed_cap, Unset):
            group_speed_cap = self.group_speed_cap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if group_speed_cap is not UNSET:
            field_dict["groupSpeedCap"] = group_speed_cap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        _standard_port = d.pop("standardPort", UNSET)
        standard_port: OswStandPortVO | Unset
        if isinstance(_standard_port, Unset):
            standard_port = UNSET
        else:
            standard_port = OswStandPortVO.from_dict(_standard_port)

        group_speed_cap = cast(list[int], d.pop("groupSpeedCap", UNSET))

        osw_stack_port_cap_vo = cls(
            standard_port=standard_port,
            group_speed_cap=group_speed_cap,
        )

        osw_stack_port_cap_vo.additional_properties = d
        return osw_stack_port_cap_vo

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
