from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceGatewayModelOpenApiVO")


@_attrs_define
class DeviceGatewayModelOpenApiVO:
    """
    Attributes:
        model (str | Unset): The model name of device.
        model_version (str | Unset): The model version of device.For example: 1.0
        show_model (str | Unset): A complete description of the device model, including name and version.
        wireless_router (bool | Unset): Whether the device supports wirelessrouter.
    """

    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    wireless_router: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        wireless_router = self.wireless_router

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if wireless_router is not UNSET:
            field_dict["wirelessRouter"] = wireless_router

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        wireless_router = d.pop("wirelessRouter", UNSET)

        device_gateway_model_open_api_vo = cls(
            model=model,
            model_version=model_version,
            show_model=show_model,
            wireless_router=wireless_router,
        )

        device_gateway_model_open_api_vo.additional_properties = d
        return device_gateway_model_open_api_vo

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
