from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_info import PortInfo


T = TypeVar("T", bound="SwitchTemplateOverviewInfo")


@_attrs_define
class SwitchTemplateOverviewInfo:
    """
    Attributes:
        id (str | Unset): Device templateId
        model (str | Unset): Model
        hw_version (str | Unset): Hardware Version
        port_list (list[PortInfo] | Unset): Port List
    """

    id: str | Unset = UNSET
    model: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    port_list: list[PortInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        model = self.model

        hw_version = self.hw_version

        port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = []
            for port_list_item_data in self.port_list:
                port_list_item = port_list_item_data.to_dict()
                port_list.append(port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if model is not UNSET:
            field_dict["model"] = model
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_info import PortInfo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        model = d.pop("model", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        _port_list = d.pop("portList", UNSET)
        port_list: list[PortInfo] | Unset = UNSET
        if _port_list is not UNSET:
            port_list = []
            for port_list_item_data in _port_list:
                port_list_item = PortInfo.from_dict(port_list_item_data)

                port_list.append(port_list_item)

        switch_template_overview_info = cls(
            id=id,
            model=model,
            hw_version=hw_version,
            port_list=port_list,
        )

        switch_template_overview_info.additional_properties = d
        return switch_template_overview_info

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
