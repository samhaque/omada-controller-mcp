from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotspotPortalsOpenApiVO")


@_attrs_define
class HotspotPortalsOpenApiVO:
    """Bound portal ID list,need to specify Content-Type of this form part as application/json.

    Attributes:
        portals (list[str]): Bound portal ID list.
        apply_to_all_portals (bool | Unset): Is the localuser effective for all portals, including all newly created
            portals
    """

    portals: list[str]
    apply_to_all_portals: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        portals = self.portals

        apply_to_all_portals = self.apply_to_all_portals

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portals": portals,
            }
        )
        if apply_to_all_portals is not UNSET:
            field_dict["applyToAllPortals"] = apply_to_all_portals

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        portals = cast(list[str], d.pop("portals"))

        apply_to_all_portals = d.pop("applyToAllPortals", UNSET)

        hotspot_portals_open_api_vo = cls(
            portals=portals,
            apply_to_all_portals=apply_to_all_portals,
        )

        hotspot_portals_open_api_vo.additional_properties = d
        return hotspot_portals_open_api_vo

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
