from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientTypeStatVO")


@_attrs_define
class ClientTypeStatVO:
    """
    Attributes:
        total (int | Unset):
        mobile (int | Unset):
        office (int | Unset):
        camera (int | Unset):
        audio_video (int | Unset):
        smart_home (int | Unset):
        network (int | Unset):
        other (int | Unset):
    """

    total: int | Unset = UNSET
    mobile: int | Unset = UNSET
    office: int | Unset = UNSET
    camera: int | Unset = UNSET
    audio_video: int | Unset = UNSET
    smart_home: int | Unset = UNSET
    network: int | Unset = UNSET
    other: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        mobile = self.mobile

        office = self.office

        camera = self.camera

        audio_video = self.audio_video

        smart_home = self.smart_home

        network = self.network

        other = self.other

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if office is not UNSET:
            field_dict["office"] = office
        if camera is not UNSET:
            field_dict["camera"] = camera
        if audio_video is not UNSET:
            field_dict["audioVideo"] = audio_video
        if smart_home is not UNSET:
            field_dict["smartHome"] = smart_home
        if network is not UNSET:
            field_dict["network"] = network
        if other is not UNSET:
            field_dict["other"] = other

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        mobile = d.pop("mobile", UNSET)

        office = d.pop("office", UNSET)

        camera = d.pop("camera", UNSET)

        audio_video = d.pop("audioVideo", UNSET)

        smart_home = d.pop("smartHome", UNSET)

        network = d.pop("network", UNSET)

        other = d.pop("other", UNSET)

        client_type_stat_vo = cls(
            total=total,
            mobile=mobile,
            office=office,
            camera=camera,
            audio_video=audio_video,
            smart_home=smart_home,
            network=network,
            other=other,
        )

        client_type_stat_vo.additional_properties = d
        return client_type_stat_vo

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
