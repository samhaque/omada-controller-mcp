from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssid_vlan_custom_setting_open_api_vo_lan_network_vlan_ids import (
        SsidVlanCustomSettingOpenApiVOLanNetworkVlanIds,
    )


T = TypeVar("T", bound="SsidVlanCustomSettingOpenApiVO")


@_attrs_define
class SsidVlanCustomSettingOpenApiVO:
    """If mode=1, this field must be entered.

    Attributes:
        custom_mode (int): If mode=1, this field must be entered.If a device does not support multiple VLANs, the
            smallest VLAN you configured will be applied to the SSID. customMode should be a value as follows: 0:by Network;
            1:by Vlan.
        lan_network_id (str | Unset): lanNetworkId. If support vlan pool, use lanNetworkVlanIds instead. If
            customMode=1, this filed must be null. If both lanNetwork and lanNetworkVlanIds parameters exist, the vlanId
            will actually take effect with the lanNetwork with the smallest vlanId in the lanNetworkVlanIds parameter.
        bridge_vlan (int | Unset): bridgeVlan. If support vlan pool, use lanNetworkVlanIds instead.  If customMode=1,
            this filed must be null.
        vlan_id (int | Unset): vlanId. If support vlanPool, use vlanPoolIds instead. If customMode=0, this filed must be
            null. If both the vlanId and vlanPoolIds parameters exist, the vlanId will actually take effect at the minimum
            value in the vlanPoolIds parameter.
        lan_network_vlan_ids (SsidVlanCustomSettingOpenApiVOLanNetworkVlanIds | Unset): Indicates the mapping between
            the lanNetworkId and the vlanId, and if the lanNetwork corresponds to a bridgeVlan, multiple vlanIds may
            correspond.  If customMode=1, this filed must be null. Cbc Pro does not support this filed.
        vlan_pool_ids (str | Unset): When customMode=1 needs to have a value.  If customMode=0, this filed must be null.
            Cbc Pro does not support this filed.
    """

    custom_mode: int
    lan_network_id: str | Unset = UNSET
    bridge_vlan: int | Unset = UNSET
    vlan_id: int | Unset = UNSET
    lan_network_vlan_ids: SsidVlanCustomSettingOpenApiVOLanNetworkVlanIds | Unset = (
        UNSET
    )
    vlan_pool_ids: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_mode = self.custom_mode

        lan_network_id = self.lan_network_id

        bridge_vlan = self.bridge_vlan

        vlan_id = self.vlan_id

        lan_network_vlan_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan_network_vlan_ids, Unset):
            lan_network_vlan_ids = self.lan_network_vlan_ids.to_dict()

        vlan_pool_ids = self.vlan_pool_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customMode": custom_mode,
            }
        )
        if lan_network_id is not UNSET:
            field_dict["lanNetworkId"] = lan_network_id
        if bridge_vlan is not UNSET:
            field_dict["bridgeVlan"] = bridge_vlan
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if lan_network_vlan_ids is not UNSET:
            field_dict["lanNetworkVlanIds"] = lan_network_vlan_ids
        if vlan_pool_ids is not UNSET:
            field_dict["vlanPoolIds"] = vlan_pool_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssid_vlan_custom_setting_open_api_vo_lan_network_vlan_ids import (
            SsidVlanCustomSettingOpenApiVOLanNetworkVlanIds,
        )

        d = dict(src_dict)
        custom_mode = d.pop("customMode")

        lan_network_id = d.pop("lanNetworkId", UNSET)

        bridge_vlan = d.pop("bridgeVlan", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        _lan_network_vlan_ids = d.pop("lanNetworkVlanIds", UNSET)
        lan_network_vlan_ids: SsidVlanCustomSettingOpenApiVOLanNetworkVlanIds | Unset
        if isinstance(_lan_network_vlan_ids, Unset):
            lan_network_vlan_ids = UNSET
        else:
            lan_network_vlan_ids = (
                SsidVlanCustomSettingOpenApiVOLanNetworkVlanIds.from_dict(
                    _lan_network_vlan_ids
                )
            )

        vlan_pool_ids = d.pop("vlanPoolIds", UNSET)

        ssid_vlan_custom_setting_open_api_vo = cls(
            custom_mode=custom_mode,
            lan_network_id=lan_network_id,
            bridge_vlan=bridge_vlan,
            vlan_id=vlan_id,
            lan_network_vlan_ids=lan_network_vlan_ids,
            vlan_pool_ids=vlan_pool_ids,
        )

        ssid_vlan_custom_setting_open_api_vo.additional_properties = d
        return ssid_vlan_custom_setting_open_api_vo

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
