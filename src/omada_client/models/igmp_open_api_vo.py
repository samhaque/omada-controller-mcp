from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO


T = TypeVar("T", bound="IgmpOpenApiVO")


@_attrs_define
class IgmpOpenApiVO:
    """IGMP's configuration.

    Attributes:
        enable (bool):
        version (int): Version should be one of the following values: 2:v2; 3:v3.
        wan_port_id (str | Unset): WAN port ID, can be obtained from 'Get internet basic info' interface. At least one
            of the WAN Port IDs or Virtual WAN Port IDs should not be null.
        virtual_wan_id (str | Unset): Virtual WAN ID, can be obtained from 'Query virtual WAN list' interface. At least
            one of the WAN Port IDs or Virtual WAN Port IDs should not be null.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    enable: bool
    version: int
    wan_port_id: str | Unset = UNSET
    virtual_wan_id: str | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        version = self.version

        wan_port_id = self.wan_port_id

        virtual_wan_id = self.virtual_wan_id

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "version": version,
            }
        )
        if wan_port_id is not UNSET:
            field_dict["wanPortId"] = wan_port_id
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO

        d = dict(src_dict)
        enable = d.pop("enable")

        version = d.pop("version")

        wan_port_id = d.pop("wanPortId", UNSET)

        virtual_wan_id = d.pop("virtualWanId", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        igmp_open_api_vo = cls(
            enable=enable,
            version=version,
            wan_port_id=wan_port_id,
            virtual_wan_id=virtual_wan_id,
            feature_description=feature_description,
        )

        igmp_open_api_vo.additional_properties = d
        return igmp_open_api_vo

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
