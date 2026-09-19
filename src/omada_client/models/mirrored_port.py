from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MirroredPort")


@_attrs_define
class MirroredPort:
    """Monitored Port

    Attributes:
        port (int | Unset): Port
        standard_port (str | Unset): Standard Port
        port_name (str | Unset): Port Name
    """

    port: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    port_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port = self.standard_port

        port_name = self.port_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if port_name is not UNSET:
            field_dict["portName"] = port_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        port_name = d.pop("portName", UNSET)

        mirrored_port = cls(
            port=port,
            standard_port=standard_port,
            port_name=port_name,
        )

        mirrored_port.additional_properties = d
        return mirrored_port

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
