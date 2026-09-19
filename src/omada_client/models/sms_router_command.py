from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.access import Access
    from ..models.reboot import Reboot
    from ..models.status import Status


T = TypeVar("T", bound="SmsRouterCommand")


@_attrs_define
class SmsRouterCommand:
    """
    Attributes:
        reboot_enable (bool): Whether to enable the control of device restart via SMS.
        status_enable (bool): Whether to enable Viewing device-related information and WAN port-related information via
            SMS.
        access_enable (bool): Whether to enable the allow list of the above functions, and only allow users in the list
            to interact with the device.
        reboot (Reboot | Unset):
        status (Status | Unset):
        access (Access | Unset):
        resource (int | Unset): The SMS router command setting creation resource, such as: 0: new created, 1: from
            template, 2: override.
    """

    reboot_enable: bool
    status_enable: bool
    access_enable: bool
    reboot: Reboot | Unset = UNSET
    status: Status | Unset = UNSET
    access: Access | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reboot_enable = self.reboot_enable

        status_enable = self.status_enable

        access_enable = self.access_enable

        reboot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reboot, Unset):
            reboot = self.reboot.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rebootEnable": reboot_enable,
                "statusEnable": status_enable,
                "accessEnable": access_enable,
            }
        )
        if reboot is not UNSET:
            field_dict["reboot"] = reboot
        if status is not UNSET:
            field_dict["status"] = status
        if access is not UNSET:
            field_dict["access"] = access
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.access import Access
        from ..models.reboot import Reboot
        from ..models.status import Status

        d = dict(src_dict)
        reboot_enable = d.pop("rebootEnable")

        status_enable = d.pop("statusEnable")

        access_enable = d.pop("accessEnable")

        _reboot = d.pop("reboot", UNSET)
        reboot: Reboot | Unset
        if isinstance(_reboot, Unset):
            reboot = UNSET
        else:
            reboot = Reboot.from_dict(_reboot)

        _status = d.pop("status", UNSET)
        status: Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status.from_dict(_status)

        _access = d.pop("access", UNSET)
        access: Access | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = Access.from_dict(_access)

        resource = d.pop("resource", UNSET)

        sms_router_command = cls(
            reboot_enable=reboot_enable,
            status_enable=status_enable,
            access_enable=access_enable,
            reboot=reboot,
            status=status,
            access=access,
            resource=resource,
        )

        sms_router_command.additional_properties = d
        return sms_router_command

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
