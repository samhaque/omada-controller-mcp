from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retry import Retry


T = TypeVar("T", bound="RetryEap")


@_attrs_define
class RetryEap:
    """AP list of retransmission packet rates tab, in descending order of average

    Attributes:
        retries (list[Retry] | Unset): AP retries timing list
        ap_mac (str | Unset): AP MAC
        name (str | Unset): AP name
        model (str | Unset): AP model
        model_version (str | Unset): AP model Version
        avg (float | Unset): Average current AP retransmission packet rate
        status (int | Unset): AP status, 0: connected, 1: disconnected
    """

    retries: list[Retry] | Unset = UNSET
    ap_mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    avg: float | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.retries, Unset):
            retries = []
            for retries_item_data in self.retries:
                retries_item = retries_item_data.to_dict()
                retries.append(retries_item)

        ap_mac = self.ap_mac

        name = self.name

        model = self.model

        model_version = self.model_version

        avg = self.avg

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retries is not UNSET:
            field_dict["retries"] = retries
        if ap_mac is not UNSET:
            field_dict["apMac"] = ap_mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if avg is not UNSET:
            field_dict["avg"] = avg
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.retry import Retry

        d = dict(src_dict)
        _retries = d.pop("retries", UNSET)
        retries: list[Retry] | Unset = UNSET
        if _retries is not UNSET:
            retries = []
            for retries_item_data in _retries:
                retries_item = Retry.from_dict(retries_item_data)

                retries.append(retries_item)

        ap_mac = d.pop("apMac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        avg = d.pop("avg", UNSET)

        status = d.pop("status", UNSET)

        retry_eap = cls(
            retries=retries,
            ap_mac=ap_mac,
            name=name,
            model=model,
            model_version=model_version,
            avg=avg,
            status=status,
        )

        retry_eap.additional_properties = d
        return retry_eap

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
