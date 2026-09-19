from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plmn_id_open_api_vo import PlmnIdOpenApiVO
    from ..models.realm_open_api_vo import RealmOpenApiVO
    from ..models.roaming_consortium_oi_open_api_vo import RoamingConsortiumOiOpenApiVO
    from ..models.venue_info_open_api_vo import VenueInfoOpenApiVO


T = TypeVar("T", bound="UpdateSsidHotspotV2SettingOpenApiVO")


@_attrs_define
class UpdateSsidHotspotV2SettingOpenApiVO:
    """
    Attributes:
        hotspot_v2_enable (bool): Whether Hotspot2.0 is enabled.<br />If hotspot2.0 is disabled, other parameters in
            Hotspot2.0 will be invalid.
        network_type (int | Unset): Specify the 802.11u network type.<br /> Parameter networkType should be a value as
            follows: [0: Private network; 1: Private network with guest access; 2: Chargeable public network; 3: Free public
            network; 4: Personal device network; 5: Emergency services only network; 14: Test or experimental; 15:
            Wildcard].
        plmn_id (list[PlmnIdOpenApiVO] | Unset): PLMN ID list, enter PLMN ID of 802.11u 3GPP cellular network.<br
            />Note: Up to 6 entries are allowed for the PLMN ID list.
        roaming_consortium_oi (list[RoamingConsortiumOiOpenApiVO] | Unset): Roaming Consortium Oi list, enter the
            802.11u roaming organization identifiers.<br />Note: Up to 3 entries are allowed for the Roaming Consortium Oi
            list.
        operator_domain (str | Unset): Enter the domain name of the hotspot operator.<br />For example,
            www.omadanetworks.com.
        dgaf_disable (bool | Unset): Whether to enable DGAF(downstream group-addressed forwarding) disable mode.<br />In
            DGAF disable mode, the AP will not forward downstream multicast and broadcast packets.
        he_ssid (str | Unset): Homogenous Extended Service Set Identifier, it is used to identify the same type of ESS
            network set.<br />Note: HESSID should be consistent with one of the BSSIDs of the APs in the zone.
        internet (bool | Unset): Internet access support status (network reachability), which indicates that the network
            is allowed to access the Internet.
        availability_ipv_4 (int | Unset): Available type information of IPv4 addresses.<br />Parameter availabilityIpv4
            should be a value as follows: [0: Address type not available; 1: Public IPv4 address available; 2: Port-
            restricted IPv4 address available; 3: Single NATed private IPv4 address available; 4: Double NATed private IPv4
            address available; 5: Port-restricted IPv4 address and single NATed IPv4 address available; 6: Port-restricted
            IPv4 address and double NATed IPv4 address available; 7: Availability of the address type is not known].
        availability_ipv_6 (int | Unset): Available type information of IPv6 addresses.<br /> Parameter availabilityIpv6
            should be a value as follows: [0: Address type not available; 1: Address type available; 2: Availability of the
            address type not known].
        operator_friendly (str | Unset): Hotspot network operator friendly name.<br />Note:Parameter operatorFriendly
            should contain between 1 and 64 visible ASCII characters, with no Spaces at the beginning and end, and Spaces in
            between.
        venue_info (VenueInfoOpenApiVO | Unset): Indicates the venue information using the combination of the network's
            venue group and venue type (using the international building code).
        realm_list (list[RealmOpenApiVO] | Unset): Add a profile to identify and describe a NAI (Network Access
            Identifier) realm accessible using the AP, and the method that this NAI realm uses for authentication.<br
            />Note: Up to 10 entries are allowed for the NAI Realm list.
    """

    hotspot_v2_enable: bool
    network_type: int | Unset = UNSET
    plmn_id: list[PlmnIdOpenApiVO] | Unset = UNSET
    roaming_consortium_oi: list[RoamingConsortiumOiOpenApiVO] | Unset = UNSET
    operator_domain: str | Unset = UNSET
    dgaf_disable: bool | Unset = UNSET
    he_ssid: str | Unset = UNSET
    internet: bool | Unset = UNSET
    availability_ipv_4: int | Unset = UNSET
    availability_ipv_6: int | Unset = UNSET
    operator_friendly: str | Unset = UNSET
    venue_info: VenueInfoOpenApiVO | Unset = UNSET
    realm_list: list[RealmOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hotspot_v2_enable = self.hotspot_v2_enable

        network_type = self.network_type

        plmn_id: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.plmn_id, Unset):
            plmn_id = []
            for plmn_id_item_data in self.plmn_id:
                plmn_id_item = plmn_id_item_data.to_dict()
                plmn_id.append(plmn_id_item)

        roaming_consortium_oi: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roaming_consortium_oi, Unset):
            roaming_consortium_oi = []
            for roaming_consortium_oi_item_data in self.roaming_consortium_oi:
                roaming_consortium_oi_item = roaming_consortium_oi_item_data.to_dict()
                roaming_consortium_oi.append(roaming_consortium_oi_item)

        operator_domain = self.operator_domain

        dgaf_disable = self.dgaf_disable

        he_ssid = self.he_ssid

        internet = self.internet

        availability_ipv_4 = self.availability_ipv_4

        availability_ipv_6 = self.availability_ipv_6

        operator_friendly = self.operator_friendly

        venue_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.venue_info, Unset):
            venue_info = self.venue_info.to_dict()

        realm_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.realm_list, Unset):
            realm_list = []
            for realm_list_item_data in self.realm_list:
                realm_list_item = realm_list_item_data.to_dict()
                realm_list.append(realm_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hotspotV2Enable": hotspot_v2_enable,
            }
        )
        if network_type is not UNSET:
            field_dict["networkType"] = network_type
        if plmn_id is not UNSET:
            field_dict["plmnId"] = plmn_id
        if roaming_consortium_oi is not UNSET:
            field_dict["roamingConsortiumOi"] = roaming_consortium_oi
        if operator_domain is not UNSET:
            field_dict["operatorDomain"] = operator_domain
        if dgaf_disable is not UNSET:
            field_dict["dgafDisable"] = dgaf_disable
        if he_ssid is not UNSET:
            field_dict["heSsid"] = he_ssid
        if internet is not UNSET:
            field_dict["internet"] = internet
        if availability_ipv_4 is not UNSET:
            field_dict["availabilityIpv4"] = availability_ipv_4
        if availability_ipv_6 is not UNSET:
            field_dict["availabilityIpv6"] = availability_ipv_6
        if operator_friendly is not UNSET:
            field_dict["operatorFriendly"] = operator_friendly
        if venue_info is not UNSET:
            field_dict["venueInfo"] = venue_info
        if realm_list is not UNSET:
            field_dict["realmList"] = realm_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.plmn_id_open_api_vo import PlmnIdOpenApiVO
        from ..models.realm_open_api_vo import RealmOpenApiVO
        from ..models.roaming_consortium_oi_open_api_vo import (
            RoamingConsortiumOiOpenApiVO,
        )
        from ..models.venue_info_open_api_vo import VenueInfoOpenApiVO

        d = dict(src_dict)
        hotspot_v2_enable = d.pop("hotspotV2Enable")

        network_type = d.pop("networkType", UNSET)

        _plmn_id = d.pop("plmnId", UNSET)
        plmn_id: list[PlmnIdOpenApiVO] | Unset = UNSET
        if _plmn_id is not UNSET:
            plmn_id = []
            for plmn_id_item_data in _plmn_id:
                plmn_id_item = PlmnIdOpenApiVO.from_dict(plmn_id_item_data)

                plmn_id.append(plmn_id_item)

        _roaming_consortium_oi = d.pop("roamingConsortiumOi", UNSET)
        roaming_consortium_oi: list[RoamingConsortiumOiOpenApiVO] | Unset = UNSET
        if _roaming_consortium_oi is not UNSET:
            roaming_consortium_oi = []
            for roaming_consortium_oi_item_data in _roaming_consortium_oi:
                roaming_consortium_oi_item = RoamingConsortiumOiOpenApiVO.from_dict(
                    roaming_consortium_oi_item_data
                )

                roaming_consortium_oi.append(roaming_consortium_oi_item)

        operator_domain = d.pop("operatorDomain", UNSET)

        dgaf_disable = d.pop("dgafDisable", UNSET)

        he_ssid = d.pop("heSsid", UNSET)

        internet = d.pop("internet", UNSET)

        availability_ipv_4 = d.pop("availabilityIpv4", UNSET)

        availability_ipv_6 = d.pop("availabilityIpv6", UNSET)

        operator_friendly = d.pop("operatorFriendly", UNSET)

        _venue_info = d.pop("venueInfo", UNSET)
        venue_info: VenueInfoOpenApiVO | Unset
        if isinstance(_venue_info, Unset):
            venue_info = UNSET
        else:
            venue_info = VenueInfoOpenApiVO.from_dict(_venue_info)

        _realm_list = d.pop("realmList", UNSET)
        realm_list: list[RealmOpenApiVO] | Unset = UNSET
        if _realm_list is not UNSET:
            realm_list = []
            for realm_list_item_data in _realm_list:
                realm_list_item = RealmOpenApiVO.from_dict(realm_list_item_data)

                realm_list.append(realm_list_item)

        update_ssid_hotspot_v2_setting_open_api_vo = cls(
            hotspot_v2_enable=hotspot_v2_enable,
            network_type=network_type,
            plmn_id=plmn_id,
            roaming_consortium_oi=roaming_consortium_oi,
            operator_domain=operator_domain,
            dgaf_disable=dgaf_disable,
            he_ssid=he_ssid,
            internet=internet,
            availability_ipv_4=availability_ipv_4,
            availability_ipv_6=availability_ipv_6,
            operator_friendly=operator_friendly,
            venue_info=venue_info,
            realm_list=realm_list,
        )

        update_ssid_hotspot_v2_setting_open_api_vo.additional_properties = d
        return update_ssid_hotspot_v2_setting_open_api_vo

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
