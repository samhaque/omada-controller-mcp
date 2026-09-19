from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO


T = TypeVar("T", bound="QuerySessionLimitRuleOpenApiVO")


@_attrs_define
class QuerySessionLimitRuleOpenApiVO:
    """
    Attributes:
        name (str): Name should contain 1 to 64 characters.
        status (bool): Status of the session limit rule.
        source_type (int): Source type should be a value as follows: 0: network; 1: IP group; 2: IP.
        max_session (int): Max sessions should be within the range of 1–999999.
        id (str | Unset): ID of the session limit rule.
        index (int | Unset): Index of the session limit rule. When the [sourceType] is 0 or 1, the index is counted in
            order, when the sourceType is 2, the index is always -1
        source_ids (list[str] | Unset): Source IDs of the session limit rule, only for network and IP group type.Network
            can be created using 'Create LAN network' interface, and network ID can be obtained from 'Get LAN network list'
            interface. IP group can be created using 'Create a new group profile' interface, and IP group ID can be obtained
            from 'Get group profile list' interface.
        ip (str | Unset): IP of the session limit rule.
        exist_ip_address (bool | Unset): Whether Source Type of Current Session Limit rule is IP Address.
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    name: str
    status: bool
    source_type: int
    max_session: int
    id: str | Unset = UNSET
    index: int | Unset = UNSET
    source_ids: list[str] | Unset = UNSET
    ip: str | Unset = UNSET
    exist_ip_address: bool | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        source_type = self.source_type

        max_session = self.max_session

        id = self.id

        index = self.index

        source_ids: list[str] | Unset = UNSET
        if not isinstance(self.source_ids, Unset):
            source_ids = self.source_ids

        ip = self.ip

        exist_ip_address = self.exist_ip_address

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "sourceType": source_type,
                "maxSession": max_session,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
        if source_ids is not UNSET:
            field_dict["sourceIds"] = source_ids
        if ip is not UNSET:
            field_dict["ip"] = ip
        if exist_ip_address is not UNSET:
            field_dict["existIpAddress"] = exist_ip_address
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        source_type = d.pop("sourceType")

        max_session = d.pop("maxSession")

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        source_ids = cast(list[str], d.pop("sourceIds", UNSET))

        ip = d.pop("ip", UNSET)

        exist_ip_address = d.pop("existIpAddress", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        query_session_limit_rule_open_api_vo = cls(
            name=name,
            status=status,
            source_type=source_type,
            max_session=max_session,
            id=id,
            index=index,
            source_ids=source_ids,
            ip=ip,
            exist_ip_address=exist_ip_address,
            feature_description=feature_description,
        )

        query_session_limit_rule_open_api_vo.additional_properties = d
        return query_session_limit_rule_open_api_vo

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
