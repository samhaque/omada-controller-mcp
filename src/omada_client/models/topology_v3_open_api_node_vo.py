from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_agg_health_dto import ClientAggHealthDTO
    from ..models.clients_query_mac_and_filter_type import ClientsQueryMacAndFilterType
    from ..models.lan_port import LanPort
    from ..models.port_label_dto import PortLabelDTO
    from ..models.topology_filter_client_count_dto import TopologyFilterClientCountDTO
    from ..models.vigi_wireless_up_info_dto import VigiWirelessUpInfoDTO
    from ..models.vrrp_group_dto import VrrpGroupDTO
    from ..models.vrrp_link_dto import VrrpLinkDTO
    from ..models.wan_port import WanPort
    from ..models.wired_port_v3dto import WiredPortV3DTO
    from ..models.wired_up_info_dto import WiredUpInfoDTO
    from ..models.wireless_up_info_dto import WirelessUpInfoDTO


T = TypeVar("T", bound="TopologyV3OpenApiNodeVO")


@_attrs_define
class TopologyV3OpenApiNodeVO:
    """Topology Nodes

    Attributes:
        type_ (str | Unset): Device Type
        name (str | Unset): Device Name
        mac (str | Unset): Device Mac
        mac_list (list[str] | Unset): Device Macs
        client_count (int | Unset): Directly Connected Client Count
        ipc_count (int | Unset): Directly Connected IPC Client Count
        is_all_clients (bool | Unset): Whether The Client Group Is All Clients Or Just Other Clients
        uplink_mac_list (list[str] | Unset): Mlag Or Vrrp Group All Members Mac List
        multi_switch_downlink_client (list[ClientsQueryMacAndFilterType] | Unset): Mlag Or Vrrp Group All Members Client
            Query Parameter
        filter_client_count (TopologyFilterClientCountDTO | Unset): Each Connection Type Client Count
        health_score (int | Unset): Health Score
        model (str | Unset): Device Model
        model_version (str | Unset): Device ModelVersion
        show_model (str | Unset): Device Show Model
        special_model (str | Unset): Special device model,for example:EAP225-Outdoor-1a20a950b8d950e8
        device_series_type (int | Unset): Device Series Type
        compatible (int | Unset): The Compatibility Type Of Device Firmware And Controller
        ecsp_first_version (int | Unset): Device Protocol First Version
        disconnected (bool | Unset): Whether The Device Is Disconnected Or Not
        active (bool | Unset): Whether The Device Is License Active Or Not
        ip (str | Unset): Device Ip
        dev_tx_rate (int | Unset): Device TxRate
        dev_rx_rate (int | Unset): Device RxRate
        client_health (ClientAggHealthDTO | Unset): Client Health
        wan_ports (list[WanPort] | Unset): Gateway Wan Port List
        lan_ports (list[LanPort] | Unset): Gateway Lan Port List
        stack_status (int | Unset): Status of the Stack Group. 0: normal; 1: abnormal; 2: stack not ready.
        abnormal_reason (int | Unset): Stack Abnormal Reason. 0: Not All Connected. 2: Not All Activated.
        stack_group (bool | Unset): Whether The Switch Device Is Stack Group Or Not
        stack_id (str | Unset): StackGroup Switch Device Id
        rd_mode_2_g (str | Unset): rdMode2g
        channel2g (int | Unset): channel2g
        rd_mode_5_g (str | Unset): rdMode5g
        channel5g (int | Unset): channel5g
        rd_mode_5_g_2 (str | Unset): rdMode5g2
        channel5g2 (int | Unset): channel5g2
        rd_mode_6_g (str | Unset): rdMode6g
        channel6g (int | Unset): channel6g
        support5g2 (bool | Unset): Whether The Device Supports 5g2 Or Not
        role (int | Unset): Identify Device Role In P2P Scenarios
        firmware_version (str | Unset): FirmwareVersion Of IPC/NVR
        channel_num (int | Unset): ChannelNum Of IPC/NVR
        connected_channel (int | Unset): Connected Channel Of IPC/NVR
        wireless_uplink (bool | Unset): Whether The IPC/NVR Is Wireless Connected Or Not
        successors (list[TopologyV3OpenApiNodeVO] | Unset): Device Successors
        wired_up_info (WiredUpInfoDTO | Unset): Multi wiredUpInfo for mlag and vrrp member or downlink device
        wired_up_infos (list[WiredUpInfoDTO] | Unset): Multi wiredUpInfo for mlag and vrrp member or downlink device
        wireless_up_info (WirelessUpInfoDTO | Unset): Wireless UpLink Info
        vigi_wireless_up_info (VigiWirelessUpInfoDTO | Unset): Wireless Vigi UpLink Info
        port_labels (PortLabelDTO | Unset): Other Device Port Labels
        description (str | Unset): Other Device Description
        capability (str | Unset): Other Device Capability
        status (int | Unset): Device Status
        status_category (int | Unset): Device Status Category
        warn_nvr_firmware (bool | Unset): Whether IPC/NVR Needs To Upgrade Firmware To Support Lldp Feature
        client_type (str | Unset): Type of Third Party Device, if type is other
        client_vlan_id (int | Unset): Vlan Id Of Client That Exists In Topology As Other Device
        omada_device_type (str | Unset): Type of Omada Device, if type is other
        specific_other_type (str | Unset): SpecificOtherType for other device
        exist_stp_loop (bool | Unset): Exist Stp Loop Or Not
        vigi_managed (bool | Unset): If Vigi Is Managed By Vms
        ippt (bool | Unset): If Gateway Is Ippt Mode
        specific_type (int | Unset): SpecificType for multiSwitchNode, 0 means mlag node and 1 means vrrp node
        mlag_id (str | Unset): Mlag group id
        multi_switch_list (list[TopologyV3OpenApiNodeVO] | Unset): All members for multiSwitchNode including mlag and
            vrrp node
        multi_switch_num (int | Unset): Serial number for mlag and vrrp node members, which is unique
        multi_switch_role (int | Unset): Role for mlag and vrrp node members
        dad_link (list[WiredPortV3DTO] | Unset): DadLink for mlag node
        peer_link (list[WiredPortV3DTO] | Unset): PeerLink for mlag node
        vrrp_link (list[VrrpLinkDTO] | Unset): Vrrp members internal link
        vlans_as_master (str | Unset): All vlans that vrrp member act as master
        vrrp_group_list (list[VrrpGroupDTO] | Unset): Vrrp node member's vrrp group information
    """

    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    mac_list: list[str] | Unset = UNSET
    client_count: int | Unset = UNSET
    ipc_count: int | Unset = UNSET
    is_all_clients: bool | Unset = UNSET
    uplink_mac_list: list[str] | Unset = UNSET
    multi_switch_downlink_client: list[ClientsQueryMacAndFilterType] | Unset = UNSET
    filter_client_count: TopologyFilterClientCountDTO | Unset = UNSET
    health_score: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    special_model: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    compatible: int | Unset = UNSET
    ecsp_first_version: int | Unset = UNSET
    disconnected: bool | Unset = UNSET
    active: bool | Unset = UNSET
    ip: str | Unset = UNSET
    dev_tx_rate: int | Unset = UNSET
    dev_rx_rate: int | Unset = UNSET
    client_health: ClientAggHealthDTO | Unset = UNSET
    wan_ports: list[WanPort] | Unset = UNSET
    lan_ports: list[LanPort] | Unset = UNSET
    stack_status: int | Unset = UNSET
    abnormal_reason: int | Unset = UNSET
    stack_group: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    rd_mode_2_g: str | Unset = UNSET
    channel2g: int | Unset = UNSET
    rd_mode_5_g: str | Unset = UNSET
    channel5g: int | Unset = UNSET
    rd_mode_5_g_2: str | Unset = UNSET
    channel5g2: int | Unset = UNSET
    rd_mode_6_g: str | Unset = UNSET
    channel6g: int | Unset = UNSET
    support5g2: bool | Unset = UNSET
    role: int | Unset = UNSET
    firmware_version: str | Unset = UNSET
    channel_num: int | Unset = UNSET
    connected_channel: int | Unset = UNSET
    wireless_uplink: bool | Unset = UNSET
    successors: list[TopologyV3OpenApiNodeVO] | Unset = UNSET
    wired_up_info: WiredUpInfoDTO | Unset = UNSET
    wired_up_infos: list[WiredUpInfoDTO] | Unset = UNSET
    wireless_up_info: WirelessUpInfoDTO | Unset = UNSET
    vigi_wireless_up_info: VigiWirelessUpInfoDTO | Unset = UNSET
    port_labels: PortLabelDTO | Unset = UNSET
    description: str | Unset = UNSET
    capability: str | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    warn_nvr_firmware: bool | Unset = UNSET
    client_type: str | Unset = UNSET
    client_vlan_id: int | Unset = UNSET
    omada_device_type: str | Unset = UNSET
    specific_other_type: str | Unset = UNSET
    exist_stp_loop: bool | Unset = UNSET
    vigi_managed: bool | Unset = UNSET
    ippt: bool | Unset = UNSET
    specific_type: int | Unset = UNSET
    mlag_id: str | Unset = UNSET
    multi_switch_list: list[TopologyV3OpenApiNodeVO] | Unset = UNSET
    multi_switch_num: int | Unset = UNSET
    multi_switch_role: int | Unset = UNSET
    dad_link: list[WiredPortV3DTO] | Unset = UNSET
    peer_link: list[WiredPortV3DTO] | Unset = UNSET
    vrrp_link: list[VrrpLinkDTO] | Unset = UNSET
    vlans_as_master: str | Unset = UNSET
    vrrp_group_list: list[VrrpGroupDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        mac = self.mac

        mac_list: list[str] | Unset = UNSET
        if not isinstance(self.mac_list, Unset):
            mac_list = self.mac_list

        client_count = self.client_count

        ipc_count = self.ipc_count

        is_all_clients = self.is_all_clients

        uplink_mac_list: list[str] | Unset = UNSET
        if not isinstance(self.uplink_mac_list, Unset):
            uplink_mac_list = self.uplink_mac_list

        multi_switch_downlink_client: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_switch_downlink_client, Unset):
            multi_switch_downlink_client = []
            for (
                multi_switch_downlink_client_item_data
            ) in self.multi_switch_downlink_client:
                multi_switch_downlink_client_item = (
                    multi_switch_downlink_client_item_data.to_dict()
                )
                multi_switch_downlink_client.append(multi_switch_downlink_client_item)

        filter_client_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_client_count, Unset):
            filter_client_count = self.filter_client_count.to_dict()

        health_score = self.health_score

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        special_model = self.special_model

        device_series_type = self.device_series_type

        compatible = self.compatible

        ecsp_first_version = self.ecsp_first_version

        disconnected = self.disconnected

        active = self.active

        ip = self.ip

        dev_tx_rate = self.dev_tx_rate

        dev_rx_rate = self.dev_rx_rate

        client_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_health, Unset):
            client_health = self.client_health.to_dict()

        wan_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_ports, Unset):
            wan_ports = []
            for wan_ports_item_data in self.wan_ports:
                wan_ports_item = wan_ports_item_data.to_dict()
                wan_ports.append(wan_ports_item)

        lan_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_ports, Unset):
            lan_ports = []
            for lan_ports_item_data in self.lan_ports:
                lan_ports_item = lan_ports_item_data.to_dict()
                lan_ports.append(lan_ports_item)

        stack_status = self.stack_status

        abnormal_reason = self.abnormal_reason

        stack_group = self.stack_group

        stack_id = self.stack_id

        rd_mode_2_g = self.rd_mode_2_g

        channel2g = self.channel2g

        rd_mode_5_g = self.rd_mode_5_g

        channel5g = self.channel5g

        rd_mode_5_g_2 = self.rd_mode_5_g_2

        channel5g2 = self.channel5g2

        rd_mode_6_g = self.rd_mode_6_g

        channel6g = self.channel6g

        support5g2 = self.support5g2

        role = self.role

        firmware_version = self.firmware_version

        channel_num = self.channel_num

        connected_channel = self.connected_channel

        wireless_uplink = self.wireless_uplink

        successors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.successors, Unset):
            successors = []
            for successors_item_data in self.successors:
                successors_item = successors_item_data.to_dict()
                successors.append(successors_item)

        wired_up_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wired_up_info, Unset):
            wired_up_info = self.wired_up_info.to_dict()

        wired_up_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wired_up_infos, Unset):
            wired_up_infos = []
            for wired_up_infos_item_data in self.wired_up_infos:
                wired_up_infos_item = wired_up_infos_item_data.to_dict()
                wired_up_infos.append(wired_up_infos_item)

        wireless_up_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_up_info, Unset):
            wireless_up_info = self.wireless_up_info.to_dict()

        vigi_wireless_up_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vigi_wireless_up_info, Unset):
            vigi_wireless_up_info = self.vigi_wireless_up_info.to_dict()

        port_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_labels, Unset):
            port_labels = self.port_labels.to_dict()

        description = self.description

        capability = self.capability

        status = self.status

        status_category = self.status_category

        warn_nvr_firmware = self.warn_nvr_firmware

        client_type = self.client_type

        client_vlan_id = self.client_vlan_id

        omada_device_type = self.omada_device_type

        specific_other_type = self.specific_other_type

        exist_stp_loop = self.exist_stp_loop

        vigi_managed = self.vigi_managed

        ippt = self.ippt

        specific_type = self.specific_type

        mlag_id = self.mlag_id

        multi_switch_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_switch_list, Unset):
            multi_switch_list = []
            for multi_switch_list_item_data in self.multi_switch_list:
                multi_switch_list_item = multi_switch_list_item_data.to_dict()
                multi_switch_list.append(multi_switch_list_item)

        multi_switch_num = self.multi_switch_num

        multi_switch_role = self.multi_switch_role

        dad_link: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dad_link, Unset):
            dad_link = []
            for dad_link_item_data in self.dad_link:
                dad_link_item = dad_link_item_data.to_dict()
                dad_link.append(dad_link_item)

        peer_link: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.peer_link, Unset):
            peer_link = []
            for peer_link_item_data in self.peer_link:
                peer_link_item = peer_link_item_data.to_dict()
                peer_link.append(peer_link_item)

        vrrp_link: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vrrp_link, Unset):
            vrrp_link = []
            for vrrp_link_item_data in self.vrrp_link:
                vrrp_link_item = vrrp_link_item_data.to_dict()
                vrrp_link.append(vrrp_link_item)

        vlans_as_master = self.vlans_as_master

        vrrp_group_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vrrp_group_list, Unset):
            vrrp_group_list = []
            for vrrp_group_list_item_data in self.vrrp_group_list:
                vrrp_group_list_item = vrrp_group_list_item_data.to_dict()
                vrrp_group_list.append(vrrp_group_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mac_list is not UNSET:
            field_dict["macList"] = mac_list
        if client_count is not UNSET:
            field_dict["clientCount"] = client_count
        if ipc_count is not UNSET:
            field_dict["ipcCount"] = ipc_count
        if is_all_clients is not UNSET:
            field_dict["isAllClients"] = is_all_clients
        if uplink_mac_list is not UNSET:
            field_dict["uplinkMacList"] = uplink_mac_list
        if multi_switch_downlink_client is not UNSET:
            field_dict["multiSwitchDownlinkClient"] = multi_switch_downlink_client
        if filter_client_count is not UNSET:
            field_dict["filterClientCount"] = filter_client_count
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if special_model is not UNSET:
            field_dict["specialModel"] = special_model
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if ecsp_first_version is not UNSET:
            field_dict["ecspFirstVersion"] = ecsp_first_version
        if disconnected is not UNSET:
            field_dict["disconnected"] = disconnected
        if active is not UNSET:
            field_dict["active"] = active
        if ip is not UNSET:
            field_dict["ip"] = ip
        if dev_tx_rate is not UNSET:
            field_dict["devTxRate"] = dev_tx_rate
        if dev_rx_rate is not UNSET:
            field_dict["devRxRate"] = dev_rx_rate
        if client_health is not UNSET:
            field_dict["clientHealth"] = client_health
        if wan_ports is not UNSET:
            field_dict["wanPorts"] = wan_ports
        if lan_ports is not UNSET:
            field_dict["lanPorts"] = lan_ports
        if stack_status is not UNSET:
            field_dict["stackStatus"] = stack_status
        if abnormal_reason is not UNSET:
            field_dict["abnormalReason"] = abnormal_reason
        if stack_group is not UNSET:
            field_dict["stackGroup"] = stack_group
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if rd_mode_2_g is not UNSET:
            field_dict["rdMode2g"] = rd_mode_2_g
        if channel2g is not UNSET:
            field_dict["channel2g"] = channel2g
        if rd_mode_5_g is not UNSET:
            field_dict["rdMode5g"] = rd_mode_5_g
        if channel5g is not UNSET:
            field_dict["channel5g"] = channel5g
        if rd_mode_5_g_2 is not UNSET:
            field_dict["rdMode5g2"] = rd_mode_5_g_2
        if channel5g2 is not UNSET:
            field_dict["channel5g2"] = channel5g2
        if rd_mode_6_g is not UNSET:
            field_dict["rdMode6g"] = rd_mode_6_g
        if channel6g is not UNSET:
            field_dict["channel6g"] = channel6g
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if role is not UNSET:
            field_dict["role"] = role
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if channel_num is not UNSET:
            field_dict["channelNum"] = channel_num
        if connected_channel is not UNSET:
            field_dict["connectedChannel"] = connected_channel
        if wireless_uplink is not UNSET:
            field_dict["wirelessUplink"] = wireless_uplink
        if successors is not UNSET:
            field_dict["successors"] = successors
        if wired_up_info is not UNSET:
            field_dict["wiredUpInfo"] = wired_up_info
        if wired_up_infos is not UNSET:
            field_dict["wiredUpInfos"] = wired_up_infos
        if wireless_up_info is not UNSET:
            field_dict["wirelessUpInfo"] = wireless_up_info
        if vigi_wireless_up_info is not UNSET:
            field_dict["vigiWirelessUpInfo"] = vigi_wireless_up_info
        if port_labels is not UNSET:
            field_dict["portLabels"] = port_labels
        if description is not UNSET:
            field_dict["description"] = description
        if capability is not UNSET:
            field_dict["capability"] = capability
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if warn_nvr_firmware is not UNSET:
            field_dict["warnNvrFirmware"] = warn_nvr_firmware
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if client_vlan_id is not UNSET:
            field_dict["clientVlanId"] = client_vlan_id
        if omada_device_type is not UNSET:
            field_dict["omadaDeviceType"] = omada_device_type
        if specific_other_type is not UNSET:
            field_dict["specificOtherType"] = specific_other_type
        if exist_stp_loop is not UNSET:
            field_dict["existStpLoop"] = exist_stp_loop
        if vigi_managed is not UNSET:
            field_dict["vigiManaged"] = vigi_managed
        if ippt is not UNSET:
            field_dict["ippt"] = ippt
        if specific_type is not UNSET:
            field_dict["specificType"] = specific_type
        if mlag_id is not UNSET:
            field_dict["mlagId"] = mlag_id
        if multi_switch_list is not UNSET:
            field_dict["multiSwitchList"] = multi_switch_list
        if multi_switch_num is not UNSET:
            field_dict["multiSwitchNum"] = multi_switch_num
        if multi_switch_role is not UNSET:
            field_dict["multiSwitchRole"] = multi_switch_role
        if dad_link is not UNSET:
            field_dict["dadLink"] = dad_link
        if peer_link is not UNSET:
            field_dict["peerLink"] = peer_link
        if vrrp_link is not UNSET:
            field_dict["vrrpLink"] = vrrp_link
        if vlans_as_master is not UNSET:
            field_dict["vlansAsMaster"] = vlans_as_master
        if vrrp_group_list is not UNSET:
            field_dict["vrrpGroupList"] = vrrp_group_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_agg_health_dto import ClientAggHealthDTO
        from ..models.clients_query_mac_and_filter_type import (
            ClientsQueryMacAndFilterType,
        )
        from ..models.lan_port import LanPort
        from ..models.port_label_dto import PortLabelDTO
        from ..models.topology_filter_client_count_dto import (
            TopologyFilterClientCountDTO,
        )
        from ..models.vigi_wireless_up_info_dto import (
            VigiWirelessUpInfoDTO,
        )
        from ..models.vrrp_group_dto import VrrpGroupDTO
        from ..models.vrrp_link_dto import VrrpLinkDTO
        from ..models.wan_port import WanPort
        from ..models.wired_port_v3dto import WiredPortV3DTO
        from ..models.wired_up_info_dto import WiredUpInfoDTO
        from ..models.wireless_up_info_dto import WirelessUpInfoDTO

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        mac_list = cast(list[str], d.pop("macList", UNSET))

        client_count = d.pop("clientCount", UNSET)

        ipc_count = d.pop("ipcCount", UNSET)

        is_all_clients = d.pop("isAllClients", UNSET)

        uplink_mac_list = cast(list[str], d.pop("uplinkMacList", UNSET))

        _multi_switch_downlink_client = d.pop("multiSwitchDownlinkClient", UNSET)
        multi_switch_downlink_client: list[ClientsQueryMacAndFilterType] | Unset = UNSET
        if _multi_switch_downlink_client is not UNSET:
            multi_switch_downlink_client = []
            for multi_switch_downlink_client_item_data in _multi_switch_downlink_client:
                multi_switch_downlink_client_item = (
                    ClientsQueryMacAndFilterType.from_dict(
                        multi_switch_downlink_client_item_data
                    )
                )

                multi_switch_downlink_client.append(multi_switch_downlink_client_item)

        _filter_client_count = d.pop("filterClientCount", UNSET)
        filter_client_count: TopologyFilterClientCountDTO | Unset
        if isinstance(_filter_client_count, Unset):
            filter_client_count = UNSET
        else:
            filter_client_count = TopologyFilterClientCountDTO.from_dict(
                _filter_client_count
            )

        health_score = d.pop("healthScore", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        special_model = d.pop("specialModel", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        compatible = d.pop("compatible", UNSET)

        ecsp_first_version = d.pop("ecspFirstVersion", UNSET)

        disconnected = d.pop("disconnected", UNSET)

        active = d.pop("active", UNSET)

        ip = d.pop("ip", UNSET)

        dev_tx_rate = d.pop("devTxRate", UNSET)

        dev_rx_rate = d.pop("devRxRate", UNSET)

        _client_health = d.pop("clientHealth", UNSET)
        client_health: ClientAggHealthDTO | Unset
        if isinstance(_client_health, Unset):
            client_health = UNSET
        else:
            client_health = ClientAggHealthDTO.from_dict(_client_health)

        _wan_ports = d.pop("wanPorts", UNSET)
        wan_ports: list[WanPort] | Unset = UNSET
        if _wan_ports is not UNSET:
            wan_ports = []
            for wan_ports_item_data in _wan_ports:
                wan_ports_item = WanPort.from_dict(wan_ports_item_data)

                wan_ports.append(wan_ports_item)

        _lan_ports = d.pop("lanPorts", UNSET)
        lan_ports: list[LanPort] | Unset = UNSET
        if _lan_ports is not UNSET:
            lan_ports = []
            for lan_ports_item_data in _lan_ports:
                lan_ports_item = LanPort.from_dict(lan_ports_item_data)

                lan_ports.append(lan_ports_item)

        stack_status = d.pop("stackStatus", UNSET)

        abnormal_reason = d.pop("abnormalReason", UNSET)

        stack_group = d.pop("stackGroup", UNSET)

        stack_id = d.pop("stackId", UNSET)

        rd_mode_2_g = d.pop("rdMode2g", UNSET)

        channel2g = d.pop("channel2g", UNSET)

        rd_mode_5_g = d.pop("rdMode5g", UNSET)

        channel5g = d.pop("channel5g", UNSET)

        rd_mode_5_g_2 = d.pop("rdMode5g2", UNSET)

        channel5g2 = d.pop("channel5g2", UNSET)

        rd_mode_6_g = d.pop("rdMode6g", UNSET)

        channel6g = d.pop("channel6g", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        role = d.pop("role", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        channel_num = d.pop("channelNum", UNSET)

        connected_channel = d.pop("connectedChannel", UNSET)

        wireless_uplink = d.pop("wirelessUplink", UNSET)

        _successors = d.pop("successors", UNSET)
        successors: list[TopologyV3OpenApiNodeVO] | Unset = UNSET
        if _successors is not UNSET:
            successors = []
            for successors_item_data in _successors:
                successors_item = TopologyV3OpenApiNodeVO.from_dict(
                    successors_item_data
                )

                successors.append(successors_item)

        _wired_up_info = d.pop("wiredUpInfo", UNSET)
        wired_up_info: WiredUpInfoDTO | Unset
        if isinstance(_wired_up_info, Unset):
            wired_up_info = UNSET
        else:
            wired_up_info = WiredUpInfoDTO.from_dict(_wired_up_info)

        _wired_up_infos = d.pop("wiredUpInfos", UNSET)
        wired_up_infos: list[WiredUpInfoDTO] | Unset = UNSET
        if _wired_up_infos is not UNSET:
            wired_up_infos = []
            for wired_up_infos_item_data in _wired_up_infos:
                wired_up_infos_item = WiredUpInfoDTO.from_dict(wired_up_infos_item_data)

                wired_up_infos.append(wired_up_infos_item)

        _wireless_up_info = d.pop("wirelessUpInfo", UNSET)
        wireless_up_info: WirelessUpInfoDTO | Unset
        if isinstance(_wireless_up_info, Unset):
            wireless_up_info = UNSET
        else:
            wireless_up_info = WirelessUpInfoDTO.from_dict(_wireless_up_info)

        _vigi_wireless_up_info = d.pop("vigiWirelessUpInfo", UNSET)
        vigi_wireless_up_info: VigiWirelessUpInfoDTO | Unset
        if isinstance(_vigi_wireless_up_info, Unset):
            vigi_wireless_up_info = UNSET
        else:
            vigi_wireless_up_info = VigiWirelessUpInfoDTO.from_dict(
                _vigi_wireless_up_info
            )

        _port_labels = d.pop("portLabels", UNSET)
        port_labels: PortLabelDTO | Unset
        if isinstance(_port_labels, Unset):
            port_labels = UNSET
        else:
            port_labels = PortLabelDTO.from_dict(_port_labels)

        description = d.pop("description", UNSET)

        capability = d.pop("capability", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        warn_nvr_firmware = d.pop("warnNvrFirmware", UNSET)

        client_type = d.pop("clientType", UNSET)

        client_vlan_id = d.pop("clientVlanId", UNSET)

        omada_device_type = d.pop("omadaDeviceType", UNSET)

        specific_other_type = d.pop("specificOtherType", UNSET)

        exist_stp_loop = d.pop("existStpLoop", UNSET)

        vigi_managed = d.pop("vigiManaged", UNSET)

        ippt = d.pop("ippt", UNSET)

        specific_type = d.pop("specificType", UNSET)

        mlag_id = d.pop("mlagId", UNSET)

        _multi_switch_list = d.pop("multiSwitchList", UNSET)
        multi_switch_list: list[TopologyV3OpenApiNodeVO] | Unset = UNSET
        if _multi_switch_list is not UNSET:
            multi_switch_list = []
            for multi_switch_list_item_data in _multi_switch_list:
                multi_switch_list_item = TopologyV3OpenApiNodeVO.from_dict(
                    multi_switch_list_item_data
                )

                multi_switch_list.append(multi_switch_list_item)

        multi_switch_num = d.pop("multiSwitchNum", UNSET)

        multi_switch_role = d.pop("multiSwitchRole", UNSET)

        _dad_link = d.pop("dadLink", UNSET)
        dad_link: list[WiredPortV3DTO] | Unset = UNSET
        if _dad_link is not UNSET:
            dad_link = []
            for dad_link_item_data in _dad_link:
                dad_link_item = WiredPortV3DTO.from_dict(dad_link_item_data)

                dad_link.append(dad_link_item)

        _peer_link = d.pop("peerLink", UNSET)
        peer_link: list[WiredPortV3DTO] | Unset = UNSET
        if _peer_link is not UNSET:
            peer_link = []
            for peer_link_item_data in _peer_link:
                peer_link_item = WiredPortV3DTO.from_dict(peer_link_item_data)

                peer_link.append(peer_link_item)

        _vrrp_link = d.pop("vrrpLink", UNSET)
        vrrp_link: list[VrrpLinkDTO] | Unset = UNSET
        if _vrrp_link is not UNSET:
            vrrp_link = []
            for vrrp_link_item_data in _vrrp_link:
                vrrp_link_item = VrrpLinkDTO.from_dict(vrrp_link_item_data)

                vrrp_link.append(vrrp_link_item)

        vlans_as_master = d.pop("vlansAsMaster", UNSET)

        _vrrp_group_list = d.pop("vrrpGroupList", UNSET)
        vrrp_group_list: list[VrrpGroupDTO] | Unset = UNSET
        if _vrrp_group_list is not UNSET:
            vrrp_group_list = []
            for vrrp_group_list_item_data in _vrrp_group_list:
                vrrp_group_list_item = VrrpGroupDTO.from_dict(vrrp_group_list_item_data)

                vrrp_group_list.append(vrrp_group_list_item)

        topology_v3_open_api_node_vo = cls(
            type_=type_,
            name=name,
            mac=mac,
            mac_list=mac_list,
            client_count=client_count,
            ipc_count=ipc_count,
            is_all_clients=is_all_clients,
            uplink_mac_list=uplink_mac_list,
            multi_switch_downlink_client=multi_switch_downlink_client,
            filter_client_count=filter_client_count,
            health_score=health_score,
            model=model,
            model_version=model_version,
            show_model=show_model,
            special_model=special_model,
            device_series_type=device_series_type,
            compatible=compatible,
            ecsp_first_version=ecsp_first_version,
            disconnected=disconnected,
            active=active,
            ip=ip,
            dev_tx_rate=dev_tx_rate,
            dev_rx_rate=dev_rx_rate,
            client_health=client_health,
            wan_ports=wan_ports,
            lan_ports=lan_ports,
            stack_status=stack_status,
            abnormal_reason=abnormal_reason,
            stack_group=stack_group,
            stack_id=stack_id,
            rd_mode_2_g=rd_mode_2_g,
            channel2g=channel2g,
            rd_mode_5_g=rd_mode_5_g,
            channel5g=channel5g,
            rd_mode_5_g_2=rd_mode_5_g_2,
            channel5g2=channel5g2,
            rd_mode_6_g=rd_mode_6_g,
            channel6g=channel6g,
            support5g2=support5g2,
            role=role,
            firmware_version=firmware_version,
            channel_num=channel_num,
            connected_channel=connected_channel,
            wireless_uplink=wireless_uplink,
            successors=successors,
            wired_up_info=wired_up_info,
            wired_up_infos=wired_up_infos,
            wireless_up_info=wireless_up_info,
            vigi_wireless_up_info=vigi_wireless_up_info,
            port_labels=port_labels,
            description=description,
            capability=capability,
            status=status,
            status_category=status_category,
            warn_nvr_firmware=warn_nvr_firmware,
            client_type=client_type,
            client_vlan_id=client_vlan_id,
            omada_device_type=omada_device_type,
            specific_other_type=specific_other_type,
            exist_stp_loop=exist_stp_loop,
            vigi_managed=vigi_managed,
            ippt=ippt,
            specific_type=specific_type,
            mlag_id=mlag_id,
            multi_switch_list=multi_switch_list,
            multi_switch_num=multi_switch_num,
            multi_switch_role=multi_switch_role,
            dad_link=dad_link,
            peer_link=peer_link,
            vrrp_link=vrrp_link,
            vlans_as_master=vlans_as_master,
            vrrp_group_list=vrrp_group_list,
        )

        topology_v3_open_api_node_vo.additional_properties = d
        return topology_v3_open_api_node_vo

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
