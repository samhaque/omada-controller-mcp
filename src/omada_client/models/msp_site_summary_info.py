from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspSiteSummaryInfo")


@_attrs_define
class MspSiteSummaryInfo:
    """
    Attributes:
        site_id (str | Unset): Site ID
        site_name (str | Unset): Site name
        tag_ids (list[str] | Unset): Site tag ID
        customer_id (str | Unset): Customer ID
        customer_name (str | Unset): Customer name
        region (str | Unset): Country/Region of the site; For the values of region, refer to the abbreviation of the ISO
            country code; For example, you need to input "United States" for the United States of America.
        time_zone (str | Unset): For the values of the timezone of the site, refer to section 5.1 of the Open API Access
            Guide.
        scenario (str | Unset): Site scenario
        longitude (float | Unset): Site longitude should be within the range of -180~180
        latitude (float | Unset): Site latitude should be within the range of -90~90
        address (str | Unset): Site address
        wan (bool | Unset): Whether exists gateway is connected of current site
        connected_ap_num (int | Unset): Connected ap num of current site
        disconnected_ap_num (int | Unset): Disconnected ap num of current site
        isolated_ap_num (int | Unset): Isolated ap num of current site
        connected_switch_num (int | Unset): Connected switch num of current site
        disconnected_switch_num (int | Unset): Disconnected switch num of current site
        type_ (int | Unset): Site type(only for pro controller). It should be a value as follows: 0: Basic Site; 1: Pro
            Site
        support_es (bool | Unset): Whether the site supports adopting Agile Series Switches
        support_l2 (bool | Unset): Whether the site supports adopting Non-Agile Series Switches
        site_public_ip (str | Unset): Adopted gateway public ip of the site, only useful for cloud based controller and
            remote management local Controller
    """

    site_id: str | Unset = UNSET
    site_name: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    customer_id: str | Unset = UNSET
    customer_name: str | Unset = UNSET
    region: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    scenario: str | Unset = UNSET
    longitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    address: str | Unset = UNSET
    wan: bool | Unset = UNSET
    connected_ap_num: int | Unset = UNSET
    disconnected_ap_num: int | Unset = UNSET
    isolated_ap_num: int | Unset = UNSET
    connected_switch_num: int | Unset = UNSET
    disconnected_switch_num: int | Unset = UNSET
    type_: int | Unset = UNSET
    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    site_public_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        site_name = self.site_name

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        customer_id = self.customer_id

        customer_name = self.customer_name

        region = self.region

        time_zone = self.time_zone

        scenario = self.scenario

        longitude = self.longitude

        latitude = self.latitude

        address = self.address

        wan = self.wan

        connected_ap_num = self.connected_ap_num

        disconnected_ap_num = self.disconnected_ap_num

        isolated_ap_num = self.isolated_ap_num

        connected_switch_num = self.connected_switch_num

        disconnected_switch_num = self.disconnected_switch_num

        type_ = self.type_

        support_es = self.support_es

        support_l2 = self.support_l2

        site_public_ip = self.site_public_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if region is not UNSET:
            field_dict["region"] = region
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if address is not UNSET:
            field_dict["address"] = address
        if wan is not UNSET:
            field_dict["wan"] = wan
        if connected_ap_num is not UNSET:
            field_dict["connectedApNum"] = connected_ap_num
        if disconnected_ap_num is not UNSET:
            field_dict["disconnectedApNum"] = disconnected_ap_num
        if isolated_ap_num is not UNSET:
            field_dict["isolatedApNum"] = isolated_ap_num
        if connected_switch_num is not UNSET:
            field_dict["connectedSwitchNum"] = connected_switch_num
        if disconnected_switch_num is not UNSET:
            field_dict["disconnectedSwitchNum"] = disconnected_switch_num
        if type_ is not UNSET:
            field_dict["type"] = type_
        if support_es is not UNSET:
            field_dict["supportES"] = support_es
        if support_l2 is not UNSET:
            field_dict["supportL2"] = support_l2
        if site_public_ip is not UNSET:
            field_dict["sitePublicIp"] = site_public_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        customer_id = d.pop("customerId", UNSET)

        customer_name = d.pop("customerName", UNSET)

        region = d.pop("region", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        scenario = d.pop("scenario", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        wan = d.pop("wan", UNSET)

        connected_ap_num = d.pop("connectedApNum", UNSET)

        disconnected_ap_num = d.pop("disconnectedApNum", UNSET)

        isolated_ap_num = d.pop("isolatedApNum", UNSET)

        connected_switch_num = d.pop("connectedSwitchNum", UNSET)

        disconnected_switch_num = d.pop("disconnectedSwitchNum", UNSET)

        type_ = d.pop("type", UNSET)

        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        site_public_ip = d.pop("sitePublicIp", UNSET)

        msp_site_summary_info = cls(
            site_id=site_id,
            site_name=site_name,
            tag_ids=tag_ids,
            customer_id=customer_id,
            customer_name=customer_name,
            region=region,
            time_zone=time_zone,
            scenario=scenario,
            longitude=longitude,
            latitude=latitude,
            address=address,
            wan=wan,
            connected_ap_num=connected_ap_num,
            disconnected_ap_num=disconnected_ap_num,
            isolated_ap_num=isolated_ap_num,
            connected_switch_num=connected_switch_num,
            disconnected_switch_num=disconnected_switch_num,
            type_=type_,
            support_es=support_es,
            support_l2=support_l2,
            site_public_ip=site_public_ip,
        )

        msp_site_summary_info.additional_properties = d
        return msp_site_summary_info

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
