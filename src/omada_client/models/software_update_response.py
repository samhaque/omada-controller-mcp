from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SoftwareUpdateResponse")


@_attrs_define
class SoftwareUpdateResponse:
    """Upgrade List

    Attributes:
        channel (int | Unset): Channel should be a value as follows: 0: stable; 1: Release Candidate(RC); 2: Beta
        update (bool | Unset): Update should be a value as follows: true: A new version is available for upgrade; false
            or null: running the latest version;
        latest_version (str | Unset): Latest version
        download_url (str | Unset): Download url of new version
        release_log (str | Unset): Release log of new version
    """

    channel: int | Unset = UNSET
    update: bool | Unset = UNSET
    latest_version: str | Unset = UNSET
    download_url: str | Unset = UNSET
    release_log: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        update = self.update

        latest_version = self.latest_version

        download_url = self.download_url

        release_log = self.release_log

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if update is not UNSET:
            field_dict["update"] = update
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if release_log is not UNSET:
            field_dict["releaseLog"] = release_log

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        update = d.pop("update", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        release_log = d.pop("releaseLog", UNSET)

        software_update_response = cls(
            channel=channel,
            update=update,
            latest_version=latest_version,
            download_url=download_url,
            release_log=release_log,
        )

        software_update_response.additional_properties = d
        return software_update_response

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
