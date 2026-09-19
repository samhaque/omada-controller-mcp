from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_count_vo_causes import AnomalyBriefCountVOCauses
    from ..models.anomaly_brief_count_vo_clients import AnomalyBriefCountVOClients
    from ..models.anomaly_brief_count_vo_content_params import (
        AnomalyBriefCountVOContentParams,
    )
    from ..models.anomaly_brief_count_vo_devices import AnomalyBriefCountVODevices
    from ..models.anomaly_brief_count_vo_title_params import (
        AnomalyBriefCountVOTitleParams,
    )


T = TypeVar("T", bound="AnomalyBriefCountVO")


@_attrs_define
class AnomalyBriefCountVO:
    """Anomaly brief information with count for device/client health view

    Attributes:
        anomaly_code (str | Unset): For the values of Anomaly event code, refer to section 5.7.2.1 of the Open API
            Access Example: 01001001.
        category (int | Unset): Anomaly category. 11: Network, 12: Device, 13: Client, etc.
        incident_id (str | Unset): Incident ID
        level (int | Unset): Anomaly severity level
        last_time (int | Unset): Last occurrence timestamp (ms)
        count (int | Unset): Total occurrence count
        object_ (list[str] | Unset): List of affected device MAC addresses
        macs (list[str] | Unset): List of affected device MAC addresses
        title_params (AnomalyBriefCountVOTitleParams | Unset): Title parameters for anomaly message
        content_params (AnomalyBriefCountVOContentParams | Unset): Content parameters for anomaly message
        devices (AnomalyBriefCountVODevices | Unset): Device objects map, key is MAC address
        clients (AnomalyBriefCountVOClients | Unset): Client objects map, key is MAC address
        causes (AnomalyBriefCountVOCauses | Unset): Root cause information map
        influencing_devices (list[str] | Unset): List of influenced device MAC addresses
        influencing_clients (list[str] | Unset): List of influenced client MAC addresses
        status (int | Unset): Anomaly incident status (0=unresolved, 1=resolved, 2=ignored, 3=ongoing)
    """

    anomaly_code: str | Unset = UNSET
    category: int | Unset = UNSET
    incident_id: str | Unset = UNSET
    level: int | Unset = UNSET
    last_time: int | Unset = UNSET
    count: int | Unset = UNSET
    object_: list[str] | Unset = UNSET
    macs: list[str] | Unset = UNSET
    title_params: AnomalyBriefCountVOTitleParams | Unset = UNSET
    content_params: AnomalyBriefCountVOContentParams | Unset = UNSET
    devices: AnomalyBriefCountVODevices | Unset = UNSET
    clients: AnomalyBriefCountVOClients | Unset = UNSET
    causes: AnomalyBriefCountVOCauses | Unset = UNSET
    influencing_devices: list[str] | Unset = UNSET
    influencing_clients: list[str] | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly_code = self.anomaly_code

        category = self.category

        incident_id = self.incident_id

        level = self.level

        last_time = self.last_time

        count = self.count

        object_: list[str] | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        title_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_params, Unset):
            title_params = self.title_params.to_dict()

        content_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_params, Unset):
            content_params = self.content_params.to_dict()

        devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        clients: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = self.clients.to_dict()

        causes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.causes, Unset):
            causes = self.causes.to_dict()

        influencing_devices: list[str] | Unset = UNSET
        if not isinstance(self.influencing_devices, Unset):
            influencing_devices = self.influencing_devices

        influencing_clients: list[str] | Unset = UNSET
        if not isinstance(self.influencing_clients, Unset):
            influencing_clients = self.influencing_clients

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly_code is not UNSET:
            field_dict["anomalyCode"] = anomaly_code
        if category is not UNSET:
            field_dict["category"] = category
        if incident_id is not UNSET:
            field_dict["incidentId"] = incident_id
        if level is not UNSET:
            field_dict["level"] = level
        if last_time is not UNSET:
            field_dict["lastTime"] = last_time
        if count is not UNSET:
            field_dict["count"] = count
        if object_ is not UNSET:
            field_dict["object"] = object_
        if macs is not UNSET:
            field_dict["macs"] = macs
        if title_params is not UNSET:
            field_dict["titleParams"] = title_params
        if content_params is not UNSET:
            field_dict["contentParams"] = content_params
        if devices is not UNSET:
            field_dict["devices"] = devices
        if clients is not UNSET:
            field_dict["clients"] = clients
        if causes is not UNSET:
            field_dict["causes"] = causes
        if influencing_devices is not UNSET:
            field_dict["influencingDevices"] = influencing_devices
        if influencing_clients is not UNSET:
            field_dict["influencingClients"] = influencing_clients
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_count_vo_causes import (
            AnomalyBriefCountVOCauses,
        )
        from ..models.anomaly_brief_count_vo_clients import (
            AnomalyBriefCountVOClients,
        )
        from ..models.anomaly_brief_count_vo_content_params import (
            AnomalyBriefCountVOContentParams,
        )
        from ..models.anomaly_brief_count_vo_devices import (
            AnomalyBriefCountVODevices,
        )
        from ..models.anomaly_brief_count_vo_title_params import (
            AnomalyBriefCountVOTitleParams,
        )

        d = dict(src_dict)
        anomaly_code = d.pop("anomalyCode", UNSET)

        category = d.pop("category", UNSET)

        incident_id = d.pop("incidentId", UNSET)

        level = d.pop("level", UNSET)

        last_time = d.pop("lastTime", UNSET)

        count = d.pop("count", UNSET)

        object_ = cast(list[str], d.pop("object", UNSET))

        macs = cast(list[str], d.pop("macs", UNSET))

        _title_params = d.pop("titleParams", UNSET)
        title_params: AnomalyBriefCountVOTitleParams | Unset
        if isinstance(_title_params, Unset):
            title_params = UNSET
        else:
            title_params = AnomalyBriefCountVOTitleParams.from_dict(_title_params)

        _content_params = d.pop("contentParams", UNSET)
        content_params: AnomalyBriefCountVOContentParams | Unset
        if isinstance(_content_params, Unset):
            content_params = UNSET
        else:
            content_params = AnomalyBriefCountVOContentParams.from_dict(_content_params)

        _devices = d.pop("devices", UNSET)
        devices: AnomalyBriefCountVODevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = AnomalyBriefCountVODevices.from_dict(_devices)

        _clients = d.pop("clients", UNSET)
        clients: AnomalyBriefCountVOClients | Unset
        if isinstance(_clients, Unset):
            clients = UNSET
        else:
            clients = AnomalyBriefCountVOClients.from_dict(_clients)

        _causes = d.pop("causes", UNSET)
        causes: AnomalyBriefCountVOCauses | Unset
        if isinstance(_causes, Unset):
            causes = UNSET
        else:
            causes = AnomalyBriefCountVOCauses.from_dict(_causes)

        influencing_devices = cast(list[str], d.pop("influencingDevices", UNSET))

        influencing_clients = cast(list[str], d.pop("influencingClients", UNSET))

        status = d.pop("status", UNSET)

        anomaly_brief_count_vo = cls(
            anomaly_code=anomaly_code,
            category=category,
            incident_id=incident_id,
            level=level,
            last_time=last_time,
            count=count,
            object_=object_,
            macs=macs,
            title_params=title_params,
            content_params=content_params,
            devices=devices,
            clients=clients,
            causes=causes,
            influencing_devices=influencing_devices,
            influencing_clients=influencing_clients,
            status=status,
        )

        anomaly_brief_count_vo.additional_properties = d
        return anomaly_brief_count_vo

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
