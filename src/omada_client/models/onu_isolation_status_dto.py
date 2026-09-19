from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.onu_isolation_status_dto_isolate_all_vlan import (
    OnuIsolationStatusDTOIsolateAllVlan,
)
from ..models.onu_isolation_status_dto_onu_isolation import (
    OnuIsolationStatusDTOOnuIsolation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnuIsolationStatusDTO")


@_attrs_define
class OnuIsolationStatusDTO:
    """
    Attributes:
        isolate_all_vlan (OnuIsolationStatusDTOIsolateAllVlan | Unset): Whether to isolate all ONUs within the
            VLANs.IsolateAllVlan should be a value as follows:DISABLE,ENABLE.Effective only when onuIsolation is set to
            ENABLE.
        vlan_list (str | Unset): vlanList should be a value as follows: "1,3-5,7".Effective only when onuIsolation is
            ENABLE and isolateAllVlan is DISABLE.
        onu_isolation (OnuIsolationStatusDTOOnuIsolation | Unset):
    """

    isolate_all_vlan: OnuIsolationStatusDTOIsolateAllVlan | Unset = UNSET
    vlan_list: str | Unset = UNSET
    onu_isolation: OnuIsolationStatusDTOOnuIsolation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        isolate_all_vlan: str | Unset = UNSET
        if not isinstance(self.isolate_all_vlan, Unset):
            isolate_all_vlan = self.isolate_all_vlan.value

        vlan_list = self.vlan_list

        onu_isolation: str | Unset = UNSET
        if not isinstance(self.onu_isolation, Unset):
            onu_isolation = self.onu_isolation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if isolate_all_vlan is not UNSET:
            field_dict["isolateAllVlan"] = isolate_all_vlan
        if vlan_list is not UNSET:
            field_dict["vlanList"] = vlan_list
        if onu_isolation is not UNSET:
            field_dict["onuIsolation"] = onu_isolation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _isolate_all_vlan = d.pop("isolateAllVlan", UNSET)
        isolate_all_vlan: OnuIsolationStatusDTOIsolateAllVlan | Unset
        if isinstance(_isolate_all_vlan, Unset):
            isolate_all_vlan = UNSET
        else:
            isolate_all_vlan = OnuIsolationStatusDTOIsolateAllVlan(_isolate_all_vlan)

        vlan_list = d.pop("vlanList", UNSET)

        _onu_isolation = d.pop("onuIsolation", UNSET)
        onu_isolation: OnuIsolationStatusDTOOnuIsolation | Unset
        if isinstance(_onu_isolation, Unset):
            onu_isolation = UNSET
        else:
            onu_isolation = OnuIsolationStatusDTOOnuIsolation(_onu_isolation)

        onu_isolation_status_dto = cls(
            isolate_all_vlan=isolate_all_vlan,
            vlan_list=vlan_list,
            onu_isolation=onu_isolation,
        )

        onu_isolation_status_dto.additional_properties = d
        return onu_isolation_status_dto

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
