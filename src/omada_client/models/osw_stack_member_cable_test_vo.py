from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_cable_test_port_vo import OswCableTestPortVO


T = TypeVar("T", bound="OswStackMemberCableTestVO")


@_attrs_define
class OswStackMemberCableTestVO:
    """stack member list

    Attributes:
        mac (str | Unset): MAC
        unit (int | Unset): Unit
        model (str | Unset): Device Model.
        model_version (str | Unset): Device Model Version.
        port_list (list[OswCableTestPortVO] | Unset): Port list
    """

    mac: str | Unset = UNSET
    unit: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    port_list: list[OswCableTestPortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        unit = self.unit

        model = self.model

        model_version = self.model_version

        port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = []
            for port_list_item_data in self.port_list:
                port_list_item = port_list_item_data.to_dict()
                port_list.append(port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if unit is not UNSET:
            field_dict["unit"] = unit
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_cable_test_port_vo import OswCableTestPortVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        unit = d.pop("unit", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        _port_list = d.pop("portList", UNSET)
        port_list: list[OswCableTestPortVO] | Unset = UNSET
        if _port_list is not UNSET:
            port_list = []
            for port_list_item_data in _port_list:
                port_list_item = OswCableTestPortVO.from_dict(port_list_item_data)

                port_list.append(port_list_item)

        osw_stack_member_cable_test_vo = cls(
            mac=mac,
            unit=unit,
            model=model,
            model_version=model_version,
            port_list=port_list,
        )

        osw_stack_member_cable_test_vo.additional_properties = d
        return osw_stack_member_cable_test_vo

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
