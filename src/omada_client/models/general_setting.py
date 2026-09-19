from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dst_open_api_vo import DstOpenApiVO


T = TypeVar("T", bound="GeneralSetting")


@_attrs_define
class GeneralSetting:
    """
    Attributes:
        name (str): General setting name should be visible ASCII, between 1 and 32 characters.
        time_zone (str): For the values of timeZone, refer to section 5.1 of the Open API Access Guide.
        region (str): Country/Region of the controller
        dst (DstOpenApiVO | Unset): Daylight Saving Time
    """

    name: str
    time_zone: str
    region: str
    dst: DstOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        time_zone = self.time_zone

        region = self.region

        dst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dst, Unset):
            dst = self.dst.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timeZone": time_zone,
                "region": region,
            }
        )
        if dst is not UNSET:
            field_dict["dst"] = dst

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dst_open_api_vo import DstOpenApiVO

        d = dict(src_dict)
        name = d.pop("name")

        time_zone = d.pop("timeZone")

        region = d.pop("region")

        _dst = d.pop("dst", UNSET)
        dst: DstOpenApiVO | Unset
        if isinstance(_dst, Unset):
            dst = UNSET
        else:
            dst = DstOpenApiVO.from_dict(_dst)

        general_setting = cls(
            name=name,
            time_zone=time_zone,
            region=region,
            dst=dst,
        )

        general_setting.additional_properties = d
        return general_setting

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
