from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_mdns_rule_open_api_vo import ApMdnsRuleOpenApiVO
    from ..models.osg_mdns_rule_template_open_api_vo import OsgMdnsRuleTemplateOpenApiVO


T = TypeVar("T", bound="MdnsRuleTemplateOpenApiVO")


@_attrs_define
class MdnsRuleTemplateOpenApiVO:
    """
    Attributes:
        id (str | Unset): MDNS rule ID
        name (str | Unset): MDNS rule name
        status (bool | Unset): MDNS rule enable status
        profile_ids (list[str] | Unset): ID list of selected Bonjour Service Profile
        type_ (int | Unset): MDNS rule band VLAN type. Type should be a value as follows: 0: By VLAN ID, 1: By Network
        ap (ApMdnsRuleOpenApiVO | Unset): MDNS rule by VLAN ID config, valid when parameter [type] is 0
        osg (OsgMdnsRuleTemplateOpenApiVO | Unset): MDNS rule by network config, valid when parameter [type] is 1
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    profile_ids: list[str] | Unset = UNSET
    type_: int | Unset = UNSET
    ap: ApMdnsRuleOpenApiVO | Unset = UNSET
    osg: OsgMdnsRuleTemplateOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        profile_ids: list[str] | Unset = UNSET
        if not isinstance(self.profile_ids, Unset):
            profile_ids = self.profile_ids

        type_ = self.type_

        ap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap, Unset):
            ap = self.ap.to_dict()

        osg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osg, Unset):
            osg = self.osg.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if profile_ids is not UNSET:
            field_dict["profileIds"] = profile_ids
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ap is not UNSET:
            field_dict["ap"] = ap
        if osg is not UNSET:
            field_dict["osg"] = osg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_mdns_rule_open_api_vo import (
            ApMdnsRuleOpenApiVO,
        )
        from ..models.osg_mdns_rule_template_open_api_vo import (
            OsgMdnsRuleTemplateOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        profile_ids = cast(list[str], d.pop("profileIds", UNSET))

        type_ = d.pop("type", UNSET)

        _ap = d.pop("ap", UNSET)
        ap: ApMdnsRuleOpenApiVO | Unset
        if isinstance(_ap, Unset):
            ap = UNSET
        else:
            ap = ApMdnsRuleOpenApiVO.from_dict(_ap)

        _osg = d.pop("osg", UNSET)
        osg: OsgMdnsRuleTemplateOpenApiVO | Unset
        if isinstance(_osg, Unset):
            osg = UNSET
        else:
            osg = OsgMdnsRuleTemplateOpenApiVO.from_dict(_osg)

        mdns_rule_template_open_api_vo = cls(
            id=id,
            name=name,
            status=status,
            profile_ids=profile_ids,
            type_=type_,
            ap=ap,
            osg=osg,
        )

        mdns_rule_template_open_api_vo.additional_properties = d
        return mdns_rule_template_open_api_vo

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
