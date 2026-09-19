from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_acl_states_entity import GatewayACLStatesEntity
    from ..models.gateway_direction_entity import GatewayDirectionEntity


T = TypeVar("T", bound="GatewayACLConfig")


@_attrs_define
class GatewayACLConfig:
    """
    Attributes:
        description (str): ACL rule description, description should contain 1 to 512 characters.
        status (bool): Status should be a value as follows: 0: disable; 1: enable
        policy (int): Policy should be a value as follows: 0: drop; 1: allow;
        protocols (list[int]): For the values of protocols, refer to section 5.5 of the Open API Access Guide.
        source_ids (list[str]): Source IDs, which depends on sourceType, for example: if sourceType is network,
            sourceIds should be LAN network ID. LAN Network can be created using 'Create LAN network' interface, and LAN
            Network ID can be obtained from 'Get LAN network list' interface.
        syslog (bool): Enable remote log
        source_type (int): SourceType should be a value as follows: 0: network; 1: IP Group; 2: IP-Port Group; 4: SSID;
            6: IPv6 Group; 7: IPv6-Port Group; 8: Country; 9: Country Group; 11: !Network; 12: !IP Group; 13: !IP-Port
            Group; 14: !IPv6 Group; 15: !IPv6-port Group
        destination_type (int): DestinationType should be a value as follows: 0: network; 1: IP Group; 2: IP-Port Group;
            6: IPv6 Group; 7: IPv6-Port Group;10: Domain Group; 11: !Network; 12: !IP Group；13: !IP-Port Group；14: !IPv6
            Group；15: !IPv6-port Group
        direction (GatewayDirectionEntity): Only for Gateway.
        state_mode (int): StateMode should be a value as follows: 0: auto; 1: manual
        destination_ids (list[str] | Unset): Source IDs, which depends on destinationType, for example: if
            destinationType is network, destinationIds should be LAN network ID. LAN Network can be created using 'Create
            LAN network' interface, and LAN Network ID can be obtained from 'Get LAN network list' interface.
        states (GatewayACLStatesEntity | Unset): Only for Gateway ACL
        time_range_id (str | Unset): Gateway ACL time range ID.
    """

    description: str
    status: bool
    policy: int
    protocols: list[int]
    source_ids: list[str]
    syslog: bool
    source_type: int
    destination_type: int
    direction: GatewayDirectionEntity
    state_mode: int
    destination_ids: list[str] | Unset = UNSET
    states: GatewayACLStatesEntity | Unset = UNSET
    time_range_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        status = self.status

        policy = self.policy

        protocols = self.protocols

        source_ids = self.source_ids

        syslog = self.syslog

        source_type = self.source_type

        destination_type = self.destination_type

        direction = self.direction.to_dict()

        state_mode = self.state_mode

        destination_ids: list[str] | Unset = UNSET
        if not isinstance(self.destination_ids, Unset):
            destination_ids = self.destination_ids

        states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.states, Unset):
            states = self.states.to_dict()

        time_range_id = self.time_range_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "status": status,
                "policy": policy,
                "protocols": protocols,
                "sourceIds": source_ids,
                "syslog": syslog,
                "sourceType": source_type,
                "destinationType": destination_type,
                "direction": direction,
                "stateMode": state_mode,
            }
        )
        if destination_ids is not UNSET:
            field_dict["destinationIds"] = destination_ids
        if states is not UNSET:
            field_dict["states"] = states
        if time_range_id is not UNSET:
            field_dict["timeRangeId"] = time_range_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.gateway_acl_states_entity import (
            GatewayACLStatesEntity,
        )
        from ..models.gateway_direction_entity import (
            GatewayDirectionEntity,
        )

        d = dict(src_dict)
        description = d.pop("description")

        status = d.pop("status")

        policy = d.pop("policy")

        protocols = cast(list[int], d.pop("protocols"))

        source_ids = cast(list[str], d.pop("sourceIds"))

        syslog = d.pop("syslog")

        source_type = d.pop("sourceType")

        destination_type = d.pop("destinationType")

        direction = GatewayDirectionEntity.from_dict(d.pop("direction"))

        state_mode = d.pop("stateMode")

        destination_ids = cast(list[str], d.pop("destinationIds", UNSET))

        _states = d.pop("states", UNSET)
        states: GatewayACLStatesEntity | Unset
        if isinstance(_states, Unset):
            states = UNSET
        else:
            states = GatewayACLStatesEntity.from_dict(_states)

        time_range_id = d.pop("timeRangeId", UNSET)

        gateway_acl_config = cls(
            description=description,
            status=status,
            policy=policy,
            protocols=protocols,
            source_ids=source_ids,
            syslog=syslog,
            source_type=source_type,
            destination_type=destination_type,
            direction=direction,
            state_mode=state_mode,
            destination_ids=destination_ids,
            states=states,
            time_range_id=time_range_id,
        )

        gateway_acl_config.additional_properties = d
        return gateway_acl_config

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
