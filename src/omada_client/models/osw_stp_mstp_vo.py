from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stp_instance import OswStpInstance
    from ..models.osw_stp_region import OswStpRegion


T = TypeVar("T", bound="OswStpMstpVO")


@_attrs_define
class OswStpMstpVO:
    """STP MSTP mode settging

    Attributes:
        region (OswStpRegion | Unset): Region
        instances (list[OswStpInstance] | Unset): Instances
    """

    region: OswStpRegion | Unset = UNSET
    instances: list[OswStpInstance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region: dict[str, Any] | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if instances is not UNSET:
            field_dict["instances"] = instances

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stp_instance import OswStpInstance
        from ..models.osw_stp_region import OswStpRegion

        d = dict(src_dict)
        _region = d.pop("region", UNSET)
        region: OswStpRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = OswStpRegion.from_dict(_region)

        _instances = d.pop("instances", UNSET)
        instances: list[OswStpInstance] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = OswStpInstance.from_dict(instances_item_data)

                instances.append(instances_item)

        osw_stp_mstp_vo = cls(
            region=region,
            instances=instances,
        )

        osw_stp_mstp_vo.additional_properties = d
        return osw_stp_mstp_vo

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
