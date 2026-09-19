from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.osw_stp_instance_config_open_api_vo import (
        OswStpInstanceConfigOpenApiVO,
    )
    from ..models.osw_stp_region_config_open_api_vo import OswStpRegionConfigOpenApiVO


T = TypeVar("T", bound="OswStpMstpConfigOpenApiVO")


@_attrs_define
class OswStpMstpConfigOpenApiVO:
    """STP MSTP Config, must not be null when stp is 3.

    Attributes:
        region (OswStpRegionConfigOpenApiVO): Region
        instances (list[OswStpInstanceConfigOpenApiVO]): Instances
    """

    region: OswStpRegionConfigOpenApiVO
    instances: list[OswStpInstanceConfigOpenApiVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region.to_dict()

        instances = []
        for instances_item_data in self.instances:
            instances_item = instances_item_data.to_dict()
            instances.append(instances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "instances": instances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stp_instance_config_open_api_vo import (
            OswStpInstanceConfigOpenApiVO,
        )
        from ..models.osw_stp_region_config_open_api_vo import (
            OswStpRegionConfigOpenApiVO,
        )

        d = dict(src_dict)
        region = OswStpRegionConfigOpenApiVO.from_dict(d.pop("region"))

        instances = []
        _instances = d.pop("instances")
        for instances_item_data in _instances:
            instances_item = OswStpInstanceConfigOpenApiVO.from_dict(
                instances_item_data
            )

            instances.append(instances_item)

        osw_stp_mstp_config_open_api_vo = cls(
            region=region,
            instances=instances,
        )

        osw_stp_mstp_config_open_api_vo.additional_properties = d
        return osw_stp_mstp_config_open_api_vo

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
