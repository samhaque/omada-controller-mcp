from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_type_distribution_vo import AuthTypeDistributionVO
    from ..models.authed_client_num_vo import AuthedClientNumVO
    from ..models.hotspot_type_distribution_vo import HotspotTypeDistributionVO


T = TypeVar("T", bound="HotspotStatisticVO")


@_attrs_define
class HotspotStatisticVO:
    """
    Attributes:
        last_connection (list[AuthedClientNumVO] | Unset):
        auth_type_distribution (AuthTypeDistributionVO | Unset):
        hotspot_distribution (HotspotTypeDistributionVO | Unset):
    """

    last_connection: list[AuthedClientNumVO] | Unset = UNSET
    auth_type_distribution: AuthTypeDistributionVO | Unset = UNSET
    hotspot_distribution: HotspotTypeDistributionVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_connection: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.last_connection, Unset):
            last_connection = []
            for last_connection_item_data in self.last_connection:
                last_connection_item = last_connection_item_data.to_dict()
                last_connection.append(last_connection_item)

        auth_type_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_type_distribution, Unset):
            auth_type_distribution = self.auth_type_distribution.to_dict()

        hotspot_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hotspot_distribution, Unset):
            hotspot_distribution = self.hotspot_distribution.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_connection is not UNSET:
            field_dict["lastConnection"] = last_connection
        if auth_type_distribution is not UNSET:
            field_dict["authTypeDistribution"] = auth_type_distribution
        if hotspot_distribution is not UNSET:
            field_dict["hotspotDistribution"] = hotspot_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_type_distribution_vo import (
            AuthTypeDistributionVO,
        )
        from ..models.authed_client_num_vo import AuthedClientNumVO
        from ..models.hotspot_type_distribution_vo import (
            HotspotTypeDistributionVO,
        )

        d = dict(src_dict)
        _last_connection = d.pop("lastConnection", UNSET)
        last_connection: list[AuthedClientNumVO] | Unset = UNSET
        if _last_connection is not UNSET:
            last_connection = []
            for last_connection_item_data in _last_connection:
                last_connection_item = AuthedClientNumVO.from_dict(
                    last_connection_item_data
                )

                last_connection.append(last_connection_item)

        _auth_type_distribution = d.pop("authTypeDistribution", UNSET)
        auth_type_distribution: AuthTypeDistributionVO | Unset
        if isinstance(_auth_type_distribution, Unset):
            auth_type_distribution = UNSET
        else:
            auth_type_distribution = AuthTypeDistributionVO.from_dict(
                _auth_type_distribution
            )

        _hotspot_distribution = d.pop("hotspotDistribution", UNSET)
        hotspot_distribution: HotspotTypeDistributionVO | Unset
        if isinstance(_hotspot_distribution, Unset):
            hotspot_distribution = UNSET
        else:
            hotspot_distribution = HotspotTypeDistributionVO.from_dict(
                _hotspot_distribution
            )

        hotspot_statistic_vo = cls(
            last_connection=last_connection,
            auth_type_distribution=auth_type_distribution,
            hotspot_distribution=hotspot_distribution,
        )

        hotspot_statistic_vo.additional_properties = d
        return hotspot_statistic_vo

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
