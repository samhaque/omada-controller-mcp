from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_stat_open_api_vo import HealthStatOpenApiVO


T = TypeVar("T", bound="GlobalDeviceStatOpenApiVO")


@_attrs_define
class GlobalDeviceStatOpenApiVO:
    """
    Attributes:
        switch_health (HealthStatOpenApiVO | Unset): the health stat of gateway
        eap_health (HealthStatOpenApiVO | Unset): the health stat of gateway
        all_devices (int | Unset): the number of all devices
        all_switchs_and_gateway (int | Unset): the number of switchs and gateway
        all_aps (int | Unset): eap health stat
        all_olts (int | Unset): eap health stat
        mesh (int | Unset): device mesh
        config (int | Unset): device config
        performance (int | Unset): device performance
        un_activated (int | Unset): device unActivated
        activated (int | Unset): device activated
        expired (int | Unset): device expired
        good (int | Unset): device health stat is good
        fair (int | Unset): device health stat is fair
        poor (int | Unset): device health stat is poor
        no_data (int | Unset): no health stat data
        gateway_health (HealthStatOpenApiVO | Unset): the health stat of gateway
    """

    switch_health: HealthStatOpenApiVO | Unset = UNSET
    eap_health: HealthStatOpenApiVO | Unset = UNSET
    all_devices: int | Unset = UNSET
    all_switchs_and_gateway: int | Unset = UNSET
    all_aps: int | Unset = UNSET
    all_olts: int | Unset = UNSET
    mesh: int | Unset = UNSET
    config: int | Unset = UNSET
    performance: int | Unset = UNSET
    un_activated: int | Unset = UNSET
    activated: int | Unset = UNSET
    expired: int | Unset = UNSET
    good: int | Unset = UNSET
    fair: int | Unset = UNSET
    poor: int | Unset = UNSET
    no_data: int | Unset = UNSET
    gateway_health: HealthStatOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        switch_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_health, Unset):
            switch_health = self.switch_health.to_dict()

        eap_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eap_health, Unset):
            eap_health = self.eap_health.to_dict()

        all_devices = self.all_devices

        all_switchs_and_gateway = self.all_switchs_and_gateway

        all_aps = self.all_aps

        all_olts = self.all_olts

        mesh = self.mesh

        config = self.config

        performance = self.performance

        un_activated = self.un_activated

        activated = self.activated

        expired = self.expired

        good = self.good

        fair = self.fair

        poor = self.poor

        no_data = self.no_data

        gateway_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_health, Unset):
            gateway_health = self.gateway_health.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if switch_health is not UNSET:
            field_dict["switchHealth"] = switch_health
        if eap_health is not UNSET:
            field_dict["eapHealth"] = eap_health
        if all_devices is not UNSET:
            field_dict["allDevices"] = all_devices
        if all_switchs_and_gateway is not UNSET:
            field_dict["allSwitchsAndGateway"] = all_switchs_and_gateway
        if all_aps is not UNSET:
            field_dict["allAps"] = all_aps
        if all_olts is not UNSET:
            field_dict["allOlts"] = all_olts
        if mesh is not UNSET:
            field_dict["mesh"] = mesh
        if config is not UNSET:
            field_dict["config"] = config
        if performance is not UNSET:
            field_dict["performance"] = performance
        if un_activated is not UNSET:
            field_dict["unActivated"] = un_activated
        if activated is not UNSET:
            field_dict["activated"] = activated
        if expired is not UNSET:
            field_dict["expired"] = expired
        if good is not UNSET:
            field_dict["good"] = good
        if fair is not UNSET:
            field_dict["fair"] = fair
        if poor is not UNSET:
            field_dict["poor"] = poor
        if no_data is not UNSET:
            field_dict["noData"] = no_data
        if gateway_health is not UNSET:
            field_dict["gatewayHealth"] = gateway_health

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.health_stat_open_api_vo import (
            HealthStatOpenApiVO,
        )

        d = dict(src_dict)
        _switch_health = d.pop("switchHealth", UNSET)
        switch_health: HealthStatOpenApiVO | Unset
        if isinstance(_switch_health, Unset):
            switch_health = UNSET
        else:
            switch_health = HealthStatOpenApiVO.from_dict(_switch_health)

        _eap_health = d.pop("eapHealth", UNSET)
        eap_health: HealthStatOpenApiVO | Unset
        if isinstance(_eap_health, Unset):
            eap_health = UNSET
        else:
            eap_health = HealthStatOpenApiVO.from_dict(_eap_health)

        all_devices = d.pop("allDevices", UNSET)

        all_switchs_and_gateway = d.pop("allSwitchsAndGateway", UNSET)

        all_aps = d.pop("allAps", UNSET)

        all_olts = d.pop("allOlts", UNSET)

        mesh = d.pop("mesh", UNSET)

        config = d.pop("config", UNSET)

        performance = d.pop("performance", UNSET)

        un_activated = d.pop("unActivated", UNSET)

        activated = d.pop("activated", UNSET)

        expired = d.pop("expired", UNSET)

        good = d.pop("good", UNSET)

        fair = d.pop("fair", UNSET)

        poor = d.pop("poor", UNSET)

        no_data = d.pop("noData", UNSET)

        _gateway_health = d.pop("gatewayHealth", UNSET)
        gateway_health: HealthStatOpenApiVO | Unset
        if isinstance(_gateway_health, Unset):
            gateway_health = UNSET
        else:
            gateway_health = HealthStatOpenApiVO.from_dict(_gateway_health)

        global_device_stat_open_api_vo = cls(
            switch_health=switch_health,
            eap_health=eap_health,
            all_devices=all_devices,
            all_switchs_and_gateway=all_switchs_and_gateway,
            all_aps=all_aps,
            all_olts=all_olts,
            mesh=mesh,
            config=config,
            performance=performance,
            un_activated=un_activated,
            activated=activated,
            expired=expired,
            good=good,
            fair=fair,
            poor=poor,
            no_data=no_data,
            gateway_health=gateway_health,
        )

        global_device_stat_open_api_vo.additional_properties = d
        return global_device_stat_open_api_vo

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
