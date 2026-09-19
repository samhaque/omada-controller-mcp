from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_snmp_open_api_vo import OsgSnmpOpenApiVO


T = TypeVar("T", bound="OsgConfigServicesOpenApiVO")


@_attrs_define
class OsgConfigServicesOpenApiVO:
    """
    Attributes:
        snmp (OsgSnmpOpenApiVO | Unset): Snmp setting
    """

    snmp: OsgSnmpOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snmp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snmp is not UNSET:
            field_dict["snmp"] = snmp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_snmp_open_api_vo import OsgSnmpOpenApiVO

        d = dict(src_dict)
        _snmp = d.pop("snmp", UNSET)
        snmp: OsgSnmpOpenApiVO | Unset
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = OsgSnmpOpenApiVO.from_dict(_snmp)

        osg_config_services_open_api_vo = cls(
            snmp=snmp,
        )

        osg_config_services_open_api_vo.additional_properties = d
        return osg_config_services_open_api_vo

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
