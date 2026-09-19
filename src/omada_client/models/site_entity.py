from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dst_dto import DstDTO


T = TypeVar("T", bound="SiteEntity")


@_attrs_define
class SiteEntity:
    """
    Attributes:
        site_id (str | Unset): Site ID
        name (str | Unset): Name of the site should contain 1 to 64 characters.
        type_ (int | Unset): Type of the site should be 0 or 1, and 0 means basic site, 1 means pro site.
        tag_ids (list[str] | Unset): Site tag ID
        region (str | Unset): Country/Region of the site; For the values of region, refer to the abbreviation of the ISO
            country code; For example, you need to input "United States" for the United States of America.
        time_zone (str | Unset): For the values of the timezone of the site, refer to section 5.1 of the Open API Access
            Guide.
        ntp_enable (bool | Unset): NTP server status of the site
        ntp_servers (list[str] | Unset): NTP server address; Up to 5 entries are allowed for the NTP server address
            list.
        dst (DstDTO | Unset): Daylight Saving Time config of the site
        scenario (str | Unset): For the values of the scenario of the site, refer to result of the interface for Get
            scenario list.
        longitude (float | Unset): Longitude of the site should be within the range of -180 - 180.
        latitude (float | Unset): Latitude of the site should be within the range of -90 - 90.
        address (str | Unset): Address of the site
        support_es (bool | Unset): Whether the site supports adopting Agile Series Switches
        support_l2 (bool | Unset): Whether the site supports adopting Non-Agile Series Switches
    """

    site_id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    region: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    ntp_enable: bool | Unset = UNSET
    ntp_servers: list[str] | Unset = UNSET
    dst: DstDTO | Unset = UNSET
    scenario: str | Unset = UNSET
    longitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    address: str | Unset = UNSET
    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        name = self.name

        type_ = self.type_

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        region = self.region

        time_zone = self.time_zone

        ntp_enable = self.ntp_enable

        ntp_servers: list[str] | Unset = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = self.ntp_servers

        dst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dst, Unset):
            dst = self.dst.to_dict()

        scenario = self.scenario

        longitude = self.longitude

        latitude = self.latitude

        address = self.address

        support_es = self.support_es

        support_l2 = self.support_l2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if region is not UNSET:
            field_dict["region"] = region
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if ntp_enable is not UNSET:
            field_dict["ntpEnable"] = ntp_enable
        if ntp_servers is not UNSET:
            field_dict["ntpServers"] = ntp_servers
        if dst is not UNSET:
            field_dict["dst"] = dst
        if scenario is not UNSET:
            field_dict["scenario"] = scenario
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if address is not UNSET:
            field_dict["address"] = address
        if support_es is not UNSET:
            field_dict["supportES"] = support_es
        if support_l2 is not UNSET:
            field_dict["supportL2"] = support_l2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dst_dto import DstDTO

        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        region = d.pop("region", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        ntp_enable = d.pop("ntpEnable", UNSET)

        ntp_servers = cast(list[str], d.pop("ntpServers", UNSET))

        _dst = d.pop("dst", UNSET)
        dst: DstDTO | Unset
        if isinstance(_dst, Unset):
            dst = UNSET
        else:
            dst = DstDTO.from_dict(_dst)

        scenario = d.pop("scenario", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        site_entity = cls(
            site_id=site_id,
            name=name,
            type_=type_,
            tag_ids=tag_ids,
            region=region,
            time_zone=time_zone,
            ntp_enable=ntp_enable,
            ntp_servers=ntp_servers,
            dst=dst,
            scenario=scenario,
            longitude=longitude,
            latitude=latitude,
            address=address,
            support_es=support_es,
            support_l2=support_l2,
        )

        site_entity.additional_properties = d
        return site_entity

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
