from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_info import APInfo
    from ..models.gateway_info import GatewayInfo
    from ..models.switch_info import SwitchInfo


T = TypeVar("T", bound="DeviceNodeInfo")


@_attrs_define
class DeviceNodeInfo:
    """Device Node info.

    Attributes:
        device_type (int | Unset): Device type, 0: AP; 1: Switch; 2: Gateway.
        name (str | Unset): Device name
        mac (str | Unset): Device MAC
        model (str | Unset): Device model name
        model_version (str | Unset): Model version of device,for example:3.0
        show_model (str | Unset): Device model name with version
        ip (str | Unset): Device IP
        ipv_6_list (list[str] | Unset): Device IPv6 list
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        status_category (int | Unset): Device status should be a value as follows: 0: Disconnected; 1: Connected; 2:
            Pending; 3: Heartbeat Missed; 4: Isolated
        dev_tx_rate (int | Unset): Device real-time uploadRate
        dev_rx_rate (int | Unset): Device real-time downloadRate
        stack_group (bool | Unset): Stack Group
        stack_id (str | Unset): Stack Id
        health_score (int | Unset): 1~3: poor; 4~7: fair; 0: no data; 8~10 good.
        ap_info (APInfo | Unset): AP info, exists when deviceType is 0.
        switch_info (SwitchInfo | Unset): Switch info, exists when deviceType is 1.
        gateway_info (GatewayInfo | Unset): Gateway info, exists when deviceType is 2.
        ap (bool | Unset):
        osg (bool | Unset):
        osw (bool | Unset):
    """

    device_type: int | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    dev_tx_rate: int | Unset = UNSET
    dev_rx_rate: int | Unset = UNSET
    stack_group: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    health_score: int | Unset = UNSET
    ap_info: APInfo | Unset = UNSET
    switch_info: SwitchInfo | Unset = UNSET
    gateway_info: GatewayInfo | Unset = UNSET
    ap: bool | Unset = UNSET
    osg: bool | Unset = UNSET
    osw: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_type = self.device_type

        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        ip = self.ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        status = self.status

        status_category = self.status_category

        dev_tx_rate = self.dev_tx_rate

        dev_rx_rate = self.dev_rx_rate

        stack_group = self.stack_group

        stack_id = self.stack_id

        health_score = self.health_score

        ap_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap_info, Unset):
            ap_info = self.ap_info.to_dict()

        switch_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_info, Unset):
            switch_info = self.switch_info.to_dict()

        gateway_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_info, Unset):
            gateway_info = self.gateway_info.to_dict()

        ap = self.ap

        osg = self.osg

        osw = self.osw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if dev_tx_rate is not UNSET:
            field_dict["devTxRate"] = dev_tx_rate
        if dev_rx_rate is not UNSET:
            field_dict["devRxRate"] = dev_rx_rate
        if stack_group is not UNSET:
            field_dict["stackGroup"] = stack_group
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if ap_info is not UNSET:
            field_dict["apInfo"] = ap_info
        if switch_info is not UNSET:
            field_dict["switchInfo"] = switch_info
        if gateway_info is not UNSET:
            field_dict["gatewayInfo"] = gateway_info
        if ap is not UNSET:
            field_dict["ap"] = ap
        if osg is not UNSET:
            field_dict["osg"] = osg
        if osw is not UNSET:
            field_dict["osw"] = osw

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_info import APInfo
        from ..models.gateway_info import GatewayInfo
        from ..models.switch_info import SwitchInfo

        d = dict(src_dict)
        device_type = d.pop("deviceType", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        dev_tx_rate = d.pop("devTxRate", UNSET)

        dev_rx_rate = d.pop("devRxRate", UNSET)

        stack_group = d.pop("stackGroup", UNSET)

        stack_id = d.pop("stackId", UNSET)

        health_score = d.pop("healthScore", UNSET)

        _ap_info = d.pop("apInfo", UNSET)
        ap_info: APInfo | Unset
        if isinstance(_ap_info, Unset):
            ap_info = UNSET
        else:
            ap_info = APInfo.from_dict(_ap_info)

        _switch_info = d.pop("switchInfo", UNSET)
        switch_info: SwitchInfo | Unset
        if isinstance(_switch_info, Unset):
            switch_info = UNSET
        else:
            switch_info = SwitchInfo.from_dict(_switch_info)

        _gateway_info = d.pop("gatewayInfo", UNSET)
        gateway_info: GatewayInfo | Unset
        if isinstance(_gateway_info, Unset):
            gateway_info = UNSET
        else:
            gateway_info = GatewayInfo.from_dict(_gateway_info)

        ap = d.pop("ap", UNSET)

        osg = d.pop("osg", UNSET)

        osw = d.pop("osw", UNSET)

        device_node_info = cls(
            device_type=device_type,
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            show_model=show_model,
            ip=ip,
            ipv_6_list=ipv_6_list,
            status=status,
            status_category=status_category,
            dev_tx_rate=dev_tx_rate,
            dev_rx_rate=dev_rx_rate,
            stack_group=stack_group,
            stack_id=stack_id,
            health_score=health_score,
            ap_info=ap_info,
            switch_info=switch_info,
            gateway_info=gateway_info,
            ap=ap,
            osg=osg,
            osw=osw,
        )

        device_node_info.additional_properties = d
        return device_node_info

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
