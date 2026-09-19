from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApOverrideAuditLogVO")


@_attrs_define
class ApOverrideAuditLogVO:
    """
    Attributes:
        global_ssid (str | Unset):
        old_ssid_name (str | Unset):
        new_ssid_name (str | Unset):
        old_vlan_id (str | Unset):
        new_vlan_id (str | Unset):
        password_modified (bool | Unset):
        ssid_name_modified (bool | Unset):
        vlan_id_modified (bool | Unset):
    """

    global_ssid: str | Unset = UNSET
    old_ssid_name: str | Unset = UNSET
    new_ssid_name: str | Unset = UNSET
    old_vlan_id: str | Unset = UNSET
    new_vlan_id: str | Unset = UNSET
    password_modified: bool | Unset = UNSET
    ssid_name_modified: bool | Unset = UNSET
    vlan_id_modified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_ssid = self.global_ssid

        old_ssid_name = self.old_ssid_name

        new_ssid_name = self.new_ssid_name

        old_vlan_id = self.old_vlan_id

        new_vlan_id = self.new_vlan_id

        password_modified = self.password_modified

        ssid_name_modified = self.ssid_name_modified

        vlan_id_modified = self.vlan_id_modified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_ssid is not UNSET:
            field_dict["globalSsid"] = global_ssid
        if old_ssid_name is not UNSET:
            field_dict["oldSsidName"] = old_ssid_name
        if new_ssid_name is not UNSET:
            field_dict["newSsidName"] = new_ssid_name
        if old_vlan_id is not UNSET:
            field_dict["oldVlanId"] = old_vlan_id
        if new_vlan_id is not UNSET:
            field_dict["newVlanId"] = new_vlan_id
        if password_modified is not UNSET:
            field_dict["passwordModified"] = password_modified
        if ssid_name_modified is not UNSET:
            field_dict["ssidNameModified"] = ssid_name_modified
        if vlan_id_modified is not UNSET:
            field_dict["vlanIdModified"] = vlan_id_modified

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        global_ssid = d.pop("globalSsid", UNSET)

        old_ssid_name = d.pop("oldSsidName", UNSET)

        new_ssid_name = d.pop("newSsidName", UNSET)

        old_vlan_id = d.pop("oldVlanId", UNSET)

        new_vlan_id = d.pop("newVlanId", UNSET)

        password_modified = d.pop("passwordModified", UNSET)

        ssid_name_modified = d.pop("ssidNameModified", UNSET)

        vlan_id_modified = d.pop("vlanIdModified", UNSET)

        ap_override_audit_log_vo = cls(
            global_ssid=global_ssid,
            old_ssid_name=old_ssid_name,
            new_ssid_name=new_ssid_name,
            old_vlan_id=old_vlan_id,
            new_vlan_id=new_vlan_id,
            password_modified=password_modified,
            ssid_name_modified=ssid_name_modified,
            vlan_id_modified=vlan_id_modified,
        )

        ap_override_audit_log_vo.additional_properties = d
        return ap_override_audit_log_vo

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
