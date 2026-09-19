from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RFPlanningResult")


@_attrs_define
class RFPlanningResult:
    """
    Attributes:
        status (int): 0: Not in scanning status and a WLAN Optimization has been just successfully executed. 1: Not in
            scanning status and there's no WLAN Optimization result. 2: In RF planning status. 3: In RF planning canceling
            status.
        planning_histroy_id (str | Unset): Planning histroy ID.
        before_index (int | Unset): Index before WLAN Optimization, between 0 and 100.
        after_index (int | Unset): Index after WLAN Optimization, between 0 and 100.
        fail_type (int | Unset): Type of failure. 0: Failure before deployment. 1: Failure after deployment.
    """

    status: int
    planning_histroy_id: str | Unset = UNSET
    before_index: int | Unset = UNSET
    after_index: int | Unset = UNSET
    fail_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        planning_histroy_id = self.planning_histroy_id

        before_index = self.before_index

        after_index = self.after_index

        fail_type = self.fail_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if planning_histroy_id is not UNSET:
            field_dict["planningHistroyId"] = planning_histroy_id
        if before_index is not UNSET:
            field_dict["beforeIndex"] = before_index
        if after_index is not UNSET:
            field_dict["afterIndex"] = after_index
        if fail_type is not UNSET:
            field_dict["failType"] = fail_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        planning_histroy_id = d.pop("planningHistroyId", UNSET)

        before_index = d.pop("beforeIndex", UNSET)

        after_index = d.pop("afterIndex", UNSET)

        fail_type = d.pop("failType", UNSET)

        rf_planning_result = cls(
            status=status,
            planning_histroy_id=planning_histroy_id,
            before_index=before_index,
            after_index=after_index,
            fail_type=fail_type,
        )

        rf_planning_result.additional_properties = d
        return rf_planning_result

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
