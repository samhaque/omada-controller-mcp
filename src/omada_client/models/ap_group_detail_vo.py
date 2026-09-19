from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_group_detail_vo_remaining_binding import (
        ApGroupDetailVORemainingBinding,
    )


T = TypeVar("T", bound="ApGroupDetailVO")


@_attrs_define
class ApGroupDetailVO:
    """
    Attributes:
        id (str | Unset): AP Group ID
        name (str | Unset): AP Group Name
        ap_num (int | Unset): Number of APs in this group
        remaining_binding (ApGroupDetailVORemainingBinding | Unset): Number of SSID remaining bindings for this group
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    ap_num: int | Unset = UNSET
    remaining_binding: ApGroupDetailVORemainingBinding | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ap_num = self.ap_num

        remaining_binding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remaining_binding, Unset):
            remaining_binding = self.remaining_binding.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ap_num is not UNSET:
            field_dict["apNum"] = ap_num
        if remaining_binding is not UNSET:
            field_dict["remainingBinding"] = remaining_binding

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_group_detail_vo_remaining_binding import (
            ApGroupDetailVORemainingBinding,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ap_num = d.pop("apNum", UNSET)

        _remaining_binding = d.pop("remainingBinding", UNSET)
        remaining_binding: ApGroupDetailVORemainingBinding | Unset
        if isinstance(_remaining_binding, Unset):
            remaining_binding = UNSET
        else:
            remaining_binding = ApGroupDetailVORemainingBinding.from_dict(
                _remaining_binding
            )

        ap_group_detail_vo = cls(
            id=id,
            name=name,
            ap_num=ap_num,
            remaining_binding=remaining_binding,
        )

        ap_group_detail_vo.additional_properties = d
        return ap_group_detail_vo

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
