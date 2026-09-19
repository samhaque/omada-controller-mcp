from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.res_error_code_vo import ResErrorCodeVO


T = TypeVar("T", bound="CheckFailedDeviceInfoForVlanVO")


@_attrs_define
class CheckFailedDeviceInfoForVlanVO:
    """
    Attributes:
        mac (str | Unset): check failed device mac
        stack_id (str | Unset): check failed stack id
        error_code (ResErrorCodeVO | Unset): Error code
    """

    mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    error_code: ResErrorCodeVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        stack_id = self.stack_id

        error_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.res_error_code_vo import ResErrorCodeVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: ResErrorCodeVO | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = ResErrorCodeVO.from_dict(_error_code)

        check_failed_device_info_for_vlan_vo = cls(
            mac=mac,
            stack_id=stack_id,
            error_code=error_code,
        )

        check_failed_device_info_for_vlan_vo.additional_properties = d
        return check_failed_device_info_for_vlan_vo

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
