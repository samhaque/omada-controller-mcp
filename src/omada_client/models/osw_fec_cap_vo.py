from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswFecCapVO")


@_attrs_define
class OswFecCapVO:
    """All LinkSpeed&FECMode combinations supported by the port

    Attributes:
        link_speed (int | Unset): speed of the link
        fec_mode (int | Unset): FEC mode, 0 - reserved, 1 - FEC-OFF, 2 - FEC-RS528, 3 - FEC-RS544, 4 - FEC-AUTO, 5 -
            FEC-BASER
    """

    link_speed: int | Unset = UNSET
    fec_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link_speed = self.link_speed

        fec_mode = self.fec_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if fec_mode is not UNSET:
            field_dict["fecMode"] = fec_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        link_speed = d.pop("linkSpeed", UNSET)

        fec_mode = d.pop("fecMode", UNSET)

        osw_fec_cap_vo = cls(
            link_speed=link_speed,
            fec_mode=fec_mode,
        )

        osw_fec_cap_vo.additional_properties = d
        return osw_fec_cap_vo

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
