from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_lag_vo import OswStackLagVO
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswPortStackSettingVO")


@_attrs_define
class OswPortStackSettingVO:
    """Port Stack Setting

    Attributes:
        mirrored_ports (list[OswStandPortVO] | Unset): Mirrored Standard Ports
        lag_setting (OswStackLagVO | Unset): Basic configuration of the LAG
        stack_id (str | Unset): Stack ID
    """

    mirrored_ports: list[OswStandPortVO] | Unset = UNSET
    lag_setting: OswStackLagVO | Unset = UNSET
    stack_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mirrored_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mirrored_ports, Unset):
            mirrored_ports = []
            for mirrored_ports_item_data in self.mirrored_ports:
                mirrored_ports_item = mirrored_ports_item_data.to_dict()
                mirrored_ports.append(mirrored_ports_item)

        lag_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lag_setting, Unset):
            lag_setting = self.lag_setting.to_dict()

        stack_id = self.stack_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if lag_setting is not UNSET:
            field_dict["lagSetting"] = lag_setting
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_lag_vo import OswStackLagVO
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        _mirrored_ports = d.pop("mirroredPorts", UNSET)
        mirrored_ports: list[OswStandPortVO] | Unset = UNSET
        if _mirrored_ports is not UNSET:
            mirrored_ports = []
            for mirrored_ports_item_data in _mirrored_ports:
                mirrored_ports_item = OswStandPortVO.from_dict(mirrored_ports_item_data)

                mirrored_ports.append(mirrored_ports_item)

        _lag_setting = d.pop("lagSetting", UNSET)
        lag_setting: OswStackLagVO | Unset
        if isinstance(_lag_setting, Unset):
            lag_setting = UNSET
        else:
            lag_setting = OswStackLagVO.from_dict(_lag_setting)

        stack_id = d.pop("stackId", UNSET)

        osw_port_stack_setting_vo = cls(
            mirrored_ports=mirrored_ports,
            lag_setting=lag_setting,
            stack_id=stack_id,
        )

        osw_port_stack_setting_vo.additional_properties = d
        return osw_port_stack_setting_vo

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
