from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_brief_device import TopologyBriefDevice


T = TypeVar("T", bound="TopologyIsolatedAndPreConfigDevice")


@_attrs_define
class TopologyIsolatedAndPreConfigDevice:
    """Isolated and preConfig devices.

    Attributes:
        isolated (list[TopologyBriefDevice] | Unset): Isolated devices.
        preconfig (list[TopologyBriefDevice] | Unset): PreConfig devices.
        total (int | Unset): Total number of devices.
    """

    isolated: list[TopologyBriefDevice] | Unset = UNSET
    preconfig: list[TopologyBriefDevice] | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        isolated: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.isolated, Unset):
            isolated = []
            for isolated_item_data in self.isolated:
                isolated_item = isolated_item_data.to_dict()
                isolated.append(isolated_item)

        preconfig: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preconfig, Unset):
            preconfig = []
            for preconfig_item_data in self.preconfig:
                preconfig_item = preconfig_item_data.to_dict()
                preconfig.append(preconfig_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if isolated is not UNSET:
            field_dict["isolated"] = isolated
        if preconfig is not UNSET:
            field_dict["preconfig"] = preconfig
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_brief_device import TopologyBriefDevice

        d = dict(src_dict)
        _isolated = d.pop("isolated", UNSET)
        isolated: list[TopologyBriefDevice] | Unset = UNSET
        if _isolated is not UNSET:
            isolated = []
            for isolated_item_data in _isolated:
                isolated_item = TopologyBriefDevice.from_dict(isolated_item_data)

                isolated.append(isolated_item)

        _preconfig = d.pop("preconfig", UNSET)
        preconfig: list[TopologyBriefDevice] | Unset = UNSET
        if _preconfig is not UNSET:
            preconfig = []
            for preconfig_item_data in _preconfig:
                preconfig_item = TopologyBriefDevice.from_dict(preconfig_item_data)

                preconfig.append(preconfig_item)

        total = d.pop("total", UNSET)

        topology_isolated_and_pre_config_device = cls(
            isolated=isolated,
            preconfig=preconfig,
            total=total,
        )

        topology_isolated_and_pre_config_device.additional_properties = d
        return topology_isolated_and_pre_config_device

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
