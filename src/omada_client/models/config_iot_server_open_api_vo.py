from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_iot_server_open_api_vo_filters import (
        ConfigIotServerOpenApiVOFilters,
    )


T = TypeVar("T", bound="ConfigIotServerOpenApiVO")


@_attrs_define
class ConfigIotServerOpenApiVO:
    """
    Attributes:
        name (str): IoT Transport Stream setting name.
        enable (bool): Whether to enable the IoT Transport Stream setting.
        server_url (str): If the service type is http, the server URL must start with http://.
        server_type (int): The server type should be a value as follows: [0: http].
        device_classes (list[int]): Supports protocol-based filtering during IoT data reporting processes.<br />The
            device class list should contain the value as follows: [0:minew; 1:iBeacon; 2:Eddystone].
        authentication (int): The parameter [authentication] should be a value as follows:[0:Use Token].
        access_token (str): This parameter becomes mandatory when the authentication method is set to "Use
            Token".<br/>Note:The parameter [clientId] should be 1 ~ 128 characters.
        client_id (str): This parameter becomes mandatory when the authentication method is set to "Use Token".<br
            />Note:The parameter [clientId] should be 1 ~ 128 characters.
        rssi_format (int): The signal strength reporting format currently supports five types: [0:Average; 1:Max;
            2:Last; 3:Smooth; 4:Bulk].
        ble_periodic_telemetry (bool): Whether to enable the BLE Periodic Telemetry. When disabled no periodic packets
            will be uploaded.
        raw_data (bool): Whether to enable the BLE Data Forwarding. When enabled, the AP directly reports the Bluetooth
            packet rawData to the server.
        report_interval (int | Unset): Data reporting interval configuration for AP devices in IoT systems.The parameter
            [reportInterval] should be within the range of 1–3600 in seconds, and it cannot be null when
            blePeriodicTelemetry is enabled.
        filters_type (list[int] | Unset): User-defined settings to manage AP device filtering rules for IoT devices.<br
            />The parameter [filtersType] should contain the value as follows:[0:Company Identifier; 1:Vendor; 2:Local Name;
            3:Service UUID; 4:Mac Oui; 5:iBeacon UUID; 6:UID; 7:URL].
        filters (ConfigIotServerOpenApiVOFilters | Unset): The keys in the [filters] map represent the filter types,
            while the values correspond to the specific filtering criteria or values associated with each filter type.<br
            />Note:<br />Filter type = 0, The Company Identifier must conform to a 4-digit or 6-digit hexadecimal encoding.
            It is only applicable to ibeacon devices<br />Filter type = 1, The Vendor should not exceed 255 bytes in
            length.<br />Filter type = 2, The Local Name should not exceed 120 bytes in length. It is only applicable to
            minew devices.<br />Filter type = 3, The Service UUID must conform to a 4-digit hexadecimal encoding. It is only
            applicable to minew and eddystone devices.<br />Filter type = 4, The Mac Oui must conform to a 6-digit
            hexadecimal encoding.<br />Filter type = 5, The iBeacon UUID must conform to a 32-digit hexadecimal encoding. It
            is only applicable to iBeacon devices.<br />Filter type = 6, The UID must conform to a 20-digit or 32-digit
            hexadecimal encoding. It is only applicable to eddystone devices.<br />Filter type = 7, The URL should not
            include a scheme. It is only applicable to eddystone devices.<br />
        count_only (bool | Unset): A switch that controls whether the AP device exclusively reports the count of IoT
            devices, and it cannot be null when blePeriodicTelemetry is enabled.
    """

    name: str
    enable: bool
    server_url: str
    server_type: int
    device_classes: list[int]
    authentication: int
    access_token: str
    client_id: str
    rssi_format: int
    ble_periodic_telemetry: bool
    raw_data: bool
    report_interval: int | Unset = UNSET
    filters_type: list[int] | Unset = UNSET
    filters: ConfigIotServerOpenApiVOFilters | Unset = UNSET
    count_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enable = self.enable

        server_url = self.server_url

        server_type = self.server_type

        device_classes = self.device_classes

        authentication = self.authentication

        access_token = self.access_token

        client_id = self.client_id

        rssi_format = self.rssi_format

        ble_periodic_telemetry = self.ble_periodic_telemetry

        raw_data = self.raw_data

        report_interval = self.report_interval

        filters_type: list[int] | Unset = UNSET
        if not isinstance(self.filters_type, Unset):
            filters_type = self.filters_type

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        count_only = self.count_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "enable": enable,
                "serverUrl": server_url,
                "serverType": server_type,
                "deviceClasses": device_classes,
                "authentication": authentication,
                "accessToken": access_token,
                "clientId": client_id,
                "rssiFormat": rssi_format,
                "blePeriodicTelemetry": ble_periodic_telemetry,
                "rawData": raw_data,
            }
        )
        if report_interval is not UNSET:
            field_dict["reportInterval"] = report_interval
        if filters_type is not UNSET:
            field_dict["filtersType"] = filters_type
        if filters is not UNSET:
            field_dict["filters"] = filters
        if count_only is not UNSET:
            field_dict["countOnly"] = count_only

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.config_iot_server_open_api_vo_filters import (
            ConfigIotServerOpenApiVOFilters,
        )

        d = dict(src_dict)
        name = d.pop("name")

        enable = d.pop("enable")

        server_url = d.pop("serverUrl")

        server_type = d.pop("serverType")

        device_classes = cast(list[int], d.pop("deviceClasses"))

        authentication = d.pop("authentication")

        access_token = d.pop("accessToken")

        client_id = d.pop("clientId")

        rssi_format = d.pop("rssiFormat")

        ble_periodic_telemetry = d.pop("blePeriodicTelemetry")

        raw_data = d.pop("rawData")

        report_interval = d.pop("reportInterval", UNSET)

        filters_type = cast(list[int], d.pop("filtersType", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: ConfigIotServerOpenApiVOFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ConfigIotServerOpenApiVOFilters.from_dict(_filters)

        count_only = d.pop("countOnly", UNSET)

        config_iot_server_open_api_vo = cls(
            name=name,
            enable=enable,
            server_url=server_url,
            server_type=server_type,
            device_classes=device_classes,
            authentication=authentication,
            access_token=access_token,
            client_id=client_id,
            rssi_format=rssi_format,
            ble_periodic_telemetry=ble_periodic_telemetry,
            raw_data=raw_data,
            report_interval=report_interval,
            filters_type=filters_type,
            filters=filters,
            count_only=count_only,
        )

        config_iot_server_open_api_vo.additional_properties = d
        return config_iot_server_open_api_vo

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
