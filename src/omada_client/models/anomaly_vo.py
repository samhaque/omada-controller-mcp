from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_vo_causes import AnomalyVOCauses
    from ..models.anomaly_vo_clients import AnomalyVOClients
    from ..models.anomaly_vo_content_params import AnomalyVOContentParams
    from ..models.anomaly_vo_detail import AnomalyVODetail
    from ..models.anomaly_vo_devices import AnomalyVODevices
    from ..models.anomaly_vo_title_params import AnomalyVOTitleParams


T = TypeVar("T", bound="AnomalyVO")


@_attrs_define
class AnomalyVO:
    """
    Attributes:
        incident_id (str | Unset):
        anomaly_code (str | Unset): For the values of Anomaly event code, refer to section 5.7.2.1 of the Open API
            Access Example: 01001001.
        category (int | Unset): Anomaly category. 11: Network, 12: Device, 13: Client, etc.
        level (int | Unset): Event severity level. 0: Critical, 1: Error, 2: Warning, 3: Info.
        object_type (str | Unset): Object type of the anomaly target: gateway, switch, ap, wiredClient, wirelessClient.
        object_ (list[str] | Unset): List of device/client names where the anomaly occurred.
        status (int | Unset): Event status. 0: Unresolved, 1: Resolved, 2: Ignored.
        time (int | Unset): Event creation time in milliseconds (Unix timestamp).
        start_time (int | Unset): Continuous event start time in milliseconds (Unix timestamp).
        end_time (int | Unset): Continuous event end time in milliseconds (Unix timestamp).
        title_params (AnomalyVOTitleParams | Unset): Title parameter map for rendering the event title template.
        content_params (AnomalyVOContentParams | Unset): Content parameter map for rendering the event content template.
        detail (AnomalyVODetail | Unset): Detailed chart data for the event content display (line chart, timeline, list,
            bar chart, protocol replay, port POE, etc.).
        devices (AnomalyVODevices | Unset): Device objects map. Key is MAC address, value is device info.
        clients (AnomalyVOClients | Unset): Client objects map. Key is MAC address, value is client info.
        impacted_devices (list[str] | Unset): Set of MAC addresses of all devices impacted by this incident.
        impacted_clients (list[str] | Unset): Set of MAC addresses of all clients impacted by this incident.
        causes (AnomalyVOCauses | Unset): Root causes map. Key is cause code, value is cause detail.
    """

    incident_id: str | Unset = UNSET
    anomaly_code: str | Unset = UNSET
    category: int | Unset = UNSET
    level: int | Unset = UNSET
    object_type: str | Unset = UNSET
    object_: list[str] | Unset = UNSET
    status: int | Unset = UNSET
    time: int | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    title_params: AnomalyVOTitleParams | Unset = UNSET
    content_params: AnomalyVOContentParams | Unset = UNSET
    detail: AnomalyVODetail | Unset = UNSET
    devices: AnomalyVODevices | Unset = UNSET
    clients: AnomalyVOClients | Unset = UNSET
    impacted_devices: list[str] | Unset = UNSET
    impacted_clients: list[str] | Unset = UNSET
    causes: AnomalyVOCauses | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        anomaly_code = self.anomaly_code

        category = self.category

        level = self.level

        object_type = self.object_type

        object_: list[str] | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_

        status = self.status

        time = self.time

        start_time = self.start_time

        end_time = self.end_time

        title_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_params, Unset):
            title_params = self.title_params.to_dict()

        content_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_params, Unset):
            content_params = self.content_params.to_dict()

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        clients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = self.clients.to_dict()

        impacted_devices: list[str] | Unset = UNSET
        if not isinstance(self.impacted_devices, Unset):
            impacted_devices = self.impacted_devices

        impacted_clients: list[str] | Unset = UNSET
        if not isinstance(self.impacted_clients, Unset):
            impacted_clients = self.impacted_clients

        causes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.causes, Unset):
            causes = self.causes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incident_id is not UNSET:
            field_dict["incidentId"] = incident_id
        if anomaly_code is not UNSET:
            field_dict["anomalyCode"] = anomaly_code
        if category is not UNSET:
            field_dict["category"] = category
        if level is not UNSET:
            field_dict["level"] = level
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if object_ is not UNSET:
            field_dict["object"] = object_
        if status is not UNSET:
            field_dict["status"] = status
        if time is not UNSET:
            field_dict["time"] = time
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if title_params is not UNSET:
            field_dict["titleParams"] = title_params
        if content_params is not UNSET:
            field_dict["contentParams"] = content_params
        if detail is not UNSET:
            field_dict["detail"] = detail
        if devices is not UNSET:
            field_dict["devices"] = devices
        if clients is not UNSET:
            field_dict["clients"] = clients
        if impacted_devices is not UNSET:
            field_dict["impactedDevices"] = impacted_devices
        if impacted_clients is not UNSET:
            field_dict["impactedClients"] = impacted_clients
        if causes is not UNSET:
            field_dict["causes"] = causes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_vo_causes import AnomalyVOCauses
        from ..models.anomaly_vo_clients import AnomalyVOClients
        from ..models.anomaly_vo_content_params import (
            AnomalyVOContentParams,
        )
        from ..models.anomaly_vo_detail import AnomalyVODetail
        from ..models.anomaly_vo_devices import AnomalyVODevices
        from ..models.anomaly_vo_title_params import (
            AnomalyVOTitleParams,
        )

        d = dict(src_dict)
        incident_id = d.pop("incidentId", UNSET)

        anomaly_code = d.pop("anomalyCode", UNSET)

        category = d.pop("category", UNSET)

        level = d.pop("level", UNSET)

        object_type = d.pop("objectType", UNSET)

        object_ = cast(list[str], d.pop("object", UNSET))

        status = d.pop("status", UNSET)

        time = d.pop("time", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        _title_params = d.pop("titleParams", UNSET)
        title_params: AnomalyVOTitleParams | Unset
        if isinstance(_title_params, Unset):
            title_params = UNSET
        else:
            title_params = AnomalyVOTitleParams.from_dict(_title_params)

        _content_params = d.pop("contentParams", UNSET)
        content_params: AnomalyVOContentParams | Unset
        if isinstance(_content_params, Unset):
            content_params = UNSET
        else:
            content_params = AnomalyVOContentParams.from_dict(_content_params)

        _detail = d.pop("detail", UNSET)
        detail: AnomalyVODetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = AnomalyVODetail.from_dict(_detail)

        _devices = d.pop("devices", UNSET)
        devices: AnomalyVODevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = AnomalyVODevices.from_dict(_devices)

        _clients = d.pop("clients", UNSET)
        clients: AnomalyVOClients | Unset
        if isinstance(_clients, Unset):
            clients = UNSET
        else:
            clients = AnomalyVOClients.from_dict(_clients)

        impacted_devices = cast(list[str], d.pop("impactedDevices", UNSET))

        impacted_clients = cast(list[str], d.pop("impactedClients", UNSET))

        _causes = d.pop("causes", UNSET)
        causes: AnomalyVOCauses | Unset
        if isinstance(_causes, Unset):
            causes = UNSET
        else:
            causes = AnomalyVOCauses.from_dict(_causes)

        anomaly_vo = cls(
            incident_id=incident_id,
            anomaly_code=anomaly_code,
            category=category,
            level=level,
            object_type=object_type,
            object_=object_,
            status=status,
            time=time,
            start_time=start_time,
            end_time=end_time,
            title_params=title_params,
            content_params=content_params,
            detail=detail,
            devices=devices,
            clients=clients,
            impacted_devices=impacted_devices,
            impacted_clients=impacted_clients,
            causes=causes,
        )

        anomaly_vo.additional_properties = d
        return anomaly_vo

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
