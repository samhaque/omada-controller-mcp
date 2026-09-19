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


T = TypeVar("T", bound="OswStackMemberPortCapAndStatusVO")


@_attrs_define
class OswStackMemberPortCapAndStatusVO:
    """Port Information

    Attributes:
        stack_support (bool | Unset): Stack Support
        standard_port (OswStandPortVO | Unset): Stack port aggregation group member port
        port_status (OswPortStatusVO | Unset): Port Status
    """

    stack_support: bool | Unset = UNSET
    standard_port: OswStandPortVO | Unset = UNSET
    port_status: OswPortStatusVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_support = self.stack_support

        standard_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard_port, Unset):
            standard_port = self.standard_port.to_dict()

        port_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_status, Unset):
            port_status = self.port_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_support is not UNSET:
            field_dict["stackSupport"] = stack_support
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if port_status is not UNSET:
            field_dict["portStatus"] = port_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_port_status_vo import OswPortStatusVO
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        stack_support = d.pop("stackSupport", UNSET)

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

        osw_stack_member_port_cap_and_status_vo = cls(
            stack_support=stack_support,
            standard_port=standard_port,
            port_status=port_status,
        )

        osw_stack_member_port_cap_and_status_vo.additional_properties = d
        return osw_stack_member_port_cap_and_status_vo

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
