from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswMlagPeerSettingVO")


@_attrs_define
class OswMlagPeerSettingVO:
    """M-LAG group peer device setting

    Attributes:
        mac (str | Unset): Device mac
        mlag_peer_ports (list[int] | Unset): M-LAG group peer device LAG ports
        mlag_peer_standard_ports (list[OswStandPortVO] | Unset): M-LAG group peer device LAG standard ports
    """

    mac: str | Unset = UNSET
    mlag_peer_ports: list[int] | Unset = UNSET
    mlag_peer_standard_ports: list[OswStandPortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        mlag_peer_ports: list[int] | Unset = UNSET
        if not isinstance(self.mlag_peer_ports, Unset):
            mlag_peer_ports = self.mlag_peer_ports

        mlag_peer_standard_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mlag_peer_standard_ports, Unset):
            mlag_peer_standard_ports = []
            for mlag_peer_standard_ports_item_data in self.mlag_peer_standard_ports:
                mlag_peer_standard_ports_item = (
                    mlag_peer_standard_ports_item_data.to_dict()
                )
                mlag_peer_standard_ports.append(mlag_peer_standard_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if mlag_peer_ports is not UNSET:
            field_dict["mlagPeerPorts"] = mlag_peer_ports
        if mlag_peer_standard_ports is not UNSET:
            field_dict["mlagPeerStandardPorts"] = mlag_peer_standard_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        mlag_peer_ports = cast(list[int], d.pop("mlagPeerPorts", UNSET))

        _mlag_peer_standard_ports = d.pop("mlagPeerStandardPorts", UNSET)
        mlag_peer_standard_ports: list[OswStandPortVO] | Unset = UNSET
        if _mlag_peer_standard_ports is not UNSET:
            mlag_peer_standard_ports = []
            for mlag_peer_standard_ports_item_data in _mlag_peer_standard_ports:
                mlag_peer_standard_ports_item = OswStandPortVO.from_dict(
                    mlag_peer_standard_ports_item_data
                )

                mlag_peer_standard_ports.append(mlag_peer_standard_ports_item)

        osw_mlag_peer_setting_vo = cls(
            mac=mac,
            mlag_peer_ports=mlag_peer_ports,
            mlag_peer_standard_ports=mlag_peer_standard_ports,
        )

        osw_mlag_peer_setting_vo.additional_properties = d
        return osw_mlag_peer_setting_vo

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
