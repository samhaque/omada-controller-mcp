from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveClientVO")


@_attrs_define
class ActiveClientVO:
    """
    Attributes:
        name (str | Unset):
        wireless (bool | Unset):
        type_ (str | Unset):
        model (str | Unset):
        mac (str | Unset):
        total_traffic (int | Unset):
    """

    name: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    mac: str | Unset = UNSET
    total_traffic: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        wireless = self.wireless

        type_ = self.type_

        model = self.model

        mac = self.mac

        total_traffic = self.total_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if mac is not UNSET:
            field_dict["mac"] = mac
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        wireless = d.pop("wireless", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        mac = d.pop("mac", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        active_client_vo = cls(
            name=name,
            wireless=wireless,
            type_=type_,
            model=model,
            mac=mac,
            total_traffic=total_traffic,
        )

        active_client_vo.additional_properties = d
        return active_client_vo

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
