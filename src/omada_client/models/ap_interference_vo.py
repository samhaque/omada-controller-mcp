from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApInterferenceVO")


@_attrs_define
class ApInterferenceVO:
    """
    Attributes:
        device (str | Unset): Device name
        model (str | Unset): Device model
        model_version (str | Unset): Device model version
        type_ (str | Unset): Device type should be a value as follows: ap.
        interference (int | Unset): Degree of interference. interference = interUtil/(interUtil+txUtil+rxUtil)
        inter_util (int | Unset): Channel interference rate
        tx_util (int | Unset): Transmit channel utilization
        rx_util (int | Unset): Receive channel utilization
    """

    device: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    interference: int | Unset = UNSET
    inter_util: int | Unset = UNSET
    tx_util: int | Unset = UNSET
    rx_util: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device = self.device

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        interference = self.interference

        inter_util = self.inter_util

        tx_util = self.tx_util

        rx_util = self.rx_util

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
        if interference is not UNSET:
            field_dict["interference"] = interference
        if inter_util is not UNSET:
            field_dict["interUtil"] = inter_util
        if tx_util is not UNSET:
            field_dict["txUtil"] = tx_util
        if rx_util is not UNSET:
            field_dict["rxUtil"] = rx_util

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device = d.pop("device", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        interference = d.pop("interference", UNSET)

        inter_util = d.pop("interUtil", UNSET)

        tx_util = d.pop("txUtil", UNSET)

        rx_util = d.pop("rxUtil", UNSET)

        ap_interference_vo = cls(
            device=device,
            model=model,
            model_version=model_version,
            type_=type_,
            interference=interference,
            inter_util=inter_util,
            tx_util=tx_util,
            rx_util=rx_util,
        )

        ap_interference_vo.additional_properties = d
        return ap_interference_vo

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
