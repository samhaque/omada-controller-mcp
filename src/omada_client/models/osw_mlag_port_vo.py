from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_port_status_vo import OswPortStatusVO
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswMlagPortVO")


@_attrs_define
class OswMlagPortVO:
    """M-LAG group device ports.

    Attributes:
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
        port_status (OswPortStatusVO | Unset): Port Status
        selectable (bool | Unset): whether the port can be selected to configure DAD Port or Peer Link Port.
        port (int | Unset):
    """

    standard_port: OswStandPortVO | Unset = UNSET
    port_status: OswPortStatusVO | Unset = UNSET
    selectable: bool | Unset = UNSET
    port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        port_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_status, Unset):
            port_status = self.port_status.to_dict()

        selectable = self.selectable

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if port_status is not UNSET:
            field_dict["portStatus"] = port_status
        if selectable is not UNSET:
            field_dict["selectable"] = selectable
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_port_status_vo import OswPortStatusVO
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        _standard_port = d.pop("standardPort", UNSET)
        standard_port: OswStandPortVO | Unset
        if isinstance(_standard_port, Unset):
            standard_port = UNSET
        else:
            standard_port = OswStandPortVO.from_dict(_standard_port)

        _port_status = d.pop("portStatus", UNSET)
        port_status: OswPortStatusVO | Unset
        if isinstance(_port_status, Unset):
            port_status = UNSET
        else:
            port_status = OswPortStatusVO.from_dict(_port_status)

        selectable = d.pop("selectable", UNSET)

        port = d.pop("port", UNSET)

        osw_mlag_port_vo = cls(
            standard_port=standard_port,
            port_status=port_status,
            selectable=selectable,
            port=port,
        )

        osw_mlag_port_vo.additional_properties = d
        return osw_mlag_port_vo

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
