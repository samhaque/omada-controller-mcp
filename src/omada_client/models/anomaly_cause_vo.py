from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_cause_vo_advices import AnomalyCauseVOAdvices
    from ..models.anomaly_cause_vo_clients import AnomalyCauseVOClients
    from ..models.anomaly_cause_vo_content_params import AnomalyCauseVOContentParams
    from ..models.anomaly_cause_vo_detail import AnomalyCauseVODetail
    from ..models.anomaly_cause_vo_devices import AnomalyCauseVODevices
    from ..models.anomaly_cause_vo_title_params import AnomalyCauseVOTitleParams


T = TypeVar("T", bound="AnomalyCauseVO")


@_attrs_define
class AnomalyCauseVO:
    """Root cause information map

    Attributes:
        title_params (AnomalyCauseVOTitleParams | Unset):
        content_params (AnomalyCauseVOContentParams | Unset):
        detail (AnomalyCauseVODetail | Unset):
        devices (AnomalyCauseVODevices | Unset):
        clients (AnomalyCauseVOClients | Unset):
        advices (AnomalyCauseVOAdvices | Unset):
    """

    title_params: AnomalyCauseVOTitleParams | Unset = UNSET
    content_params: AnomalyCauseVOContentParams | Unset = UNSET
    detail: AnomalyCauseVODetail | Unset = UNSET
    devices: AnomalyCauseVODevices | Unset = UNSET
    clients: AnomalyCauseVOClients | Unset = UNSET
    advices: AnomalyCauseVOAdvices | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        advices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advices, Unset):
            advices = self.advices.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if advices is not UNSET:
            field_dict["advices"] = advices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_cause_vo_advices import (
            AnomalyCauseVOAdvices,
        )
        from ..models.anomaly_cause_vo_clients import (
            AnomalyCauseVOClients,
        )
        from ..models.anomaly_cause_vo_content_params import (
            AnomalyCauseVOContentParams,
        )
        from ..models.anomaly_cause_vo_detail import (
            AnomalyCauseVODetail,
        )
        from ..models.anomaly_cause_vo_devices import (
            AnomalyCauseVODevices,
        )
        from ..models.anomaly_cause_vo_title_params import (
            AnomalyCauseVOTitleParams,
        )

        d = dict(src_dict)
        _title_params = d.pop("titleParams", UNSET)
        title_params: AnomalyCauseVOTitleParams | Unset
        if isinstance(_title_params, Unset):
            title_params = UNSET
        else:
            title_params = AnomalyCauseVOTitleParams.from_dict(_title_params)

        _content_params = d.pop("contentParams", UNSET)
        content_params: AnomalyCauseVOContentParams | Unset
        if isinstance(_content_params, Unset):
            content_params = UNSET
        else:
            content_params = AnomalyCauseVOContentParams.from_dict(_content_params)

        _detail = d.pop("detail", UNSET)
        detail: AnomalyCauseVODetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = AnomalyCauseVODetail.from_dict(_detail)

        _devices = d.pop("devices", UNSET)
        devices: AnomalyCauseVODevices | Unset
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = AnomalyCauseVODevices.from_dict(_devices)

        _clients = d.pop("clients", UNSET)
        clients: AnomalyCauseVOClients | Unset
        if isinstance(_clients, Unset):
            clients = UNSET
        else:
            clients = AnomalyCauseVOClients.from_dict(_clients)

        _advices = d.pop("advices", UNSET)
        advices: AnomalyCauseVOAdvices | Unset
        if isinstance(_advices, Unset):
            advices = UNSET
        else:
            advices = AnomalyCauseVOAdvices.from_dict(_advices)

        anomaly_cause_vo = cls(
            title_params=title_params,
            content_params=content_params,
            detail=detail,
            devices=devices,
            clients=clients,
            advices=advices,
        )

        anomaly_cause_vo.additional_properties = d
        return anomaly_cause_vo

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
