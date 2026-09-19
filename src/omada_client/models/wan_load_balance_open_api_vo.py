from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_weight_open_api_vo import VirtualWanWeightOpenApiVO


T = TypeVar("T", bound="WanLoadBalanceOpenApiVO")


@_attrs_define
class WanLoadBalanceOpenApiVO:
    """
    Attributes:
        weights (list[int]): Load Balancing Weights,item of weights should be within the range of 1 to the max int
            value(2147483647). It is sorted by port ID.
        app_opt_routing (bool): Application Optimized Routing
        link_backup (bool): Link Backup
        method (str | Unset): effective only for 'linkBackup: true'
        primary_wans (list[str] | Unset): Primary WAN port IDs. It is required when [linkBackup] is true.
        backup_wan (str | Unset): Backup WAN ID. It is required when [linkBackup] is true.
        backup_mode (int | Unset): It is required when [linkBackup] is true. 0: The system will try to forward the
            traffic via the backup WAN port when primary WAN fails. Even if the primary WAN is recovered, it will not switch
            back unless the backup WAN fails; 1: Traffic is always forwarded through the primary WAN port unless it fails.
            The system will try to forward the traffic via the backup WAN port when it fails, and switch back when it
            recovers.
        mode (int | Unset): It is required when [linkBackup] is true. 0: Enable backup link when any primary WAN fails.
            1: Enable backup link when all primary WANs fail. 2: Timing
        time_range_id (str | Unset): Time Range ID. It is required when [mode] is timing.
        virtual_wan_weights (list[VirtualWanWeightOpenApiVO] | Unset): virtual wan load balance
    """

    weights: list[int]
    app_opt_routing: bool
    link_backup: bool
    method: str | Unset = UNSET
    primary_wans: list[str] | Unset = UNSET
    backup_wan: str | Unset = UNSET
    backup_mode: int | Unset = UNSET
    mode: int | Unset = UNSET
    time_range_id: str | Unset = UNSET
    virtual_wan_weights: list[VirtualWanWeightOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weights = self.weights

        app_opt_routing = self.app_opt_routing

        link_backup = self.link_backup

        method = self.method

        primary_wans: list[str] | Unset = UNSET
        if not isinstance(self.primary_wans, Unset):
            primary_wans = self.primary_wans

        backup_wan = self.backup_wan

        backup_mode = self.backup_mode

        mode = self.mode

        time_range_id = self.time_range_id

        virtual_wan_weights: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.virtual_wan_weights, Unset):
            virtual_wan_weights = []
            for virtual_wan_weights_item_data in self.virtual_wan_weights:
                virtual_wan_weights_item = virtual_wan_weights_item_data.to_dict()
                virtual_wan_weights.append(virtual_wan_weights_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weights": weights,
                "appOptRouting": app_opt_routing,
                "linkBackup": link_backup,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if primary_wans is not UNSET:
            field_dict["primaryWans"] = primary_wans
        if backup_wan is not UNSET:
            field_dict["backupWan"] = backup_wan
        if backup_mode is not UNSET:
            field_dict["backupMode"] = backup_mode
        if mode is not UNSET:
            field_dict["mode"] = mode
        if time_range_id is not UNSET:
            field_dict["timeRangeId"] = time_range_id
        if virtual_wan_weights is not UNSET:
            field_dict["virtualWanWeights"] = virtual_wan_weights

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_weight_open_api_vo import (
            VirtualWanWeightOpenApiVO,
        )

        d = dict(src_dict)
        weights = cast(list[int], d.pop("weights"))

        app_opt_routing = d.pop("appOptRouting")

        link_backup = d.pop("linkBackup")

        method = d.pop("method", UNSET)

        primary_wans = cast(list[str], d.pop("primaryWans", UNSET))

        backup_wan = d.pop("backupWan", UNSET)

        backup_mode = d.pop("backupMode", UNSET)

        mode = d.pop("mode", UNSET)

        time_range_id = d.pop("timeRangeId", UNSET)

        _virtual_wan_weights = d.pop("virtualWanWeights", UNSET)
        virtual_wan_weights: list[VirtualWanWeightOpenApiVO] | Unset = UNSET
        if _virtual_wan_weights is not UNSET:
            virtual_wan_weights = []
            for virtual_wan_weights_item_data in _virtual_wan_weights:
                virtual_wan_weights_item = VirtualWanWeightOpenApiVO.from_dict(
                    virtual_wan_weights_item_data
                )

                virtual_wan_weights.append(virtual_wan_weights_item)

        wan_load_balance_open_api_vo = cls(
            weights=weights,
            app_opt_routing=app_opt_routing,
            link_backup=link_backup,
            method=method,
            primary_wans=primary_wans,
            backup_wan=backup_wan,
            backup_mode=backup_mode,
            mode=mode,
            time_range_id=time_range_id,
            virtual_wan_weights=virtual_wan_weights,
        )

        wan_load_balance_open_api_vo.additional_properties = d
        return wan_load_balance_open_api_vo

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
