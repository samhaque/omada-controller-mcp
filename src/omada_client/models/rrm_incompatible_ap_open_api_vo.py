from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RrmIncompatibleApOpenApiVO")


@_attrs_define
class RrmIncompatibleApOpenApiVO:
    """
    Attributes:
        name (str | Unset): Device name.
        mac (str | Unset): Device MAC.
        status_category (int | Unset): Status category. 0 : Disconnected. 1: Connected. 2: Pending. 3: Heartbeat Missed.
            4: Isolated.
        status (int | Unset): Detailed status.
        version (str | Unset): Simplified version of firmware,for example:2.5.0
        type_ (str | Unset): Device type.
        model (str | Unset): Device model.
        model_version (str | Unset): Model version.
        show_model (str | Unset): The model name of device.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    version: str | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        status_category = self.status_category

        status = self.status

        version = self.version

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        version = d.pop("version", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        rrm_incompatible_ap_open_api_vo = cls(
            name=name,
            mac=mac,
            status_category=status_category,
            status=status,
            version=version,
            type_=type_,
            model=model,
            model_version=model_version,
            show_model=show_model,
        )

        rrm_incompatible_ap_open_api_vo.additional_properties = d
        return rrm_incompatible_ap_open_api_vo

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
