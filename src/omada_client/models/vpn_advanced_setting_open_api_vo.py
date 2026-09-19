from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnAdvancedSettingOpenApiVO")


@_attrs_define
class VpnAdvancedSettingOpenApiVO:
    """Advanced setting list of the VPN, only for IPSec type.

    Attributes:
        key_exchange_version (int | Unset): Key exchange version should be a value as follows: 0: IKEv1; 1: IKEv2.
        phase_1_proposal_1 (int | Unset): Phase1 proposal1 should be a value as follows: 0: MD5; 1: SHA1; 2: SHA256; 3:
            SHA384; 4: SHA512.
        phase_1_proposal_2 (int | Unset): Phase1 proposal2 should be a value as follows: 0: DES; 1: 3DES; 2: AES128; 3:
            AES192; 4: AES256.
        phase_1_proposal_3 (int | Unset): Phase1 proposal3 should be a value as follows: 0: DH1; 1: DH2; 2: DH5; 3:
            DH14; 4: DH15; 5: DH16; 6: DH19; 7: DH20; 8: DH21; 9: DH25; 10: DH26.
        exchange_mode (int | Unset): Exchange mode should be a value as follows: 0: Main Mode; 1: Aggressive Mode.
        negotiation_mode (int | Unset): Negotiation mode should be a value as follows: 0: Initiator; 1: Aggressive Mode.
        local_id_type (int | Unset): Local ID type should be a value as follows: 0: IP Address; 1: Name.
        local_name (str | Unset): Local name of the VPN advanced setting.
        remote_id_type (int | Unset): Remote ID type should be a value as follows: 0: IP Address; 1: Name.
        remote_name (str | Unset): Remote name of the VPN advanced setting.
        sa_lifetime (int | Unset): SA lifetime of the VPN advanced setting should be within the range of 60-604800
            seconds.
        dpd (bool | Unset): DPD of the VPN advanced setting.
        dpd_interval (int | Unset): DPD interval of the VPN advanced setting should be within the range of 1-300
            seconds.
        encapsulation_mode (int | Unset): Encapsulation mode should be a value as follows: 0: Tunnel Mode; 1: Transport
            Mode.
        phase_2_proposal_1 (int | Unset): Phase2 proposal1 should be a value as follows: 0: AH; 1: ESP.
        phase_2_proposal_2 (int | Unset): Phase2 proposal2 should be a value as follows: 0: MD5; 1: SHA1; 2: SHA256; 3:
            SHA384; 4:SHA512.
        phase_2_proposal_3 (int | Unset): Phase2 proposal3 should be a value as follows: 0: DES; 1: 3DES; 2: AES128; 3:
            AES192; 4: AES256.
        pfs (int | Unset): PFS should be a value as follows: 0: None; 1: dh1; 2: dh2; 3: dh5; 14: dh14; 15: dh15.
        sa_lifetime_2 (int | Unset): SA lifetime2 of the VPN advanced setting should be within the range of 120-604800
            seconds.
    """

    key_exchange_version: int | Unset = UNSET
    phase_1_proposal_1: int | Unset = UNSET
    phase_1_proposal_2: int | Unset = UNSET
    phase_1_proposal_3: int | Unset = UNSET
    exchange_mode: int | Unset = UNSET
    negotiation_mode: int | Unset = UNSET
    local_id_type: int | Unset = UNSET
    local_name: str | Unset = UNSET
    remote_id_type: int | Unset = UNSET
    remote_name: str | Unset = UNSET
    sa_lifetime: int | Unset = UNSET
    dpd: bool | Unset = UNSET
    dpd_interval: int | Unset = UNSET
    encapsulation_mode: int | Unset = UNSET
    phase_2_proposal_1: int | Unset = UNSET
    phase_2_proposal_2: int | Unset = UNSET
    phase_2_proposal_3: int | Unset = UNSET
    pfs: int | Unset = UNSET
    sa_lifetime_2: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_exchange_version = self.key_exchange_version

        phase_1_proposal_1 = self.phase_1_proposal_1

        phase_1_proposal_2 = self.phase_1_proposal_2

        phase_1_proposal_3 = self.phase_1_proposal_3

        exchange_mode = self.exchange_mode

        negotiation_mode = self.negotiation_mode

        local_id_type = self.local_id_type

        local_name = self.local_name

        remote_id_type = self.remote_id_type

        remote_name = self.remote_name

        sa_lifetime = self.sa_lifetime

        dpd = self.dpd

        dpd_interval = self.dpd_interval

        encapsulation_mode = self.encapsulation_mode

        phase_2_proposal_1 = self.phase_2_proposal_1

        phase_2_proposal_2 = self.phase_2_proposal_2

        phase_2_proposal_3 = self.phase_2_proposal_3

        pfs = self.pfs

        sa_lifetime_2 = self.sa_lifetime_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_exchange_version is not UNSET:
            field_dict["keyExchangeVersion"] = key_exchange_version
        if phase_1_proposal_1 is not UNSET:
            field_dict["phase1Proposal1"] = phase_1_proposal_1
        if phase_1_proposal_2 is not UNSET:
            field_dict["phase1Proposal2"] = phase_1_proposal_2
        if phase_1_proposal_3 is not UNSET:
            field_dict["phase1Proposal3"] = phase_1_proposal_3
        if exchange_mode is not UNSET:
            field_dict["exchangeMode"] = exchange_mode
        if negotiation_mode is not UNSET:
            field_dict["negotiationMode"] = negotiation_mode
        if local_id_type is not UNSET:
            field_dict["localIdType"] = local_id_type
        if local_name is not UNSET:
            field_dict["localName"] = local_name
        if remote_id_type is not UNSET:
            field_dict["remoteIdType"] = remote_id_type
        if remote_name is not UNSET:
            field_dict["remoteName"] = remote_name
        if sa_lifetime is not UNSET:
            field_dict["saLifetime"] = sa_lifetime
        if dpd is not UNSET:
            field_dict["dpd"] = dpd
        if dpd_interval is not UNSET:
            field_dict["dpdInterval"] = dpd_interval
        if encapsulation_mode is not UNSET:
            field_dict["encapsulationMode"] = encapsulation_mode
        if phase_2_proposal_1 is not UNSET:
            field_dict["phase2Proposal1"] = phase_2_proposal_1
        if phase_2_proposal_2 is not UNSET:
            field_dict["phase2Proposal2"] = phase_2_proposal_2
        if phase_2_proposal_3 is not UNSET:
            field_dict["phase2Proposal3"] = phase_2_proposal_3
        if pfs is not UNSET:
            field_dict["pfs"] = pfs
        if sa_lifetime_2 is not UNSET:
            field_dict["saLifetime2"] = sa_lifetime_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key_exchange_version = d.pop("keyExchangeVersion", UNSET)

        phase_1_proposal_1 = d.pop("phase1Proposal1", UNSET)

        phase_1_proposal_2 = d.pop("phase1Proposal2", UNSET)

        phase_1_proposal_3 = d.pop("phase1Proposal3", UNSET)

        exchange_mode = d.pop("exchangeMode", UNSET)

        negotiation_mode = d.pop("negotiationMode", UNSET)

        local_id_type = d.pop("localIdType", UNSET)

        local_name = d.pop("localName", UNSET)

        remote_id_type = d.pop("remoteIdType", UNSET)

        remote_name = d.pop("remoteName", UNSET)

        sa_lifetime = d.pop("saLifetime", UNSET)

        dpd = d.pop("dpd", UNSET)

        dpd_interval = d.pop("dpdInterval", UNSET)

        encapsulation_mode = d.pop("encapsulationMode", UNSET)

        phase_2_proposal_1 = d.pop("phase2Proposal1", UNSET)

        phase_2_proposal_2 = d.pop("phase2Proposal2", UNSET)

        phase_2_proposal_3 = d.pop("phase2Proposal3", UNSET)

        pfs = d.pop("pfs", UNSET)

        sa_lifetime_2 = d.pop("saLifetime2", UNSET)

        vpn_advanced_setting_open_api_vo = cls(
            key_exchange_version=key_exchange_version,
            phase_1_proposal_1=phase_1_proposal_1,
            phase_1_proposal_2=phase_1_proposal_2,
            phase_1_proposal_3=phase_1_proposal_3,
            exchange_mode=exchange_mode,
            negotiation_mode=negotiation_mode,
            local_id_type=local_id_type,
            local_name=local_name,
            remote_id_type=remote_id_type,
            remote_name=remote_name,
            sa_lifetime=sa_lifetime,
            dpd=dpd,
            dpd_interval=dpd_interval,
            encapsulation_mode=encapsulation_mode,
            phase_2_proposal_1=phase_2_proposal_1,
            phase_2_proposal_2=phase_2_proposal_2,
            phase_2_proposal_3=phase_2_proposal_3,
            pfs=pfs,
            sa_lifetime_2=sa_lifetime_2,
        )

        vpn_advanced_setting_open_api_vo.additional_properties = d
        return vpn_advanced_setting_open_api_vo

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
