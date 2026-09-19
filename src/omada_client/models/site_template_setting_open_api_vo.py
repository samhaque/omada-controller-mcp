from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.advanced_feature_open_api_vo import AdvancedFeatureOpenApiVO
    from ..models.airtime_fairness_setting_open_api_vo import (
        AirtimeFairnessSettingOpenApiVO,
    )
    from ..models.band_steering_multi_band_open_api_vo import (
        BandSteeringMultiBandOpenApiVO,
    )
    from ..models.band_steering_open_api_vo import BandSteeringOpenApiVO
    from ..models.beacon_control_open_api_vo import BeaconControlOpenApiVO
    from ..models.new_channel_limit_setting_open_api_vo import (
        NewChannelLimitSettingOpenApiVO,
    )
    from ..models.new_mcast_rate_limit_setting_open_api_vo import (
        NewMcastRateLimitSettingOpenApiVO,
    )
    from ..models.new_mesh_setting_open_api_vo import NewMeshSettingOpenApiVO
    from ..models.new_roaming_setting_open_api_vo import NewRoamingSettingOpenApiVO
    from ..models.remote_log_setting_open_api_vo import RemoteLogSettingOpenApiVO
    from ..models.site_ap_lldp_setting_open_api_vo import SiteApLldpSettingOpenApiVO
    from ..models.site_led_setting import SiteLedSetting
    from ..models.site_template_open_api_vo import SiteTemplateOpenApiVO


T = TypeVar("T", bound="SiteTemplateSettingOpenApiVO")


@_attrs_define
class SiteTemplateSettingOpenApiVO:
    """
    Attributes:
        site_template (SiteTemplateOpenApiVO | Unset): Site template setting.
        mesh (NewMeshSettingOpenApiVO | Unset): Site mesh setting.
        remote_log (RemoteLogSettingOpenApiVO | Unset): Site remote logging setting.
        advanced_feature (AdvancedFeatureOpenApiVO | Unset):
        channel_limit (NewChannelLimitSettingOpenApiVO | Unset):
        lldp (SiteApLldpSettingOpenApiVO | Unset): Site lldp setting.
        beacon_control (BeaconControlOpenApiVO | Unset): Site beacon control setting.
        band_steering (BandSteeringOpenApiVO | Unset): Site band steering setting.
        band_steering_for_multi_band (BandSteeringMultiBandOpenApiVO | Unset): Site band steering multi band setting.
        airtime_fairness (AirtimeFairnessSettingOpenApiVO | Unset): Site airtime fairness setting.
        led (SiteLedSetting | Unset): Site led setting
        roaming (NewRoamingSettingOpenApiVO | Unset): Site roaming setting
        site_multicast_rate_limit_setting (NewMcastRateLimitSettingOpenApiVO | Unset): Site multicast rate limit setting
    """

    site_template: SiteTemplateOpenApiVO | Unset = UNSET
    mesh: NewMeshSettingOpenApiVO | Unset = UNSET
    remote_log: RemoteLogSettingOpenApiVO | Unset = UNSET
    advanced_feature: AdvancedFeatureOpenApiVO | Unset = UNSET
    channel_limit: NewChannelLimitSettingOpenApiVO | Unset = UNSET
    lldp: SiteApLldpSettingOpenApiVO | Unset = UNSET
    beacon_control: BeaconControlOpenApiVO | Unset = UNSET
    band_steering: BandSteeringOpenApiVO | Unset = UNSET
    band_steering_for_multi_band: BandSteeringMultiBandOpenApiVO | Unset = UNSET
    airtime_fairness: AirtimeFairnessSettingOpenApiVO | Unset = UNSET
    led: SiteLedSetting | Unset = UNSET
    roaming: NewRoamingSettingOpenApiVO | Unset = UNSET
    site_multicast_rate_limit_setting: NewMcastRateLimitSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site_template, Unset):
            site_template = self.site_template.to_dict()

        mesh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mesh, Unset):
            mesh = self.mesh.to_dict()

        remote_log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote_log, Unset):
            remote_log = self.remote_log.to_dict()

        advanced_feature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_feature, Unset):
            advanced_feature = self.advanced_feature.to_dict()

        channel_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_limit, Unset):
            channel_limit = self.channel_limit.to_dict()

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

        led: dict[str, Any] | Unset = UNSET
        if not isinstance(self.led, Unset):
            led = self.led.to_dict()

        roaming: dict[str, Any] | Unset = UNSET
        if not isinstance(self.roaming, Unset):
            roaming = self.roaming.to_dict()

        site_multicast_rate_limit_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site_multicast_rate_limit_setting, Unset):
            site_multicast_rate_limit_setting = (
                self.site_multicast_rate_limit_setting.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_template is not UNSET:
            field_dict["siteTemplate"] = site_template
        if mesh is not UNSET:
            field_dict["mesh"] = mesh
        if remote_log is not UNSET:
            field_dict["remoteLog"] = remote_log
        if advanced_feature is not UNSET:
            field_dict["advancedFeature"] = advanced_feature
        if channel_limit is not UNSET:
            field_dict["channelLimit"] = channel_limit
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
        if led is not UNSET:
            field_dict["led"] = led
        if roaming is not UNSET:
            field_dict["roaming"] = roaming
        if site_multicast_rate_limit_setting is not UNSET:
            field_dict["SiteMulticastRateLimitSetting"] = (
                site_multicast_rate_limit_setting
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.advanced_feature_open_api_vo import (
            AdvancedFeatureOpenApiVO,
        )
        from ..models.airtime_fairness_setting_open_api_vo import (
            AirtimeFairnessSettingOpenApiVO,
        )
        from ..models.band_steering_multi_band_open_api_vo import (
            BandSteeringMultiBandOpenApiVO,
        )
        from ..models.band_steering_open_api_vo import (
            BandSteeringOpenApiVO,
        )
        from ..models.beacon_control_open_api_vo import (
            BeaconControlOpenApiVO,
        )
        from ..models.new_channel_limit_setting_open_api_vo import (
            NewChannelLimitSettingOpenApiVO,
        )
        from ..models.new_mcast_rate_limit_setting_open_api_vo import (
            NewMcastRateLimitSettingOpenApiVO,
        )
        from ..models.new_mesh_setting_open_api_vo import (
            NewMeshSettingOpenApiVO,
        )
        from ..models.new_roaming_setting_open_api_vo import (
            NewRoamingSettingOpenApiVO,
        )
        from ..models.remote_log_setting_open_api_vo import (
            RemoteLogSettingOpenApiVO,
        )
        from ..models.site_ap_lldp_setting_open_api_vo import (
            SiteApLldpSettingOpenApiVO,
        )
        from ..models.site_led_setting import SiteLedSetting
        from ..models.site_template_open_api_vo import (
            SiteTemplateOpenApiVO,
        )

        d = dict(src_dict)
        _site_template = d.pop("siteTemplate", UNSET)
        site_template: SiteTemplateOpenApiVO | Unset
        if isinstance(_site_template, Unset):
            site_template = UNSET
        else:
            site_template = SiteTemplateOpenApiVO.from_dict(_site_template)

        _mesh = d.pop("mesh", UNSET)
        mesh: NewMeshSettingOpenApiVO | Unset
        if isinstance(_mesh, Unset):
            mesh = UNSET
        else:
            mesh = NewMeshSettingOpenApiVO.from_dict(_mesh)

        _remote_log = d.pop("remoteLog", UNSET)
        remote_log: RemoteLogSettingOpenApiVO | Unset
        if isinstance(_remote_log, Unset):
            remote_log = UNSET
        else:
            remote_log = RemoteLogSettingOpenApiVO.from_dict(_remote_log)

        _advanced_feature = d.pop("advancedFeature", UNSET)
        advanced_feature: AdvancedFeatureOpenApiVO | Unset
        if isinstance(_advanced_feature, Unset):
            advanced_feature = UNSET
        else:
            advanced_feature = AdvancedFeatureOpenApiVO.from_dict(_advanced_feature)

        _channel_limit = d.pop("channelLimit", UNSET)
        channel_limit: NewChannelLimitSettingOpenApiVO | Unset
        if isinstance(_channel_limit, Unset):
            channel_limit = UNSET
        else:
            channel_limit = NewChannelLimitSettingOpenApiVO.from_dict(_channel_limit)

        _lldp = d.pop("lldp", UNSET)
        lldp: SiteApLldpSettingOpenApiVO | Unset
        if isinstance(_lldp, Unset):
            lldp = UNSET
        else:
            lldp = SiteApLldpSettingOpenApiVO.from_dict(_lldp)

        _beacon_control = d.pop("beaconControl", UNSET)
        beacon_control: BeaconControlOpenApiVO | Unset
        if isinstance(_beacon_control, Unset):
            beacon_control = UNSET
        else:
            beacon_control = BeaconControlOpenApiVO.from_dict(_beacon_control)

        _band_steering = d.pop("bandSteering", UNSET)
        band_steering: BandSteeringOpenApiVO | Unset
        if isinstance(_band_steering, Unset):
            band_steering = UNSET
        else:
            band_steering = BandSteeringOpenApiVO.from_dict(_band_steering)

        _band_steering_for_multi_band = d.pop("bandSteeringForMultiBand", UNSET)
        band_steering_for_multi_band: BandSteeringMultiBandOpenApiVO | Unset
        if isinstance(_band_steering_for_multi_band, Unset):
            band_steering_for_multi_band = UNSET
        else:
            band_steering_for_multi_band = BandSteeringMultiBandOpenApiVO.from_dict(
                _band_steering_for_multi_band
            )

        _airtime_fairness = d.pop("airtimeFairness", UNSET)
        airtime_fairness: AirtimeFairnessSettingOpenApiVO | Unset
        if isinstance(_airtime_fairness, Unset):
            airtime_fairness = UNSET
        else:
            airtime_fairness = AirtimeFairnessSettingOpenApiVO.from_dict(
                _airtime_fairness
            )

        _led = d.pop("led", UNSET)
        led: SiteLedSetting | Unset
        if isinstance(_led, Unset):
            led = UNSET
        else:
            led = SiteLedSetting.from_dict(_led)

        _roaming = d.pop("roaming", UNSET)
        roaming: NewRoamingSettingOpenApiVO | Unset
        if isinstance(_roaming, Unset):
            roaming = UNSET
        else:
            roaming = NewRoamingSettingOpenApiVO.from_dict(_roaming)

        _site_multicast_rate_limit_setting = d.pop(
            "SiteMulticastRateLimitSetting", UNSET
        )
        site_multicast_rate_limit_setting: NewMcastRateLimitSettingOpenApiVO | Unset
        if isinstance(_site_multicast_rate_limit_setting, Unset):
            site_multicast_rate_limit_setting = UNSET
        else:
            site_multicast_rate_limit_setting = (
                NewMcastRateLimitSettingOpenApiVO.from_dict(
                    _site_multicast_rate_limit_setting
                )
            )

        site_template_setting_open_api_vo = cls(
            site_template=site_template,
            mesh=mesh,
            remote_log=remote_log,
            advanced_feature=advanced_feature,
            channel_limit=channel_limit,
            lldp=lldp,
            beacon_control=beacon_control,
            band_steering=band_steering,
            band_steering_for_multi_band=band_steering_for_multi_band,
            airtime_fairness=airtime_fairness,
            led=led,
            roaming=roaming,
            site_multicast_rate_limit_setting=site_multicast_rate_limit_setting,
        )

        site_template_setting_open_api_vo.additional_properties = d
        return site_template_setting_open_api_vo

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
