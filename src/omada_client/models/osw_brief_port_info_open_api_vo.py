from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswBriefPortInfoOpenApiVO")


@_attrs_define
class OswBriefPortInfoOpenApiVO:
    """Port list

    Attributes:
        port (int | Unset): Port
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
    """

    port: int | Unset = UNSET
    standard_port: OswStandPortVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        _standard_port = d.pop("standardPort", UNSET)
        standard_port: OswStandPortVO | Unset
        if isinstance(_standard_port, Unset):
            standard_port = UNSET
        else:
            standard_port = OswStandPortVO.from_dict(_standard_port)

        osw_brief_port_info_open_api_vo = cls(
            port=port,
            standard_port=standard_port,
        )

        osw_brief_port_info_open_api_vo.additional_properties = d
        return osw_brief_port_info_open_api_vo

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
