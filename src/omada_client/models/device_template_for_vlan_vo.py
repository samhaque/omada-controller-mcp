from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTemplateForVlanVO")


@_attrs_define
class DeviceTemplateForVlanVO:
    """DeviceTemplateForVlanVO

    Attributes:
        id (str | Unset): Device template id.
        mac (str | Unset): Device template mac, it is the same with id.
        name (str | Unset): Device template name.
        mode (str | Unset): Device template model.
        model_version (str | Unset): Device template model version.
        show_model (str | Unset): Device template show model
        type_ (str | Unset): Device template type, it should be a value as follows: "gateway", "switch"
    """

    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    mode: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac = self.mac

        name = self.name

        mode = self.mode

        model_version = self.model_version

        show_model = self.show_model

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        mode = d.pop("mode", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        type_ = d.pop("type", UNSET)

        device_template_for_vlan_vo = cls(
            id=id,
            mac=mac,
            name=name,
            mode=mode,
            model_version=model_version,
            show_model=show_model,
            type_=type_,
        )

        device_template_for_vlan_vo.additional_properties = d
        return device_template_for_vlan_vo

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
