from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vlan_network_affecting_es_detail_vo import (
        VlanNetworkAffectingEsDetailVO,
    )
    from ..models.vlan_network_affecting_internet_detail_vo import (
        VlanNetworkAffectingInternetDetailVO,
    )
    from ..models.vlan_network_affecting_osg_detail_vo import (
        VlanNetworkAffectingOsgDetailVO,
    )
    from ..models.vlan_network_affecting_stack_detail_vo import (
        VlanNetworkAffectingStackDetailVO,
    )
    from ..models.vlan_network_affecting_switch_detail_vo import (
        VlanNetworkAffectingSwitchDetailVO,
    )


T = TypeVar("T", bound="VlanNetworkAffectingDeviceDetailVO")


@_attrs_define
class VlanNetworkAffectingDeviceDetailVO:
    """
    Attributes:
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        mac (str | Unset): Device mac
        name (str | Unset): Device name,default value is the mac address of device
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        es (bool | Unset): It indicates whether the device is easy managed switch.
        stack_id (str | Unset): Only valid when the device is stack.
        gateway_info (VlanNetworkAffectingOsgDetailVO | Unset): Gateway Info, only valid when type is gateway.
        internet_info (VlanNetworkAffectingInternetDetailVO | Unset): Internet Info, only valid when enable WAN Settings
            Overrides.
        switch_info (VlanNetworkAffectingSwitchDetailVO | Unset): Switch Info, only valid when type is switch and es is
            false and stackId is empty.
        es_info (VlanNetworkAffectingEsDetailVO | Unset): Agile Series Switch detail info, only valid when type is
            switch and es is true.
        stack_info (VlanNetworkAffectingStackDetailVO | Unset): Stack info, only valid when type is switch and stackId
            is not empty.
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    status_category: int | Unset = UNSET
    es: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    gateway_info: VlanNetworkAffectingOsgDetailVO | Unset = UNSET
    internet_info: VlanNetworkAffectingInternetDetailVO | Unset = UNSET
    switch_info: VlanNetworkAffectingSwitchDetailVO | Unset = UNSET
    es_info: VlanNetworkAffectingEsDetailVO | Unset = UNSET
    stack_info: VlanNetworkAffectingStackDetailVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        status_category = self.status_category

        es = self.es

        stack_id = self.stack_id

        gateway_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_info, Unset):
            gateway_info = self.gateway_info.to_dict()

        internet_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internet_info, Unset):
            internet_info = self.internet_info.to_dict()

        switch_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_info, Unset):
            switch_info = self.switch_info.to_dict()

        es_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.es_info, Unset):
            es_info = self.es_info.to_dict()

        stack_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stack_info, Unset):
            stack_info = self.stack_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if es is not UNSET:
            field_dict["es"] = es
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if gateway_info is not UNSET:
            field_dict["gatewayInfo"] = gateway_info
        if internet_info is not UNSET:
            field_dict["internetInfo"] = internet_info
        if switch_info is not UNSET:
            field_dict["switchInfo"] = switch_info
        if es_info is not UNSET:
            field_dict["esInfo"] = es_info
        if stack_info is not UNSET:
            field_dict["stackInfo"] = stack_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vlan_network_affecting_es_detail_vo import (
            VlanNetworkAffectingEsDetailVO,
        )
        from ..models.vlan_network_affecting_internet_detail_vo import (
            VlanNetworkAffectingInternetDetailVO,
        )
        from ..models.vlan_network_affecting_osg_detail_vo import (
            VlanNetworkAffectingOsgDetailVO,
        )
        from ..models.vlan_network_affecting_stack_detail_vo import (
            VlanNetworkAffectingStackDetailVO,
        )
        from ..models.vlan_network_affecting_switch_detail_vo import (
            VlanNetworkAffectingSwitchDetailVO,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        es = d.pop("es", UNSET)

        stack_id = d.pop("stackId", UNSET)

        _gateway_info = d.pop("gatewayInfo", UNSET)
        gateway_info: VlanNetworkAffectingOsgDetailVO | Unset
        if isinstance(_gateway_info, Unset):
            gateway_info = UNSET
        else:
            gateway_info = VlanNetworkAffectingOsgDetailVO.from_dict(_gateway_info)

        _internet_info = d.pop("internetInfo", UNSET)
        internet_info: VlanNetworkAffectingInternetDetailVO | Unset
        if isinstance(_internet_info, Unset):
            internet_info = UNSET
        else:
            internet_info = VlanNetworkAffectingInternetDetailVO.from_dict(
                _internet_info
            )

        _switch_info = d.pop("switchInfo", UNSET)
        switch_info: VlanNetworkAffectingSwitchDetailVO | Unset
        if isinstance(_switch_info, Unset):
            switch_info = UNSET
        else:
            switch_info = VlanNetworkAffectingSwitchDetailVO.from_dict(_switch_info)

        _es_info = d.pop("esInfo", UNSET)
        es_info: VlanNetworkAffectingEsDetailVO | Unset
        if isinstance(_es_info, Unset):
            es_info = UNSET
        else:
            es_info = VlanNetworkAffectingEsDetailVO.from_dict(_es_info)

        _stack_info = d.pop("stackInfo", UNSET)
        stack_info: VlanNetworkAffectingStackDetailVO | Unset
        if isinstance(_stack_info, Unset):
            stack_info = UNSET
        else:
            stack_info = VlanNetworkAffectingStackDetailVO.from_dict(_stack_info)

        vlan_network_affecting_device_detail_vo = cls(
            type_=type_,
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            status_category=status_category,
            es=es,
            stack_id=stack_id,
            gateway_info=gateway_info,
            internet_info=internet_info,
            switch_info=switch_info,
            es_info=es_info,
            stack_info=stack_info,
        )

        vlan_network_affecting_device_detail_vo.additional_properties = d
        return vlan_network_affecting_device_detail_vo

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
