from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnownClientVO")


@_attrs_define
class KnownClientVO:
    """
    Attributes:
        name (str | Unset):
        mac (str | Unset):
        wireless (bool | Unset):
        guest (bool | Unset):
        download (int | Unset):
        upload (int | Unset):
        duration (int | Unset):
        last_seen (int | Unset):
        block (bool | Unset):
        manager (bool | Unset):
        lock_to_ap (bool | Unset):
        block_disable (bool | Unset):
        vid (int | Unset):
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    guest: bool | Unset = UNSET
    download: int | Unset = UNSET
    upload: int | Unset = UNSET
    duration: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    block: bool | Unset = UNSET
    manager: bool | Unset = UNSET
    lock_to_ap: bool | Unset = UNSET
    block_disable: bool | Unset = UNSET
    vid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        wireless = self.wireless

        guest = self.guest

        download = self.download

        upload = self.upload

        duration = self.duration

        last_seen = self.last_seen

        block = self.block

        manager = self.manager

        lock_to_ap = self.lock_to_ap

        block_disable = self.block_disable

        vid = self.vid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if guest is not UNSET:
            field_dict["guest"] = guest
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if duration is not UNSET:
            field_dict["duration"] = duration
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if block is not UNSET:
            field_dict["block"] = block
        if manager is not UNSET:
            field_dict["manager"] = manager
        if lock_to_ap is not UNSET:
            field_dict["lockToAp"] = lock_to_ap
        if block_disable is not UNSET:
            field_dict["blockDisable"] = block_disable
        if vid is not UNSET:
            field_dict["vid"] = vid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        wireless = d.pop("wireless", UNSET)

        guest = d.pop("guest", UNSET)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        duration = d.pop("duration", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        block = d.pop("block", UNSET)

        manager = d.pop("manager", UNSET)

        lock_to_ap = d.pop("lockToAp", UNSET)

        block_disable = d.pop("blockDisable", UNSET)

        vid = d.pop("vid", UNSET)

        known_client_vo = cls(
            name=name,
            mac=mac,
            wireless=wireless,
            guest=guest,
            download=download,
            upload=upload,
            duration=duration,
            last_seen=last_seen,
            block=block,
            manager=manager,
            lock_to_ap=lock_to_ap,
            block_disable=block_disable,
            vid=vid,
        )

        known_client_vo.additional_properties = d
        return known_client_vo

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
