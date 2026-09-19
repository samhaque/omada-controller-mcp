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


T = TypeVar("T", bound="OswMlagMemberVO")


@_attrs_define
class OswMlagMemberVO:
    """M-LAG Group member list

    Attributes:
        mac (str | Unset): Device Mac
        name (str | Unset): Device Name
        role (int | Unset): Role
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        status (int | Unset): Device Status
        ip (str | Unset): IP
        dad_status (int | Unset): DAD status should be a value as follows: 0: PEER_UNDETECTED; 1: NORMAL; 2:
            DAD_DISABLE.
        ka_status (int | Unset): Keep Alive status should be a value as follows: 0: HEARTBEAT_MISSED; 1:
            HEARTBEAT_NORMAL.
        cfg_check (int | Unset): MLAG group configuration check status should be a value as follows: 0: All cfg pass; 1:
            Type2 cfg not pass;2: Type1 and Type2 not pass;3: Type1 not pass
        priority (int | Unset): Priority of the device in the M-LAG group.
        dad_ip (str | Unset): DAD IP Address
        compound_model (str | Unset): Model complex used in the backend.
        show_model (str | Unset): Model complex shown in the front end.
        model_version (str | Unset): Model version of device,for example:3.0
        model (str | Unset): Model of device,for example:EAP225.
        firmware_version (str | Unset): Version of firmware,for example:2.5.0 Build 20190118 Rel. 64821.
        added_in_advanced (bool | Unset):
        version (str | Unset): Simplified version of firmware,for example:2.5.0.
        hw_version (str | Unset): Version of hardware,for example 1.0.
        special_model (str | Unset): Special device model,for example:EAP225-Outdoor-1a20a950b8d950e8.
        category (str | Unset): Category of license.
        uptime (str | Unset): Device uptime.
        license_status (int | Unset): License status(cloud base exclusive).LicenseStatus should be a value as follows:
            0:unActive 1:Unbind 2:Expired 3:active.
        active (bool | Unset): whether to active the device(cloud base exclusive).
        device_type (int | Unset): Device type, 1: Gateway; 2: Switch; 3: Ap.
        due_time (int | Unset): Expire timestamp of license(cloud base exclusive).
        due_time_left (int | Unset): Milliseconds from the current moment to the expiration time(cloud base exclusive)
        license_unbinding_limit (int | Unset): Remaining unbind count for license on detail Page of device(cloud base
            exclusive).
        public_ip (str | Unset): Device public IP.
        ipv6 (list[str] | Unset): Device IPv6 list.
        support_mlag_ipv_6 (bool | Unset): Whether the device support the configuration of M-LAG group IPv6.
        dad_enable (bool | Unset): Whether the DAD enable.
        dad_link_ports (list[str] | Unset): DAD Link Ports
        dad_local_ip (str | Unset): DAD Local IP
        dad_local_ipv_6 (str | Unset): DAD Local IPv6
        dad_peer_ip (str | Unset): DAD Peer IP
        dad_peer_ipv_6 (str | Unset): DAD Peer IPv6
        peer_link_ports (list[str] | Unset): Peer Link Ports
        locate_enable (bool | Unset): Whether the locate function is enabled.
        in_white_list (bool | Unset): Whether the device is in white list.
        eost (int | Unset): End of service time of device(CBC exclusive).
        eos (int | Unset): End of support time of device(CBC exclusive).
        compatible (int | Unset): Device firmware and controller compatibility type.Compatible should be a value as
            follows: 0:COMPATIBLE;1:HIGH_MAJOR_VER;2:LOW_MAJOR_VER;3:HIGH_MINOR_VER;4:LOW_MINOR_VER;7:HIGH_COMPONENT_VER;10:
            DEVICE_NOT_COMPATIBLE;11:HIGH_ADOPT_COMMPONENT;12:DEVICE_CATEGORY_NOT_COMPATIBLE;14:DEVICE_NOT_COMPATIBLE_IN_CLU
            STER.
        mlag_version (str | Unset): M-LAG version.
        mlag_group_id (int | Unset): M-LAG group ID.
        ports (list[OswMlagPortVO] | Unset): M-LAG group device ports.
        support_peer_link_ports (list[OswStandPortVO] | Unset): Support the configuration of peer link ports for devices
            in the MLAG group.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    role: int | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    ip: str | Unset = UNSET
    dad_status: int | Unset = UNSET
    ka_status: int | Unset = UNSET
    cfg_check: int | Unset = UNSET
    priority: int | Unset = UNSET
    dad_ip: str | Unset = UNSET
    compound_model: str | Unset = UNSET
    show_model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    model: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    version: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    special_model: str | Unset = UNSET
    category: str | Unset = UNSET
    uptime: str | Unset = UNSET
    license_status: int | Unset = UNSET
    active: bool | Unset = UNSET
    device_type: int | Unset = UNSET
    due_time: int | Unset = UNSET
    due_time_left: int | Unset = UNSET
    license_unbinding_limit: int | Unset = UNSET
    public_ip: str | Unset = UNSET
    ipv6: list[str] | Unset = UNSET
    support_mlag_ipv_6: bool | Unset = UNSET
    dad_enable: bool | Unset = UNSET
    dad_link_ports: list[str] | Unset = UNSET
    dad_local_ip: str | Unset = UNSET
    dad_local_ipv_6: str | Unset = UNSET
    dad_peer_ip: str | Unset = UNSET
    dad_peer_ipv_6: str | Unset = UNSET
    peer_link_ports: list[str] | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    in_white_list: bool | Unset = UNSET
    eost: int | Unset = UNSET
    eos: int | Unset = UNSET
    compatible: int | Unset = UNSET
    mlag_version: str | Unset = UNSET
    mlag_group_id: int | Unset = UNSET
    ports: list[OswMlagPortVO] | Unset = UNSET
    support_peer_link_ports: list[OswStandPortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        role = self.role

        status_category = self.status_category

        status = self.status

        ip = self.ip

        dad_status = self.dad_status

        ka_status = self.ka_status

        cfg_check = self.cfg_check

        priority = self.priority

        dad_ip = self.dad_ip

        compound_model = self.compound_model

        show_model = self.show_model

        model_version = self.model_version

        model = self.model

        firmware_version = self.firmware_version

        added_in_advanced = self.added_in_advanced

        version = self.version

        hw_version = self.hw_version

        special_model = self.special_model

        category = self.category

        uptime = self.uptime

        license_status = self.license_status

        active = self.active

        device_type = self.device_type

        due_time = self.due_time

        due_time_left = self.due_time_left

        license_unbinding_limit = self.license_unbinding_limit

        public_ip = self.public_ip

        ipv6: list[str] | Unset = UNSET
        if not isinstance(self.ipv6, Unset):
            ipv6 = self.ipv6

        support_mlag_ipv_6 = self.support_mlag_ipv_6

        dad_enable = self.dad_enable

        dad_link_ports: list[str] | Unset = UNSET
        if not isinstance(self.dad_link_ports, Unset):
            dad_link_ports = self.dad_link_ports

        dad_local_ip = self.dad_local_ip

        dad_local_ipv_6 = self.dad_local_ipv_6

        dad_peer_ip = self.dad_peer_ip

        dad_peer_ipv_6 = self.dad_peer_ipv_6

        peer_link_ports: list[str] | Unset = UNSET
        if not isinstance(self.peer_link_ports, Unset):
            peer_link_ports = self.peer_link_ports

        locate_enable = self.locate_enable

        in_white_list = self.in_white_list

        eost = self.eost

        eos = self.eos

        compatible = self.compatible

        mlag_version = self.mlag_version

        mlag_group_id = self.mlag_group_id

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
        if role is not UNSET:
            field_dict["role"] = role
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if ip is not UNSET:
            field_dict["ip"] = ip
        if dad_status is not UNSET:
            field_dict["dadStatus"] = dad_status
        if ka_status is not UNSET:
            field_dict["kaStatus"] = ka_status
        if cfg_check is not UNSET:
            field_dict["cfgCheck"] = cfg_check
        if priority is not UNSET:
            field_dict["priority"] = priority
        if dad_ip is not UNSET:
            field_dict["dadIp"] = dad_ip
        if compound_model is not UNSET:
            field_dict["compoundModel"] = compound_model
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if model is not UNSET:
            field_dict["model"] = model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if version is not UNSET:
            field_dict["version"] = version
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if special_model is not UNSET:
            field_dict["specialModel"] = special_model
        if category is not UNSET:
            field_dict["category"] = category
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if license_status is not UNSET:
            field_dict["licenseStatus"] = license_status
        if active is not UNSET:
            field_dict["active"] = active
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if due_time is not UNSET:
            field_dict["dueTime"] = due_time
        if due_time_left is not UNSET:
            field_dict["dueTimeLeft"] = due_time_left
        if license_unbinding_limit is not UNSET:
            field_dict["licenseUnbindingLimit"] = license_unbinding_limit
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if support_mlag_ipv_6 is not UNSET:
            field_dict["supportMlagIpv6"] = support_mlag_ipv_6
        if dad_enable is not UNSET:
            field_dict["dadEnable"] = dad_enable
        if dad_link_ports is not UNSET:
            field_dict["dadLinkPorts"] = dad_link_ports
        if dad_local_ip is not UNSET:
            field_dict["dadLocalIp"] = dad_local_ip
        if dad_local_ipv_6 is not UNSET:
            field_dict["dadLocalIpv6"] = dad_local_ipv_6
        if dad_peer_ip is not UNSET:
            field_dict["dadPeerIp"] = dad_peer_ip
        if dad_peer_ipv_6 is not UNSET:
            field_dict["dadPeerIpv6"] = dad_peer_ipv_6
        if peer_link_ports is not UNSET:
            field_dict["peerLinkPorts"] = peer_link_ports
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if in_white_list is not UNSET:
            field_dict["inWhiteList"] = in_white_list
        if eost is not UNSET:
            field_dict["eost"] = eost
        if eos is not UNSET:
            field_dict["eos"] = eos
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if mlag_version is not UNSET:
            field_dict["mlagVersion"] = mlag_version
        if mlag_group_id is not UNSET:
            field_dict["mlagGroupId"] = mlag_group_id
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

        role = d.pop("role", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        ip = d.pop("ip", UNSET)

        dad_status = d.pop("dadStatus", UNSET)

        ka_status = d.pop("kaStatus", UNSET)

        cfg_check = d.pop("cfgCheck", UNSET)

        priority = d.pop("priority", UNSET)

        dad_ip = d.pop("dadIp", UNSET)

        compound_model = d.pop("compoundModel", UNSET)

        show_model = d.pop("showModel", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        model = d.pop("model", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        version = d.pop("version", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        special_model = d.pop("specialModel", UNSET)

        category = d.pop("category", UNSET)

        uptime = d.pop("uptime", UNSET)

        license_status = d.pop("licenseStatus", UNSET)

        active = d.pop("active", UNSET)

        device_type = d.pop("deviceType", UNSET)

        due_time = d.pop("dueTime", UNSET)

        due_time_left = d.pop("dueTimeLeft", UNSET)

        license_unbinding_limit = d.pop("licenseUnbindingLimit", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        ipv6 = cast(list[str], d.pop("ipv6", UNSET))

        support_mlag_ipv_6 = d.pop("supportMlagIpv6", UNSET)

        dad_enable = d.pop("dadEnable", UNSET)

        dad_link_ports = cast(list[str], d.pop("dadLinkPorts", UNSET))

        dad_local_ip = d.pop("dadLocalIp", UNSET)

        dad_local_ipv_6 = d.pop("dadLocalIpv6", UNSET)

        dad_peer_ip = d.pop("dadPeerIp", UNSET)

        dad_peer_ipv_6 = d.pop("dadPeerIpv6", UNSET)

        peer_link_ports = cast(list[str], d.pop("peerLinkPorts", UNSET))

        locate_enable = d.pop("locateEnable", UNSET)

        in_white_list = d.pop("inWhiteList", UNSET)

        eost = d.pop("eost", UNSET)

        eos = d.pop("eos", UNSET)

        compatible = d.pop("compatible", UNSET)

        mlag_version = d.pop("mlagVersion", UNSET)

        mlag_group_id = d.pop("mlagGroupId", UNSET)

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

        osw_mlag_member_vo = cls(
            mac=mac,
            name=name,
            role=role,
            status_category=status_category,
            status=status,
            ip=ip,
            dad_status=dad_status,
            ka_status=ka_status,
            cfg_check=cfg_check,
            priority=priority,
            dad_ip=dad_ip,
            compound_model=compound_model,
            show_model=show_model,
            model_version=model_version,
            model=model,
            firmware_version=firmware_version,
            added_in_advanced=added_in_advanced,
            version=version,
            hw_version=hw_version,
            special_model=special_model,
            category=category,
            uptime=uptime,
            license_status=license_status,
            active=active,
            device_type=device_type,
            due_time=due_time,
            due_time_left=due_time_left,
            license_unbinding_limit=license_unbinding_limit,
            public_ip=public_ip,
            ipv6=ipv6,
            support_mlag_ipv_6=support_mlag_ipv_6,
            dad_enable=dad_enable,
            dad_link_ports=dad_link_ports,
            dad_local_ip=dad_local_ip,
            dad_local_ipv_6=dad_local_ipv_6,
            dad_peer_ip=dad_peer_ip,
            dad_peer_ipv_6=dad_peer_ipv_6,
            peer_link_ports=peer_link_ports,
            locate_enable=locate_enable,
            in_white_list=in_white_list,
            eost=eost,
            eos=eos,
            compatible=compatible,
            mlag_version=mlag_version,
            mlag_group_id=mlag_group_id,
            ports=ports,
            support_peer_link_ports=support_peer_link_ports,
        )

        osw_mlag_member_vo.additional_properties = d
        return osw_mlag_member_vo

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
