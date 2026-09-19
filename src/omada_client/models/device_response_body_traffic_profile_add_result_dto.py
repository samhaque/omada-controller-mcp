from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.device_response_body_traffic_profile_add_result_dto_device_type import (
    DeviceResponseBodyTrafficProfileAddResultDTODeviceType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.traffic_profile_add_result_dto import TrafficProfileAddResultDTO


T = TypeVar("T", bound="DeviceResponseBodyTrafficProfileAddResultDTO")


@_attrs_define
class DeviceResponseBodyTrafficProfileAddResultDTO:
    """
    Attributes:
        device_type (DeviceResponseBodyTrafficProfileAddResultDTODeviceType | Unset): deviceType should be a value as
            follows:ap,gateway,switch,pro ap,pro gateway,pro switch,festa ap,festa gateway,festa switch,ems,olt,onu.
        errcode (int | Unset): Device error code.
        message (str | Unset): Device error message
        data (TrafficProfileAddResultDTO | Unset): Device configuration information.If the type of data is
            'Object',ignore this field
    """

    device_type: DeviceResponseBodyTrafficProfileAddResultDTODeviceType | Unset = UNSET
    errcode: int | Unset = UNSET
    message: str | Unset = UNSET
    data: TrafficProfileAddResultDTO | Unset = UNSET
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
        from ..models.traffic_profile_add_result_dto import (
            TrafficProfileAddResultDTO,
        )

        d = dict(src_dict)
        _device_type = d.pop("deviceType", UNSET)
        device_type: DeviceResponseBodyTrafficProfileAddResultDTODeviceType | Unset
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = DeviceResponseBodyTrafficProfileAddResultDTODeviceType(
                _device_type
            )

        errcode = d.pop("errcode", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: TrafficProfileAddResultDTO | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TrafficProfileAddResultDTO.from_dict(_data)

        device_response_body_traffic_profile_add_result_dto = cls(
            device_type=device_type,
            errcode=errcode,
            message=message,
            data=data,
        )

        device_response_body_traffic_profile_add_result_dto.additional_properties = d
        return device_response_body_traffic_profile_add_result_dto

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
