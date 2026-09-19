from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStatDownLinkVO")


@_attrs_define
class OswStatDownLinkVO:
    """Downlink devices of the port

    Attributes:
        mac (str | Unset): Device mac
        type_ (str | Unset): Type of down-link device
        client_type (str | Unset): Type of down-link client
        name (str | Unset): Device name
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected; 1:Connected; 2:Pending; 3:Heartbeat Missed; 4:Isolated
        model (str | Unset): Model of device
        model_version (str | Unset): Model version of device
    """

    mac: str | Unset = UNSET
    type_: str | Unset = UNSET
    client_type: str | Unset = UNSET
    name: str | Unset = UNSET
    status_category: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        type_ = self.type_

        client_type = self.client_type

        name = self.name

        status_category = self.status_category

        model = self.model

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if type_ is not UNSET:
            field_dict["type"] = type_
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if name is not UNSET:
            field_dict["name"] = name
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
        mac = d.pop("mac", UNSET)

        type_ = d.pop("type", UNSET)

        client_type = d.pop("clientType", UNSET)

        name = d.pop("name", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        osw_stat_down_link_vo = cls(
            mac=mac,
            type_=type_,
            client_type=client_type,
            name=name,
            status_category=status_category,
            model=model,
            model_version=model_version,
        )

        osw_stat_down_link_vo.additional_properties = d
        return osw_stat_down_link_vo

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
