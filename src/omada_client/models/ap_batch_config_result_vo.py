from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_config_result_vo import ApConfigResultVO


T = TypeVar("T", bound="ApBatchConfigResultVO")


@_attrs_define
class ApBatchConfigResultVO:
    """
    Attributes:
        config_result_list (list[ApConfigResultVO] | Unset): Configuration results for devices with partial or complete
            configuration failures.
    """

    config_result_list: list[ApConfigResultVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_result_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.config_result_list, Unset):
            config_result_list = []
            for config_result_list_item_data in self.config_result_list:
                config_result_list_item = config_result_list_item_data.to_dict()
                config_result_list.append(config_result_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_result_list is not UNSET:
            field_dict["configResultList"] = config_result_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_config_result_vo import ApConfigResultVO

        d = dict(src_dict)
        _config_result_list = d.pop("configResultList", UNSET)
        config_result_list: list[ApConfigResultVO] | Unset = UNSET
        if _config_result_list is not UNSET:
            config_result_list = []
            for config_result_list_item_data in _config_result_list:
                config_result_list_item = ApConfigResultVO.from_dict(
                    config_result_list_item_data
                )

                config_result_list.append(config_result_list_item)

        ap_batch_config_result_vo = cls(
            config_result_list=config_result_list,
        )

        ap_batch_config_result_vo.additional_properties = d
        return ap_batch_config_result_vo

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
