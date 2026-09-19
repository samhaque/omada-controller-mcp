from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interface_info import InterfaceInfo


T = TypeVar("T", bound="DeviceInterfaces")


@_attrs_define
class DeviceInterfaces:
    """
    Attributes:
        interfaces (list[InterfaceInfo] | Unset):
        support_layout (bool | Unset): Whether the device supports reporting port layout information.
    """

    interfaces: list[InterfaceInfo] | Unset = UNSET
    support_layout: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        support_layout = self.support_layout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if support_layout is not UNSET:
            field_dict["supportLayout"] = support_layout

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.interface_info import InterfaceInfo

        d = dict(src_dict)
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[InterfaceInfo] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = InterfaceInfo.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        support_layout = d.pop("supportLayout", UNSET)

        device_interfaces = cls(
            interfaces=interfaces,
            support_layout=support_layout,
        )

        device_interfaces.additional_properties = d
        return device_interfaces

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
