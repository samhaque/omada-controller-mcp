from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cause_vo_advices import CauseVOAdvices
    from ..models.cause_vo_cause_title_params import CauseVOCauseTitleParams


T = TypeVar("T", bound="CauseVO")


@_attrs_define
class CauseVO:
    """Root causes and advices for this anomaly.

    Attributes:
        cause_code (str | Unset): Root cause code.
        cause_title_params (CauseVOCauseTitleParams | Unset): Title parameter map for rendering the root cause title
            template.
        advices (CauseVOAdvices | Unset): Advices for this root cause. Key is advice code, value is advice detail.
    """

    cause_code: str | Unset = UNSET
    cause_title_params: CauseVOCauseTitleParams | Unset = UNSET
    advices: CauseVOAdvices | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cause_code = self.cause_code

        cause_title_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cause_title_params, Unset):
            cause_title_params = self.cause_title_params.to_dict()

        advices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advices, Unset):
            advices = self.advices.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cause_code is not UNSET:
            field_dict["causeCode"] = cause_code
        if cause_title_params is not UNSET:
            field_dict["causeTitleParams"] = cause_title_params
        if advices is not UNSET:
            field_dict["advices"] = advices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cause_vo_advices import CauseVOAdvices
        from ..models.cause_vo_cause_title_params import (
            CauseVOCauseTitleParams,
        )

        d = dict(src_dict)
        cause_code = d.pop("causeCode", UNSET)

        _cause_title_params = d.pop("causeTitleParams", UNSET)
        cause_title_params: CauseVOCauseTitleParams | Unset
        if isinstance(_cause_title_params, Unset):
            cause_title_params = UNSET
        else:
            cause_title_params = CauseVOCauseTitleParams.from_dict(_cause_title_params)

        _advices = d.pop("advices", UNSET)
        advices: CauseVOAdvices | Unset
        if isinstance(_advices, Unset):
            advices = UNSET
        else:
            advices = CauseVOAdvices.from_dict(_advices)

        cause_vo = cls(
            cause_code=cause_code,
            cause_title_params=cause_title_params,
            advices=advices,
        )

        cause_vo.additional_properties = d
        return cause_vo

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
