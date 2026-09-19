from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UIInterface")


@_attrs_define
class UIInterface:
    """
    Attributes:
        refresh_rate (int): Refresh rate should be a value as follows: 0: 15 seconds;1: 1 minute; 2: 2 minutes; 3: 5
            minutes; 4: never refresh.
        time_zone (int | Unset): Time zone should be a value as follows: 0: Site's; 1: Browser's; 2: Controller's; 3:
            UTC
        private_labeling_enable (bool | Unset): Enable customer labeling of controller, this configuration applies to
            Omada Pro Controller only
        private_labeling_url (str | Unset): The redirection url of labeling image, this configuration applies to Omada
            Pro Controller only
        private_labeling_file_id (str | Unset): The file id of labeling image, this configuration applies to Omada Pro
            Controller only
        private_labeling_file_name (str | Unset): The file name of labeling image, this configuration applies to Omada
            Pro Controller only
        mac_format (int | Unset):
    """

    refresh_rate: int
    time_zone: int | Unset = UNSET
    private_labeling_enable: bool | Unset = UNSET
    private_labeling_url: str | Unset = UNSET
    private_labeling_file_id: str | Unset = UNSET
    private_labeling_file_name: str | Unset = UNSET
    mac_format: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refresh_rate = self.refresh_rate

        time_zone = self.time_zone

        private_labeling_enable = self.private_labeling_enable

        private_labeling_url = self.private_labeling_url

        private_labeling_file_id = self.private_labeling_file_id

        private_labeling_file_name = self.private_labeling_file_name

        mac_format = self.mac_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refreshRate": refresh_rate,
            }
        )
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if private_labeling_enable is not UNSET:
            field_dict["privateLabelingEnable"] = private_labeling_enable
        if private_labeling_url is not UNSET:
            field_dict["privateLabelingUrl"] = private_labeling_url
        if private_labeling_file_id is not UNSET:
            field_dict["privateLabelingFileId"] = private_labeling_file_id
        if private_labeling_file_name is not UNSET:
            field_dict["privateLabelingFileName"] = private_labeling_file_name
        if mac_format is not UNSET:
            field_dict["macFormat"] = mac_format

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        refresh_rate = d.pop("refreshRate")

        time_zone = d.pop("timeZone", UNSET)

        private_labeling_enable = d.pop("privateLabelingEnable", UNSET)

        private_labeling_url = d.pop("privateLabelingUrl", UNSET)

        private_labeling_file_id = d.pop("privateLabelingFileId", UNSET)

        private_labeling_file_name = d.pop("privateLabelingFileName", UNSET)

        mac_format = d.pop("macFormat", UNSET)

        ui_interface = cls(
            refresh_rate=refresh_rate,
            time_zone=time_zone,
            private_labeling_enable=private_labeling_enable,
            private_labeling_url=private_labeling_url,
            private_labeling_file_id=private_labeling_file_id,
            private_labeling_file_name=private_labeling_file_name,
            mac_format=mac_format,
        )

        ui_interface.additional_properties = d
        return ui_interface

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
