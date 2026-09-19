from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.osw_network_base_open_api import OswNetworkBaseOpenApi


T = TypeVar("T", bound="BatchApplyOswNetworkOpenApi")


@_attrs_define
class BatchApplyOswNetworkOpenApi:
    """
    Attributes:
        apply_list (list[OswNetworkBaseOpenApi]): Batch config networks status.
    """

    apply_list: list[OswNetworkBaseOpenApi]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apply_list = []
        for apply_list_item_data in self.apply_list:
            apply_list_item = apply_list_item_data.to_dict()
            apply_list.append(apply_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applyList": apply_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_network_base_open_api import (
            OswNetworkBaseOpenApi,
        )

        d = dict(src_dict)
        apply_list = []
        _apply_list = d.pop("applyList")
        for apply_list_item_data in _apply_list:
            apply_list_item = OswNetworkBaseOpenApi.from_dict(apply_list_item_data)

            apply_list.append(apply_list_item)

        batch_apply_osw_network_open_api = cls(
            apply_list=apply_list,
        )

        batch_apply_osw_network_open_api.additional_properties = d
        return batch_apply_osw_network_open_api

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
