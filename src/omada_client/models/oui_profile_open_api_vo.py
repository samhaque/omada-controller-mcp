from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oui_and_description import OUIAndDescription


T = TypeVar("T", bound="OuiProfileOpenApiVO")


@_attrs_define
class OuiProfileOpenApiVO:
    """OUIProfileOpenApiVO

    Attributes:
        name (str): OUI Profile name should contain 1 to 64 characters.
        oui_combine (list[OUIAndDescription] | Unset): OUI and description
    """

    name: str
    oui_combine: list[OUIAndDescription] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        oui_combine: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.oui_combine, Unset):
            oui_combine = []
            for oui_combine_item_data in self.oui_combine:
                oui_combine_item = oui_combine_item_data.to_dict()
                oui_combine.append(oui_combine_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if oui_combine is not UNSET:
            field_dict["ouiCombine"] = oui_combine

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.oui_and_description import OUIAndDescription

        d = dict(src_dict)
        name = d.pop("name")

        _oui_combine = d.pop("ouiCombine", UNSET)
        oui_combine: list[OUIAndDescription] | Unset = UNSET
        if _oui_combine is not UNSET:
            oui_combine = []
            for oui_combine_item_data in _oui_combine:
                oui_combine_item = OUIAndDescription.from_dict(oui_combine_item_data)

                oui_combine.append(oui_combine_item)

        oui_profile_open_api_vo = cls(
            name=name,
            oui_combine=oui_combine,
        )

        oui_profile_open_api_vo.additional_properties = d
        return oui_profile_open_api_vo

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
