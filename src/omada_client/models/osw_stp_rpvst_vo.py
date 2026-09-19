from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stp_rpvst_instance_vo import OswStpRpvstInstanceVO


T = TypeVar("T", bound="OswStpRpvstVO")


@_attrs_define
class OswStpRpvstVO:
    """STP RPVST Config, must not be null when stp is 4.

    Attributes:
        instances (list[OswStpRpvstInstanceVO] | Unset): Instances
    """

    instances: list[OswStpRpvstInstanceVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instances is not UNSET:
            field_dict["instances"] = instances

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stp_rpvst_instance_vo import (
            OswStpRpvstInstanceVO,
        )

        d = dict(src_dict)
        _instances = d.pop("instances", UNSET)
        instances: list[OswStpRpvstInstanceVO] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = OswStpRpvstInstanceVO.from_dict(instances_item_data)

                instances.append(instances_item)

        osw_stp_rpvst_vo = cls(
            instances=instances,
        )

        osw_stp_rpvst_vo.additional_properties = d
        return osw_stp_rpvst_vo

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
