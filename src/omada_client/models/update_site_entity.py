from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.modify_dst_dto import ModifyDstDTO
    from ..models.ntp_server import NtpServer


T = TypeVar("T", bound="UpdateSiteEntity")


@_attrs_define
class UpdateSiteEntity:
    """
    Attributes:
        region (str): Country/Region of the site; For the values of region, refer to the abbreviation of the ISO country
            code; For example, you need to input "United States" for the United States of America.
        time_zone (str): For the values of the timezone of the site, refer to section 5.1 of the Open API Access Guide.
        scenario (str): For the values of the scenario of the site, refer to result of the interface for Get scenario
            list.
        name (str | Unset): Site name should contain 1 to 64 characters.
        tag_ids (list[str] | Unset): Site tag ID, Site tag ID can be created using "Create new site tag" interface, and
            site tag ID can be obtained from "Get site tag list" interface
        ntp_enable (bool | Unset): NTP server status of the site
        ntp_servers (list[NtpServer] | Unset): NTP server address; Up to 5 entries are allowed for the NTP server
            address list.
        dst (ModifyDstDTO | Unset): Daylight Saving Time config of the site
        longitude (float | Unset): Longitude of the site should be within the range of -180 - 180.
        latitude (float | Unset): Latitude of the site should be within the range of -90 - 90.
        address (str | Unset): Address of the site
        support_es (bool | Unset): Whether the site supports adopting Agile Series Switches
        support_l2 (bool | Unset): Whether the site supports adopting Non-Agile Series Switches
    """

    region: str
    time_zone: str
    scenario: str
    name: str | Unset = UNSET
    tag_ids: list[str] | Unset = UNSET
    ntp_enable: bool | Unset = UNSET
    ntp_servers: list[NtpServer] | Unset = UNSET
    dst: ModifyDstDTO | Unset = UNSET
    longitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    address: str | Unset = UNSET
    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region

        time_zone = self.time_zone

        scenario = self.scenario

        name = self.name

        tag_ids: list[str] | Unset = UNSET
        if not isinstance(self.tag_ids, Unset):
            tag_ids = self.tag_ids

        ntp_enable = self.ntp_enable

        ntp_servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = []
            for ntp_servers_item_data in self.ntp_servers:
                ntp_servers_item = ntp_servers_item_data.to_dict()
                ntp_servers.append(ntp_servers_item)

        dst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dst, Unset):
            dst = self.dst.to_dict()

        longitude = self.longitude

        latitude = self.latitude

        address = self.address

        support_es = self.support_es

        support_l2 = self.support_l2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "timeZone": time_zone,
                "scenario": scenario,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if tag_ids is not UNSET:
            field_dict["tagIds"] = tag_ids
        if ntp_enable is not UNSET:
            field_dict["ntpEnable"] = ntp_enable
        if ntp_servers is not UNSET:
            field_dict["ntpServers"] = ntp_servers
        if dst is not UNSET:
            field_dict["dst"] = dst
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
        from ..models.modify_dst_dto import ModifyDstDTO
        from ..models.ntp_server import NtpServer

        d = dict(src_dict)
        region = d.pop("region")

        time_zone = d.pop("timeZone")

        scenario = d.pop("scenario")

        name = d.pop("name", UNSET)

        tag_ids = cast(list[str], d.pop("tagIds", UNSET))

        ntp_enable = d.pop("ntpEnable", UNSET)

        _ntp_servers = d.pop("ntpServers", UNSET)
        ntp_servers: list[NtpServer] | Unset = UNSET
        if _ntp_servers is not UNSET:
            ntp_servers = []
            for ntp_servers_item_data in _ntp_servers:
                ntp_servers_item = NtpServer.from_dict(ntp_servers_item_data)

                ntp_servers.append(ntp_servers_item)

        _dst = d.pop("dst", UNSET)
        dst: ModifyDstDTO | Unset
        if isinstance(_dst, Unset):
            dst = UNSET
        else:
            dst = ModifyDstDTO.from_dict(_dst)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        update_site_entity = cls(
            region=region,
            time_zone=time_zone,
            scenario=scenario,
            name=name,
            tag_ids=tag_ids,
            ntp_enable=ntp_enable,
            ntp_servers=ntp_servers,
            dst=dst,
            longitude=longitude,
            latitude=latitude,
            address=address,
            support_es=support_es,
            support_l2=support_l2,
        )

        update_site_entity.additional_properties = d
        return update_site_entity

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
