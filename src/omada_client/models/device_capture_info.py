from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_info import ChannelInfo
    from ..models.interface_info import InterfaceInfo


T = TypeVar("T", bound="DeviceCaptureInfo")


@_attrs_define
class DeviceCaptureInfo:
    """
    Attributes:
        mac (str | Unset): Device MAC.
        name (str | Unset): Device name.
        model (str | Unset): Model of device,for example:EAP225.
        model_version (str | Unset): Model version of device,for example:3.0
        show_model (str | Unset): Model complex shown in the front end.Ap：model+(country)+modelVersion,EAP225(EU) v3.0
            Gateway/Switch：model+modelVersion,Osg v3.0
        ip (str | Unset): IP Address.
        support_capture (bool | Unset): Parameter [supportCapture] indicates whether the device supports packet capture.
        support2g (bool | Unset): Whether the device supports 2.4GHz.
        support5g (bool | Unset): Whether the device supports 5GHz.
        support5g2 (bool | Unset): Whether the device supports 5GHz frequency splitting into two parts.
        support6g (bool | Unset): Whether the device supports 6GHz.
        firmware_version (str | Unset): Device firmware version.
        support_lan_capture (bool | Unset): Parameter [supportLanCapture] indicates whether the device supports LAN port
            packet capture.
        interfaces (list[InterfaceInfo] | Unset): Interface info.
        device_series_type (int | Unset): Device type: 0: Advanced; 1: Pro.
        type_ (str | Unset): Device Type.
        stack (bool | Unset): Parameter [stack] indicates whether the device supports stacking.
        stack_id (str | Unset): Stack ID.
        support_ota_capture (bool | Unset): Parameter [supportOTACapture] indicates whether the device supports air
            interface packet capture and flow-mode packet capture.
        current_channel_2_g (int | Unset): Current channel of 2.4 GHz.
        channel_list_2_g (list[ChannelInfo] | Unset): Channel list that device supports in 2.4 GHz.
        current_channel_5_g (int | Unset): Current channel of 5 GHz.
        channel_list_5_g (list[ChannelInfo] | Unset): Channel list that device supports in 5 GHz.
        current_channel_5_g_2 (int | Unset): Current channel of 5 GHz(2).
        channel_list_5_g_2 (list[ChannelInfo] | Unset): Channel list that device supports in 5 GHz(2).
        current_channel_6_g (int | Unset): Current channel of 6 GHz.
        channel_list_6_g (list[ChannelInfo] | Unset): Channel list that device supports in 6 GHz.
        file_size (int | Unset): Size limit of the captured file, in MB.
        support_stream_capture (bool | Unset): Parameter [supportStreamCapture] indicates whether the device supports
            flow-mode packet capture.
        support_scan_radio (bool | Unset): Parameter [supportScanRadio] indicates whether the device has independent
            radio frequency capabilities.
        scan_status (int | Unset): Scan Status of device,status should be a value as follows:  0:Not Scanned, 1:Spectrum
            Scanning, 2:RFScanning, 3:packet capturing, 4:RFPlanning, 5:Interference Detecting;
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    ip: str | Unset = UNSET
    support_capture: bool | Unset = UNSET
    support2g: bool | Unset = UNSET
    support5g: bool | Unset = UNSET
    support5g2: bool | Unset = UNSET
    support6g: bool | Unset = UNSET
    firmware_version: str | Unset = UNSET
    support_lan_capture: bool | Unset = UNSET
    interfaces: list[InterfaceInfo] | Unset = UNSET
    device_series_type: int | Unset = UNSET
    type_: str | Unset = UNSET
    stack: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    support_ota_capture: bool | Unset = UNSET
    current_channel_2_g: int | Unset = UNSET
    channel_list_2_g: list[ChannelInfo] | Unset = UNSET
    current_channel_5_g: int | Unset = UNSET
    channel_list_5_g: list[ChannelInfo] | Unset = UNSET
    current_channel_5_g_2: int | Unset = UNSET
    channel_list_5_g_2: list[ChannelInfo] | Unset = UNSET
    current_channel_6_g: int | Unset = UNSET
    channel_list_6_g: list[ChannelInfo] | Unset = UNSET
    file_size: int | Unset = UNSET
    support_stream_capture: bool | Unset = UNSET
    support_scan_radio: bool | Unset = UNSET
    scan_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        ip = self.ip

        support_capture = self.support_capture

        support2g = self.support2g

        support5g = self.support5g

        support5g2 = self.support5g2

        support6g = self.support6g

        firmware_version = self.firmware_version

        support_lan_capture = self.support_lan_capture

        interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        device_series_type = self.device_series_type

        type_ = self.type_

        stack = self.stack

        stack_id = self.stack_id

        support_ota_capture = self.support_ota_capture

        current_channel_2_g = self.current_channel_2_g

        channel_list_2_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_list_2_g, Unset):
            channel_list_2_g = []
            for channel_list_2_g_item_data in self.channel_list_2_g:
                channel_list_2_g_item = channel_list_2_g_item_data.to_dict()
                channel_list_2_g.append(channel_list_2_g_item)

        current_channel_5_g = self.current_channel_5_g

        channel_list_5_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_list_5_g, Unset):
            channel_list_5_g = []
            for channel_list_5_g_item_data in self.channel_list_5_g:
                channel_list_5_g_item = channel_list_5_g_item_data.to_dict()
                channel_list_5_g.append(channel_list_5_g_item)

        current_channel_5_g_2 = self.current_channel_5_g_2

        channel_list_5_g_2: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_list_5_g_2, Unset):
            channel_list_5_g_2 = []
            for channel_list_5_g_2_item_data in self.channel_list_5_g_2:
                channel_list_5_g_2_item = channel_list_5_g_2_item_data.to_dict()
                channel_list_5_g_2.append(channel_list_5_g_2_item)

        current_channel_6_g = self.current_channel_6_g

        channel_list_6_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_list_6_g, Unset):
            channel_list_6_g = []
            for channel_list_6_g_item_data in self.channel_list_6_g:
                channel_list_6_g_item = channel_list_6_g_item_data.to_dict()
                channel_list_6_g.append(channel_list_6_g_item)

        file_size = self.file_size

        support_stream_capture = self.support_stream_capture

        support_scan_radio = self.support_scan_radio

        scan_status = self.scan_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if ip is not UNSET:
            field_dict["ip"] = ip
        if support_capture is not UNSET:
            field_dict["supportCapture"] = support_capture
        if support2g is not UNSET:
            field_dict["support2g"] = support2g
        if support5g is not UNSET:
            field_dict["support5g"] = support5g
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if support6g is not UNSET:
            field_dict["support6g"] = support6g
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if support_lan_capture is not UNSET:
            field_dict["supportLanCapture"] = support_lan_capture
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if stack is not UNSET:
            field_dict["stack"] = stack
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if support_ota_capture is not UNSET:
            field_dict["supportOTACapture"] = support_ota_capture
        if current_channel_2_g is not UNSET:
            field_dict["currentChannel2g"] = current_channel_2_g
        if channel_list_2_g is not UNSET:
            field_dict["channelList2g"] = channel_list_2_g
        if current_channel_5_g is not UNSET:
            field_dict["currentChannel5g"] = current_channel_5_g
        if channel_list_5_g is not UNSET:
            field_dict["channelList5g"] = channel_list_5_g
        if current_channel_5_g_2 is not UNSET:
            field_dict["currentChannel5g2"] = current_channel_5_g_2
        if channel_list_5_g_2 is not UNSET:
            field_dict["channelList5g2"] = channel_list_5_g_2
        if current_channel_6_g is not UNSET:
            field_dict["currentChannel6g"] = current_channel_6_g
        if channel_list_6_g is not UNSET:
            field_dict["channelList6g"] = channel_list_6_g
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if support_stream_capture is not UNSET:
            field_dict["supportStreamCapture"] = support_stream_capture
        if support_scan_radio is not UNSET:
            field_dict["supportScanRadio"] = support_scan_radio
        if scan_status is not UNSET:
            field_dict["scanStatus"] = scan_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.channel_info import ChannelInfo
        from ..models.interface_info import InterfaceInfo

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        ip = d.pop("ip", UNSET)

        support_capture = d.pop("supportCapture", UNSET)

        support2g = d.pop("support2g", UNSET)

        support5g = d.pop("support5g", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        support6g = d.pop("support6g", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        support_lan_capture = d.pop("supportLanCapture", UNSET)

        _interfaces = d.pop("interfaces", UNSET)
        interfaces: list[InterfaceInfo] | Unset = UNSET
        if _interfaces is not UNSET:
            interfaces = []
            for interfaces_item_data in _interfaces:
                interfaces_item = InterfaceInfo.from_dict(interfaces_item_data)

                interfaces.append(interfaces_item)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        type_ = d.pop("type", UNSET)

        stack = d.pop("stack", UNSET)

        stack_id = d.pop("stackId", UNSET)

        support_ota_capture = d.pop("supportOTACapture", UNSET)

        current_channel_2_g = d.pop("currentChannel2g", UNSET)

        _channel_list_2_g = d.pop("channelList2g", UNSET)
        channel_list_2_g: list[ChannelInfo] | Unset = UNSET
        if _channel_list_2_g is not UNSET:
            channel_list_2_g = []
            for channel_list_2_g_item_data in _channel_list_2_g:
                channel_list_2_g_item = ChannelInfo.from_dict(
                    channel_list_2_g_item_data
                )

                channel_list_2_g.append(channel_list_2_g_item)

        current_channel_5_g = d.pop("currentChannel5g", UNSET)

        _channel_list_5_g = d.pop("channelList5g", UNSET)
        channel_list_5_g: list[ChannelInfo] | Unset = UNSET
        if _channel_list_5_g is not UNSET:
            channel_list_5_g = []
            for channel_list_5_g_item_data in _channel_list_5_g:
                channel_list_5_g_item = ChannelInfo.from_dict(
                    channel_list_5_g_item_data
                )

                channel_list_5_g.append(channel_list_5_g_item)

        current_channel_5_g_2 = d.pop("currentChannel5g2", UNSET)

        _channel_list_5_g_2 = d.pop("channelList5g2", UNSET)
        channel_list_5_g_2: list[ChannelInfo] | Unset = UNSET
        if _channel_list_5_g_2 is not UNSET:
            channel_list_5_g_2 = []
            for channel_list_5_g_2_item_data in _channel_list_5_g_2:
                channel_list_5_g_2_item = ChannelInfo.from_dict(
                    channel_list_5_g_2_item_data
                )

                channel_list_5_g_2.append(channel_list_5_g_2_item)

        current_channel_6_g = d.pop("currentChannel6g", UNSET)

        _channel_list_6_g = d.pop("channelList6g", UNSET)
        channel_list_6_g: list[ChannelInfo] | Unset = UNSET
        if _channel_list_6_g is not UNSET:
            channel_list_6_g = []
            for channel_list_6_g_item_data in _channel_list_6_g:
                channel_list_6_g_item = ChannelInfo.from_dict(
                    channel_list_6_g_item_data
                )

                channel_list_6_g.append(channel_list_6_g_item)

        file_size = d.pop("fileSize", UNSET)

        support_stream_capture = d.pop("supportStreamCapture", UNSET)

        support_scan_radio = d.pop("supportScanRadio", UNSET)

        scan_status = d.pop("scanStatus", UNSET)

        device_capture_info = cls(
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            show_model=show_model,
            ip=ip,
            support_capture=support_capture,
            support2g=support2g,
            support5g=support5g,
            support5g2=support5g2,
            support6g=support6g,
            firmware_version=firmware_version,
            support_lan_capture=support_lan_capture,
            interfaces=interfaces,
            device_series_type=device_series_type,
            type_=type_,
            stack=stack,
            stack_id=stack_id,
            support_ota_capture=support_ota_capture,
            current_channel_2_g=current_channel_2_g,
            channel_list_2_g=channel_list_2_g,
            current_channel_5_g=current_channel_5_g,
            channel_list_5_g=channel_list_5_g,
            current_channel_5_g_2=current_channel_5_g_2,
            channel_list_5_g_2=channel_list_5_g_2,
            current_channel_6_g=current_channel_6_g,
            channel_list_6_g=channel_list_6_g,
            file_size=file_size,
            support_stream_capture=support_stream_capture,
            support_scan_radio=support_scan_radio,
            scan_status=scan_status,
        )

        device_capture_info.additional_properties = d
        return device_capture_info

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
