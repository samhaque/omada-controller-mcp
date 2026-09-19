from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopModelBaseVO")


@_attrs_define
class TopModelBaseVO:
    """
    Attributes:
        device (str | Unset): Device name
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        ip (str | Unset): Device IP
        model_type (str | Unset):
        type_ (str | Unset): Device type should be a value as follows: ap; switch
        status (int | Unset): Device status should be a value as follows: 0:DISCONNECTED, 1:CONNECTED, 2:PENDING,
            3:HEARTBEAT MISSED, 4: ISOLATED
        health (int | Unset): Device health core
        mac (str | Unset): Device mac
        util (int | Unset): Utilization
        traffic (int | Unset): Total traffic
        ratio (int | Unset): Percent
        poe_power (int | Unset): POE power
        client_count (int | Unset): Count of clients
    """

    device: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    ip: str | Unset = UNSET
    model_type: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: int | Unset = UNSET
    health: int | Unset = UNSET
    mac: str | Unset = UNSET
    util: int | Unset = UNSET
    traffic: int | Unset = UNSET
    ratio: int | Unset = UNSET
    poe_power: int | Unset = UNSET
    client_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device

        model = self.model

        model_version = self.model_version

        ip = self.ip

        model_type = self.model_type

        type_ = self.type_

        status = self.status

        health = self.health

        mac = self.mac

        util = self.util

        traffic = self.traffic

        ratio = self.ratio

        poe_power = self.poe_power

        client_count = self.client_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if model_type is not UNSET:
            field_dict["modelType"] = model_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if health is not UNSET:
            field_dict["health"] = health
        if mac is not UNSET:
            field_dict["mac"] = mac
        if util is not UNSET:
            field_dict["util"] = util
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if ratio is not UNSET:
            field_dict["ratio"] = ratio
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power
        if client_count is not UNSET:
            field_dict["clientCount"] = client_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device = d.pop("device", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        ip = d.pop("ip", UNSET)

        model_type = d.pop("modelType", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        health = d.pop("health", UNSET)

        mac = d.pop("mac", UNSET)

        util = d.pop("util", UNSET)

        traffic = d.pop("traffic", UNSET)

        ratio = d.pop("ratio", UNSET)

        poe_power = d.pop("poePower", UNSET)

        client_count = d.pop("clientCount", UNSET)

        top_model_base_vo = cls(
            device=device,
            model=model,
            model_version=model_version,
            ip=ip,
            model_type=model_type,
            type_=type_,
            status=status,
            health=health,
            mac=mac,
            util=util,
            traffic=traffic,
            ratio=ratio,
            poe_power=poe_power,
            client_count=client_count,
        )

        top_model_base_vo.additional_properties = d
        return top_model_base_vo

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
