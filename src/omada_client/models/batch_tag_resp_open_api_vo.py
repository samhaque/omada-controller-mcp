from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.set_tag_result_open_api_vo import SetTagResultOpenApiVO


T = TypeVar("T", bound="BatchTagRespOpenApiVO")


@_attrs_define
class BatchTagRespOpenApiVO:
    """
    Attributes:
        batch_tag_result (list[SetTagResultOpenApiVO] | Unset): batch set tag result
    """

    batch_tag_result: list[SetTagResultOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_tag_result: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.batch_tag_result, Unset):
            batch_tag_result = []
            for batch_tag_result_item_data in self.batch_tag_result:
                batch_tag_result_item = batch_tag_result_item_data.to_dict()
                batch_tag_result.append(batch_tag_result_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_tag_result is not UNSET:
            field_dict["batchTagResult"] = batch_tag_result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.set_tag_result_open_api_vo import (
            SetTagResultOpenApiVO,
        )

        d = dict(src_dict)
        _batch_tag_result = d.pop("batchTagResult", UNSET)
        batch_tag_result: list[SetTagResultOpenApiVO] | Unset = UNSET
        if _batch_tag_result is not UNSET:
            batch_tag_result = []
            for batch_tag_result_item_data in _batch_tag_result:
                batch_tag_result_item = SetTagResultOpenApiVO.from_dict(
                    batch_tag_result_item_data
                )

                batch_tag_result.append(batch_tag_result_item)

        batch_tag_resp_open_api_vo = cls(
            batch_tag_result=batch_tag_result,
        )

        batch_tag_resp_open_api_vo.additional_properties = d
        return batch_tag_resp_open_api_vo

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
