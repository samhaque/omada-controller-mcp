from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgPvIdNameVO")


@_attrs_define
class OsgPvIdNameVO:
    """
    Attributes:
        pv_id (int | Unset):
        pv_name (str | Unset):
        qos_tag_enable (bool | Unset):
    """

    pv_id: int | Unset = UNSET
    pv_name: str | Unset = UNSET
    qos_tag_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pv_id = self.pv_id

        pv_name = self.pv_name

        qos_tag_enable = self.qos_tag_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pv_id is not UNSET:
            field_dict["pvId"] = pv_id
        if pv_name is not UNSET:
            field_dict["pvName"] = pv_name
        if qos_tag_enable is not UNSET:
            field_dict["qosTagEnable"] = qos_tag_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pv_id = d.pop("pvId", UNSET)

        pv_name = d.pop("pvName", UNSET)

        qos_tag_enable = d.pop("qosTagEnable", UNSET)

        osg_pv_id_name_vo = cls(
            pv_id=pv_id,
            pv_name=pv_name,
            qos_tag_enable=qos_tag_enable,
        )

        osg_pv_id_name_vo.additional_properties = d
        return osg_pv_id_name_vo

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
