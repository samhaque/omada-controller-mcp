from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interference_data_entity import InterferenceDataEntity


T = TypeVar("T", bound="Interference")


@_attrs_define
class Interference:
    """At most two types of interference data are reported in Inter, sorted in descending order of interference intensity

    Attributes:
        inf (int | Unset): Interference should be within the range of -96 ~ -48
        inf_type (int | Unset): Interference Type should be a value as follows: 0: invalid parameter; 1: MWO; 2: CW; 3:
            WLAN; 4: FHSS.
        inf_data (InterferenceDataEntity | Unset): Interference data, the data refer to the interference intensity and
            the times of interferences, and they are used to create histograms.
    """

    inf: int | Unset = UNSET
    inf_type: int | Unset = UNSET
    inf_data: InterferenceDataEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inf = self.inf

        inf_type = self.inf_type

        inf_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inf_data, Unset):
            inf_data = self.inf_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inf is not UNSET:
            field_dict["inf"] = inf
        if inf_type is not UNSET:
            field_dict["infType"] = inf_type
        if inf_data is not UNSET:
            field_dict["infData"] = inf_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.interference_data_entity import (
            InterferenceDataEntity,
        )

        d = dict(src_dict)
        inf = d.pop("inf", UNSET)

        inf_type = d.pop("infType", UNSET)

        _inf_data = d.pop("infData", UNSET)
        inf_data: InterferenceDataEntity | Unset
        if isinstance(_inf_data, Unset):
            inf_data = UNSET
        else:
            inf_data = InterferenceDataEntity.from_dict(_inf_data)

        interference = cls(
            inf=inf,
            inf_type=inf_type,
            inf_data=inf_data,
        )

        interference.additional_properties = d
        return interference

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
