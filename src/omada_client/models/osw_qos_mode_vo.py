from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswQosModeVO")


@_attrs_define
class OswQosModeVO:
    """
    Attributes:
        qos_mode (int | Unset): Switch QoS Mode, 0:old mode(Based on Qos Profile implementation), 1:new mode(Based on
            QoS rules implementation.)
        completed (int | Unset): Indicates whether the new mode switch has been completed. 0: Not completed, 1:
            Completed. If it is in the preview state, qosMode is 1 and completed is 0.
    """

    qos_mode: int | Unset = UNSET
    completed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qos_mode = self.qos_mode

        completed = self.completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qos_mode is not UNSET:
            field_dict["qosMode"] = qos_mode
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        qos_mode = d.pop("qosMode", UNSET)

        completed = d.pop("completed", UNSET)

        osw_qos_mode_vo = cls(
            qos_mode=qos_mode,
            completed=completed,
        )

        osw_qos_mode_vo.additional_properties = d
        return osw_qos_mode_vo

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
