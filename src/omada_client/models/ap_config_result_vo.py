from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_config_result_settings_vo import ApConfigResultSettingsVO


T = TypeVar("T", bound="ApConfigResultVO")


@_attrs_define
class ApConfigResultVO:
    """Configuration results for devices with partial or complete configuration failures.

    Attributes:
        type_ (str | Unset): Device type:ap、gateway、switch、olt
        mac (str | Unset): Device mac
        name (str | Unset): Device name,default value is the mac address of device
        status (int | Unset): Status of device,status should be a value as follows: 0:Disconnected;1:Disconnected(Migrat
            ing);10:Provisioning;11:Configuring;12:Upgrading;13:Rebooting;14:Connected;15:Connected(Wireless);16:Connected(M
            igrating);17:Connected(Wireless,Migrating);20:Pending;21:Pending(Wireless);22:Adopting;23:Adopting(Wireless);24:
            Adopt Failed;25:Adopt Failed(Wireless);26:Managed By Others;27:Managed By Others(Wireless);30:Heartbeat
            Missed;31:Heartbeat Missed(Wireless);32:Heartbeat Missed(Migrating);33:Heartbeat
            Missed(Wireless,Migrating);40:Isolated;41:Isolated(Migrating);50:Slice Configuring
        status_category (int | Unset): Category of device status,statusCategory should be a value as follows:
            0:Disconnected;1:Connected;2:Pending;3:Heartbeat Missed;4:Isolated
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
        error_code (int | Unset): error code.
        msg (str | Unset): error msg
        ap_config_result_settings (ApConfigResultSettingsVO | Unset): ap config result detail setting.
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    error_code: int | Unset = UNSET
    msg: str | Unset = UNSET
    ap_config_result_settings: ApConfigResultSettingsVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        status = self.status

        status_category = self.status_category

        model = self.model

        model_version = self.model_version

        error_code = self.error_code

        msg = self.msg

        ap_config_result_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap_config_result_settings, Unset):
            ap_config_result_settings = self.ap_config_result_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if msg is not UNSET:
            field_dict["msg"] = msg
        if ap_config_result_settings is not UNSET:
            field_dict["apConfigResultSettings"] = ap_config_result_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_config_result_settings_vo import (
            ApConfigResultSettingsVO,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        error_code = d.pop("errorCode", UNSET)

        msg = d.pop("msg", UNSET)

        _ap_config_result_settings = d.pop("apConfigResultSettings", UNSET)
        ap_config_result_settings: ApConfigResultSettingsVO | Unset
        if isinstance(_ap_config_result_settings, Unset):
            ap_config_result_settings = UNSET
        else:
            ap_config_result_settings = ApConfigResultSettingsVO.from_dict(
                _ap_config_result_settings
            )

        ap_config_result_vo = cls(
            type_=type_,
            mac=mac,
            name=name,
            status=status,
            status_category=status_category,
            model=model,
            model_version=model_version,
            error_code=error_code,
            msg=msg,
            ap_config_result_settings=ap_config_result_settings,
        )

        ap_config_result_vo.additional_properties = d
        return ap_config_result_vo

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
