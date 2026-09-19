from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_mlag_port_vo import OswMlagPortVO
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="MlagAdoptOswVO")


@_attrs_define
class MlagAdoptOswVO:
    """The switches contained in the M-LAG.

    Attributes:
        mac (str | Unset): Device mac
        name (str | Unset): Device name,default value is the mac address of device
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
        version (str | Unset): Simplified version of firmware,for example:2.5.0.
        show_model (str | Unset): Model complex shown in the front end.Ap：model+(country)+modelVersion,EAP225(EU) v3.0
            Gateway/Switch：model+modelVersion,Osg v3.0
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        category (str | Unset): Category of license.
        license_status (int | Unset): Device license status (Only for cloud base) should be a value as follows: 0:
            unActive; 1: Unbind; 2: Expired; 3: active
        due_time (int | Unset): Expire timestamp of license(cloud base exclusive).
        due_time_left (int | Unset): Milliseconds from the current moment to the expiration time(cloud base exclusive)
        active (bool | Unset): whether to active the device(cloud base exclusive).
        device_type (int | Unset): Device type, 1: Gateway; 2: Switch; 3: Ap.
        mlag_version (str | Unset): M-LAG version.
        mlag_group_id (int | Unset): M-LAG group ID.
        ip (str | Unset): IP
        public_ip (str | Unset): Device public IP.
        ipv_6_list (list[str] | Unset): Device IPv6 list.
        support_mlag_ipv_6 (bool | Unset): Whether the device support the configuration of M-LAG group IPv6.
        ports (list[OswMlagPortVO] | Unset): M-LAG group device ports.
        support_peer_link_ports (list[OswStandPortVO] | Unset): Support the configuration of peer link ports for devices
            in the MLAG group.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    status: int | Unset = UNSET
    category: str | Unset = UNSET
    license_status: int | Unset = UNSET
    due_time: int | Unset = UNSET
    due_time_left: int | Unset = UNSET
    active: bool | Unset = UNSET
    device_type: int | Unset = UNSET
    mlag_version: str | Unset = UNSET
    mlag_group_id: int | Unset = UNSET
    ip: str | Unset = UNSET
    public_ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    support_mlag_ipv_6: bool | Unset = UNSET
    ports: list[OswMlagPortVO] | Unset = UNSET
    support_peer_link_ports: list[OswStandPortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        added_in_advanced = self.added_in_advanced

        version = self.version

        show_model = self.show_model

        status = self.status

        category = self.category

        license_status = self.license_status

        due_time = self.due_time

        due_time_left = self.due_time_left

        active = self.active

        device_type = self.device_type

        mlag_version = self.mlag_version

        mlag_group_id = self.mlag_group_id

        ip = self.ip

        public_ip = self.public_ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        support_mlag_ipv_6 = self.support_mlag_ipv_6

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        support_peer_link_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.support_peer_link_ports, Unset):
            support_peer_link_ports = []
            for support_peer_link_ports_item_data in self.support_peer_link_ports:
                support_peer_link_ports_item = (
                    support_peer_link_ports_item_data.to_dict()
                )
                support_peer_link_ports.append(support_peer_link_ports_item)

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
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if version is not UNSET:
            field_dict["version"] = version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if status is not UNSET:
            field_dict["status"] = status
        if category is not UNSET:
            field_dict["category"] = category
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if due_time is not UNSET:
            field_dict["dueTime"] = due_time
        if due_time_left is not UNSET:
            field_dict["dueTimeLeft"] = due_time_left
        if active is not UNSET:
            field_dict["active"] = active
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if mlag_version is not UNSET:
            field_dict["mlagVersion"] = mlag_version
        if mlag_group_id is not UNSET:
            field_dict["mlagGroupId"] = mlag_group_id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if support_mlag_ipv_6 is not UNSET:
            field_dict["supportMlagIpv6"] = support_mlag_ipv_6
        if ports is not UNSET:
            field_dict["ports"] = ports
        if support_peer_link_ports is not UNSET:
            field_dict["supportPeerLinkPorts"] = support_peer_link_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_mlag_port_vo import OswMlagPortVO
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        version = d.pop("version", UNSET)

        show_model = d.pop("showModel", UNSET)

        status = d.pop("status", UNSET)

        category = d.pop("category", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        due_time = d.pop("dueTime", UNSET)

        due_time_left = d.pop("dueTimeLeft", UNSET)

        active = d.pop("active", UNSET)

        device_type = d.pop("deviceType", UNSET)

        mlag_version = d.pop("mlagVersion", UNSET)

        mlag_group_id = d.pop("mlagGroupId", UNSET)

        ip = d.pop("ip", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        support_mlag_ipv_6 = d.pop("supportMlagIpv6", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[OswMlagPortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = OswMlagPortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        _support_peer_link_ports = d.pop("supportPeerLinkPorts", UNSET)
        support_peer_link_ports: list[OswStandPortVO] | Unset = UNSET
        if _support_peer_link_ports is not UNSET:
            support_peer_link_ports = []
            for support_peer_link_ports_item_data in _support_peer_link_ports:
                support_peer_link_ports_item = OswStandPortVO.from_dict(
                    support_peer_link_ports_item_data
                )

                support_peer_link_ports.append(support_peer_link_ports_item)

        mlag_adopt_osw_vo = cls(
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            added_in_advanced=added_in_advanced,
            version=version,
            show_model=show_model,
            status=status,
            category=category,
            license_status=license_status,
            due_time=due_time,
            due_time_left=due_time_left,
            active=active,
            device_type=device_type,
            mlag_version=mlag_version,
            mlag_group_id=mlag_group_id,
            ip=ip,
            public_ip=public_ip,
            ipv_6_list=ipv_6_list,
            support_mlag_ipv_6=support_mlag_ipv_6,
            ports=ports,
            support_peer_link_ports=support_peer_link_ports,
        )

        mlag_adopt_osw_vo.additional_properties = d
        return mlag_adopt_osw_vo

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
