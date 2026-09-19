from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_global_config_status_dto_onu_isolation import (
    OnuGlobalConfigStatusDTOOnuIsolation,
)
from ..models.onu_global_config_status_dto_support_onu_isolation import (
    OnuGlobalConfigStatusDTOSupportOnuIsolation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnuGlobalConfigStatusDTO")


@_attrs_define
class OnuGlobalConfigStatusDTO:
    """
    Attributes:
        onu_isolation (OnuGlobalConfigStatusDTOOnuIsolation | Unset): Whether to enable ONU isolation,onuIsolation
            should be a value as follows:ENABLE,DISABLE
        support_onu_isolation (OnuGlobalConfigStatusDTOSupportOnuIsolation | Unset): Whether the ONU support
            isolation.SupportOnuIsolation should be a value as follows:ENABLE,DISABLE
    """

    onu_isolation: OnuGlobalConfigStatusDTOOnuIsolation | Unset = UNSET
    support_onu_isolation: OnuGlobalConfigStatusDTOSupportOnuIsolation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        onu_isolation: str | Unset = UNSET
        if not isinstance(self.onu_isolation, Unset):
            onu_isolation = self.onu_isolation.value

        support_onu_isolation: str | Unset = UNSET
        if not isinstance(self.support_onu_isolation, Unset):
            support_onu_isolation = self.support_onu_isolation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if onu_isolation is not UNSET:
            field_dict["onuIsolation"] = onu_isolation
        if support_onu_isolation is not UNSET:
            field_dict["supportOnuIsolation"] = support_onu_isolation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _onu_isolation = d.pop("onuIsolation", UNSET)
        onu_isolation: OnuGlobalConfigStatusDTOOnuIsolation | Unset
        if isinstance(_onu_isolation, Unset):
            onu_isolation = UNSET
        else:
            onu_isolation = OnuGlobalConfigStatusDTOOnuIsolation(_onu_isolation)

        _support_onu_isolation = d.pop("supportOnuIsolation", UNSET)
        support_onu_isolation: OnuGlobalConfigStatusDTOSupportOnuIsolation | Unset
        if isinstance(_support_onu_isolation, Unset):
            support_onu_isolation = UNSET
        else:
            support_onu_isolation = OnuGlobalConfigStatusDTOSupportOnuIsolation(
                _support_onu_isolation
            )

        onu_global_config_status_dto = cls(
            onu_isolation=onu_isolation,
            support_onu_isolation=support_onu_isolation,
        )

        onu_global_config_status_dto.additional_properties = d
        return onu_global_config_status_dto

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
