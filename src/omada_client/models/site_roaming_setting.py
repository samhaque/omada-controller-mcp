from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.roaming_open_api_vo import RoamingOpenApiVO


T = TypeVar("T", bound="SiteRoamingSetting")


@_attrs_define
class SiteRoamingSetting:
    """Site roaming setting

    Attributes:
        roaming (RoamingOpenApiVO): Site roaming.
    """

    roaming: RoamingOpenApiVO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        roaming = self.roaming.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roaming": roaming,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.roaming_open_api_vo import RoamingOpenApiVO

        d = dict(src_dict)
        roaming = RoamingOpenApiVO.from_dict(d.pop("roaming"))

        site_roaming_setting = cls(
            roaming=roaming,
        )

        site_roaming_setting.additional_properties = d
        return site_roaming_setting

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
