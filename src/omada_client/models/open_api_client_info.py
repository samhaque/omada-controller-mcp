from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_info_open_api_vo import AuthInfoOpenApiVO
    from ..models.client_ip_setting import ClientIpSetting
    from ..models.client_lock_to_ap_setting import ClientLockToApSetting
    from ..models.client_multifrequency_info import ClientMultifrequencyInfo
    from ..models.rate_limit_setting_of_client import RateLimitSettingOfClient


T = TypeVar("T", bound="OpenApiClientInfo")


@_attrs_define
class OpenApiClientInfo:
    """
    Attributes:
        id (str | Unset): Client ID.
        mac (str | Unset): Client MAC Address.
        name (str | Unset): Client Name, alias.
        host_name (str | Unset): Host name, device name.
        vendor (str | Unset): Vendor.
        device_type (str | Unset): Device Type: iphone, ipod, android, pc, printer, tv...
        device_category (str | Unset): Device Category: loT, TV, computer, phone...
        os_name (str | Unset): Device system version.
        model (str | Unset): Model of client device.
        ip (str | Unset): IP Address.
        ipv_6_list (list[str] | Unset): IPv6 Address.
        connect_type (int | Unset): Connect type should be a value as follows: 0: wireless guest; 1: wireless user; 2:
            wired user.
        connect_dev_type (str | Unset): connect device type should be a value as follows: ap, switch, gateway.
        connected_to_wireless_router (bool | Unset): true: Client is connecting to a wireless router.
        wireless (bool | Unset): true: Wireless device (connectDevType=ap);  false: Not wireless
            device(connectDevType=switch or gateway).
        ssid (str | Unset): (Wireless)  SSID name.
        signal_level (int | Unset): (Wireless) Signal strength percentage should be within the range of 0-100.
        health_score (int | Unset): 1~3: poor; 4~7: fair; 0: no data; 8~10 good.
        signal_rank (int | Unset): (Wireless) Signal strength level should be within the range of 0-5.
        wifi_mode (int | Unset): (Wireless) Wifi mode should be a value as follows: 0: 11a; 1: 11b; 2: 11g; 3: 11na; 4:
            11ng; 5: 11ac; 6: 11axa; 7: 11axg; 8: 11beg; 9: 11bea.
        ap_name (str | Unset): (Wireless)  AP Name.
        ap_mac (str | Unset): (Wireless)  AP MAC Address.
        radio_id (int | Unset): (Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3:
            6GHz.
        channel (int | Unset): (Wireless)  Actual channel.
        rx_rate (int | Unset): (Wireless) Uplink negotiation rate (Kbit/s).
        tx_rate (int | Unset): (Wireless) Downlink negotiation rate (Kbit/s).
        power_save (bool | Unset): (Wireless)  true: Power save mode enabled.
        rssi (int | Unset): (Wireless) Signal strength, unit: dBm.
        snr (int | Unset): (Wireless) Signal Noise Ratio.
        switch_mac (str | Unset): (Wired, connectDevType=switch)  Switch MAC address.
        switch_name (str | Unset): (Wired, connectDevType=switch)  Switch name.
        support_locate (bool | Unset): Whether the client supports locate.True when the client is wired connected to a
            switch or stack that supports locate port.
        locate_enable (bool | Unset): Whether locate function is enabled
        gateway_mac (str | Unset): (Wired, connectDevType=gateway)  Gateway MAC Address.
        gateway_name (str | Unset): (Wired, connectDevType=gateway)  Gateway name.
        vid (int | Unset): (Wired) vlan.
        network_name (str | Unset): (Wired) Network name.
        dot_1_x_identity (str | Unset): (Wired) 802.1x authentication identity.
        dot_1_x_vlan (int | Unset): (Wired) Network name corresponding to the VLAN obtained by 802.1x D-VLAN.
        port (int | Unset): (Wired) Port ID.
        port_name (str | Unset): (Wired) Port name.
        lag_id (int | Unset): (Wired) LAG ID. Exists only when the client is connected to the LAG.
        switch_ports_in_lag (list[int] | Unset): Switch ports in Lag. Exists only when lagId exists and stackId is null
        st_ports_in_lag (list[str] | Unset): Standard switch ports in Lag. Exists only when lagId exists and stackId
            exists
        activity (int | Unset): Real-time downlink rate (Byte/s).
        upload_activity (int | Unset): Real-time uplink rate (Byte/s).
        traffic_down (int | Unset): Downstream traffic (Byte).
        traffic_up (int | Unset): Upstream traffic (Byte).
        uptime (int | Unset): Up time (unit: s).
        last_seen (int | Unset): Last found time, timestamp (ms).
        auth_status (int | Unset): Authentication status should be a value as follows: 0: CONNECTED // Access without
            any authentication method; 1: PENDING // Access to Portal, but authentication failed; 2: AUTHORIZED // Pass
            through portal, pass other authentication without portal; 3: AUTH-FREE // No portal authentication required.
        blocked (bool | Unset): Whether the client is blocked.
        guest (bool | Unset): (Wireless) Whether it is Guest (used to display the wireless Guest client icon).
        active (bool | Unset): Whether the client is online.
        manager (bool | Unset): Whether it is the client currently being managed.
        ip_setting (ClientIpSetting | Unset): Client IP setting.
        down_packet (int | Unset): Number of downstream packets.
        up_packet (int | Unset): Number of upstream packets.
        rate_limit (RateLimitSettingOfClient | Unset): RateLimit setting.
        client_lock_to_ap_setting (ClientLockToApSetting | Unset): Client lock to ap setting.
        support5g2 (bool | Unset): Whether the client is connecting under 5g2.
        multi_link (list[ClientMultifrequencyInfo] | Unset): (Wireless) Client multifrequency info list.
        unit (int | Unset): Unit ID.
        standard_port (str | Unset): Standard port.
        system_name (str | Unset): Device system name.
        description (str | Unset): Device description.
        capabilities (list[str] | Unset): One or more of the following values: Station、DOCSIS cable
            device、Telephone、Router、WLAN access point、Bridge、Repeater、other.
        block_disable (bool | Unset): Block client disabled, default value: false.
        dhcp_lease_time (int | Unset): DHCP lease time, unit seconds
        stackable_switch (bool | Unset): Whether the connected device is a stackable switch.
        stack_id (str | Unset): Stack Id
        stack_name (str | Unset): Stack name
        ppsk_profile_name (str | Unset): (Wireless)  SSID PPSK profile name
        incident_num (int | Unset): Number of anomaly incidents in the last 10 minutes.
        auth_info (list[AuthInfoOpenApiVO] | Unset): Client portal authentication information
    """

    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    host_name: str | Unset = UNSET
    vendor: str | Unset = UNSET
    device_type: str | Unset = UNSET
    device_category: str | Unset = UNSET
    os_name: str | Unset = UNSET
    model: str | Unset = UNSET
    ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    connect_type: int | Unset = UNSET
    connect_dev_type: str | Unset = UNSET
    connected_to_wireless_router: bool | Unset = UNSET
    wireless: bool | Unset = UNSET
    ssid: str | Unset = UNSET
    signal_level: int | Unset = UNSET
    health_score: int | Unset = UNSET
    signal_rank: int | Unset = UNSET
    wifi_mode: int | Unset = UNSET
    ap_name: str | Unset = UNSET
    ap_mac: str | Unset = UNSET
    radio_id: int | Unset = UNSET
    channel: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    power_save: bool | Unset = UNSET
    rssi: int | Unset = UNSET
    snr: int | Unset = UNSET
    switch_mac: str | Unset = UNSET
    switch_name: str | Unset = UNSET
    support_locate: bool | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    gateway_mac: str | Unset = UNSET
    gateway_name: str | Unset = UNSET
    vid: int | Unset = UNSET
    network_name: str | Unset = UNSET
    dot_1_x_identity: str | Unset = UNSET
    dot_1_x_vlan: int | Unset = UNSET
    port: int | Unset = UNSET
    port_name: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    switch_ports_in_lag: list[int] | Unset = UNSET
    st_ports_in_lag: list[str] | Unset = UNSET
    activity: int | Unset = UNSET
    upload_activity: int | Unset = UNSET
    traffic_down: int | Unset = UNSET
    traffic_up: int | Unset = UNSET
    uptime: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    auth_status: int | Unset = UNSET
    blocked: bool | Unset = UNSET
    guest: bool | Unset = UNSET
    active: bool | Unset = UNSET
    manager: bool | Unset = UNSET
    ip_setting: ClientIpSetting | Unset = UNSET
    down_packet: int | Unset = UNSET
    up_packet: int | Unset = UNSET
    rate_limit: RateLimitSettingOfClient | Unset = UNSET
    client_lock_to_ap_setting: ClientLockToApSetting | Unset = UNSET
    support5g2: bool | Unset = UNSET
    multi_link: list[ClientMultifrequencyInfo] | Unset = UNSET
    unit: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    system_name: str | Unset = UNSET
    description: str | Unset = UNSET
    capabilities: list[str] | Unset = UNSET
    block_disable: bool | Unset = UNSET
    dhcp_lease_time: int | Unset = UNSET
    stackable_switch: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    ppsk_profile_name: str | Unset = UNSET
    incident_num: int | Unset = UNSET
    auth_info: list[AuthInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac = self.mac

        name = self.name

        host_name = self.host_name

        vendor = self.vendor

        device_type = self.device_type

        device_category = self.device_category

        os_name = self.os_name

        model = self.model

        ip = self.ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        connect_type = self.connect_type

        connect_dev_type = self.connect_dev_type

        connected_to_wireless_router = self.connected_to_wireless_router

        wireless = self.wireless

        ssid = self.ssid

        signal_level = self.signal_level

        health_score = self.health_score

        signal_rank = self.signal_rank

        wifi_mode = self.wifi_mode

        ap_name = self.ap_name

        ap_mac = self.ap_mac

        radio_id = self.radio_id

        channel = self.channel

        rx_rate = self.rx_rate

        tx_rate = self.tx_rate

        power_save = self.power_save

        rssi = self.rssi

        snr = self.snr

        switch_mac = self.switch_mac

        switch_name = self.switch_name

        support_locate = self.support_locate

        locate_enable = self.locate_enable

        gateway_mac = self.gateway_mac

        gateway_name = self.gateway_name

        vid = self.vid

        network_name = self.network_name

        dot_1_x_identity = self.dot_1_x_identity

        dot_1_x_vlan = self.dot_1_x_vlan

        port = self.port

        port_name = self.port_name

        lag_id = self.lag_id

        switch_ports_in_lag: list[int] | Unset = UNSET
        if not isinstance(self.switch_ports_in_lag, Unset):
            switch_ports_in_lag = self.switch_ports_in_lag

        st_ports_in_lag: list[str] | Unset = UNSET
        if not isinstance(self.st_ports_in_lag, Unset):
            st_ports_in_lag = self.st_ports_in_lag

        activity = self.activity

        upload_activity = self.upload_activity

        traffic_down = self.traffic_down

        traffic_up = self.traffic_up

        uptime = self.uptime

        last_seen = self.last_seen

        auth_status = self.auth_status

        blocked = self.blocked

        guest = self.guest

        active = self.active

        manager = self.manager

        ip_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_setting, Unset):
            ip_setting = self.ip_setting.to_dict()

        down_packet = self.down_packet

        up_packet = self.up_packet

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        client_lock_to_ap_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_lock_to_ap_setting, Unset):
            client_lock_to_ap_setting = self.client_lock_to_ap_setting.to_dict()

        support5g2 = self.support5g2

        multi_link: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.multi_link, Unset):
            multi_link = []
            for multi_link_item_data in self.multi_link:
                multi_link_item = multi_link_item_data.to_dict()
                multi_link.append(multi_link_item)

        unit = self.unit

        standard_port = self.standard_port

        system_name = self.system_name

        description = self.description

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities

        block_disable = self.block_disable

        dhcp_lease_time = self.dhcp_lease_time

        stackable_switch = self.stackable_switch

        stack_id = self.stack_id

        stack_name = self.stack_name

        ppsk_profile_name = self.ppsk_profile_name

        incident_num = self.incident_num

        auth_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auth_info, Unset):
            auth_info = []
            for auth_info_item_data in self.auth_info:
                auth_info_item = auth_info_item_data.to_dict()
                auth_info.append(auth_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if device_category is not UNSET:
            field_dict["deviceCategory"] = device_category
        if os_name is not UNSET:
            field_dict["osName"] = os_name
        if model is not UNSET:
            field_dict["model"] = model
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if connect_type is not UNSET:
            field_dict["connectType"] = connect_type
        if connect_dev_type is not UNSET:
            field_dict["connectDevType"] = connect_dev_type
        if connected_to_wireless_router is not UNSET:
            field_dict["connectedToWirelessRouter"] = connected_to_wireless_router
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if signal_level is not UNSET:
            field_dict["signalLevel"] = signal_level
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if signal_rank is not UNSET:
            field_dict["signalRank"] = signal_rank
        if wifi_mode is not UNSET:
            field_dict["wifiMode"] = wifi_mode
        if ap_name is not UNSET:
            field_dict["apName"] = ap_name
        if ap_mac is not UNSET:
            field_dict["apMac"] = ap_mac
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if power_save is not UNSET:
            field_dict["powerSave"] = power_save
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr
        if switch_mac is not UNSET:
            field_dict["switchMac"] = switch_mac
        if switch_name is not UNSET:
            field_dict["switchName"] = switch_name
        if support_locate is not UNSET:
            field_dict["supportLocate"] = support_locate
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if gateway_mac is not UNSET:
            field_dict["gatewayMac"] = gateway_mac
        if gateway_name is not UNSET:
            field_dict["gatewayName"] = gateway_name
        if vid is not UNSET:
            field_dict["vid"] = vid
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if dot_1_x_identity is not UNSET:
            field_dict["dot1xIdentity"] = dot_1_x_identity
        if dot_1_x_vlan is not UNSET:
            field_dict["dot1xVlan"] = dot_1_x_vlan
        if port is not UNSET:
            field_dict["port"] = port
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if switch_ports_in_lag is not UNSET:
            field_dict["switchPortsInLag"] = switch_ports_in_lag
        if st_ports_in_lag is not UNSET:
            field_dict["stPortsInLag"] = st_ports_in_lag
        if activity is not UNSET:
            field_dict["activity"] = activity
        if upload_activity is not UNSET:
            field_dict["uploadActivity"] = upload_activity
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if guest is not UNSET:
            field_dict["guest"] = guest
        if active is not UNSET:
            field_dict["active"] = active
        if manager is not UNSET:
            field_dict["manager"] = manager
        if ip_setting is not UNSET:
            field_dict["ipSetting"] = ip_setting
        if down_packet is not UNSET:
            field_dict["downPacket"] = down_packet
        if up_packet is not UNSET:
            field_dict["upPacket"] = up_packet
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if client_lock_to_ap_setting is not UNSET:
            field_dict["clientLockToApSetting"] = client_lock_to_ap_setting
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if multi_link is not UNSET:
            field_dict["multiLink"] = multi_link
        if unit is not UNSET:
            field_dict["unit"] = unit
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if description is not UNSET:
            field_dict["description"] = description
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if block_disable is not UNSET:
            field_dict["blockDisable"] = block_disable
        if dhcp_lease_time is not UNSET:
            field_dict["dhcpLeaseTime"] = dhcp_lease_time
        if stackable_switch is not UNSET:
            field_dict["stackableSwitch"] = stackable_switch
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if ppsk_profile_name is not UNSET:
            field_dict["ppskProfileName"] = ppsk_profile_name
        if incident_num is not UNSET:
            field_dict["incidentNum"] = incident_num
        if auth_info is not UNSET:
            field_dict["authInfo"] = auth_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_info_open_api_vo import AuthInfoOpenApiVO
        from ..models.client_ip_setting import ClientIpSetting
        from ..models.client_lock_to_ap_setting import (
            ClientLockToApSetting,
        )
        from ..models.client_multifrequency_info import (
            ClientMultifrequencyInfo,
        )
        from ..models.rate_limit_setting_of_client import (
            RateLimitSettingOfClient,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        host_name = d.pop("hostName", UNSET)

        vendor = d.pop("vendor", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_category = d.pop("deviceCategory", UNSET)

        os_name = d.pop("osName", UNSET)

        model = d.pop("model", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        connect_type = d.pop("connectType", UNSET)

        connect_dev_type = d.pop("connectDevType", UNSET)

        connected_to_wireless_router = d.pop("connectedToWirelessRouter", UNSET)

        wireless = d.pop("wireless", UNSET)

        ssid = d.pop("ssid", UNSET)

        signal_level = d.pop("signalLevel", UNSET)

        health_score = d.pop("healthScore", UNSET)

        signal_rank = d.pop("signalRank", UNSET)

        wifi_mode = d.pop("wifiMode", UNSET)

        ap_name = d.pop("apName", UNSET)

        ap_mac = d.pop("apMac", UNSET)

        radio_id = d.pop("radioId", UNSET)

        channel = d.pop("channel", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        power_save = d.pop("powerSave", UNSET)

        rssi = d.pop("rssi", UNSET)

        snr = d.pop("snr", UNSET)

        switch_mac = d.pop("switchMac", UNSET)

        switch_name = d.pop("switchName", UNSET)

        support_locate = d.pop("supportLocate", UNSET)

        locate_enable = d.pop("locateEnable", UNSET)

        gateway_mac = d.pop("gatewayMac", UNSET)

        gateway_name = d.pop("gatewayName", UNSET)

        vid = d.pop("vid", UNSET)

        network_name = d.pop("networkName", UNSET)

        dot_1_x_identity = d.pop("dot1xIdentity", UNSET)

        dot_1_x_vlan = d.pop("dot1xVlan", UNSET)

        port = d.pop("port", UNSET)

        port_name = d.pop("portName", UNSET)

        lag_id = d.pop("lagId", UNSET)

        switch_ports_in_lag = cast(list[int], d.pop("switchPortsInLag", UNSET))

        st_ports_in_lag = cast(list[str], d.pop("stPortsInLag", UNSET))

        activity = d.pop("activity", UNSET)

        upload_activity = d.pop("uploadActivity", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        uptime = d.pop("uptime", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        auth_status = d.pop("authStatus", UNSET)

        blocked = d.pop("blocked", UNSET)

        guest = d.pop("guest", UNSET)

        active = d.pop("active", UNSET)

        manager = d.pop("manager", UNSET)

        _ip_setting = d.pop("ipSetting", UNSET)
        ip_setting: ClientIpSetting | Unset
        if isinstance(_ip_setting, Unset):
            ip_setting = UNSET
        else:
            ip_setting = ClientIpSetting.from_dict(_ip_setting)

        down_packet = d.pop("downPacket", UNSET)

        up_packet = d.pop("upPacket", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: RateLimitSettingOfClient | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = RateLimitSettingOfClient.from_dict(_rate_limit)

        _client_lock_to_ap_setting = d.pop("clientLockToApSetting", UNSET)
        client_lock_to_ap_setting: ClientLockToApSetting | Unset
        if isinstance(_client_lock_to_ap_setting, Unset):
            client_lock_to_ap_setting = UNSET
        else:
            client_lock_to_ap_setting = ClientLockToApSetting.from_dict(
                _client_lock_to_ap_setting
            )

        support5g2 = d.pop("support5g2", UNSET)

        _multi_link = d.pop("multiLink", UNSET)
        multi_link: list[ClientMultifrequencyInfo] | Unset = UNSET
        if _multi_link is not UNSET:
            multi_link = []
            for multi_link_item_data in _multi_link:
                multi_link_item = ClientMultifrequencyInfo.from_dict(
                    multi_link_item_data
                )

                multi_link.append(multi_link_item)

        unit = d.pop("unit", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        system_name = d.pop("systemName", UNSET)

        description = d.pop("description", UNSET)

        capabilities = cast(list[str], d.pop("capabilities", UNSET))

        block_disable = d.pop("blockDisable", UNSET)

        dhcp_lease_time = d.pop("dhcpLeaseTime", UNSET)

        stackable_switch = d.pop("stackableSwitch", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        ppsk_profile_name = d.pop("ppskProfileName", UNSET)

        incident_num = d.pop("incidentNum", UNSET)

        _auth_info = d.pop("authInfo", UNSET)
        auth_info: list[AuthInfoOpenApiVO] | Unset = UNSET
        if _auth_info is not UNSET:
            auth_info = []
            for auth_info_item_data in _auth_info:
                auth_info_item = AuthInfoOpenApiVO.from_dict(auth_info_item_data)

                auth_info.append(auth_info_item)

        open_api_client_info = cls(
            id=id,
            mac=mac,
            name=name,
            host_name=host_name,
            vendor=vendor,
            device_type=device_type,
            device_category=device_category,
            os_name=os_name,
            model=model,
            ip=ip,
            ipv_6_list=ipv_6_list,
            connect_type=connect_type,
            connect_dev_type=connect_dev_type,
            connected_to_wireless_router=connected_to_wireless_router,
            wireless=wireless,
            ssid=ssid,
            signal_level=signal_level,
            health_score=health_score,
            signal_rank=signal_rank,
            wifi_mode=wifi_mode,
            ap_name=ap_name,
            ap_mac=ap_mac,
            radio_id=radio_id,
            channel=channel,
            rx_rate=rx_rate,
            tx_rate=tx_rate,
            power_save=power_save,
            rssi=rssi,
            snr=snr,
            switch_mac=switch_mac,
            switch_name=switch_name,
            support_locate=support_locate,
            locate_enable=locate_enable,
            gateway_mac=gateway_mac,
            gateway_name=gateway_name,
            vid=vid,
            network_name=network_name,
            dot_1_x_identity=dot_1_x_identity,
            dot_1_x_vlan=dot_1_x_vlan,
            port=port,
            port_name=port_name,
            lag_id=lag_id,
            switch_ports_in_lag=switch_ports_in_lag,
            st_ports_in_lag=st_ports_in_lag,
            activity=activity,
            upload_activity=upload_activity,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            uptime=uptime,
            last_seen=last_seen,
            auth_status=auth_status,
            blocked=blocked,
            guest=guest,
            active=active,
            manager=manager,
            ip_setting=ip_setting,
            down_packet=down_packet,
            up_packet=up_packet,
            rate_limit=rate_limit,
            client_lock_to_ap_setting=client_lock_to_ap_setting,
            support5g2=support5g2,
            multi_link=multi_link,
            unit=unit,
            standard_port=standard_port,
            system_name=system_name,
            description=description,
            capabilities=capabilities,
            block_disable=block_disable,
            dhcp_lease_time=dhcp_lease_time,
            stackable_switch=stackable_switch,
            stack_id=stack_id,
            stack_name=stack_name,
            ppsk_profile_name=ppsk_profile_name,
            incident_num=incident_num,
            auth_info=auth_info,
        )

        open_api_client_info.additional_properties = d
        return open_api_client_info

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
