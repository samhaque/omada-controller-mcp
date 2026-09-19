from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BandCtrlVO")


@_attrs_define
class BandCtrlVO:
    """BandCtrl

    Attributes:
        egress_enable (bool): Egress enable status
        ingress_enable (bool): Ingress enable status
        egress_limit (int | Unset): EgressLimit
        egress_unit (int | Unset): EgressUnit should be a value as follows: 1: Kbps and 2: Mbps
        ingress_limit (int | Unset): IngressLimit
        ingress_unit (int | Unset): IngressUnit should be a value as follows: 1: Kbps and 2: Mbps
    """

    egress_enable: bool
    ingress_enable: bool
    egress_limit: int | Unset = UNSET
    egress_unit: int | Unset = UNSET
    ingress_limit: int | Unset = UNSET
    ingress_unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        egress_enable = self.egress_enable

        ingress_enable = self.ingress_enable

        egress_limit = self.egress_limit

        egress_unit = self.egress_unit

        ingress_limit = self.ingress_limit

        ingress_unit = self.ingress_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "egressEnable": egress_enable,
                "ingressEnable": ingress_enable,
            }
        )
        if egress_limit is not UNSET:
            field_dict["egressLimit"] = egress_limit
        if egress_unit is not UNSET:
            field_dict["egressUnit"] = egress_unit
        if ingress_limit is not UNSET:
            field_dict["ingressLimit"] = ingress_limit
        if ingress_unit is not UNSET:
            field_dict["ingressUnit"] = ingress_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        egress_enable = d.pop("egressEnable")

        ingress_enable = d.pop("ingressEnable")

        egress_limit = d.pop("egressLimit", UNSET)

        egress_unit = d.pop("egressUnit", UNSET)

        ingress_limit = d.pop("ingressLimit", UNSET)

        ingress_unit = d.pop("ingressUnit", UNSET)

        band_ctrl_vo = cls(
            egress_enable=egress_enable,
            ingress_enable=ingress_enable,
            egress_limit=egress_limit,
            egress_unit=egress_unit,
            ingress_limit=ingress_limit,
            ingress_unit=ingress_unit,
        )

        band_ctrl_vo.additional_properties = d
        return band_ctrl_vo

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
