from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mlag_msg_vo import MlagMsgVO
    from ..models.osw_stat_port_vo import OswStatPortVO
    from ..models.osw_stat_uplink_vo import OswStatUplinkVO


T = TypeVar("T", bound="StatisticsOswVO")


@_attrs_define
class StatisticsOswVO:
    """
    Attributes:
        name (str | Unset): Device name,default value is the mac address of device
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;
            1:Disconnected(Migrating); 10:Provisioning; 11:Configuring; 12:Upgrading; 13:Rebooting; 14:Connected;
            15:Connected(Wireless); 16:Connected(Migrating); 17:Connected(Wireless,Migrating); 20:Pending;
            21:Pending(Wireless); 22:Adopting; 23:Adopting(Wireless); 24:Adopt Failed; 25:Adopt Failed(Wireless); 26:Managed
            By Others; 27:Managed By Others(Wireless); 30:Heartbeat Missed; 31:Heartbeat Missed(Wireless); 32:Heartbeat
            Missed(Migrating); 33:Heartbeat Missed(Wireless,Migrating); 40:Isolated; 41:Isolated(Migrating); 50:Slice
            Configuring
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected; 1:Connected; 2:Pending; 3:Heartbeat Missed; 4:Isolated
        port_num (int | Unset): Port number
        ports (list[OswStatPortVO] | Unset): Ports information
        uplink (OswStatUplinkVO | Unset): Uplink device information
        support_poe (bool | Unset): Whether the device supports POE function
        speeds (list[int] | Unset): Supported rate list for all ports. Speeds should be a value as follows: 0:auto;
            1:10M; 2:100M; 3:1000M; 4:2.5G; 5:10G; 6:5G; 7:25G; 8:100G; 9:40G; -1:error; no value:all rate supported
        support_stack (bool | Unset): Whether device supports stack function
        support_stp (bool | Unset): Whether device supports stp function
        mlag_msg (MlagMsgVO | Unset): M-LAG Message
    """

    name: str | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    port_num: int | Unset = UNSET
    ports: list[OswStatPortVO] | Unset = UNSET
    uplink: OswStatUplinkVO | Unset = UNSET
    support_poe: bool | Unset = UNSET
    speeds: list[int] | Unset = UNSET
    support_stack: bool | Unset = UNSET
    support_stp: bool | Unset = UNSET
    mlag_msg: MlagMsgVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        status_category = self.status_category

        port_num = self.port_num

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        uplink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uplink, Unset):
            uplink = self.uplink.to_dict()

        support_poe = self.support_poe

        speeds: list[int] | Unset = UNSET
        if not isinstance(self.speeds, Unset):
            speeds = self.speeds

        support_stack = self.support_stack

        support_stp = self.support_stp

        mlag_msg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mlag_msg, Unset):
            mlag_msg = self.mlag_msg.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if ports is not UNSET:
            field_dict["ports"] = ports
        if uplink is not UNSET:
            field_dict["uplink"] = uplink
        if support_poe is not UNSET:
            field_dict["supportPoe"] = support_poe
        if speeds is not UNSET:
            field_dict["speeds"] = speeds
        if support_stack is not UNSET:
            field_dict["supportStack"] = support_stack
        if support_stp is not UNSET:
            field_dict["supportSTP"] = support_stp
        if mlag_msg is not UNSET:
            field_dict["mlagMsg"] = mlag_msg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mlag_msg_vo import MlagMsgVO
        from ..models.osw_stat_port_vo import OswStatPortVO
        from ..models.osw_stat_uplink_vo import OswStatUplinkVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        port_num = d.pop("portNum", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[OswStatPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswStatPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _uplink = d.pop("uplink", UNSET)
        uplink: OswStatUplinkVO | Unset
        if isinstance(_uplink, Unset):
            uplink = UNSET
        else:
            uplink = OswStatUplinkVO.from_dict(_uplink)

        support_poe = d.pop("supportPoe", UNSET)

        speeds = cast(list[int], d.pop("speeds", UNSET))

        support_stack = d.pop("supportStack", UNSET)

        support_stp = d.pop("supportSTP", UNSET)

        _mlag_msg = d.pop("mlagMsg", UNSET)
        mlag_msg: MlagMsgVO | Unset
        if isinstance(_mlag_msg, Unset):
            mlag_msg = UNSET
        else:
            mlag_msg = MlagMsgVO.from_dict(_mlag_msg)

        statistics_osw_vo = cls(
            name=name,
            status=status,
            status_category=status_category,
            port_num=port_num,
            ports=ports,
            uplink=uplink,
            support_poe=support_poe,
            speeds=speeds,
            support_stack=support_stack,
            support_stp=support_stp,
            mlag_msg=mlag_msg,
        )

        statistics_osw_vo.additional_properties = d
        return statistics_osw_vo

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
