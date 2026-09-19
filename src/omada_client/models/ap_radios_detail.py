from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_radio_channel import ApRadioChannel
    from ..models.ap_radio_traffic_entity import APRadioTrafficEntity


T = TypeVar("T", bound="ApRadiosDetail")


@_attrs_define
class ApRadiosDetail:
    """
    Attributes:
        radio_traffic_2_g (APRadioTrafficEntity | Unset):
        radio_traffic_5_g (APRadioTrafficEntity | Unset):
        radio_traffic_5_g_2 (APRadioTrafficEntity | Unset):
        radio_traffic_6_g (APRadioTrafficEntity | Unset):
        wp2g (ApRadioChannel | Unset):
        wp5g (ApRadioChannel | Unset):
        wp5g2 (ApRadioChannel | Unset):
        wp6g (ApRadioChannel | Unset):
    """

    radio_traffic_2_g: APRadioTrafficEntity | Unset = UNSET
    radio_traffic_5_g: APRadioTrafficEntity | Unset = UNSET
    radio_traffic_5_g_2: APRadioTrafficEntity | Unset = UNSET
    radio_traffic_6_g: APRadioTrafficEntity | Unset = UNSET
    wp2g: ApRadioChannel | Unset = UNSET
    wp5g: ApRadioChannel | Unset = UNSET
    wp5g2: ApRadioChannel | Unset = UNSET
    wp6g: ApRadioChannel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_traffic_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_2_g, Unset):
            radio_traffic_2_g = self.radio_traffic_2_g.to_dict()

        radio_traffic_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_5_g, Unset):
            radio_traffic_5_g = self.radio_traffic_5_g.to_dict()

        radio_traffic_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_5_g_2, Unset):
            radio_traffic_5_g_2 = self.radio_traffic_5_g_2.to_dict()

        radio_traffic_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_traffic_6_g, Unset):
            radio_traffic_6_g = self.radio_traffic_6_g.to_dict()

        wp2g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp2g, Unset):
            wp2g = self.wp2g.to_dict()

        wp5g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp5g, Unset):
            wp5g = self.wp5g.to_dict()

        wp5g2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp5g2, Unset):
            wp5g2 = self.wp5g2.to_dict()

        wp6g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wp6g, Unset):
            wp6g = self.wp6g.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_traffic_2_g is not UNSET:
            field_dict["radioTraffic2g"] = radio_traffic_2_g
        if radio_traffic_5_g is not UNSET:
            field_dict["radioTraffic5g"] = radio_traffic_5_g
        if radio_traffic_5_g_2 is not UNSET:
            field_dict["radioTraffic5g2"] = radio_traffic_5_g_2
        if radio_traffic_6_g is not UNSET:
            field_dict["radioTraffic6g"] = radio_traffic_6_g
        if wp2g is not UNSET:
            field_dict["wp2g"] = wp2g
        if wp5g is not UNSET:
            field_dict["wp5g"] = wp5g
        if wp5g2 is not UNSET:
            field_dict["wp5g2"] = wp5g2
        if wp6g is not UNSET:
            field_dict["wp6g"] = wp6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_radio_channel import ApRadioChannel
        from ..models.ap_radio_traffic_entity import (
            APRadioTrafficEntity,
        )

        d = dict(src_dict)
        _radio_traffic_2_g = d.pop("radioTraffic2g", UNSET)
        radio_traffic_2_g: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_2_g, Unset):
            radio_traffic_2_g = UNSET
        else:
            radio_traffic_2_g = APRadioTrafficEntity.from_dict(_radio_traffic_2_g)

        _radio_traffic_5_g = d.pop("radioTraffic5g", UNSET)
        radio_traffic_5_g: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_5_g, Unset):
            radio_traffic_5_g = UNSET
        else:
            radio_traffic_5_g = APRadioTrafficEntity.from_dict(_radio_traffic_5_g)

        _radio_traffic_5_g_2 = d.pop("radioTraffic5g2", UNSET)
        radio_traffic_5_g_2: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_5_g_2, Unset):
            radio_traffic_5_g_2 = UNSET
        else:
            radio_traffic_5_g_2 = APRadioTrafficEntity.from_dict(_radio_traffic_5_g_2)

        _radio_traffic_6_g = d.pop("radioTraffic6g", UNSET)
        radio_traffic_6_g: APRadioTrafficEntity | Unset
        if isinstance(_radio_traffic_6_g, Unset):
            radio_traffic_6_g = UNSET
        else:
            radio_traffic_6_g = APRadioTrafficEntity.from_dict(_radio_traffic_6_g)

        _wp2g = d.pop("wp2g", UNSET)
        wp2g: ApRadioChannel | Unset
        if isinstance(_wp2g, Unset):
            wp2g = UNSET
        else:
            wp2g = ApRadioChannel.from_dict(_wp2g)

        _wp5g = d.pop("wp5g", UNSET)
        wp5g: ApRadioChannel | Unset
        if isinstance(_wp5g, Unset):
            wp5g = UNSET
        else:
            wp5g = ApRadioChannel.from_dict(_wp5g)

        _wp5g2 = d.pop("wp5g2", UNSET)
        wp5g2: ApRadioChannel | Unset
        if isinstance(_wp5g2, Unset):
            wp5g2 = UNSET
        else:
            wp5g2 = ApRadioChannel.from_dict(_wp5g2)

        _wp6g = d.pop("wp6g", UNSET)
        wp6g: ApRadioChannel | Unset
        if isinstance(_wp6g, Unset):
            wp6g = UNSET
        else:
            wp6g = ApRadioChannel.from_dict(_wp6g)

        ap_radios_detail = cls(
            radio_traffic_2_g=radio_traffic_2_g,
            radio_traffic_5_g=radio_traffic_5_g,
            radio_traffic_5_g_2=radio_traffic_5_g_2,
            radio_traffic_6_g=radio_traffic_6_g,
            wp2g=wp2g,
            wp5g=wp5g,
            wp5g2=wp5g2,
            wp6g=wp6g,
        )

        ap_radios_detail.additional_properties = d
        return ap_radios_detail

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
