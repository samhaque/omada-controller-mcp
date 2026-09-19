from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iot_server_open_api_vo_filters_iot_server import (
        IotServerOpenApiVOFiltersIotServer,
    )


T = TypeVar("T", bound="IotServerOpenApiVO")


@_attrs_define
class IotServerOpenApiVO:
    """
    Attributes:
        name_iot_server (str): IoT Transport Stream setting name.
        enable_iot_server (bool): Whether to enable the IoT Transport Stream setting.
        server_url_iot_server (str): If the service type is http, the server URL must start with http://.
        server_type_iot_server (int): The server type should be a value as follows: [0: http].
        device_classes_iot_server (list[int]): Supports protocol-based filtering during IoT data reporting processes.<br
            />The device class list should contain the value as follows: [0:minew; 1:iBeacon; 2:Eddystone].
        authentication_iot_server (int): The parameter [authentication] should be a value as follows:[0:Use Token].
        rssi_format_iot_server (int): The signal strength reporting format currently supports five types: [0:Average;
            1:Max; 2:Last; 3:Smooth; 4:Bulk].
        ble_periodic_telemetry_iot_server (bool): Whether to enable the BLE Periodic Telemetry. When disabled no
            periodic packets will be uploaded.
        raw_data_iot_server (bool): Whether to enable the BLE Data Forwarding. When enabled, the AP directly reports the
            Bluetooth packet rawData to the server.
        id (str | Unset): The IoT Transport Stream entry ID.
        report_interval_iot_server (int | Unset): Data reporting interval configuration for AP devices in IoT systems.
        access_token_iot_server (str | Unset): This parameter becomes mandatory when the authentication method is set to
            "Use Token".<br/>Note:The parameter [clientId] should be 1 ~ 128 characters.
        client_id_iot_server (str | Unset): This parameter becomes mandatory when the authentication method is set to
            "Use Token".<br />Note:The parameter [clientId] should be 1 ~ 128 characters.
        filters_type_iot_server (list[int] | Unset): User-defined settings to manage AP device filtering rules for IoT
            devices.<br />The parameter [filtersType] should contain the value as follows:[0:Company Identifier; 1:Vendor;
            2:Local Name; 3:Service UUID; 4:Mac Oui; 5:iBeacon UUID; 6:UID; 7:URL].
        filters_iot_server (IotServerOpenApiVOFiltersIotServer | Unset): The keys in the [filters] map represent the
            filter types, while the values correspond to the specific filtering criteria or values associated with each
            filter type.<br />Note:<br />Filter type = 0, The Company Identifier must conform to a 4-digit or 6-digit
            hexadecimal encoding. It is only applicable to ibeacon devices<br />Filter type = 1, The Vendor should not
            exceed 255 bytes in length.<br />Filter type = 2, The Local Name should not exceed 120 bytes in length. It is
            only applicable to minew devices.<br />Filter type = 3, The Service UUID must conform to a 4-digit hexadecimal
            encoding. It is only applicable to minew and eddystone devices.<br />Filter type = 4, The Mac Oui must conform
            to a 6-digit hexadecimal encoding.<br />Filter type = 5, The iBeacon UUID must conform to a 32-digit hexadecimal
            encoding. It is only applicable to iBeacon devices.<br />Filter type = 6, The UID must conform to a 20-digit or
            32-digit hexadecimal encoding. It is only applicable to eddystone devices.<br />Filter type = 7, The URL should
            not include a scheme. It is only applicable to eddystone devices.<br />
        count_only_iot_server (bool | Unset): A switch that controls whether the AP device exclusively reports the count
            of IoT devices.
    """

    name_iot_server: str
    enable_iot_server: bool
    server_url_iot_server: str
    server_type_iot_server: int
    device_classes_iot_server: list[int]
    authentication_iot_server: int
    rssi_format_iot_server: int
    ble_periodic_telemetry_iot_server: bool
    raw_data_iot_server: bool
    id: str | Unset = UNSET
    report_interval_iot_server: int | Unset = UNSET
    access_token_iot_server: str | Unset = UNSET
    client_id_iot_server: str | Unset = UNSET
    filters_type_iot_server: list[int] | Unset = UNSET
    filters_iot_server: IotServerOpenApiVOFiltersIotServer | Unset = UNSET
    count_only_iot_server: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_iot_server = self.name_iot_server

        enable_iot_server = self.enable_iot_server

        server_url_iot_server = self.server_url_iot_server

        server_type_iot_server = self.server_type_iot_server

        device_classes_iot_server = self.device_classes_iot_server

        authentication_iot_server = self.authentication_iot_server

        rssi_format_iot_server = self.rssi_format_iot_server

        ble_periodic_telemetry_iot_server = self.ble_periodic_telemetry_iot_server

        raw_data_iot_server = self.raw_data_iot_server

        id = self.id

        report_interval_iot_server = self.report_interval_iot_server

        access_token_iot_server = self.access_token_iot_server

        client_id_iot_server = self.client_id_iot_server

        filters_type_iot_server: list[int] | Unset = UNSET
        if not isinstance(self.filters_type_iot_server, Unset):
            filters_type_iot_server = self.filters_type_iot_server

        filters_iot_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters_iot_server, Unset):
            filters_iot_server = self.filters_iot_server.to_dict()

        count_only_iot_server = self.count_only_iot_server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name_iotServer": name_iot_server,
                "enable_iotServer": enable_iot_server,
                "serverUrl_iotServer": server_url_iot_server,
                "serverType_iotServer": server_type_iot_server,
                "deviceClasses_iotServer": device_classes_iot_server,
                "authentication_iotServer": authentication_iot_server,
                "rssiFormat_iotServer": rssi_format_iot_server,
                "blePeriodicTelemetry_iotServer": ble_periodic_telemetry_iot_server,
                "rawData_iotServer": raw_data_iot_server,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if report_interval_iot_server is not UNSET:
            field_dict["reportInterval_iotServer"] = report_interval_iot_server
        if access_token_iot_server is not UNSET:
            field_dict["accessToken_iotServer"] = access_token_iot_server
        if client_id_iot_server is not UNSET:
            field_dict["clientId_iotServer"] = client_id_iot_server
        if filters_type_iot_server is not UNSET:
            field_dict["filtersType_iotServer"] = filters_type_iot_server
        if filters_iot_server is not UNSET:
            field_dict["filters_iotServer"] = filters_iot_server
        if count_only_iot_server is not UNSET:
            field_dict["countOnly_iotServer"] = count_only_iot_server

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.iot_server_open_api_vo_filters_iot_server import (
            IotServerOpenApiVOFiltersIotServer,
        )

        d = dict(src_dict)
        name_iot_server = d.pop("name_iotServer")

        enable_iot_server = d.pop("enable_iotServer")

        server_url_iot_server = d.pop("serverUrl_iotServer")

        server_type_iot_server = d.pop("serverType_iotServer")

        device_classes_iot_server = cast(list[int], d.pop("deviceClasses_iotServer"))

        authentication_iot_server = d.pop("authentication_iotServer")

        rssi_format_iot_server = d.pop("rssiFormat_iotServer")

        ble_periodic_telemetry_iot_server = d.pop("blePeriodicTelemetry_iotServer")

        raw_data_iot_server = d.pop("rawData_iotServer")

        id = d.pop("id", UNSET)

        report_interval_iot_server = d.pop("reportInterval_iotServer", UNSET)

        access_token_iot_server = d.pop("accessToken_iotServer", UNSET)

        client_id_iot_server = d.pop("clientId_iotServer", UNSET)

        filters_type_iot_server = cast(list[int], d.pop("filtersType_iotServer", UNSET))

        _filters_iot_server = d.pop("filters_iotServer", UNSET)
        filters_iot_server: IotServerOpenApiVOFiltersIotServer | Unset
        if isinstance(_filters_iot_server, Unset):
            filters_iot_server = UNSET
        else:
            filters_iot_server = IotServerOpenApiVOFiltersIotServer.from_dict(
                _filters_iot_server
            )

        count_only_iot_server = d.pop("countOnly_iotServer", UNSET)

        iot_server_open_api_vo = cls(
            name_iot_server=name_iot_server,
            enable_iot_server=enable_iot_server,
            server_url_iot_server=server_url_iot_server,
            server_type_iot_server=server_type_iot_server,
            device_classes_iot_server=device_classes_iot_server,
            authentication_iot_server=authentication_iot_server,
            rssi_format_iot_server=rssi_format_iot_server,
            ble_periodic_telemetry_iot_server=ble_periodic_telemetry_iot_server,
            raw_data_iot_server=raw_data_iot_server,
            id=id,
            report_interval_iot_server=report_interval_iot_server,
            access_token_iot_server=access_token_iot_server,
            client_id_iot_server=client_id_iot_server,
            filters_type_iot_server=filters_type_iot_server,
            filters_iot_server=filters_iot_server,
            count_only_iot_server=count_only_iot_server,
        )

        iot_server_open_api_vo.additional_properties = d
        return iot_server_open_api_vo

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
