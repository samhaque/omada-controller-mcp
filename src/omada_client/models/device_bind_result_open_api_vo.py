from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceBindResultOpenApiVO")


@_attrs_define
class DeviceBindResultOpenApiVO:
    """Devices with failed operation.

    Attributes:
        mac (str | Unset): The mac address of device, like AA-BB-CC-DD-EE-FF.
        site_id (str | Unset): The ID of target site.
        error_code (int | Unset): The error code for failed operation.
        msg (str | Unset): The message for failed operation.
    """

    mac: str | Unset = UNSET
    site_id: str | Unset = UNSET
    error_code: int | Unset = UNSET
    msg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        site_id = self.site_id

        error_code = self.error_code

        msg = self.msg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if msg is not UNSET:
            field_dict["msg"] = msg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        site_id = d.pop("siteId", UNSET)

        error_code = d.pop("errorCode", UNSET)

        msg = d.pop("msg", UNSET)

        device_bind_result_open_api_vo = cls(
            mac=mac,
            site_id=site_id,
            error_code=error_code,
            msg=msg,
        )

        device_bind_result_open_api_vo.additional_properties = d
        return device_bind_result_open_api_vo

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
