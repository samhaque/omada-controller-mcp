from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.device_response_body_line_profile_dto_device_type import (
    DeviceResponseBodyLineProfileDTODeviceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_profile_dto import LineProfileDTO


T = TypeVar("T", bound="DeviceResponseBodyLineProfileDTO")


@_attrs_define
class DeviceResponseBodyLineProfileDTO:
    """
    Attributes:
        device_type (DeviceResponseBodyLineProfileDTODeviceType | Unset): deviceType should be a value as
            follows:ap,gateway,switch,pro ap,pro gateway,pro switch,festa ap,festa gateway,festa switch,ems,olt,onu.
        errcode (int | Unset): Device error code.
        message (str | Unset): Device error message
        data (LineProfileDTO | Unset):
    """

    device_type: DeviceResponseBodyLineProfileDTODeviceType | Unset = UNSET
    errcode: int | Unset = UNSET
    message: str | Unset = UNSET
    data: LineProfileDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_type: str | Unset = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type.value

        errcode = self.errcode

        message = self.message

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if errcode is not UNSET:
            field_dict["errcode"] = errcode
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.line_profile_dto import LineProfileDTO

        d = dict(src_dict)
        _device_type = d.pop("deviceType", UNSET)
        device_type: DeviceResponseBodyLineProfileDTODeviceType | Unset
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = DeviceResponseBodyLineProfileDTODeviceType(_device_type)

        errcode = d.pop("errcode", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: LineProfileDTO | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = LineProfileDTO.from_dict(_data)

        device_response_body_line_profile_dto = cls(
            device_type=device_type,
            errcode=errcode,
            message=message,
            data=data,
        )

        device_response_body_line_profile_dto.additional_properties = d
        return device_response_body_line_profile_dto

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
