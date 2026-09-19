from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ospf_process_area_open_api_vo import OspfProcessAreaOpenApiVO


T = TypeVar("T", bound="OspfProcessConfigOpenApiVO")


@_attrs_define
class OspfProcessConfigOpenApiVO:
    """
    Attributes:
        device_name (str): The name of the device
        mac (str): Device Mac
        process_id (int): Process ID should be within the range of 1-65535.
        router_mode (int): RouterMode, its value should be a value as follows: 0: AUTO, 1: MANUAL.
        static_enable (bool): Static routing protocol switch
        connected_enable (bool): Direct connection routing protocol switch
        router_id (str | Unset): Router ID
        static_metric (int | Unset): Set the metric value to be used as the metric of redistributed routes. It should be
            within the range of 1-16777214 and the default is equal to Default Metric configured on Basic page.
        static_metric_type (int | Unset): Set the OSPF metric type of redistributed routes. It should be a value as
            follows: 1: External Type 1, 2: External Type 2. The default is External Type 2.
        connected_metric (int | Unset): Set the metric value to be used as the metric of redistributed routes. It should
            be within the range of 1-16777214 and the default is equal to Default Metric configured on Basic page.
        connected_metric_type (int | Unset): Set the OSPF metric type of redistributed routes. It should be a value as
            follows: 1: External Type 1, 2: External Type 2. The default is External Type 2.
        auto_cost_enable (bool | Unset): enable Auto-Cost Reference Bandwidth.
        auto_cost (int | Unset): Auto-Cost Reference Bandwidth.
        vrf_id (str | Unset): VRF ID.
        area_list (list[OspfProcessAreaOpenApiVO] | Unset):  Up to 16 entries are allowed for the areaList.
    """

    device_name: str
    mac: str
    process_id: int
    router_mode: int
    static_enable: bool
    connected_enable: bool
    router_id: str | Unset = UNSET
    static_metric: int | Unset = UNSET
    static_metric_type: int | Unset = UNSET
    connected_metric: int | Unset = UNSET
    connected_metric_type: int | Unset = UNSET
    auto_cost_enable: bool | Unset = UNSET
    auto_cost: int | Unset = UNSET
    vrf_id: str | Unset = UNSET
    area_list: list[OspfProcessAreaOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        mac = self.mac

        process_id = self.process_id

        router_mode = self.router_mode

        static_enable = self.static_enable

        connected_enable = self.connected_enable

        router_id = self.router_id

        static_metric = self.static_metric

        static_metric_type = self.static_metric_type

        connected_metric = self.connected_metric

        connected_metric_type = self.connected_metric_type

        auto_cost_enable = self.auto_cost_enable

        auto_cost = self.auto_cost

        vrf_id = self.vrf_id

        area_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.area_list, Unset):
            area_list = []
            for area_list_item_data in self.area_list:
                area_list_item = area_list_item_data.to_dict()
                area_list.append(area_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceName": device_name,
                "mac": mac,
                "processId": process_id,
                "routerMode": router_mode,
                "staticEnable": static_enable,
                "connectedEnable": connected_enable,
            }
        )
        if router_id is not UNSET:
            field_dict["routerId"] = router_id
        if static_metric is not UNSET:
            field_dict["staticMetric"] = static_metric
        if static_metric_type is not UNSET:
            field_dict["staticMetricType"] = static_metric_type
        if connected_metric is not UNSET:
            field_dict["connectedMetric"] = connected_metric
        if connected_metric_type is not UNSET:
            field_dict["connectedMetricType"] = connected_metric_type
        if auto_cost_enable is not UNSET:
            field_dict["autoCostEnable"] = auto_cost_enable
        if auto_cost is not UNSET:
            field_dict["autoCost"] = auto_cost
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if area_list is not UNSET:
            field_dict["areaList"] = area_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ospf_process_area_open_api_vo import (
            OspfProcessAreaOpenApiVO,
        )

        d = dict(src_dict)
        device_name = d.pop("deviceName")

        mac = d.pop("mac")

        process_id = d.pop("processId")

        router_mode = d.pop("routerMode")

        static_enable = d.pop("staticEnable")

        connected_enable = d.pop("connectedEnable")

        router_id = d.pop("routerId", UNSET)

        static_metric = d.pop("staticMetric", UNSET)

        static_metric_type = d.pop("staticMetricType", UNSET)

        connected_metric = d.pop("connectedMetric", UNSET)

        connected_metric_type = d.pop("connectedMetricType", UNSET)

        auto_cost_enable = d.pop("autoCostEnable", UNSET)

        auto_cost = d.pop("autoCost", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        _area_list = d.pop("areaList", UNSET)
        area_list: list[OspfProcessAreaOpenApiVO] | Unset = UNSET
        if _area_list is not UNSET:
            area_list = []
            for area_list_item_data in _area_list:
                area_list_item = OspfProcessAreaOpenApiVO.from_dict(area_list_item_data)

                area_list.append(area_list_item)

        ospf_process_config_open_api_vo = cls(
            device_name=device_name,
            mac=mac,
            process_id=process_id,
            router_mode=router_mode,
            static_enable=static_enable,
            connected_enable=connected_enable,
            router_id=router_id,
            static_metric=static_metric,
            static_metric_type=static_metric_type,
            connected_metric=connected_metric,
            connected_metric_type=connected_metric_type,
            auto_cost_enable=auto_cost_enable,
            auto_cost=auto_cost,
            vrf_id=vrf_id,
            area_list=area_list,
        )

        ospf_process_config_open_api_vo.additional_properties = d
        return ospf_process_config_open_api_vo

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
