from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_category_options_open_api_vo import (
        ClientCategoryOptionsOpenApiVO,
    )
    from ..models.client_filtering_device_detail_open_api_vo import (
        ClientFilteringDeviceDetailOpenApiVO,
    )


T = TypeVar("T", bound="ClientFilteringOptions")


@_attrs_define
class ClientFilteringOptions:
    """
    Attributes:
        device_type (list[ClientCategoryOptionsOpenApiVO] | Unset): Type list of clients.
        vendor (list[str] | Unset): Vendor list of clients.
        device (list[str] | Unset): Device list.
        network (list[str] | Unset): Network list.
        ssid (list[str] | Unset): Ssid list.
        device_detail (list[ClientFilteringDeviceDetailOpenApiVO] | Unset): Device detail info list.
    """

    device_type: list[ClientCategoryOptionsOpenApiVO] | Unset = UNSET
    vendor: list[str] | Unset = UNSET
    device: list[str] | Unset = UNSET
    network: list[str] | Unset = UNSET
    ssid: list[str] | Unset = UNSET
    device_detail: list[ClientFilteringDeviceDetailOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = []
            for device_type_item_data in self.device_type:
                device_type_item = device_type_item_data.to_dict()
                device_type.append(device_type_item)

        vendor: list[str] | Unset = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor

        device: list[str] | Unset = UNSET
        if not isinstance(self.device, Unset):
            device = self.device

        network: list[str] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network

        ssid: list[str] | Unset = UNSET
        if not isinstance(self.ssid, Unset):
            ssid = self.ssid

        device_detail: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_detail, Unset):
            device_detail = []
            for device_detail_item_data in self.device_detail:
                device_detail_item = device_detail_item_data.to_dict()
                device_detail.append(device_detail_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if device is not UNSET:
            field_dict["device"] = device
        if network is not UNSET:
            field_dict["network"] = network
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if device_detail is not UNSET:
            field_dict["deviceDetail"] = device_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_category_options_open_api_vo import (
            ClientCategoryOptionsOpenApiVO,
        )
        from ..models.client_filtering_device_detail_open_api_vo import (
            ClientFilteringDeviceDetailOpenApiVO,
        )

        d = dict(src_dict)
        _device_type = d.pop("deviceType", UNSET)
        device_type: list[ClientCategoryOptionsOpenApiVO] | Unset = UNSET
        if _device_type is not UNSET:
            device_type = []
            for device_type_item_data in _device_type:
                device_type_item = ClientCategoryOptionsOpenApiVO.from_dict(
                    device_type_item_data
                )

                device_type.append(device_type_item)

        vendor = cast(list[str], d.pop("vendor", UNSET))

        device = cast(list[str], d.pop("device", UNSET))

        network = cast(list[str], d.pop("network", UNSET))

        ssid = cast(list[str], d.pop("ssid", UNSET))

        _device_detail = d.pop("deviceDetail", UNSET)
        device_detail: list[ClientFilteringDeviceDetailOpenApiVO] | Unset = UNSET
        if _device_detail is not UNSET:
            device_detail = []
            for device_detail_item_data in _device_detail:
                device_detail_item = ClientFilteringDeviceDetailOpenApiVO.from_dict(
                    device_detail_item_data
                )

                device_detail.append(device_detail_item)

        client_filtering_options = cls(
            device_type=device_type,
            vendor=vendor,
            device=device,
            network=network,
            ssid=ssid,
            device_detail=device_detail,
        )

        client_filtering_options.additional_properties = d
        return client_filtering_options

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
