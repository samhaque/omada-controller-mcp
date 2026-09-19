from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.modify_dst_dto import ModifyDstDTO


T = TypeVar("T", bound="ModifyMspGeneralSettingOpenApiVO")


@_attrs_define
class ModifyMspGeneralSettingOpenApiVO:
    """
    Attributes:
        name (str | Unset): Parameter [name] should be within the range of 1–36 visible ASCII characters.
        time_zone (str | Unset): For the values of timeZone, refer to section 5.1 of the Open API Access Guide.
        dst (ModifyDstDTO | Unset): Daylight Saving Time config of the site
    """

    name: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    dst: ModifyDstDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        time_zone = self.time_zone

        dst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dst, Unset):
            dst = self.dst.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if dst is not UNSET:
            field_dict["dst"] = dst

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.modify_dst_dto import ModifyDstDTO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        _dst = d.pop("dst", UNSET)
        dst: ModifyDstDTO | Unset
        if isinstance(_dst, Unset):
            dst = UNSET
        else:
            dst = ModifyDstDTO.from_dict(_dst)

        modify_msp_general_setting_open_api_vo = cls(
            name=name,
            time_zone=time_zone,
            dst=dst,
        )

        modify_msp_general_setting_open_api_vo.additional_properties = d
        return modify_msp_general_setting_open_api_vo

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
