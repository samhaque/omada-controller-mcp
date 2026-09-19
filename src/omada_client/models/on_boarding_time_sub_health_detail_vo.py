from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
    from ..models.time_value_item_vo import TimeValueItemVO


T = TypeVar("T", bound="OnBoardingTimeSubHealthDetailVO")


@_attrs_define
class OnBoardingTimeSubHealthDetailVO:
    """Onboarding time health info and score

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        assoc_time (list[TimeValueItemVO] | Unset): Client association cost time list.
        auth_time (list[TimeValueItemVO] | Unset): Client authorization cost time list.
        dhcp_time (list[TimeValueItemVO] | Unset): Client DHCP cost time list.
        dns_time (list[TimeValueItemVO] | Unset): Client dns cost time list.
        average_assoc_time (int | Unset): Average association time.
        average_auth_time (int | Unset): Average authorization time.
        average_dhcp_time (int | Unset): Average DHCP time.
        average_dns_time (int | Unset): Average DNS time.
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    assoc_time: list[TimeValueItemVO] | Unset = UNSET
    auth_time: list[TimeValueItemVO] | Unset = UNSET
    dhcp_time: list[TimeValueItemVO] | Unset = UNSET
    dns_time: list[TimeValueItemVO] | Unset = UNSET
    average_assoc_time: int | Unset = UNSET
    average_auth_time: int | Unset = UNSET
    average_dhcp_time: int | Unset = UNSET
    average_dns_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary_score = self.summary_score

        support = self.support

        incidents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incidents, Unset):
            incidents = []
            for incidents_item_data in self.incidents:
                incidents_item = incidents_item_data.to_dict()
                incidents.append(incidents_item)

        assoc_time: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assoc_time, Unset):
            assoc_time = []
            for assoc_time_item_data in self.assoc_time:
                assoc_time_item = assoc_time_item_data.to_dict()
                assoc_time.append(assoc_time_item)

        auth_time: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auth_time, Unset):
            auth_time = []
            for auth_time_item_data in self.auth_time:
                auth_time_item = auth_time_item_data.to_dict()
                auth_time.append(auth_time_item)

        dhcp_time: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dhcp_time, Unset):
            dhcp_time = []
            for dhcp_time_item_data in self.dhcp_time:
                dhcp_time_item = dhcp_time_item_data.to_dict()
                dhcp_time.append(dhcp_time_item)

        dns_time: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dns_time, Unset):
            dns_time = []
            for dns_time_item_data in self.dns_time:
                dns_time_item = dns_time_item_data.to_dict()
                dns_time.append(dns_time_item)

        average_assoc_time = self.average_assoc_time

        average_auth_time = self.average_auth_time

        average_dhcp_time = self.average_dhcp_time

        average_dns_time = self.average_dns_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if assoc_time is not UNSET:
            field_dict["assocTime"] = assoc_time
        if auth_time is not UNSET:
            field_dict["authTime"] = auth_time
        if dhcp_time is not UNSET:
            field_dict["dhcpTime"] = dhcp_time
        if dns_time is not UNSET:
            field_dict["dnsTime"] = dns_time
        if average_assoc_time is not UNSET:
            field_dict["averageAssocTime"] = average_assoc_time
        if average_auth_time is not UNSET:
            field_dict["averageAuthTime"] = average_auth_time
        if average_dhcp_time is not UNSET:
            field_dict["averageDhcpTime"] = average_dhcp_time
        if average_dns_time is not UNSET:
            field_dict["averageDnsTime"] = average_dns_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
        from ..models.time_value_item_vo import TimeValueItemVO

        d = dict(src_dict)
        summary_score = d.pop("summaryScore", UNSET)

        support = d.pop("support", UNSET)

        _incidents = d.pop("incidents", UNSET)
        incidents: list[AnomalyBriefCountVO] | Unset = UNSET
        if _incidents is not UNSET:
            incidents = []
            for incidents_item_data in _incidents:
                incidents_item = AnomalyBriefCountVO.from_dict(incidents_item_data)

                incidents.append(incidents_item)

        _assoc_time = d.pop("assocTime", UNSET)
        assoc_time: list[TimeValueItemVO] | Unset = UNSET
        if _assoc_time is not UNSET:
            assoc_time = []
            for assoc_time_item_data in _assoc_time:
                assoc_time_item = TimeValueItemVO.from_dict(assoc_time_item_data)

                assoc_time.append(assoc_time_item)

        _auth_time = d.pop("authTime", UNSET)
        auth_time: list[TimeValueItemVO] | Unset = UNSET
        if _auth_time is not UNSET:
            auth_time = []
            for auth_time_item_data in _auth_time:
                auth_time_item = TimeValueItemVO.from_dict(auth_time_item_data)

                auth_time.append(auth_time_item)

        _dhcp_time = d.pop("dhcpTime", UNSET)
        dhcp_time: list[TimeValueItemVO] | Unset = UNSET
        if _dhcp_time is not UNSET:
            dhcp_time = []
            for dhcp_time_item_data in _dhcp_time:
                dhcp_time_item = TimeValueItemVO.from_dict(dhcp_time_item_data)

                dhcp_time.append(dhcp_time_item)

        _dns_time = d.pop("dnsTime", UNSET)
        dns_time: list[TimeValueItemVO] | Unset = UNSET
        if _dns_time is not UNSET:
            dns_time = []
            for dns_time_item_data in _dns_time:
                dns_time_item = TimeValueItemVO.from_dict(dns_time_item_data)

                dns_time.append(dns_time_item)

        average_assoc_time = d.pop("averageAssocTime", UNSET)

        average_auth_time = d.pop("averageAuthTime", UNSET)

        average_dhcp_time = d.pop("averageDhcpTime", UNSET)

        average_dns_time = d.pop("averageDnsTime", UNSET)

        on_boarding_time_sub_health_detail_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            assoc_time=assoc_time,
            auth_time=auth_time,
            dhcp_time=dhcp_time,
            dns_time=dns_time,
            average_assoc_time=average_assoc_time,
            average_auth_time=average_auth_time,
            average_dhcp_time=average_dhcp_time,
            average_dns_time=average_dns_time,
        )

        on_boarding_time_sub_health_detail_vo.additional_properties = d
        return on_boarding_time_sub_health_detail_vo

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
