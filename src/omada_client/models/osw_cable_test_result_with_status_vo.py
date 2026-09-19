from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_cable_test_result_vo import OswCableTestResultVO
    from ..models.osw_stack_member_cable_test_result_vo import (
        OswStackMemberCableTestResultVO,
    )


T = TypeVar("T", bound="OswCableTestResultWithStatusVO")


@_attrs_define
class OswCableTestResultWithStatusVO:
    """
    Attributes:
        status (int | Unset): Test status.It should be a value as follows: 0:free. 1:testing. 2:test done. 3:time out.
        data (list[OswCableTestResultVO] | Unset): Test results.
        stack_data (list[OswStackMemberCableTestResultVO] | Unset): Stack Test results
    """

    status: int | Unset = UNSET
    data: list[OswCableTestResultVO] | Unset = UNSET
    stack_data: list[OswStackMemberCableTestResultVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        stack_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_data, Unset):
            stack_data = []
            for stack_data_item_data in self.stack_data:
                stack_data_item = stack_data_item_data.to_dict()
                stack_data.append(stack_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data
        if stack_data is not UNSET:
            field_dict["stackData"] = stack_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_cable_test_result_vo import (
            OswCableTestResultVO,
        )
        from ..models.osw_stack_member_cable_test_result_vo import (
            OswStackMemberCableTestResultVO,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: list[OswCableTestResultVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = OswCableTestResultVO.from_dict(data_item_data)

                data.append(data_item)

        _stack_data = d.pop("stackData", UNSET)
        stack_data: list[OswStackMemberCableTestResultVO] | Unset = UNSET
        if _stack_data is not UNSET:
            stack_data = []
            for stack_data_item_data in _stack_data:
                stack_data_item = OswStackMemberCableTestResultVO.from_dict(
                    stack_data_item_data
                )

                stack_data.append(stack_data_item)

        osw_cable_test_result_with_status_vo = cls(
            status=status,
            data=data,
            stack_data=stack_data,
        )

        osw_cable_test_result_with_status_vo.additional_properties = d
        return osw_cable_test_result_with_status_vo

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
