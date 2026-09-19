from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_mapping_vo import LanMappingVO
    from ..models.wan_mapping_vo import WanMappingVO


T = TypeVar("T", bound="NetworkMappingVO")


@_attrs_define
class NetworkMappingVO:
    """
    Attributes:
        wan_mapping (WanMappingVO | Unset):
        lan_mapping (LanMappingVO | Unset):
        dest_model (int | Unset):
        wan_num (int | Unset):
    """

    wan_mapping: WanMappingVO | Unset = UNSET
    lan_mapping: LanMappingVO | Unset = UNSET
    dest_model: int | Unset = UNSET
    wan_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_mapping, Unset):
            wan_mapping = self.wan_mapping.to_dict()

        lan_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan_mapping, Unset):
            lan_mapping = self.lan_mapping.to_dict()

        dest_model = self.dest_model

        wan_num = self.wan_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wan_mapping is not UNSET:
            field_dict["wanMapping"] = wan_mapping
        if lan_mapping is not UNSET:
            field_dict["lanMapping"] = lan_mapping
        if dest_model is not UNSET:
            field_dict["destModel"] = dest_model
        if wan_num is not UNSET:
            field_dict["wanNum"] = wan_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_mapping_vo import LanMappingVO
        from ..models.wan_mapping_vo import WanMappingVO

        d = dict(src_dict)
        _wan_mapping = d.pop("wanMapping", UNSET)
        wan_mapping: WanMappingVO | Unset
        if isinstance(_wan_mapping, Unset):
            wan_mapping = UNSET
        else:
            wan_mapping = WanMappingVO.from_dict(_wan_mapping)

        _lan_mapping = d.pop("lanMapping", UNSET)
        lan_mapping: LanMappingVO | Unset
        if isinstance(_lan_mapping, Unset):
            lan_mapping = UNSET
        else:
            lan_mapping = LanMappingVO.from_dict(_lan_mapping)

        dest_model = d.pop("destModel", UNSET)

        wan_num = d.pop("wanNum", UNSET)

        network_mapping_vo = cls(
            wan_mapping=wan_mapping,
            lan_mapping=lan_mapping,
            dest_model=dest_model,
            wan_num=wan_num,
        )

        network_mapping_vo.additional_properties = d
        return network_mapping_vo

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
