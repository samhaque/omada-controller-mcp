from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_feature_vo import AdvancedFeatureVO
    from ..models.airtime_fairness_setting_vo import AirtimeFairnessSettingVO
    from ..models.band_steering_multi_band_vo import BandSteeringMultiBandVO
    from ..models.band_steering_vo import BandSteeringVO
    from ..models.beacon_control_vo import BeaconControlVO
    from ..models.mcast_rate_limit_setting_vo import McastRateLimitSettingVO
    from ..models.mesh_setting_vo import MeshSettingVO
    from ..models.roaming_setting_vo import RoamingSettingVO
    from ..models.site_ap_lldp_setting_vo import SiteApLldpSettingVO


T = TypeVar("T", bound="SiteTemplateWirelessFeature")


@_attrs_define
class SiteTemplateWirelessFeature:
    """
    Attributes:
        mesh (MeshSettingVO | Unset): Site mesh.
        advanced_feature (AdvancedFeatureVO | Unset): advanced feature
        lldp (SiteApLldpSettingVO | Unset): Site LLDP.
        beacon_control (BeaconControlVO | Unset): Site beacon control.
        band_steering (BandSteeringVO | Unset): band Steering
        band_steering_for_multi_band (BandSteeringMultiBandVO | Unset): Site band steering.
        airtime_fairness (AirtimeFairnessSettingVO | Unset): Site airtimeFairness.
        roaming (RoamingSettingVO | Unset): roaming setting
        mcast_rate_limit (McastRateLimitSettingVO | Unset):
    """

    mesh: MeshSettingVO | Unset = UNSET
    advanced_feature: AdvancedFeatureVO | Unset = UNSET
    lldp: SiteApLldpSettingVO | Unset = UNSET
    beacon_control: BeaconControlVO | Unset = UNSET
    band_steering: BandSteeringVO | Unset = UNSET
    band_steering_for_multi_band: BandSteeringMultiBandVO | Unset = UNSET
    airtime_fairness: AirtimeFairnessSettingVO | Unset = UNSET
    roaming: RoamingSettingVO | Unset = UNSET
    mcast_rate_limit: McastRateLimitSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mesh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mesh, Unset):
            mesh = self.mesh.to_dict()

        advanced_feature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_feature, Unset):
            advanced_feature = self.advanced_feature.to_dict()

        lldp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lldp, Unset):
            lldp = self.lldp.to_dict()

        beacon_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.beacon_control, Unset):
            beacon_control = self.beacon_control.to_dict()

        band_steering: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_steering, Unset):
            band_steering = self.band_steering.to_dict()

        band_steering_for_multi_band: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_steering_for_multi_band, Unset):
            band_steering_for_multi_band = self.band_steering_for_multi_band.to_dict()

        airtime_fairness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.airtime_fairness, Unset):
            airtime_fairness = self.airtime_fairness.to_dict()

        roaming: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roaming, Unset):
            roaming = self.roaming.to_dict()

        mcast_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcast_rate_limit, Unset):
            mcast_rate_limit = self.mcast_rate_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mesh is not UNSET:
            field_dict["mesh"] = mesh
        if advanced_feature is not UNSET:
            field_dict["advancedFeature"] = advanced_feature
        if lldp is not UNSET:
            field_dict["lldp"] = lldp
        if beacon_control is not UNSET:
            field_dict["beaconControl"] = beacon_control
        if band_steering is not UNSET:
            field_dict["bandSteering"] = band_steering
        if band_steering_for_multi_band is not UNSET:
            field_dict["bandSteeringForMultiBand"] = band_steering_for_multi_band
        if airtime_fairness is not UNSET:
            field_dict["airtimeFairness"] = airtime_fairness
        if roaming is not UNSET:
            field_dict["roaming"] = roaming
        if mcast_rate_limit is not UNSET:
            field_dict["mcastRateLimit"] = mcast_rate_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.advanced_feature_vo import AdvancedFeatureVO
        from ..models.airtime_fairness_setting_vo import (
            AirtimeFairnessSettingVO,
        )
        from ..models.band_steering_multi_band_vo import (
            BandSteeringMultiBandVO,
        )
        from ..models.band_steering_vo import BandSteeringVO
        from ..models.beacon_control_vo import BeaconControlVO
        from ..models.mcast_rate_limit_setting_vo import (
            McastRateLimitSettingVO,
        )
        from ..models.mesh_setting_vo import MeshSettingVO
        from ..models.roaming_setting_vo import RoamingSettingVO
        from ..models.site_ap_lldp_setting_vo import (
            SiteApLldpSettingVO,
        )

        d = dict(src_dict)
        _mesh = d.pop("mesh", UNSET)
        mesh: MeshSettingVO | Unset
        if isinstance(_mesh, Unset):
            mesh = UNSET
        else:
            mesh = MeshSettingVO.from_dict(_mesh)

        _advanced_feature = d.pop("advancedFeature", UNSET)
        advanced_feature: AdvancedFeatureVO | Unset
        if isinstance(_advanced_feature, Unset):
            advanced_feature = UNSET
        else:
            advanced_feature = AdvancedFeatureVO.from_dict(_advanced_feature)

        _lldp = d.pop("lldp", UNSET)
        lldp: SiteApLldpSettingVO | Unset
        if isinstance(_lldp, Unset):
            lldp = UNSET
        else:
            lldp = SiteApLldpSettingVO.from_dict(_lldp)

        _beacon_control = d.pop("beaconControl", UNSET)
        beacon_control: BeaconControlVO | Unset
        if isinstance(_beacon_control, Unset):
            beacon_control = UNSET
        else:
            beacon_control = BeaconControlVO.from_dict(_beacon_control)

        _band_steering = d.pop("bandSteering", UNSET)
        band_steering: BandSteeringVO | Unset
        if isinstance(_band_steering, Unset):
            band_steering = UNSET
        else:
            band_steering = BandSteeringVO.from_dict(_band_steering)

        _band_steering_for_multi_band = d.pop("bandSteeringForMultiBand", UNSET)
        band_steering_for_multi_band: BandSteeringMultiBandVO | Unset
        if isinstance(_band_steering_for_multi_band, Unset):
            band_steering_for_multi_band = UNSET
        else:
            band_steering_for_multi_band = BandSteeringMultiBandVO.from_dict(
                _band_steering_for_multi_band
            )

        _airtime_fairness = d.pop("airtimeFairness", UNSET)
        airtime_fairness: AirtimeFairnessSettingVO | Unset
        if isinstance(_airtime_fairness, Unset):
            airtime_fairness = UNSET
        else:
            airtime_fairness = AirtimeFairnessSettingVO.from_dict(_airtime_fairness)

        _roaming = d.pop("roaming", UNSET)
        roaming: RoamingSettingVO | Unset
        if isinstance(_roaming, Unset):
            roaming = UNSET
        else:
            roaming = RoamingSettingVO.from_dict(_roaming)

        _mcast_rate_limit = d.pop("mcastRateLimit", UNSET)
        mcast_rate_limit: McastRateLimitSettingVO | Unset
        if isinstance(_mcast_rate_limit, Unset):
            mcast_rate_limit = UNSET
        else:
            mcast_rate_limit = McastRateLimitSettingVO.from_dict(_mcast_rate_limit)

        site_template_wireless_feature = cls(
            mesh=mesh,
            advanced_feature=advanced_feature,
            lldp=lldp,
            beacon_control=beacon_control,
            band_steering=band_steering,
            band_steering_for_multi_band=band_steering_for_multi_band,
            airtime_fairness=airtime_fairness,
            roaming=roaming,
            mcast_rate_limit=mcast_rate_limit,
        )

        site_template_wireless_feature.additional_properties = d
        return site_template_wireless_feature

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
