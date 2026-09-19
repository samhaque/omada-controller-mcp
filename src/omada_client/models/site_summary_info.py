from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteSummaryInfo")


@_attrs_define
class SiteSummaryInfo:
    """Site summary info

    Attributes:
        site_id (str | Unset): Site ID
        name (str | Unset): Name of the site should contain 1 to 64 characters.
        tag_ids (list[str] | Unset): Site tag ID
        region (str | Unset): Country/Region of the site; For the values of region, refer to the abbreviation of the ISO
            country code; For example, you need to input "United States" for the United States of America.
        time_zone (str | Unset): For the values of the timezone of the site, refer to section 5.1 of the Open API Access
            Guide.
        scenario (str | Unset): For the values of the scenario of the site, refer to result of the interface for Get
            scenario list.
        longitude (float | Unset): Longitude of the site should be within the range of -180 - 180.
        latitude (float | Unset): Latitude of the site should be within the range of -90 - 90.
        address (str | Unset): Address of the site
        type_ (int | Unset): Site type(only for pro controller). It should be a value as follows: 0: Basic Site; 1: Pro
            Site
        support_es (bool | Unset): Whether the site supports adopting Agile Series Switches
        support_l2 (bool | Unset): Whether the site supports adopting Non-Agile Series Switches
        site_public_ip (str | Unset): Adopted gateway public ip of the site, only useful for cloud based controller and
            remote management local Controller
        primary (bool | Unset): Default Site mark
    """

    site_id: str | Unset = UNSET
    name: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    region: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    scenario: str | Unset = UNSET
    longitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    address: str | Unset = UNSET
    type_: int | Unset = UNSET
    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    site_public_ip: str | Unset = UNSET
    primary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        name = self.name

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        region = self.region

        time_zone = self.time_zone

        scenario = self.scenario

        longitude = self.longitude

        latitude = self.latitude

        address = self.address

        type_ = self.type_

        support_es = self.support_es

        support_l2 = self.support_l2

        site_public_ip = self.site_public_ip

        primary = self.primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if name is not UNSET:
            field_dict["name"] = name
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if support_es is not UNSET:
            field_dict["supportES"] = support_es
        if support_l2 is not UNSET:
            field_dict["supportL2"] = support_l2
        if site_public_ip is not UNSET:
            field_dict["sitePublicIp"] = site_public_ip
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        name = d.pop("name", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        region = d.pop("region", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        scenario = d.pop("scenario", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        type_ = d.pop("type", UNSET)

        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        site_public_ip = d.pop("sitePublicIp", UNSET)

        primary = d.pop("primary", UNSET)

        site_summary_info = cls(
            site_id=site_id,
            name=name,
            tag_ids=tag_ids,
            region=region,
            time_zone=time_zone,
            scenario=scenario,
            longitude=longitude,
            latitude=latitude,
            address=address,
            type_=type_,
            support_es=support_es,
            support_l2=support_l2,
            site_public_ip=site_public_ip,
            primary=primary,
        )

        site_summary_info.additional_properties = d
        return site_summary_info

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
