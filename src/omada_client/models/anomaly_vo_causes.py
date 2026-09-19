from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.anomaly_cause_vo import AnomalyCauseVO


T = TypeVar("T", bound="AnomalyVOCauses")


@_attrs_define
class AnomalyVOCauses:
    """Root causes map. Key is cause code, value is cause detail."""

    additional_properties: dict[str, AnomalyCauseVO] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_cause_vo import AnomalyCauseVO

        d = dict(src_dict)
        anomaly_vo_causes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AnomalyCauseVO.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        anomaly_vo_causes.additional_properties = additional_properties
        return anomaly_vo_causes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> AnomalyCauseVO:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: AnomalyCauseVO) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
