from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceGlobalSearchSummary")


@_attrs_define
class DeviceGlobalSearchSummary:
    """device list result

    Attributes:
        mac (str | Unset):
        active (bool | Unset):
        status (int | Unset):
        status_category (int | Unset):
        fw_download (bool | Unset):
        need_upgrade (bool | Unset):
        name (str | Unset):
        site (str | Unset):
        model (str | Unset):
        model_version (str | Unset):
        type_ (str | Unset):
        added_in_advance (bool | Unset):
    """

    mac: str | Unset = UNSET
    active: bool | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    fw_download: bool | Unset = UNSET
    need_upgrade: bool | Unset = UNSET
    name: str | Unset = UNSET
    site: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    added_in_advance: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        active = self.active

        status = self.status

        status_category = self.status_category

        fw_download = self.fw_download

        need_upgrade = self.need_upgrade

        name = self.name

        site = self.site

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        added_in_advance = self.added_in_advance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if active is not UNSET:
            field_dict["active"] = active
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if fw_download is not UNSET:
            field_dict["fwDownload"] = fw_download
        if need_upgrade is not UNSET:
            field_dict["needUpgrade"] = need_upgrade
        if name is not UNSET:
            field_dict["name"] = name
        if site is not UNSET:
            field_dict["site"] = site
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if added_in_advance is not UNSET:
            field_dict["addedInAdvance"] = added_in_advance

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        active = d.pop("active", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        fw_download = d.pop("fwDownload", UNSET)

        need_upgrade = d.pop("needUpgrade", UNSET)

        name = d.pop("name", UNSET)

        site = d.pop("site", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        added_in_advance = d.pop("addedInAdvance", UNSET)

        device_global_search_summary = cls(
            mac=mac,
            active=active,
            status=status,
            status_category=status_category,
            fw_download=fw_download,
            need_upgrade=need_upgrade,
            name=name,
            site=site,
            model=model,
            model_version=model_version,
            type_=type_,
            added_in_advance=added_in_advance,
        )

        device_global_search_summary.additional_properties = d
        return device_global_search_summary

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
