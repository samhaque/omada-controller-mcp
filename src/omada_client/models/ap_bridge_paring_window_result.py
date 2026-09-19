from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_bridge_client_ap_open_api_vo import ApBridgeClientApOpenApiVO


T = TypeVar("T", bound="APBridgeParingWindowResult")


@_attrs_define
class APBridgeParingWindowResult:
    """
    Attributes:
        status (int | Unset):
        countdown (int | Unset):
        client_aps (list[ApBridgeClientApOpenApiVO] | Unset):
    """

    status: int | Unset = UNSET
    countdown: int | Unset = UNSET
    client_aps: list[ApBridgeClientApOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        countdown = self.countdown

        client_aps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_aps, Unset):
            client_aps = []
            for client_aps_item_data in self.client_aps:
                client_aps_item = client_aps_item_data.to_dict()
                client_aps.append(client_aps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if countdown is not UNSET:
            field_dict["countdown"] = countdown
        if client_aps is not UNSET:
            field_dict["clientAps"] = client_aps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_bridge_client_ap_open_api_vo import (
            ApBridgeClientApOpenApiVO,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        countdown = d.pop("countdown", UNSET)

        _client_aps = d.pop("clientAps", UNSET)
        client_aps: list[ApBridgeClientApOpenApiVO] | Unset = UNSET
        if _client_aps is not UNSET:
            client_aps = []
            for client_aps_item_data in _client_aps:
                client_aps_item = ApBridgeClientApOpenApiVO.from_dict(
                    client_aps_item_data
                )

                client_aps.append(client_aps_item)

        ap_bridge_paring_window_result = cls(
            status=status,
            countdown=countdown,
            client_aps=client_aps,
        )

        ap_bridge_paring_window_result.additional_properties = d
        return ap_bridge_paring_window_result

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
