from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_time_id_open_api_vo import SiteTimeIdOpenApiVO


T = TypeVar("T", bound="DeleteGlobalThreatOpenApiVO")


@_attrs_define
class DeleteGlobalThreatOpenApiVO:
    """
    Attributes:
        threat_id (list[SiteTimeIdOpenApiVO] | Unset): The global view needs to pass in a site ID.
    """

    threat_id: list[SiteTimeIdOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threat_id: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.threat_id, Unset):
            threat_id = []
            for threat_id_item_data in self.threat_id:
                threat_id_item = threat_id_item_data.to_dict()
                threat_id.append(threat_id_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if threat_id is not UNSET:
            field_dict["threatId"] = threat_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_time_id_open_api_vo import (
            SiteTimeIdOpenApiVO,
        )

        d = dict(src_dict)
        _threat_id = d.pop("threatId", UNSET)
        threat_id: list[SiteTimeIdOpenApiVO] | Unset = UNSET
        if _threat_id is not UNSET:
            threat_id = []
            for threat_id_item_data in _threat_id:
                threat_id_item = SiteTimeIdOpenApiVO.from_dict(threat_id_item_data)

                threat_id.append(threat_id_item)

        delete_global_threat_open_api_vo = cls(
            threat_id=threat_id,
        )

        delete_global_threat_open_api_vo.additional_properties = d
        return delete_global_threat_open_api_vo

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
