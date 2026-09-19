from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTemplateOpenApiQueryVO")


@_attrs_define
class DeviceTemplateOpenApiQueryVO:
    """
    Attributes:
        id (str | Unset):
        template_name (str | Unset):
        model (str | Unset):
        model_version (str | Unset):
        show_model (str | Unset):
        device_type (str | Unset):
        bind_device_num (int | Unset):
        override (str | Unset):
        wireless_router (bool | Unset):
        auto_bind (bool | Unset):
        status (int | Unset):
        multi_bind (bool | Unset):
        switch_type (int | Unset):
        template_settings (list[int] | Unset):
    """

    id: str | Unset = UNSET
    template_name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    device_type: str | Unset = UNSET
    bind_device_num: int | Unset = UNSET
    override: str | Unset = UNSET
    wireless_router: bool | Unset = UNSET
    auto_bind: bool | Unset = UNSET
    status: int | Unset = UNSET
    multi_bind: bool | Unset = UNSET
    switch_type: int | Unset = UNSET
    template_settings: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_name = self.template_name

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        device_type = self.device_type

        bind_device_num = self.bind_device_num

        override = self.override

        wireless_router = self.wireless_router

        auto_bind = self.auto_bind

        status = self.status

        multi_bind = self.multi_bind

        switch_type = self.switch_type

        template_settings: list[int] | Unset = UNSET
        if not isinstance(self.template_settings, Unset):
            template_settings = self.template_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if bind_device_num is not UNSET:
            field_dict["bindDeviceNum"] = bind_device_num
        if override is not UNSET:
            field_dict["override"] = override
        if wireless_router is not UNSET:
            field_dict["wirelessRouter"] = wireless_router
        if auto_bind is not UNSET:
            field_dict["autoBind"] = auto_bind
        if status is not UNSET:
            field_dict["status"] = status
        if multi_bind is not UNSET:
            field_dict["multiBind"] = multi_bind
        if switch_type is not UNSET:
            field_dict["switchType"] = switch_type
        if template_settings is not UNSET:
            field_dict["templateSettings"] = template_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        template_name = d.pop("templateName", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        device_type = d.pop("deviceType", UNSET)

        bind_device_num = d.pop("bindDeviceNum", UNSET)

        override = d.pop("override", UNSET)

        wireless_router = d.pop("wirelessRouter", UNSET)

        auto_bind = d.pop("autoBind", UNSET)

        status = d.pop("status", UNSET)

        multi_bind = d.pop("multiBind", UNSET)

        switch_type = d.pop("switchType", UNSET)

        template_settings = cast(list[int], d.pop("templateSettings", UNSET))

        device_template_open_api_query_vo = cls(
            id=id,
            template_name=template_name,
            model=model,
            model_version=model_version,
            show_model=show_model,
            device_type=device_type,
            bind_device_num=bind_device_num,
            override=override,
            wireless_router=wireless_router,
            auto_bind=auto_bind,
            status=status,
            multi_bind=multi_bind,
            switch_type=switch_type,
            template_settings=template_settings,
        )

        device_template_open_api_query_vo.additional_properties = d
        return device_template_open_api_query_vo

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
