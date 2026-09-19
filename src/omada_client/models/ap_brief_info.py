from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApBriefInfo")


@_attrs_define
class ApBriefInfo:
    """
    Attributes:
        mac (str | Unset): Device MAC, e.g. 00-00-FF-FF-0C-E9
        name (str | Unset): Device name
        ip (str | Unset): Device IP
        status_category (int | Unset): Device status should be a value as follows: 0: Disconnected; 1: Connected; 2:
            Pending; 3: Heartbeat Missed; 4: Isolated
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        model (str | Unset): Device model name, such as EAP225.
        model_version (str | Unset): Model version of device,for example:3.0
        type_ (str | Unset): Device type
        show_model (str | Unset): Device model name with version, such as EAP225(EU) v3.0.
        special_model (str | Unset): Special device model,for example:EAP225-Outdoor-1a20a950b8d950e8
        active (bool | Unset): Mark whether the device is activated: When license (specific to cloud base) is false, the
            status column shows the pre-bound status. When it is true or null, the status column displays as it originally
            did.
        support_lock_to_ap (bool | Unset): Whether the device support function [Lock to ap].
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    show_model: str | Unset = UNSET
    special_model: str | Unset = UNSET
    active: bool | Unset = UNSET
    support_lock_to_ap: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        ip = self.ip

        status_category = self.status_category

        status = self.status

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        show_model = self.show_model

        special_model = self.special_model

        active = self.active

        support_lock_to_ap = self.support_lock_to_ap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if special_model is not UNSET:
            field_dict["specialModel"] = special_model
        if active is not UNSET:
            field_dict["active"] = active
        if support_lock_to_ap is not UNSET:
            field_dict["supportLockToAp"] = support_lock_to_ap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        show_model = d.pop("showModel", UNSET)

        special_model = d.pop("specialModel", UNSET)

        active = d.pop("active", UNSET)

        support_lock_to_ap = d.pop("supportLockToAp", UNSET)

        ap_brief_info = cls(
            mac=mac,
            name=name,
            ip=ip,
            status_category=status_category,
            status=status,
            model=model,
            model_version=model_version,
            type_=type_,
            show_model=show_model,
            special_model=special_model,
            active=active,
            support_lock_to_ap=support_lock_to_ap,
        )

        ap_brief_info.additional_properties = d
        return ap_brief_info

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
