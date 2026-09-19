from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_category_event_count_vo import AnomalyCategoryEventCountVO


T = TypeVar("T", bound="OverviewStatisticsOpenApiVO")


@_attrs_define
class OverviewStatisticsOpenApiVO:
    """
    Attributes:
        all_status (int | Unset): Total incident count across all statuses Example: 20.
        ongoing (int | Unset): Number of ongoing incidents Example: 5.
        resolved (int | Unset): Number of resolved incidents Example: 15.
        ignored (int | Unset): Number of ignored incidents Example: 0.
        unresolved (int | Unset): Number of unresolved incidents Example: 0.
        all_ (int | Unset): Total incident count across all categories Example: 20.
        security (int | Unset): Number of security incidents (category code 19) Example: 5.
        device_status (int | Unset): Number of device status incidents (category code 18) Example: 3.
        wan_and_services (int | Unset): Number of WAN and services incidents (category code 17) Example: 7.
        link (int | Unset): Number of link incidents (category code 16) Example: 2.
        wired_network (int | Unset): Number of wired network incidents (category code 15) Example: 4.
        wireless_network (int | Unset): Number of wireless network incidents (category code 14) Example: 6.
        roaming (int | Unset): Number of roaming incidents (category code 13) Example: 1.
        authentication (int | Unset): Number of authentication incidents (category code 12) Example: 8.
        access (int | Unset): Number of access incidents (category code 11) Example: 9.
        all_level (int | Unset): Total incident count across all levels Example: 20.
        critical (int | Unset): Number of critical-level incidents Example: 2.
        error (int | Unset): Number of error-level incidents Example: 5.
        warning (int | Unset): Number of warning-level incidents Example: 10.
        info (int | Unset): Number of info-level incidents Example: 3.
        others (int | Unset): Deprecated events since v6.3 Example: 2.
        anomaly_category_event_counts (list[AnomalyCategoryEventCountVO] | Unset): Anomaly-code level event count
            information
    """

    all_status: int | Unset = UNSET
    ongoing: int | Unset = UNSET
    resolved: int | Unset = UNSET
    ignored: int | Unset = UNSET
    unresolved: int | Unset = UNSET
    all_: int | Unset = UNSET
    security: int | Unset = UNSET
    device_status: int | Unset = UNSET
    wan_and_services: int | Unset = UNSET
    link: int | Unset = UNSET
    wired_network: int | Unset = UNSET
    wireless_network: int | Unset = UNSET
    roaming: int | Unset = UNSET
    authentication: int | Unset = UNSET
    access: int | Unset = UNSET
    all_level: int | Unset = UNSET
    critical: int | Unset = UNSET
    error: int | Unset = UNSET
    warning: int | Unset = UNSET
    info: int | Unset = UNSET
    others: int | Unset = UNSET
    anomaly_category_event_counts: list[AnomalyCategoryEventCountVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_status = self.all_status

        ongoing = self.ongoing

        resolved = self.resolved

        ignored = self.ignored

        unresolved = self.unresolved

        all_ = self.all_

        security = self.security

        device_status = self.device_status

        wan_and_services = self.wan_and_services

        link = self.link

        wired_network = self.wired_network

        wireless_network = self.wireless_network

        roaming = self.roaming

        authentication = self.authentication

        access = self.access

        all_level = self.all_level

        critical = self.critical

        error = self.error

        warning = self.warning

        info = self.info

        others = self.others

        anomaly_category_event_counts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.anomaly_category_event_counts, Unset):
            anomaly_category_event_counts = []
            for (
                anomaly_category_event_counts_item_data
            ) in self.anomaly_category_event_counts:
                anomaly_category_event_counts_item = (
                    anomaly_category_event_counts_item_data.to_dict()
                )
                anomaly_category_event_counts.append(anomaly_category_event_counts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_status is not UNSET:
            field_dict["allStatus"] = all_status
        if ongoing is not UNSET:
            field_dict["ongoing"] = ongoing
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if ignored is not UNSET:
            field_dict["ignored"] = ignored
        if unresolved is not UNSET:
            field_dict["unresolved"] = unresolved
        if all_ is not UNSET:
            field_dict["all"] = all_
        if security is not UNSET:
            field_dict["security"] = security
        if device_status is not UNSET:
            field_dict["deviceStatus"] = device_status
        if wan_and_services is not UNSET:
            field_dict["wanAndServices"] = wan_and_services
        if link is not UNSET:
            field_dict["link"] = link
        if wired_network is not UNSET:
            field_dict["wiredNetwork"] = wired_network
        if wireless_network is not UNSET:
            field_dict["wirelessNetwork"] = wireless_network
        if roaming is not UNSET:
            field_dict["roaming"] = roaming
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if access is not UNSET:
            field_dict["access"] = access
        if all_level is not UNSET:
            field_dict["allLevel"] = all_level
        if critical is not UNSET:
            field_dict["critical"] = critical
        if error is not UNSET:
            field_dict["error"] = error
        if warning is not UNSET:
            field_dict["warning"] = warning
        if info is not UNSET:
            field_dict["info"] = info
        if others is not UNSET:
            field_dict["others"] = others
        if anomaly_category_event_counts is not UNSET:
            field_dict["anomalyCategoryEventCounts"] = anomaly_category_event_counts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_category_event_count_vo import (
            AnomalyCategoryEventCountVO,
        )

        d = dict(src_dict)
        all_status = d.pop("allStatus", UNSET)

        ongoing = d.pop("ongoing", UNSET)

        resolved = d.pop("resolved", UNSET)

        ignored = d.pop("ignored", UNSET)

        unresolved = d.pop("unresolved", UNSET)

        all_ = d.pop("all", UNSET)

        security = d.pop("security", UNSET)

        device_status = d.pop("deviceStatus", UNSET)

        wan_and_services = d.pop("wanAndServices", UNSET)

        link = d.pop("link", UNSET)

        wired_network = d.pop("wiredNetwork", UNSET)

        wireless_network = d.pop("wirelessNetwork", UNSET)

        roaming = d.pop("roaming", UNSET)

        authentication = d.pop("authentication", UNSET)

        access = d.pop("access", UNSET)

        all_level = d.pop("allLevel", UNSET)

        critical = d.pop("critical", UNSET)

        error = d.pop("error", UNSET)

        warning = d.pop("warning", UNSET)

        info = d.pop("info", UNSET)

        others = d.pop("others", UNSET)

        _anomaly_category_event_counts = d.pop("anomalyCategoryEventCounts", UNSET)
        anomaly_category_event_counts: list[AnomalyCategoryEventCountVO] | Unset = UNSET
        if _anomaly_category_event_counts is not UNSET:
            anomaly_category_event_counts = []
            for (
                anomaly_category_event_counts_item_data
            ) in _anomaly_category_event_counts:
                anomaly_category_event_counts_item = (
                    AnomalyCategoryEventCountVO.from_dict(
                        anomaly_category_event_counts_item_data
                    )
                )

                anomaly_category_event_counts.append(anomaly_category_event_counts_item)

        overview_statistics_open_api_vo = cls(
            all_status=all_status,
            ongoing=ongoing,
            resolved=resolved,
            ignored=ignored,
            unresolved=unresolved,
            all_=all_,
            security=security,
            device_status=device_status,
            wan_and_services=wan_and_services,
            link=link,
            wired_network=wired_network,
            wireless_network=wireless_network,
            roaming=roaming,
            authentication=authentication,
            access=access,
            all_level=all_level,
            critical=critical,
            error=error,
            warning=warning,
            info=info,
            others=others,
            anomaly_category_event_counts=anomaly_category_event_counts,
        )

        overview_statistics_open_api_vo.additional_properties = d
        return overview_statistics_open_api_vo

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
