from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspUserInterfaceOpenApiVO")


@_attrs_define
class MspUserInterfaceOpenApiVO:
    """
    Attributes:
        refresh_rate (int): It should be a value as follows: 0: 15 seconds; 1: 1 minute; 2: 2 minutes; 3: 5 minutes; 4:
            never refresh
        private_labeling_enable (bool | Unset): Enable private label. This field applies to the Omada Pro Controller
            only.
        private_labeling_url (str | Unset): The url of private label. This field applies to the Omada Pro Controller
            only.
        private_labeling_file_id (str | Unset): The file id of private label picture. This field applies to the Omada
            Pro Controller only.
        private_labeling_file_name (str | Unset): The file name of private label picture. This field applies to the
            Omada Pro Controller only.
    """

    refresh_rate: int
    private_labeling_enable: bool | Unset = UNSET
    private_labeling_url: str | Unset = UNSET
    private_labeling_file_id: str | Unset = UNSET
    private_labeling_file_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refresh_rate = self.refresh_rate

        private_labeling_enable = self.private_labeling_enable

        private_labeling_url = self.private_labeling_url

        private_labeling_file_id = self.private_labeling_file_id

        private_labeling_file_name = self.private_labeling_file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refreshRate": refresh_rate,
            }
        )
        if private_labeling_enable is not UNSET:
            field_dict["privateLabelingEnable"] = private_labeling_enable
        if private_labeling_url is not UNSET:
            field_dict["privateLabelingUrl"] = private_labeling_url
        if private_labeling_file_id is not UNSET:
            field_dict["privateLabelingFileId"] = private_labeling_file_id
        if private_labeling_file_name is not UNSET:
            field_dict["privateLabelingFileName"] = private_labeling_file_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        refresh_rate = d.pop("refreshRate")

        private_labeling_enable = d.pop("privateLabelingEnable", UNSET)

        private_labeling_url = d.pop("privateLabelingUrl", UNSET)

        private_labeling_file_id = d.pop("privateLabelingFileId", UNSET)

        private_labeling_file_name = d.pop("privateLabelingFileName", UNSET)

        msp_user_interface_open_api_vo = cls(
            refresh_rate=refresh_rate,
            private_labeling_enable=private_labeling_enable,
            private_labeling_url=private_labeling_url,
            private_labeling_file_id=private_labeling_file_id,
            private_labeling_file_name=private_labeling_file_name,
        )

        msp_user_interface_open_api_vo.additional_properties = d
        return msp_user_interface_open_api_vo

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
