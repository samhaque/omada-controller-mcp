from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_server import NtpServer
    from ..models.site_settingdst import SiteSettingdst


T = TypeVar("T", bound="SiteTemplateOpenApiVO")


@_attrs_define
class SiteTemplateOpenApiVO:
    """Site template setting.

    Attributes:
        time_zone (str | Unset): For the values of the timezone of the site, refer to section 5.1 of the Open API Access
            Guide.
        dst (SiteSettingdst | Unset): Daylight Saving Time.
        ntp_enable (bool | Unset): NTP server status of the site.
        ntp_servers (list[NtpServer] | Unset): NTP server address; Up to 5 entries are allowed for the NTP server
            address list.
    """

    time_zone: str | Unset = UNSET
    dst: SiteSettingdst | Unset = UNSET
    ntp_enable: bool | Unset = UNSET
    ntp_servers: list[NtpServer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_zone = self.time_zone

        dst: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dst, Unset):
            dst = self.dst.to_dict()

        ntp_enable = self.ntp_enable

        ntp_servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ntp_servers, Unset):
            ntp_servers = []
            for ntp_servers_item_data in self.ntp_servers:
                ntp_servers_item = ntp_servers_item_data.to_dict()
                ntp_servers.append(ntp_servers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if dst is not UNSET:
            field_dict["dst"] = dst
        if ntp_enable is not UNSET:
            field_dict["ntpEnable"] = ntp_enable
        if ntp_servers is not UNSET:
            field_dict["ntpServers"] = ntp_servers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ntp_server import NtpServer
        from ..models.site_settingdst import SiteSettingdst

        d = dict(src_dict)
        time_zone = d.pop("timeZone", UNSET)

        _dst = d.pop("dst", UNSET)
        dst: SiteSettingdst | Unset
        if isinstance(_dst, Unset):
            dst = UNSET
        else:
            dst = SiteSettingdst.from_dict(_dst)

        ntp_enable = d.pop("ntpEnable", UNSET)

        _ntp_servers = d.pop("ntpServers", UNSET)
        ntp_servers: list[NtpServer] | Unset = UNSET
        if _ntp_servers is not UNSET:
            ntp_servers = []
            for ntp_servers_item_data in _ntp_servers:
                ntp_servers_item = NtpServer.from_dict(ntp_servers_item_data)

                ntp_servers.append(ntp_servers_item)

        site_template_open_api_vo = cls(
            time_zone=time_zone,
            dst=dst,
            ntp_enable=ntp_enable,
            ntp_servers=ntp_servers,
        )

        site_template_open_api_vo.additional_properties = d
        return site_template_open_api_vo

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
