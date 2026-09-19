from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspUiInterfaceOpenApiVO")


@_attrs_define
class MspUiInterfaceOpenApiVO:
    """
    Attributes:
        use24hour (bool):
        fixed_menu (bool):
        refresh_btn_enable (bool): Enable refresh button
        refresh_rate (int): It should be a value as follows: 0: 15 seconds; 1: 1 minute; 2: 2 minutes; 3: 5 minutes; 4:
            never refresh
        websocket_enable (bool): Enable websocket connection
        language (int | Unset): It should be a value as follows: 1: English; 4: German; 7: French; 8: Spanish; 10:
            Italian; 12: Portuguese; 13: Russian; 15: Turkish; 17: Japanese; 18: Traditional Chinese; 21: Korean
        theme (int | Unset): It should be a value as follows: 0: default; 1: dark
        show_p_devices (bool | Unset): Show pending devices
        controller_notification (bool | Unset): Enable controller upgrade notification
        private_labeling_enable (bool | Unset): Enable private label
        private_labeling_url (str | Unset): The url of private label
        private_labeling_file_id (str | Unset): The file id of private label picture
        private_labeling_file_name (str | Unset): The file name of private label picture
    """

    use24hour: bool
    fixed_menu: bool
    refresh_btn_enable: bool
    refresh_rate: int
    websocket_enable: bool
    language: int | Unset = UNSET
    theme: int | Unset = UNSET
    show_p_devices: bool | Unset = UNSET
    controller_notification: bool | Unset = UNSET
    private_labeling_enable: bool | Unset = UNSET
    private_labeling_url: str | Unset = UNSET
    private_labeling_file_id: str | Unset = UNSET
    private_labeling_file_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        use24hour = self.use24hour

        fixed_menu = self.fixed_menu

        refresh_btn_enable = self.refresh_btn_enable

        refresh_rate = self.refresh_rate

        websocket_enable = self.websocket_enable

        language = self.language

        theme = self.theme

        show_p_devices = self.show_p_devices

        controller_notification = self.controller_notification

        private_labeling_enable = self.private_labeling_enable

        private_labeling_url = self.private_labeling_url

        private_labeling_file_id = self.private_labeling_file_id

        private_labeling_file_name = self.private_labeling_file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "use24hour": use24hour,
                "fixedMenu": fixed_menu,
                "refreshBtnEnable": refresh_btn_enable,
                "refreshRate": refresh_rate,
                "websocketEnable": websocket_enable,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if theme is not UNSET:
            field_dict["theme"] = theme
        if show_p_devices is not UNSET:
            field_dict["showPDevices"] = show_p_devices
        if controller_notification is not UNSET:
            field_dict["controllerNotification"] = controller_notification
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
        use24hour = d.pop("use24hour")

        fixed_menu = d.pop("fixedMenu")

        refresh_btn_enable = d.pop("refreshBtnEnable")

        refresh_rate = d.pop("refreshRate")

        websocket_enable = d.pop("websocketEnable")

        language = d.pop("language", UNSET)

        theme = d.pop("theme", UNSET)

        show_p_devices = d.pop("showPDevices", UNSET)

        controller_notification = d.pop("controllerNotification", UNSET)

        private_labeling_enable = d.pop("privateLabelingEnable", UNSET)

        private_labeling_url = d.pop("privateLabelingUrl", UNSET)

        private_labeling_file_id = d.pop("privateLabelingFileId", UNSET)

        private_labeling_file_name = d.pop("privateLabelingFileName", UNSET)

        msp_ui_interface_open_api_vo = cls(
            use24hour=use24hour,
            fixed_menu=fixed_menu,
            refresh_btn_enable=refresh_btn_enable,
            refresh_rate=refresh_rate,
            websocket_enable=websocket_enable,
            language=language,
            theme=theme,
            show_p_devices=show_p_devices,
            controller_notification=controller_notification,
            private_labeling_enable=private_labeling_enable,
            private_labeling_url=private_labeling_url,
            private_labeling_file_id=private_labeling_file_id,
            private_labeling_file_name=private_labeling_file_name,
        )

        msp_ui_interface_open_api_vo.additional_properties = d
        return msp_ui_interface_open_api_vo

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
