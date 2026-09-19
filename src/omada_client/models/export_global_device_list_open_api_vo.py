from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_api_query_data_vo import OpenApiQueryDataVO


T = TypeVar("T", bound="ExportGlobalDeviceListOpenApiVO")


@_attrs_define
class ExportGlobalDeviceListOpenApiVO:
    """
    Attributes:
        mode (int): Value of mode should be 0 or 1 or 2. 0 : All columns, 1 : Customize the export columns, 2 : Default
            columns.
        format_ (int): Format should be a value as follows. 0 means CSV , 1 means XLSX.
        display_columns (list[str] | Unset): In mode 1, the displayColumns cannot be empty. Allowed column name for
            input : ['deviceName', 'serialNumber', 'macAddress', 'ipAddress', 'publicIpAddress',  'ipv6Address', 'status',
            'model', 'version', 'uplink', 'downlink', 'uptime', 'memoryUsage', 'cpuUsage',  'clients', 'downloadTraffic',
            'uploadTraffic', 'loopback', 'hop', 'wlanGroup', 'override',  'radio2G', 'radio5G', 'radio6G', '2gClients',
            '5gClients', '6gClients', 'bSsid', 'txRate', 'rxRate', 'channel', 'channelUtilization2G',
            'channelUtilization5G', 'channelUtilization6G', 'tags', 'lastSeen',  'configurationResult', 'licenseStatus'(pro
            controller exclusive), 'dueTime'(pro controller exclusive), 'series'(pro controller exclusive), 'health'(pro
            controller exclusive), 'stackGroup'(site view exclusive),  'uplinkDeviceName'(site view exclusive),
            'uplinkDevicePort'(site view exclusive),  'linkSpeed'(site view exclusive), 'duplex'(site view exclusive)]
        query_data (OpenApiQueryDataVO | Unset):
    """

    mode: int
    format_: int
    display_columns: list[str] | Unset = UNSET
    query_data: OpenApiQueryDataVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        format_ = self.format_

        display_columns: list[str] | Unset = UNSET
        if not isinstance(self.display_columns, Unset):
            display_columns = self.display_columns

        query_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_data, Unset):
            query_data = self.query_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "format": format_,
            }
        )
        if display_columns is not UNSET:
            field_dict["displayColumns"] = display_columns
        if query_data is not UNSET:
            field_dict["queryData"] = query_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.open_api_query_data_vo import OpenApiQueryDataVO

        d = dict(src_dict)
        mode = d.pop("mode")

        format_ = d.pop("format")

        display_columns = cast(list[str], d.pop("displayColumns", UNSET))

        _query_data = d.pop("queryData", UNSET)
        query_data: OpenApiQueryDataVO | Unset
        if isinstance(_query_data, Unset):
            query_data = UNSET
        else:
            query_data = OpenApiQueryDataVO.from_dict(_query_data)

        export_global_device_list_open_api_vo = cls(
            mode=mode,
            format_=format_,
            display_columns=display_columns,
            query_data=query_data,
        )

        export_global_device_list_open_api_vo.additional_properties = d
        return export_global_device_list_open_api_vo

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
