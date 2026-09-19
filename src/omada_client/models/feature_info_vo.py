from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeatureInfoVO")


@_attrs_define
class FeatureInfoVO:
    """Gateway Feature Description.

    Attributes:
        feature (str | Unset): Gateway feature name.
        feature_state (int | Unset): Gateway feature status: 0: The current gateway supports this feature. 1: The
            current gateway does not support this feature, but it is pre-configured. 2: The current gateway does not support
            this feature.
        changeable (bool | Unset): If the current gateway does not support this feature, then the [changeable] is false.
    """

    feature: str | Unset = UNSET
    feature_state: int | Unset = UNSET
    changeable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature = self.feature

        feature_state = self.feature_state

        changeable = self.changeable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature is not UNSET:
            field_dict["feature"] = feature
        if feature_state is not UNSET:
            field_dict["featureState"] = feature_state
        if changeable is not UNSET:
            field_dict["changeable"] = changeable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        feature = d.pop("feature", UNSET)

        feature_state = d.pop("featureState", UNSET)

        changeable = d.pop("changeable", UNSET)

        feature_info_vo = cls(
            feature=feature,
            feature_state=feature_state,
            changeable=changeable,
        )

        feature_info_vo.additional_properties = d
        return feature_info_vo

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
