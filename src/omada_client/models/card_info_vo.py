from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_summary_trend_vo import AlertSummaryTrendVO
    from ..models.ap_utilization_vo import ApUtilizationVO
    from ..models.app_category_traffics_vo import AppCategoryTrafficsVO
    from ..models.client_association_activities import ClientAssociationActivities
    from ..models.client_connection_trend import ClientConnectionTrend
    from ..models.client_health_trend_vo import ClientHealthTrendVO
    from ..models.client_statistics_overview import ClientStatisticsOverview
    from ..models.client_traffic_info import ClientTrafficInfo
    from ..models.clients_with_on_boarding_times import ClientsWithOnBoardingTimes
    from ..models.data_rate_distribution_vo import DataRateDistributionVO
    from ..models.device_health_vo import DeviceHealthVO
    from ..models.gateway_summary_vo import GatewaySummaryVO
    from ..models.isp_load_vo import IspLoadVO
    from ..models.network_activity_vo import NetworkActivityVO
    from ..models.network_vo import NetworkVO
    from ..models.online_offline_vo import OnlineOfflineVO
    from ..models.over_view_summary_vo import OverViewSummaryVO
    from ..models.poe_power_trend_vo import PoePowerTrendVO
    from ..models.rssi_distribution_vo import RssiDistributionVO
    from ..models.snr_distribution_vo import SnrDistributionVO
    from ..models.switch_alert_reboot_vo import SwitchAlertRebootVO
    from ..models.switch_utilization_vo import SwitchUtilizationVO
    from ..models.top_ap_by_conn_failure_vo import TopApByConnFailureVO
    from ..models.top_ap_by_interference_vo import TopApByInterferenceVO
    from ..models.top_ap_by_rt_drop_vo import TopApByRtDropVO
    from ..models.top_ap_by_traffic_and_client_vo import TopApByTrafficAndClientVO
    from ..models.top_application_by_traffic_vo import TopApplicationByTrafficVO
    from ..models.top_ssid_traffic_vo import TopSsidTrafficVO
    from ..models.top_switch_by_packet_vo import TopSwitchByPacketVO
    from ..models.top_switch_vo import TopSwitchVO
    from ..models.top_traffic_and_uptime_clients import TopTrafficAndUptimeClients
    from ..models.traffic_distribution_vo import TrafficDistributionVO
    from ..models.traffic_summary_vo import TrafficSummaryVO
    from ..models.wan_health_trend_vo import WanHealthTrendVO
    from ..models.wifi_health_vo import WifiHealthVO
    from ..models.wireless_traffic_single_vo import WirelessTrafficSingleVO
    from ..models.wireless_traffic_vo import WirelessTrafficVO


T = TypeVar("T", bound="CardInfoVO")


@_attrs_define
class CardInfoVO:
    """
    Attributes:
        overview_summary (OverViewSummaryVO | Unset):
        traffic_summary (TrafficSummaryVO | Unset):
        traffic_distribution (TrafficDistributionVO | Unset):
        alert_summary (AlertSummaryTrendVO | Unset):
        device_status (list[OnlineOfflineVO] | Unset):
        device_health_trend (list[DeviceHealthVO] | Unset):
        network (NetworkVO | Unset): The collection of snooping network ids related to this multicast snooping config.
        gateway_summary (GatewaySummaryVO | Unset): Gateway summary
        isp_load (list[IspLoadVO] | Unset): ISP Load
        switch_alert_reboot (SwitchAlertRebootVO | Unset):
        top_switch_by_traffic_and_poe_power (TopSwitchVO | Unset):
        top_switch_cpu_memory (SwitchUtilizationVO | Unset):
        poe_power_trend (list[PoePowerTrendVO] | Unset):
        switch_status (list[OnlineOfflineVO] | Unset):
        switch_health_trend (list[DeviceHealthVO] | Unset):
        wan_health_trend (list[WanHealthTrendVO] | Unset):
        wireless_traffic (WirelessTrafficVO | Unset):
        wifi_health (WifiHealthVO | Unset):
        top_ap_by_traffic_and_client (TopApByTrafficAndClientVO | Unset):
        top_ap_by_cpu_and_memory (ApUtilizationVO | Unset):
        top_ap_by_interference (TopApByInterferenceVO | Unset):
        top_ap_by_rt_and_drop (TopApByRtDropVO | Unset):
        top_ssid_by_traffic (list[TopSsidTrafficVO] | Unset):
        ap_status (list[OnlineOfflineVO] | Unset):
        wireless_traffic_single (WirelessTrafficSingleVO | Unset):
        ap_health (list[DeviceHealthVO] | Unset):
        client_traffic (ClientTrafficInfo | Unset): Client traffic info.
        client_connection_trend (ClientConnectionTrend | Unset): Client connection trend.
        clients_overview (ClientStatisticsOverview | Unset): Client statistics overview.
        clients_association_activities (list[ClientAssociationActivities] | Unset): Clients association activities with
            time.
        clients_with_onboarding_times (ClientsWithOnBoardingTimes | Unset): Client distribution with association times.
        top_client (TopTrafficAndUptimeClients | Unset): Top traffic and uptime clients.
        app_categories (AppCategoryTrafficsVO | Unset):
        top_application_by_traffic (list[TopApplicationByTrafficVO] | Unset):
        internet (NetworkActivityVO | Unset):
        client_health_trend (list[ClientHealthTrendVO] | Unset):
        clients_rssi (list[RssiDistributionVO] | Unset): Clients RSSI distribution trend
        clients_snr (list[SnrDistributionVO] | Unset): Clients SNR distribution trend
        clients_data_rate (list[DataRateDistributionVO] | Unset): Clients data rate distribution trend
        top_ap_by_conn_failure (TopApByConnFailureVO | Unset): Top AP by connection failure
        top_switch_by_packet (TopSwitchByPacketVO | Unset): Top switch by packet loss and error
    """

    overview_summary: OverViewSummaryVO | Unset = UNSET
    traffic_summary: TrafficSummaryVO | Unset = UNSET
    traffic_distribution: TrafficDistributionVO | Unset = UNSET
    alert_summary: AlertSummaryTrendVO | Unset = UNSET
    device_status: list[OnlineOfflineVO] | Unset = UNSET
    device_health_trend: list[DeviceHealthVO] | Unset = UNSET
    network: NetworkVO | Unset = UNSET
    gateway_summary: GatewaySummaryVO | Unset = UNSET
    isp_load: list[IspLoadVO] | Unset = UNSET
    switch_alert_reboot: SwitchAlertRebootVO | Unset = UNSET
    top_switch_by_traffic_and_poe_power: TopSwitchVO | Unset = UNSET
    top_switch_cpu_memory: SwitchUtilizationVO | Unset = UNSET
    poe_power_trend: list[PoePowerTrendVO] | Unset = UNSET
    switch_status: list[OnlineOfflineVO] | Unset = UNSET
    switch_health_trend: list[DeviceHealthVO] | Unset = UNSET
    wan_health_trend: list[WanHealthTrendVO] | Unset = UNSET
    wireless_traffic: WirelessTrafficVO | Unset = UNSET
    wifi_health: WifiHealthVO | Unset = UNSET
    top_ap_by_traffic_and_client: TopApByTrafficAndClientVO | Unset = UNSET
    top_ap_by_cpu_and_memory: ApUtilizationVO | Unset = UNSET
    top_ap_by_interference: TopApByInterferenceVO | Unset = UNSET
    top_ap_by_rt_and_drop: TopApByRtDropVO | Unset = UNSET
    top_ssid_by_traffic: list[TopSsidTrafficVO] | Unset = UNSET
    ap_status: list[OnlineOfflineVO] | Unset = UNSET
    wireless_traffic_single: WirelessTrafficSingleVO | Unset = UNSET
    ap_health: list[DeviceHealthVO] | Unset = UNSET
    client_traffic: ClientTrafficInfo | Unset = UNSET
    client_connection_trend: ClientConnectionTrend | Unset = UNSET
    clients_overview: ClientStatisticsOverview | Unset = UNSET
    clients_association_activities: list[ClientAssociationActivities] | Unset = UNSET
    clients_with_onboarding_times: ClientsWithOnBoardingTimes | Unset = UNSET
    top_client: TopTrafficAndUptimeClients | Unset = UNSET
    app_categories: AppCategoryTrafficsVO | Unset = UNSET
    top_application_by_traffic: list[TopApplicationByTrafficVO] | Unset = UNSET
    internet: NetworkActivityVO | Unset = UNSET
    client_health_trend: list[ClientHealthTrendVO] | Unset = UNSET
    clients_rssi: list[RssiDistributionVO] | Unset = UNSET
    clients_snr: list[SnrDistributionVO] | Unset = UNSET
    clients_data_rate: list[DataRateDistributionVO] | Unset = UNSET
    top_ap_by_conn_failure: TopApByConnFailureVO | Unset = UNSET
    top_switch_by_packet: TopSwitchByPacketVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overview_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overview_summary, Unset):
            overview_summary = self.overview_summary.to_dict()

        traffic_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic_summary, Unset):
            traffic_summary = self.traffic_summary.to_dict()

        traffic_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic_distribution, Unset):
            traffic_distribution = self.traffic_distribution.to_dict()

        alert_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_summary, Unset):
            alert_summary = self.alert_summary.to_dict()

        device_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_status, Unset):
            device_status = []
            for device_status_item_data in self.device_status:
                device_status_item = device_status_item_data.to_dict()
                device_status.append(device_status_item)

        device_health_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_health_trend, Unset):
            device_health_trend = []
            for device_health_trend_item_data in self.device_health_trend:
                device_health_trend_item = device_health_trend_item_data.to_dict()
                device_health_trend.append(device_health_trend_item)

        network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network.to_dict()

        gateway_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_summary, Unset):
            gateway_summary = self.gateway_summary.to_dict()

        isp_load: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.isp_load, Unset):
            isp_load = []
            for isp_load_item_data in self.isp_load:
                isp_load_item = isp_load_item_data.to_dict()
                isp_load.append(isp_load_item)

        switch_alert_reboot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_alert_reboot, Unset):
            switch_alert_reboot = self.switch_alert_reboot.to_dict()

        top_switch_by_traffic_and_poe_power: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_switch_by_traffic_and_poe_power, Unset):
            top_switch_by_traffic_and_poe_power = (
                self.top_switch_by_traffic_and_poe_power.to_dict()
            )

        top_switch_cpu_memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_switch_cpu_memory, Unset):
            top_switch_cpu_memory = self.top_switch_cpu_memory.to_dict()

        poe_power_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.poe_power_trend, Unset):
            poe_power_trend = []
            for poe_power_trend_item_data in self.poe_power_trend:
                poe_power_trend_item = poe_power_trend_item_data.to_dict()
                poe_power_trend.append(poe_power_trend_item)

        switch_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switch_status, Unset):
            switch_status = []
            for switch_status_item_data in self.switch_status:
                switch_status_item = switch_status_item_data.to_dict()
                switch_status.append(switch_status_item)

        switch_health_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switch_health_trend, Unset):
            switch_health_trend = []
            for switch_health_trend_item_data in self.switch_health_trend:
                switch_health_trend_item = switch_health_trend_item_data.to_dict()
                switch_health_trend.append(switch_health_trend_item)

        wan_health_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_health_trend, Unset):
            wan_health_trend = []
            for wan_health_trend_item_data in self.wan_health_trend:
                wan_health_trend_item = wan_health_trend_item_data.to_dict()
                wan_health_trend.append(wan_health_trend_item)

        wireless_traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_traffic, Unset):
            wireless_traffic = self.wireless_traffic.to_dict()

        wifi_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wifi_health, Unset):
            wifi_health = self.wifi_health.to_dict()

        top_ap_by_traffic_and_client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_ap_by_traffic_and_client, Unset):
            top_ap_by_traffic_and_client = self.top_ap_by_traffic_and_client.to_dict()

        top_ap_by_cpu_and_memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_ap_by_cpu_and_memory, Unset):
            top_ap_by_cpu_and_memory = self.top_ap_by_cpu_and_memory.to_dict()

        top_ap_by_interference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_ap_by_interference, Unset):
            top_ap_by_interference = self.top_ap_by_interference.to_dict()

        top_ap_by_rt_and_drop: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_ap_by_rt_and_drop, Unset):
            top_ap_by_rt_and_drop = self.top_ap_by_rt_and_drop.to_dict()

        top_ssid_by_traffic: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ssid_by_traffic, Unset):
            top_ssid_by_traffic = []
            for top_ssid_by_traffic_item_data in self.top_ssid_by_traffic:
                top_ssid_by_traffic_item = top_ssid_by_traffic_item_data.to_dict()
                top_ssid_by_traffic.append(top_ssid_by_traffic_item)

        ap_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ap_status, Unset):
            ap_status = []
            for ap_status_item_data in self.ap_status:
                ap_status_item = ap_status_item_data.to_dict()
                ap_status.append(ap_status_item)

        wireless_traffic_single: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_traffic_single, Unset):
            wireless_traffic_single = self.wireless_traffic_single.to_dict()

        ap_health: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ap_health, Unset):
            ap_health = []
            for ap_health_item_data in self.ap_health:
                ap_health_item = ap_health_item_data.to_dict()
                ap_health.append(ap_health_item)

        client_traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_traffic, Unset):
            client_traffic = self.client_traffic.to_dict()

        client_connection_trend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_connection_trend, Unset):
            client_connection_trend = self.client_connection_trend.to_dict()

        clients_overview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clients_overview, Unset):
            clients_overview = self.clients_overview.to_dict()

        clients_association_activities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients_association_activities, Unset):
            clients_association_activities = []
            for (
                clients_association_activities_item_data
            ) in self.clients_association_activities:
                clients_association_activities_item = (
                    clients_association_activities_item_data.to_dict()
                )
                clients_association_activities.append(
                    clients_association_activities_item
                )

        clients_with_onboarding_times: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clients_with_onboarding_times, Unset):
            clients_with_onboarding_times = self.clients_with_onboarding_times.to_dict()

        top_client: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_client, Unset):
            top_client = self.top_client.to_dict()

        app_categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app_categories, Unset):
            app_categories = self.app_categories.to_dict()

        top_application_by_traffic: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_application_by_traffic, Unset):
            top_application_by_traffic = []
            for top_application_by_traffic_item_data in self.top_application_by_traffic:
                top_application_by_traffic_item = (
                    top_application_by_traffic_item_data.to_dict()
                )
                top_application_by_traffic.append(top_application_by_traffic_item)

        internet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internet, Unset):
            internet = self.internet.to_dict()

        client_health_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_health_trend, Unset):
            client_health_trend = []
            for client_health_trend_item_data in self.client_health_trend:
                client_health_trend_item = client_health_trend_item_data.to_dict()
                client_health_trend.append(client_health_trend_item)

        clients_rssi: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients_rssi, Unset):
            clients_rssi = []
            for clients_rssi_item_data in self.clients_rssi:
                clients_rssi_item = clients_rssi_item_data.to_dict()
                clients_rssi.append(clients_rssi_item)

        clients_snr: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients_snr, Unset):
            clients_snr = []
            for clients_snr_item_data in self.clients_snr:
                clients_snr_item = clients_snr_item_data.to_dict()
                clients_snr.append(clients_snr_item)

        clients_data_rate: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients_data_rate, Unset):
            clients_data_rate = []
            for clients_data_rate_item_data in self.clients_data_rate:
                clients_data_rate_item = clients_data_rate_item_data.to_dict()
                clients_data_rate.append(clients_data_rate_item)

        top_ap_by_conn_failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_ap_by_conn_failure, Unset):
            top_ap_by_conn_failure = self.top_ap_by_conn_failure.to_dict()

        top_switch_by_packet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_switch_by_packet, Unset):
            top_switch_by_packet = self.top_switch_by_packet.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overview_summary is not UNSET:
            field_dict["overviewSummary"] = overview_summary
        if traffic_summary is not UNSET:
            field_dict["trafficSummary"] = traffic_summary
        if traffic_distribution is not UNSET:
            field_dict["trafficDistribution"] = traffic_distribution
        if alert_summary is not UNSET:
            field_dict["alertSummary"] = alert_summary
        if device_status is not UNSET:
            field_dict["deviceStatus"] = device_status
        if device_health_trend is not UNSET:
            field_dict["deviceHealthTrend"] = device_health_trend
        if network is not UNSET:
            field_dict["network"] = network
        if gateway_summary is not UNSET:
            field_dict["gatewaySummary"] = gateway_summary
        if isp_load is not UNSET:
            field_dict["ispLoad"] = isp_load
        if switch_alert_reboot is not UNSET:
            field_dict["switchAlertReboot"] = switch_alert_reboot
        if top_switch_by_traffic_and_poe_power is not UNSET:
            field_dict["topSwitchByTrafficAndPoePower"] = (
                top_switch_by_traffic_and_poe_power
            )
        if top_switch_cpu_memory is not UNSET:
            field_dict["topSwitchCpuMemory"] = top_switch_cpu_memory
        if poe_power_trend is not UNSET:
            field_dict["poePowerTrend"] = poe_power_trend
        if switch_status is not UNSET:
            field_dict["switchStatus"] = switch_status
        if switch_health_trend is not UNSET:
            field_dict["switchHealthTrend"] = switch_health_trend
        if wan_health_trend is not UNSET:
            field_dict["wanHealthTrend"] = wan_health_trend
        if wireless_traffic is not UNSET:
            field_dict["wirelessTraffic"] = wireless_traffic
        if wifi_health is not UNSET:
            field_dict["wifiHealth"] = wifi_health
        if top_ap_by_traffic_and_client is not UNSET:
            field_dict["topApByTrafficAndClient"] = top_ap_by_traffic_and_client
        if top_ap_by_cpu_and_memory is not UNSET:
            field_dict["topApByCpuAndMemory"] = top_ap_by_cpu_and_memory
        if top_ap_by_interference is not UNSET:
            field_dict["topApByInterference"] = top_ap_by_interference
        if top_ap_by_rt_and_drop is not UNSET:
            field_dict["topApByRtAndDrop"] = top_ap_by_rt_and_drop
        if top_ssid_by_traffic is not UNSET:
            field_dict["topSsidByTraffic"] = top_ssid_by_traffic
        if ap_status is not UNSET:
            field_dict["apStatus"] = ap_status
        if wireless_traffic_single is not UNSET:
            field_dict["wirelessTrafficSingle"] = wireless_traffic_single
        if ap_health is not UNSET:
            field_dict["apHealth"] = ap_health
        if client_traffic is not UNSET:
            field_dict["clientTraffic"] = client_traffic
        if client_connection_trend is not UNSET:
            field_dict["clientConnectionTrend"] = client_connection_trend
        if clients_overview is not UNSET:
            field_dict["clientsOverview"] = clients_overview
        if clients_association_activities is not UNSET:
            field_dict["clientsAssociationActivities"] = clients_association_activities
        if clients_with_onboarding_times is not UNSET:
            field_dict["clientsWithOnboardingTimes"] = clients_with_onboarding_times
        if top_client is not UNSET:
            field_dict["topClient"] = top_client
        if app_categories is not UNSET:
            field_dict["appCategories"] = app_categories
        if top_application_by_traffic is not UNSET:
            field_dict["topApplicationByTraffic"] = top_application_by_traffic
        if internet is not UNSET:
            field_dict["internet"] = internet
        if client_health_trend is not UNSET:
            field_dict["clientHealthTrend"] = client_health_trend
        if clients_rssi is not UNSET:
            field_dict["clientsRssi"] = clients_rssi
        if clients_snr is not UNSET:
            field_dict["clientsSnr"] = clients_snr
        if clients_data_rate is not UNSET:
            field_dict["clientsDataRate"] = clients_data_rate
        if top_ap_by_conn_failure is not UNSET:
            field_dict["topApByConnFailure"] = top_ap_by_conn_failure
        if top_switch_by_packet is not UNSET:
            field_dict["topSwitchByPacket"] = top_switch_by_packet

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_summary_trend_vo import AlertSummaryTrendVO
        from ..models.ap_utilization_vo import ApUtilizationVO
        from ..models.app_category_traffics_vo import (
            AppCategoryTrafficsVO,
        )
        from ..models.client_association_activities import (
            ClientAssociationActivities,
        )
        from ..models.client_connection_trend import (
            ClientConnectionTrend,
        )
        from ..models.client_health_trend_vo import ClientHealthTrendVO
        from ..models.client_statistics_overview import (
            ClientStatisticsOverview,
        )
        from ..models.client_traffic_info import ClientTrafficInfo
        from ..models.clients_with_on_boarding_times import (
            ClientsWithOnBoardingTimes,
        )
        from ..models.data_rate_distribution_vo import (
            DataRateDistributionVO,
        )
        from ..models.device_health_vo import DeviceHealthVO
        from ..models.gateway_summary_vo import GatewaySummaryVO
        from ..models.isp_load_vo import IspLoadVO
        from ..models.network_activity_vo import NetworkActivityVO
        from ..models.network_vo import NetworkVO
        from ..models.online_offline_vo import OnlineOfflineVO
        from ..models.over_view_summary_vo import OverViewSummaryVO
        from ..models.poe_power_trend_vo import PoePowerTrendVO
        from ..models.rssi_distribution_vo import RssiDistributionVO
        from ..models.snr_distribution_vo import SnrDistributionVO
        from ..models.switch_alert_reboot_vo import SwitchAlertRebootVO
        from ..models.switch_utilization_vo import SwitchUtilizationVO
        from ..models.top_ap_by_conn_failure_vo import (
            TopApByConnFailureVO,
        )
        from ..models.top_ap_by_interference_vo import (
            TopApByInterferenceVO,
        )
        from ..models.top_ap_by_rt_drop_vo import TopApByRtDropVO
        from ..models.top_ap_by_traffic_and_client_vo import (
            TopApByTrafficAndClientVO,
        )
        from ..models.top_application_by_traffic_vo import (
            TopApplicationByTrafficVO,
        )
        from ..models.top_ssid_traffic_vo import TopSsidTrafficVO
        from ..models.top_switch_by_packet_vo import (
            TopSwitchByPacketVO,
        )
        from ..models.top_switch_vo import TopSwitchVO
        from ..models.top_traffic_and_uptime_clients import (
            TopTrafficAndUptimeClients,
        )
        from ..models.traffic_distribution_vo import (
            TrafficDistributionVO,
        )
        from ..models.traffic_summary_vo import TrafficSummaryVO
        from ..models.wan_health_trend_vo import WanHealthTrendVO
        from ..models.wifi_health_vo import WifiHealthVO
        from ..models.wireless_traffic_single_vo import (
            WirelessTrafficSingleVO,
        )
        from ..models.wireless_traffic_vo import WirelessTrafficVO

        d = dict(src_dict)
        _overview_summary = d.pop("overviewSummary", UNSET)
        overview_summary: OverViewSummaryVO | Unset
        if isinstance(_overview_summary, Unset):
            overview_summary = UNSET
        else:
            overview_summary = OverViewSummaryVO.from_dict(_overview_summary)

        _traffic_summary = d.pop("trafficSummary", UNSET)
        traffic_summary: TrafficSummaryVO | Unset
        if isinstance(_traffic_summary, Unset):
            traffic_summary = UNSET
        else:
            traffic_summary = TrafficSummaryVO.from_dict(_traffic_summary)

        _traffic_distribution = d.pop("trafficDistribution", UNSET)
        traffic_distribution: TrafficDistributionVO | Unset
        if isinstance(_traffic_distribution, Unset):
            traffic_distribution = UNSET
        else:
            traffic_distribution = TrafficDistributionVO.from_dict(
                _traffic_distribution
            )

        _alert_summary = d.pop("alertSummary", UNSET)
        alert_summary: AlertSummaryTrendVO | Unset
        if isinstance(_alert_summary, Unset):
            alert_summary = UNSET
        else:
            alert_summary = AlertSummaryTrendVO.from_dict(_alert_summary)

        _device_status = d.pop("deviceStatus", UNSET)
        device_status: list[OnlineOfflineVO] | Unset = UNSET
        if _device_status is not UNSET:
            device_status = []
            for device_status_item_data in _device_status:
                device_status_item = OnlineOfflineVO.from_dict(device_status_item_data)

                device_status.append(device_status_item)

        _device_health_trend = d.pop("deviceHealthTrend", UNSET)
        device_health_trend: list[DeviceHealthVO] | Unset = UNSET
        if _device_health_trend is not UNSET:
            device_health_trend = []
            for device_health_trend_item_data in _device_health_trend:
                device_health_trend_item = DeviceHealthVO.from_dict(
                    device_health_trend_item_data
                )

                device_health_trend.append(device_health_trend_item)

        _network = d.pop("network", UNSET)
        network: NetworkVO | Unset
        if isinstance(_network, Unset):
            network = UNSET
        else:
            network = NetworkVO.from_dict(_network)

        _gateway_summary = d.pop("gatewaySummary", UNSET)
        gateway_summary: GatewaySummaryVO | Unset
        if isinstance(_gateway_summary, Unset):
            gateway_summary = UNSET
        else:
            gateway_summary = GatewaySummaryVO.from_dict(_gateway_summary)

        _isp_load = d.pop("ispLoad", UNSET)
        isp_load: list[IspLoadVO] | Unset = UNSET
        if _isp_load is not UNSET:
            isp_load = []
            for isp_load_item_data in _isp_load:
                isp_load_item = IspLoadVO.from_dict(isp_load_item_data)

                isp_load.append(isp_load_item)

        _switch_alert_reboot = d.pop("switchAlertReboot", UNSET)
        switch_alert_reboot: SwitchAlertRebootVO | Unset
        if isinstance(_switch_alert_reboot, Unset):
            switch_alert_reboot = UNSET
        else:
            switch_alert_reboot = SwitchAlertRebootVO.from_dict(_switch_alert_reboot)

        _top_switch_by_traffic_and_poe_power = d.pop(
            "topSwitchByTrafficAndPoePower", UNSET
        )
        top_switch_by_traffic_and_poe_power: TopSwitchVO | Unset
        if isinstance(_top_switch_by_traffic_and_poe_power, Unset):
            top_switch_by_traffic_and_poe_power = UNSET
        else:
            top_switch_by_traffic_and_poe_power = TopSwitchVO.from_dict(
                _top_switch_by_traffic_and_poe_power
            )

        _top_switch_cpu_memory = d.pop("topSwitchCpuMemory", UNSET)
        top_switch_cpu_memory: SwitchUtilizationVO | Unset
        if isinstance(_top_switch_cpu_memory, Unset):
            top_switch_cpu_memory = UNSET
        else:
            top_switch_cpu_memory = SwitchUtilizationVO.from_dict(
                _top_switch_cpu_memory
            )

        _poe_power_trend = d.pop("poePowerTrend", UNSET)
        poe_power_trend: list[PoePowerTrendVO] | Unset = UNSET
        if _poe_power_trend is not UNSET:
            poe_power_trend = []
            for poe_power_trend_item_data in _poe_power_trend:
                poe_power_trend_item = PoePowerTrendVO.from_dict(
                    poe_power_trend_item_data
                )

                poe_power_trend.append(poe_power_trend_item)

        _switch_status = d.pop("switchStatus", UNSET)
        switch_status: list[OnlineOfflineVO] | Unset = UNSET
        if _switch_status is not UNSET:
            switch_status = []
            for switch_status_item_data in _switch_status:
                switch_status_item = OnlineOfflineVO.from_dict(switch_status_item_data)

                switch_status.append(switch_status_item)

        _switch_health_trend = d.pop("switchHealthTrend", UNSET)
        switch_health_trend: list[DeviceHealthVO] | Unset = UNSET
        if _switch_health_trend is not UNSET:
            switch_health_trend = []
            for switch_health_trend_item_data in _switch_health_trend:
                switch_health_trend_item = DeviceHealthVO.from_dict(
                    switch_health_trend_item_data
                )

                switch_health_trend.append(switch_health_trend_item)

        _wan_health_trend = d.pop("wanHealthTrend", UNSET)
        wan_health_trend: list[WanHealthTrendVO] | Unset = UNSET
        if _wan_health_trend is not UNSET:
            wan_health_trend = []
            for wan_health_trend_item_data in _wan_health_trend:
                wan_health_trend_item = WanHealthTrendVO.from_dict(
                    wan_health_trend_item_data
                )

                wan_health_trend.append(wan_health_trend_item)

        _wireless_traffic = d.pop("wirelessTraffic", UNSET)
        wireless_traffic: WirelessTrafficVO | Unset
        if isinstance(_wireless_traffic, Unset):
            wireless_traffic = UNSET
        else:
            wireless_traffic = WirelessTrafficVO.from_dict(_wireless_traffic)

        _wifi_health = d.pop("wifiHealth", UNSET)
        wifi_health: WifiHealthVO | Unset
        if isinstance(_wifi_health, Unset):
            wifi_health = UNSET
        else:
            wifi_health = WifiHealthVO.from_dict(_wifi_health)

        _top_ap_by_traffic_and_client = d.pop("topApByTrafficAndClient", UNSET)
        top_ap_by_traffic_and_client: TopApByTrafficAndClientVO | Unset
        if isinstance(_top_ap_by_traffic_and_client, Unset):
            top_ap_by_traffic_and_client = UNSET
        else:
            top_ap_by_traffic_and_client = TopApByTrafficAndClientVO.from_dict(
                _top_ap_by_traffic_and_client
            )

        _top_ap_by_cpu_and_memory = d.pop("topApByCpuAndMemory", UNSET)
        top_ap_by_cpu_and_memory: ApUtilizationVO | Unset
        if isinstance(_top_ap_by_cpu_and_memory, Unset):
            top_ap_by_cpu_and_memory = UNSET
        else:
            top_ap_by_cpu_and_memory = ApUtilizationVO.from_dict(
                _top_ap_by_cpu_and_memory
            )

        _top_ap_by_interference = d.pop("topApByInterference", UNSET)
        top_ap_by_interference: TopApByInterferenceVO | Unset
        if isinstance(_top_ap_by_interference, Unset):
            top_ap_by_interference = UNSET
        else:
            top_ap_by_interference = TopApByInterferenceVO.from_dict(
                _top_ap_by_interference
            )

        _top_ap_by_rt_and_drop = d.pop("topApByRtAndDrop", UNSET)
        top_ap_by_rt_and_drop: TopApByRtDropVO | Unset
        if isinstance(_top_ap_by_rt_and_drop, Unset):
            top_ap_by_rt_and_drop = UNSET
        else:
            top_ap_by_rt_and_drop = TopApByRtDropVO.from_dict(_top_ap_by_rt_and_drop)

        _top_ssid_by_traffic = d.pop("topSsidByTraffic", UNSET)
        top_ssid_by_traffic: list[TopSsidTrafficVO] | Unset = UNSET
        if _top_ssid_by_traffic is not UNSET:
            top_ssid_by_traffic = []
            for top_ssid_by_traffic_item_data in _top_ssid_by_traffic:
                top_ssid_by_traffic_item = TopSsidTrafficVO.from_dict(
                    top_ssid_by_traffic_item_data
                )

                top_ssid_by_traffic.append(top_ssid_by_traffic_item)

        _ap_status = d.pop("apStatus", UNSET)
        ap_status: list[OnlineOfflineVO] | Unset = UNSET
        if _ap_status is not UNSET:
            ap_status = []
            for ap_status_item_data in _ap_status:
                ap_status_item = OnlineOfflineVO.from_dict(ap_status_item_data)

                ap_status.append(ap_status_item)

        _wireless_traffic_single = d.pop("wirelessTrafficSingle", UNSET)
        wireless_traffic_single: WirelessTrafficSingleVO | Unset
        if isinstance(_wireless_traffic_single, Unset):
            wireless_traffic_single = UNSET
        else:
            wireless_traffic_single = WirelessTrafficSingleVO.from_dict(
                _wireless_traffic_single
            )

        _ap_health = d.pop("apHealth", UNSET)
        ap_health: list[DeviceHealthVO] | Unset = UNSET
        if _ap_health is not UNSET:
            ap_health = []
            for ap_health_item_data in _ap_health:
                ap_health_item = DeviceHealthVO.from_dict(ap_health_item_data)

                ap_health.append(ap_health_item)

        _client_traffic = d.pop("clientTraffic", UNSET)
        client_traffic: ClientTrafficInfo | Unset
        if isinstance(_client_traffic, Unset):
            client_traffic = UNSET
        else:
            client_traffic = ClientTrafficInfo.from_dict(_client_traffic)

        _client_connection_trend = d.pop("clientConnectionTrend", UNSET)
        client_connection_trend: ClientConnectionTrend | Unset
        if isinstance(_client_connection_trend, Unset):
            client_connection_trend = UNSET
        else:
            client_connection_trend = ClientConnectionTrend.from_dict(
                _client_connection_trend
            )

        _clients_overview = d.pop("clientsOverview", UNSET)
        clients_overview: ClientStatisticsOverview | Unset
        if isinstance(_clients_overview, Unset):
            clients_overview = UNSET
        else:
            clients_overview = ClientStatisticsOverview.from_dict(_clients_overview)

        _clients_association_activities = d.pop("clientsAssociationActivities", UNSET)
        clients_association_activities: list[ClientAssociationActivities] | Unset = (
            UNSET
        )
        if _clients_association_activities is not UNSET:
            clients_association_activities = []
            for (
                clients_association_activities_item_data
            ) in _clients_association_activities:
                clients_association_activities_item = (
                    ClientAssociationActivities.from_dict(
                        clients_association_activities_item_data
                    )
                )

                clients_association_activities.append(
                    clients_association_activities_item
                )

        _clients_with_onboarding_times = d.pop("clientsWithOnboardingTimes", UNSET)
        clients_with_onboarding_times: ClientsWithOnBoardingTimes | Unset
        if isinstance(_clients_with_onboarding_times, Unset):
            clients_with_onboarding_times = UNSET
        else:
            clients_with_onboarding_times = ClientsWithOnBoardingTimes.from_dict(
                _clients_with_onboarding_times
            )

        _top_client = d.pop("topClient", UNSET)
        top_client: TopTrafficAndUptimeClients | Unset
        if isinstance(_top_client, Unset):
            top_client = UNSET
        else:
            top_client = TopTrafficAndUptimeClients.from_dict(_top_client)

        _app_categories = d.pop("appCategories", UNSET)
        app_categories: AppCategoryTrafficsVO | Unset
        if isinstance(_app_categories, Unset):
            app_categories = UNSET
        else:
            app_categories = AppCategoryTrafficsVO.from_dict(_app_categories)

        _top_application_by_traffic = d.pop("topApplicationByTraffic", UNSET)
        top_application_by_traffic: list[TopApplicationByTrafficVO] | Unset = UNSET
        if _top_application_by_traffic is not UNSET:
            top_application_by_traffic = []
            for top_application_by_traffic_item_data in _top_application_by_traffic:
                top_application_by_traffic_item = TopApplicationByTrafficVO.from_dict(
                    top_application_by_traffic_item_data
                )

                top_application_by_traffic.append(top_application_by_traffic_item)

        _internet = d.pop("internet", UNSET)
        internet: NetworkActivityVO | Unset
        if isinstance(_internet, Unset):
            internet = UNSET
        else:
            internet = NetworkActivityVO.from_dict(_internet)

        _client_health_trend = d.pop("clientHealthTrend", UNSET)
        client_health_trend: list[ClientHealthTrendVO] | Unset = UNSET
        if _client_health_trend is not UNSET:
            client_health_trend = []
            for client_health_trend_item_data in _client_health_trend:
                client_health_trend_item = ClientHealthTrendVO.from_dict(
                    client_health_trend_item_data
                )

                client_health_trend.append(client_health_trend_item)

        _clients_rssi = d.pop("clientsRssi", UNSET)
        clients_rssi: list[RssiDistributionVO] | Unset = UNSET
        if _clients_rssi is not UNSET:
            clients_rssi = []
            for clients_rssi_item_data in _clients_rssi:
                clients_rssi_item = RssiDistributionVO.from_dict(clients_rssi_item_data)

                clients_rssi.append(clients_rssi_item)

        _clients_snr = d.pop("clientsSnr", UNSET)
        clients_snr: list[SnrDistributionVO] | Unset = UNSET
        if _clients_snr is not UNSET:
            clients_snr = []
            for clients_snr_item_data in _clients_snr:
                clients_snr_item = SnrDistributionVO.from_dict(clients_snr_item_data)

                clients_snr.append(clients_snr_item)

        _clients_data_rate = d.pop("clientsDataRate", UNSET)
        clients_data_rate: list[DataRateDistributionVO] | Unset = UNSET
        if _clients_data_rate is not UNSET:
            clients_data_rate = []
            for clients_data_rate_item_data in _clients_data_rate:
                clients_data_rate_item = DataRateDistributionVO.from_dict(
                    clients_data_rate_item_data
                )

                clients_data_rate.append(clients_data_rate_item)

        _top_ap_by_conn_failure = d.pop("topApByConnFailure", UNSET)
        top_ap_by_conn_failure: TopApByConnFailureVO | Unset
        if isinstance(_top_ap_by_conn_failure, Unset):
            top_ap_by_conn_failure = UNSET
        else:
            top_ap_by_conn_failure = TopApByConnFailureVO.from_dict(
                _top_ap_by_conn_failure
            )

        _top_switch_by_packet = d.pop("topSwitchByPacket", UNSET)
        top_switch_by_packet: TopSwitchByPacketVO | Unset
        if isinstance(_top_switch_by_packet, Unset):
            top_switch_by_packet = UNSET
        else:
            top_switch_by_packet = TopSwitchByPacketVO.from_dict(_top_switch_by_packet)

        card_info_vo = cls(
            overview_summary=overview_summary,
            traffic_summary=traffic_summary,
            traffic_distribution=traffic_distribution,
            alert_summary=alert_summary,
            device_status=device_status,
            device_health_trend=device_health_trend,
            network=network,
            gateway_summary=gateway_summary,
            isp_load=isp_load,
            switch_alert_reboot=switch_alert_reboot,
            top_switch_by_traffic_and_poe_power=top_switch_by_traffic_and_poe_power,
            top_switch_cpu_memory=top_switch_cpu_memory,
            poe_power_trend=poe_power_trend,
            switch_status=switch_status,
            switch_health_trend=switch_health_trend,
            wan_health_trend=wan_health_trend,
            wireless_traffic=wireless_traffic,
            wifi_health=wifi_health,
            top_ap_by_traffic_and_client=top_ap_by_traffic_and_client,
            top_ap_by_cpu_and_memory=top_ap_by_cpu_and_memory,
            top_ap_by_interference=top_ap_by_interference,
            top_ap_by_rt_and_drop=top_ap_by_rt_and_drop,
            top_ssid_by_traffic=top_ssid_by_traffic,
            ap_status=ap_status,
            wireless_traffic_single=wireless_traffic_single,
            ap_health=ap_health,
            client_traffic=client_traffic,
            client_connection_trend=client_connection_trend,
            clients_overview=clients_overview,
            clients_association_activities=clients_association_activities,
            clients_with_onboarding_times=clients_with_onboarding_times,
            top_client=top_client,
            app_categories=app_categories,
            top_application_by_traffic=top_application_by_traffic,
            internet=internet,
            client_health_trend=client_health_trend,
            clients_rssi=clients_rssi,
            clients_snr=clients_snr,
            clients_data_rate=clients_data_rate,
            top_ap_by_conn_failure=top_ap_by_conn_failure,
            top_switch_by_packet=top_switch_by_packet,
        )

        card_info_vo.additional_properties = d
        return card_info_vo

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
