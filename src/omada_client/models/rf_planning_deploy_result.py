from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RFPlanningDeployResult")


@_attrs_define
class RFPlanningDeployResult:
    """
    Attributes:
        first_deploy (bool | Unset): Parameter [firstDeploy] means whether WLAN Optimization has been successfully
            performed before. True: no. False: yes.
    """

    first_deploy: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_deploy = self.first_deploy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_deploy is not UNSET:
            field_dict["firstDeploy"] = first_deploy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        first_deploy = d.pop("firstDeploy", UNSET)

        rf_planning_deploy_result = cls(
            first_deploy=first_deploy,
        )

        rf_planning_deploy_result.additional_properties = d
        return rf_planning_deploy_result

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
