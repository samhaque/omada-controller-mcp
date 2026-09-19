from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStatUplinkVO")


@_attrs_define
class OswStatUplinkVO:
    """Uplink device information

    Attributes:
        port (int | Unset): Port ID
        mac (str | Unset): Device mac
        name (str | Unset): Device name
        type_ (str | Unset): Device type
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected; 1:Connected; 2:Pending; 3:Heartbeat Missed; 4:Isolated
        model (str | Unset): Model of device
        model_version (str | Unset): Model version of device
    """

    port: int | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    status_category: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        mac = self.mac

        name = self.name

        type_ = self.type_

        status_category = self.status_category

        model = self.model

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        osw_stat_uplink_vo = cls(
            port=port,
            mac=mac,
            name=name,
            type_=type_,
            status_category=status_category,
            model=model,
            model_version=model_version,
        )

        osw_stat_uplink_vo.additional_properties = d
        return osw_stat_uplink_vo

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
