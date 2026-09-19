from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_server import NtpServer
    from ..models.site_settingdst import SiteSettingdst


T = TypeVar("T", bound="SiteTemplateSettings")


@_attrs_define
class SiteTemplateSettings:
    """
    Attributes:
        id (str | Unset): site template id
        omadac_id (str | Unset): omadacId
        name (str | Unset): site template name
        time_zone (str | Unset): time zone
        dst (SiteSettingdst | Unset): Daylight Saving Time.
        ntp_enable (bool | Unset): Network Time Protocol enable
        ntp_servers (list[NtpServer] | Unset): ntp servers
        type_ (int | Unset): site type. 0：Basic；1：Pro
        settings (list[str] | Unset): list of supported configurations
    """

    id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    name: str | Unset = UNSET
    time_zone: str | Unset = UNSET
    dst: SiteSettingdst | Unset = UNSET
    ntp_enable: bool | Unset = UNSET
    ntp_servers: list[NtpServer] | Unset = UNSET
    type_: int | Unset = UNSET
    settings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        omadac_id = self.omadac_id

        name = self.name

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

        type_ = self.type_

        settings: list[str] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if name is not UNSET:
            field_dict["name"] = name
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if dst is not UNSET:
            field_dict["dst"] = dst
        if ntp_enable is not UNSET:
            field_dict["ntpEnable"] = ntp_enable
        if ntp_servers is not UNSET:
            field_dict["ntpServers"] = ntp_servers
        if type_ is not UNSET:
            field_dict["type"] = type_
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ntp_server import NtpServer
        from ..models.site_settingdst import SiteSettingdst

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        name = d.pop("name", UNSET)

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

        type_ = d.pop("type", UNSET)

        settings = cast(list[str], d.pop("settings", UNSET))

        site_template_settings = cls(
            id=id,
            omadac_id=omadac_id,
            name=name,
            time_zone=time_zone,
            dst=dst,
            ntp_enable=ntp_enable,
            ntp_servers=ntp_servers,
            type_=type_,
            settings=settings,
        )

        site_template_settings.additional_properties = d
        return site_template_settings

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
