from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_gateway_model_open_api_vo import DeviceGatewayModelOpenApiVO
    from ..models.device_switch_model_open_api_vo import DeviceSwitchModelOpenApiVO


T = TypeVar("T", bound="ValidDeviceModelOpenApiVO")


@_attrs_define
class ValidDeviceModelOpenApiVO:
    """
    Attributes:
        gateways (list[DeviceGatewayModelOpenApiVO] | Unset):
        switches (list[DeviceSwitchModelOpenApiVO] | Unset):
    """

    gateways: list[DeviceGatewayModelOpenApiVO] | Unset = UNSET
    switches: list[DeviceSwitchModelOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateways: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateways, Unset):
            gateways = []
            for gateways_item_data in self.gateways:
                gateways_item = gateways_item_data.to_dict()
                gateways.append(gateways_item)

        switches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switches, Unset):
            switches = []
            for switches_item_data in self.switches:
                switches_item = switches_item_data.to_dict()
                switches.append(switches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateways is not UNSET:
            field_dict["gateways"] = gateways
        if switches is not UNSET:
            field_dict["switches"] = switches

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_gateway_model_open_api_vo import (
            DeviceGatewayModelOpenApiVO,
        )
        from ..models.device_switch_model_open_api_vo import (
            DeviceSwitchModelOpenApiVO,
        )

        d = dict(src_dict)
        _gateways = d.pop("gateways", UNSET)
        gateways: list[DeviceGatewayModelOpenApiVO] | Unset = UNSET
        if _gateways is not UNSET:
            gateways = []
            for gateways_item_data in _gateways:
                gateways_item = DeviceGatewayModelOpenApiVO.from_dict(
                    gateways_item_data
                )

                gateways.append(gateways_item)

        _switches = d.pop("switches", UNSET)
        switches: list[DeviceSwitchModelOpenApiVO] | Unset = UNSET
        if _switches is not UNSET:
            switches = []
            for switches_item_data in _switches:
                switches_item = DeviceSwitchModelOpenApiVO.from_dict(switches_item_data)

                switches.append(switches_item)

        valid_device_model_open_api_vo = cls(
            gateways=gateways,
            switches=switches,
        )

        valid_device_model_open_api_vo.additional_properties = d
        return valid_device_model_open_api_vo

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
