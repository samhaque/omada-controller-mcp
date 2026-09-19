from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnFailureApVO")


@_attrs_define
class ConnFailureApVO:
    """Top AP by connection failure on 6G band

    Attributes:
        device (str | Unset): Device name
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        type_ (str | Unset): Device type
        mac (str | Unset): Device mac
        failure_rate (int | Unset): Connection failure percentage (0-100)
        failure_num (int | Unset): Connection failure count
        success_num (int | Unset): Connection success count
    """

    device: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    failure_rate: int | Unset = UNSET
    failure_num: int | Unset = UNSET
    success_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        mac = self.mac

        failure_rate = self.failure_rate

        failure_num = self.failure_num

        success_num = self.success_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if failure_rate is not UNSET:
            field_dict["failureRate"] = failure_rate
        if failure_num is not UNSET:
            field_dict["failureNum"] = failure_num
        if success_num is not UNSET:
            field_dict["successNum"] = success_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device = d.pop("device", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        failure_rate = d.pop("failureRate", UNSET)

        failure_num = d.pop("failureNum", UNSET)

        success_num = d.pop("successNum", UNSET)

        conn_failure_ap_vo = cls(
            device=device,
            model=model,
            model_version=model_version,
            type_=type_,
            mac=mac,
            failure_rate=failure_rate,
            failure_num=failure_num,
            success_num=success_num,
        )

        conn_failure_ap_vo.additional_properties = d
        return conn_failure_ap_vo

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
