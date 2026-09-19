from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceCapacity")


@_attrs_define
class DeviceCapacity:
    """Device capacity

    Attributes:
        adopted_ap_num (int | Unset): Adopted AP num of controller
        ap_capacity (int | Unset): Ap capacity of controller
        adopted_osw_num (int | Unset): Adopted switch num of controller
        osw_capacity (int | Unset): Switch capacity of controller
        adopted_osg_num (int | Unset): Adopted gateway num of controller
        osg_capacity (int | Unset): Gateway capacity of controller
    """

    adopted_ap_num: int | Unset = UNSET
    ap_capacity: int | Unset = UNSET
    adopted_osw_num: int | Unset = UNSET
    osw_capacity: int | Unset = UNSET
    adopted_osg_num: int | Unset = UNSET
    osg_capacity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adopted_ap_num = self.adopted_ap_num

        ap_capacity = self.ap_capacity

        adopted_osw_num = self.adopted_osw_num

        osw_capacity = self.osw_capacity

        adopted_osg_num = self.adopted_osg_num

        osg_capacity = self.osg_capacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adopted_ap_num is not UNSET:
            field_dict["adoptedApNum"] = adopted_ap_num
        if ap_capacity is not UNSET:
            field_dict["apCapacity"] = ap_capacity
        if adopted_osw_num is not UNSET:
            field_dict["adoptedOswNum"] = adopted_osw_num
        if osw_capacity is not UNSET:
            field_dict["oswCapacity"] = osw_capacity
        if adopted_osg_num is not UNSET:
            field_dict["adoptedOsgNum"] = adopted_osg_num
        if osg_capacity is not UNSET:
            field_dict["osgCapacity"] = osg_capacity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        adopted_ap_num = d.pop("adoptedApNum", UNSET)

        ap_capacity = d.pop("apCapacity", UNSET)

        adopted_osw_num = d.pop("adoptedOswNum", UNSET)

        osw_capacity = d.pop("oswCapacity", UNSET)

        adopted_osg_num = d.pop("adoptedOsgNum", UNSET)

        osg_capacity = d.pop("osgCapacity", UNSET)

        device_capacity = cls(
            adopted_ap_num=adopted_ap_num,
            ap_capacity=ap_capacity,
            adopted_osw_num=adopted_osw_num,
            osw_capacity=osw_capacity,
            adopted_osg_num=adopted_osg_num,
            osg_capacity=osg_capacity,
        )

        device_capacity.additional_properties = d
        return device_capacity

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
