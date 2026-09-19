from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_device import ActiveDevice


T = TypeVar("T", bound="GetActiveDeviceV2OpenApiVO")


@_attrs_define
class GetActiveDeviceV2OpenApiVO:
    """
    Attributes:
        active_aps (list[ActiveDevice] | Unset): Most Active APs devices by traffic
        total_traffic (float | Unset): The sum of the traffic of all AP devices under the site
    """

    active_aps: list[ActiveDevice] | Unset = UNSET
    total_traffic: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_aps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active_aps, Unset):
            active_aps = []
            for active_aps_item_data in self.active_aps:
                active_aps_item = active_aps_item_data.to_dict()
                active_aps.append(active_aps_item)

        total_traffic = self.total_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_aps is not UNSET:
            field_dict["activeAps"] = active_aps
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.active_device import ActiveDevice

        d = dict(src_dict)
        _active_aps = d.pop("activeAps", UNSET)
        active_aps: list[ActiveDevice] | Unset = UNSET
        if _active_aps is not UNSET:
            active_aps = []
            for active_aps_item_data in _active_aps:
                active_aps_item = ActiveDevice.from_dict(active_aps_item_data)

                active_aps.append(active_aps_item)

        total_traffic = d.pop("totalTraffic", UNSET)

        get_active_device_v2_open_api_vo = cls(
            active_aps=active_aps,
            total_traffic=total_traffic,
        )

        get_active_device_v2_open_api_vo.additional_properties = d
        return get_active_device_v2_open_api_vo

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
