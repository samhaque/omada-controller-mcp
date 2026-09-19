from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_advice_vo_content_params import AnomalyAdviceVOContentParams
    from ..models.anomaly_advice_vo_devices import AnomalyAdviceVODevices


T = TypeVar("T", bound="AnomalyAdviceVO")


@_attrs_define
class AnomalyAdviceVO:
    """
    Attributes:
        content_params (AnomalyAdviceVOContentParams | Unset): Content parameter map for rendering the advice content
            template.
        devices (AnomalyAdviceVODevices | Unset): Device objects map used by this advice. Key is MAC address, value is
            device info.
        helpful (int | Unset): Whether the advice is helpful. 0: Not set, 1: Helpful, 2: Not helpful.
    """

    content_params: AnomalyAdviceVOContentParams | Unset = UNSET
    devices: AnomalyAdviceVODevices | Unset = UNSET
    helpful: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_params, Unset):
            content_params = self.content_params.to_dict()

        devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        helpful = self.helpful

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_params is not UNSET:
            field_dict["contentParams"] = content_params
        if devices is not UNSET:
            field_dict["devices"] = devices
        if helpful is not UNSET:
            field_dict["helpful"] = helpful

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_advice_vo_content_params import (
            AnomalyAdviceVOContentParams,
        )
        from ..models.anomaly_advice_vo_devices import (
            AnomalyAdviceVODevices,
        )

        d = dict(src_dict)
        _content_params = d.pop("contentParams", UNSET)
        content_params: AnomalyAdviceVOContentParams | Unset
        if isinstance(_content_params, Unset):
            content_params = UNSET
        else:
            content_params = AnomalyAdviceVOContentParams.from_dict(_content_params)

        _devices = d.pop("devices", UNSET)
        devices: AnomalyAdviceVODevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = AnomalyAdviceVODevices.from_dict(_devices)

        helpful = d.pop("helpful", UNSET)

        anomaly_advice_vo = cls(
            content_params=content_params,
            devices=devices,
            helpful=helpful,
        )

        anomaly_advice_vo.additional_properties = d
        return anomaly_advice_vo

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
