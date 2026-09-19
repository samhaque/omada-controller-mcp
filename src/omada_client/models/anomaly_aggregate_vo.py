from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_aggregate_vo_clients import AnomalyAggregateVOClients
    from ..models.anomaly_aggregate_vo_content_params import (
        AnomalyAggregateVOContentParams,
    )
    from ..models.anomaly_aggregate_vo_devices import AnomalyAggregateVODevices
    from ..models.anomaly_aggregate_vo_title_params import AnomalyAggregateVOTitleParams
    from ..models.cause_vo import CauseVO


T = TypeVar("T", bound="AnomalyAggregateVO")


@_attrs_define
class AnomalyAggregateVO:
    """
    Attributes:
        anomaly_code (str | Unset): For the values of Anomaly event code, refer to section 5.7.2.1 of the Open API
            Access Example: 01001001.
        category (int | Unset): Anomaly category. 11: Network, 12: Device, 13: Client, etc.
        level (int | Unset): Event severity level. 0: Critical, 1: Error, 2: Warning, 3: Info.
        title_params (AnomalyAggregateVOTitleParams | Unset): Title parameter map for rendering the event title
            template.
        content_params (AnomalyAggregateVOContentParams | Unset): Content parameter map for rendering the event content
            template.
        object_type (str | Unset): Object type of the anomaly target: gateway, switch, ap, wiredClient, wirelessClient.
        object_ (list[str] | Unset): List of device/client names where the anomaly occurred.
        count (int | Unset): Number of occurrences of this anomaly.
        last_time (int | Unset): Last occurrence time in milliseconds (Unix timestamp).
        first_time (int | Unset): First occurrence time in milliseconds (Unix timestamp).
        status (int | Unset): Event status. 0: Unresolved, 1: Resolved, 2: Ignored.
        devices (AnomalyAggregateVODevices | Unset): Device objects map. Key is MAC address, value is device info.
        clients (AnomalyAggregateVOClients | Unset): Client objects map. Key is MAC address, value is client info.
        influencing_devices (list[str] | Unset): List of MAC addresses of influencing/impacted devices.
        influencing_clients (list[str] | Unset): List of MAC addresses of influencing/impacted clients.
        causes (list[CauseVO] | Unset): Root causes and advices for this anomaly.
    """

    anomaly_code: str | Unset = UNSET
    category: int | Unset = UNSET
    level: int | Unset = UNSET
    title_params: AnomalyAggregateVOTitleParams | Unset = UNSET
    content_params: AnomalyAggregateVOContentParams | Unset = UNSET
    object_type: str | Unset = UNSET
    object_: list[str] | Unset = UNSET
    count: int | Unset = UNSET
    last_time: int | Unset = UNSET
    first_time: int | Unset = UNSET
    status: int | Unset = UNSET
    devices: AnomalyAggregateVODevices | Unset = UNSET
    clients: AnomalyAggregateVOClients | Unset = UNSET
    influencing_devices: list[str] | Unset = UNSET
    influencing_clients: list[str] | Unset = UNSET
    causes: list[CauseVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly_code = self.anomaly_code

        category = self.category

        level = self.level

        title_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_params, Unset):
            title_params = self.title_params.to_dict()

        content_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_params, Unset):
            content_params = self.content_params.to_dict()

        object_type = self.object_type

        object_: list[str] | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_

        count = self.count

        last_time = self.last_time

        first_time = self.first_time

        status = self.status

        devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        clients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = self.clients.to_dict()

        influencing_devices: list[str] | Unset = UNSET
        if not isinstance(self.influencing_devices, Unset):
            influencing_devices = self.influencing_devices

        influencing_clients: list[str] | Unset = UNSET
        if not isinstance(self.influencing_clients, Unset):
            influencing_clients = self.influencing_clients

        causes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.causes, Unset):
            causes = []
            for causes_item_data in self.causes:
                causes_item = causes_item_data.to_dict()
                causes.append(causes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly_code is not UNSET:
            field_dict["anomalyCode"] = anomaly_code
        if category is not UNSET:
            field_dict["category"] = category
        if level is not UNSET:
            field_dict["level"] = level
        if title_params is not UNSET:
            field_dict["titleParams"] = title_params
        if content_params is not UNSET:
            field_dict["contentParams"] = content_params
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if object_ is not UNSET:
            field_dict["object"] = object_
        if count is not UNSET:
            field_dict["count"] = count
        if last_time is not UNSET:
            field_dict["lastTime"] = last_time
        if first_time is not UNSET:
            field_dict["firstTime"] = first_time
        if status is not UNSET:
            field_dict["status"] = status
        if devices is not UNSET:
            field_dict["devices"] = devices
        if clients is not UNSET:
            field_dict["clients"] = clients
        if influencing_devices is not UNSET:
            field_dict["influencingDevices"] = influencing_devices
        if influencing_clients is not UNSET:
            field_dict["influencingClients"] = influencing_clients
        if causes is not UNSET:
            field_dict["causes"] = causes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_aggregate_vo_clients import (
            AnomalyAggregateVOClients,
        )
        from ..models.anomaly_aggregate_vo_content_params import (
            AnomalyAggregateVOContentParams,
        )
        from ..models.anomaly_aggregate_vo_devices import (
            AnomalyAggregateVODevices,
        )
        from ..models.anomaly_aggregate_vo_title_params import (
            AnomalyAggregateVOTitleParams,
        )
        from ..models.cause_vo import CauseVO

        d = dict(src_dict)
        anomaly_code = d.pop("anomalyCode", UNSET)

        category = d.pop("category", UNSET)

        level = d.pop("level", UNSET)

        _title_params = d.pop("titleParams", UNSET)
        title_params: AnomalyAggregateVOTitleParams | Unset
        if isinstance(_title_params, Unset):
            title_params = UNSET
        else:
            title_params = AnomalyAggregateVOTitleParams.from_dict(_title_params)

        _content_params = d.pop("contentParams", UNSET)
        content_params: AnomalyAggregateVOContentParams | Unset
        if isinstance(_content_params, Unset):
            content_params = UNSET
        else:
            content_params = AnomalyAggregateVOContentParams.from_dict(_content_params)

        object_type = d.pop("objectType", UNSET)

        object_ = cast(list[str], d.pop("object", UNSET))

        count = d.pop("count", UNSET)

        last_time = d.pop("lastTime", UNSET)

        first_time = d.pop("firstTime", UNSET)

        status = d.pop("status", UNSET)

        _devices = d.pop("devices", UNSET)
        devices: AnomalyAggregateVODevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = AnomalyAggregateVODevices.from_dict(_devices)

        _clients = d.pop("clients", UNSET)
        clients: AnomalyAggregateVOClients | Unset
        if isinstance(_clients, Unset):
            clients = UNSET
        else:
            clients = AnomalyAggregateVOClients.from_dict(_clients)

        influencing_devices = cast(list[str], d.pop("influencingDevices", UNSET))

        influencing_clients = cast(list[str], d.pop("influencingClients", UNSET))

        _causes = d.pop("causes", UNSET)
        causes: list[CauseVO] | Unset = UNSET
        if _causes is not UNSET:
            causes = []
            for causes_item_data in _causes:
                causes_item = CauseVO.from_dict(causes_item_data)

                causes.append(causes_item)

        anomaly_aggregate_vo = cls(
            anomaly_code=anomaly_code,
            category=category,
            level=level,
            title_params=title_params,
            content_params=content_params,
            object_type=object_type,
            object_=object_,
            count=count,
            last_time=last_time,
            first_time=first_time,
            status=status,
            devices=devices,
            clients=clients,
            influencing_devices=influencing_devices,
            influencing_clients=influencing_clients,
            causes=causes,
        )

        anomaly_aggregate_vo.additional_properties = d
        return anomaly_aggregate_vo

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
