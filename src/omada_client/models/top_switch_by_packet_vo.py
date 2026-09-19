from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.switch_packet_error_vo import SwitchPacketErrorVO
    from ..models.switch_packet_loss_vo import SwitchPacketLossVO


T = TypeVar("T", bound="TopSwitchByPacketVO")


@_attrs_define
class TopSwitchByPacketVO:
    """Top switch by packet loss and error

    Attributes:
        top_packet_loss (list[SwitchPacketLossVO] | Unset): Top switches by packet loss
        top_packet_error (list[SwitchPacketErrorVO] | Unset): Top switches by packet error
        need_tip (bool | Unset): Not supported by the firmware on some devices
    """

    top_packet_loss: list[SwitchPacketLossVO] | Unset = UNSET
    top_packet_error: list[SwitchPacketErrorVO] | Unset = UNSET
    need_tip: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_packet_loss: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_packet_loss, Unset):
            top_packet_loss = []
            for top_packet_loss_item_data in self.top_packet_loss:
                top_packet_loss_item = top_packet_loss_item_data.to_dict()
                top_packet_loss.append(top_packet_loss_item)

        top_packet_error: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_packet_error, Unset):
            top_packet_error = []
            for top_packet_error_item_data in self.top_packet_error:
                top_packet_error_item = top_packet_error_item_data.to_dict()
                top_packet_error.append(top_packet_error_item)

        need_tip = self.need_tip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_packet_loss is not UNSET:
            field_dict["topPacketLoss"] = top_packet_loss
        if top_packet_error is not UNSET:
            field_dict["topPacketError"] = top_packet_error
        if need_tip is not UNSET:
            field_dict["needTip"] = need_tip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.switch_packet_error_vo import SwitchPacketErrorVO
        from ..models.switch_packet_loss_vo import SwitchPacketLossVO

        d = dict(src_dict)
        _top_packet_loss = d.pop("topPacketLoss", UNSET)
        top_packet_loss: list[SwitchPacketLossVO] | Unset = UNSET
        if _top_packet_loss is not UNSET:
            top_packet_loss = []
            for top_packet_loss_item_data in _top_packet_loss:
                top_packet_loss_item = SwitchPacketLossVO.from_dict(
                    top_packet_loss_item_data
                )

                top_packet_loss.append(top_packet_loss_item)

        _top_packet_error = d.pop("topPacketError", UNSET)
        top_packet_error: list[SwitchPacketErrorVO] | Unset = UNSET
        if _top_packet_error is not UNSET:
            top_packet_error = []
            for top_packet_error_item_data in _top_packet_error:
                top_packet_error_item = SwitchPacketErrorVO.from_dict(
                    top_packet_error_item_data
                )

                top_packet_error.append(top_packet_error_item)

        need_tip = d.pop("needTip", UNSET)

        top_switch_by_packet_vo = cls(
            top_packet_loss=top_packet_loss,
            top_packet_error=top_packet_error,
            need_tip=need_tip,
        )

        top_switch_by_packet_vo.additional_properties = d
        return top_switch_by_packet_vo

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
