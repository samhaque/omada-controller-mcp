from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExcludeApVO")


@_attrs_define
class ExcludeApVO:
    """
    Attributes:
        unsupport_type (int | Unset): 0: Not support mesh(cannot be excluded). 1: Not support channel deployment. 2: Not
            support power deployment.
        name (str | Unset): Device name.
        ip (str | Unset): IP adress.
        mac (str | Unset): Device MAC.
        status_category (int | Unset): Status category. 0 : Disconnected. 1: Connected. 2: Pending. 3: Heartbeat Missed.
            4: Isolated.
        status (int | Unset): Detailed status.
        model (str | Unset): Device model.
        model_version (str | Unset): Model version.
        show_model (str | Unset): The model name of device.
        type_ (str | Unset): Device type.
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
    """

    unsupport_type: int | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    mac: str | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    type_: str | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unsupport_type = self.unsupport_type

        name = self.name

        ip = self.ip

        mac = self.mac

        status_category = self.status_category

        status = self.status

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        type_ = self.type_

        added_in_advanced = self.added_in_advanced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unsupport_type is not UNSET:
            field_dict["unsupportType"] = unsupport_type
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mac is not UNSET:
            field_dict["mac"] = mac
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if type_ is not UNSET:
            field_dict["type"] = type_
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unsupport_type = d.pop("unsupportType", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        mac = d.pop("mac", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        type_ = d.pop("type", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        exclude_ap_vo = cls(
            unsupport_type=unsupport_type,
            name=name,
            ip=ip,
            mac=mac,
            status_category=status_category,
            status=status,
            model=model,
            model_version=model_version,
            show_model=show_model,
            type_=type_,
            added_in_advanced=added_in_advanced,
        )

        exclude_ap_vo.additional_properties = d
        return exclude_ap_vo

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
