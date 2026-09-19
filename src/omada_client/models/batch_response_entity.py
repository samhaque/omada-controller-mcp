from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_response_object import OperationResponseObject


T = TypeVar("T", bound="BatchResponseEntity")


@_attrs_define
class BatchResponseEntity:
    """
    Attributes:
        response (list[OperationResponseObject] | Unset): A response list
    """

    response: list[OperationResponseObject] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = []
            for response_item_data in self.response:
                response_item = response_item_data.to_dict()
                response.append(response_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.operation_response_object import (
            OperationResponseObject,
        )

        d = dict(src_dict)
        _response = d.pop("response", UNSET)
        response: list[OperationResponseObject] | Unset = UNSET
        if _response is not UNSET:
            response = []
            for response_item_data in _response:
                response_item = OperationResponseObject.from_dict(response_item_data)

                response.append(response_item)

        batch_response_entity = cls(
            response=response,
        )

        batch_response_entity.additional_properties = d
        return batch_response_entity

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
