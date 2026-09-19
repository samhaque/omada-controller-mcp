from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_timeout_setting import AuthTimeoutSetting
    from ..models.external_radius_setting import ExternalRadiusSetting
    from ..models.external_server_portal_setting import ExternalServerPortalSetting
    from ..models.google_o_auth_setting_open_api_vo import GoogleOAuthSettingOpenApiVO
    from ..models.hotspot_radius_setting import HotspotRadiusSetting
    from ..models.hotspot_setting import HotspotSetting
    from ..models.imported_portal_page_open_api_vo import ImportedPortalPageOpenApiVO
    from ..models.ldap_setting import LdapSetting
    from ..models.no_auth_setting import NoAuthSetting
    from ..models.portal_customize_open_api_vo import PortalCustomizeOpenApiVO
    from ..models.simple_password_setting import SimplePasswordSetting
    from ..models.sms_setting import SmsSetting
    from ..models.social_login_setting_open_api_vo import SocialLoginSettingOpenApiVO


T = TypeVar("T", bound="PortalSetting")


@_attrs_define
class PortalSetting:
    """Portal Setting.

    Attributes:
        name (str): Portal Name, should contain 1 to 128 characters
        enable (bool): Portal Enable
        auth_type (int): Auth Type, should be a value as follows: <br/>0：No Authentication; 1：Simple Password;<br/>2:
            External RADIUS Server; 4：External Portal Server;<br/>11：Hotspot; 15: Ldap; 16: Social Login
        auth_timeout (AuthTimeoutSetting): Auth Timeout Setting.
        https_redirect_enable (bool): With this option enabled, unauthenticated clients will be redirected to the Portal
            page when they are trying to browse HTTPS websites.
        landing_page (int): LandingPage enum: 1: Redirect to the original URL, 2: Redirect to Promotional URL, 3:
            Redirect to Logout Page. <br/>With The Original URL selected, clients are directed to the URL they request for
            after they pass Portal authentication. <br/>With The Promotional URL selected, clients are directed to the
            specified URL here after they pass Portal authentication. <br/>With The Logout Page selected, clients are
            directed to the Portal Logout Page after they pass Portal authentication.
        ssid_list (list[str] | Unset): SSID ID list bound with this Portal. SSID can be created using 'Create new SSID'
            ('Create new SSID template') interface, and SSID ID can be obtained from 'Get SSID list' ('Get SSID template
            list') interface
        network_list (list[str] | Unset): Lan network ID list bound with this Portal. LAN Network can be created using
            'Create LAN network' ('Create LAN network template') interface, and LAN Network ID can be obtained from 'Get LAN
            network list' ('Get LAN network template list') interface
        landing_url_scheme (str | Unset): If Parameter [landingPage] is 2(Redirect to Promotional URL),this Parameter is
            requested, content is http or https.
        landing_url (str | Unset): If Parameter [landingPage] is 2(Redirect to Promotional URL),this Parameter is
            requested.
        no_auth (NoAuthSetting | Unset): No Auth Portal Setting.
        simple_password (SimplePasswordSetting | Unset): Simple Password Portal Setting.
        hotspot (HotspotSetting | Unset): Hotspot types setting.
        social_login (SocialLoginSettingOpenApiVO | Unset): Social login setting, required when Parameter[authType] is
            16. Should be a value as follows:<br/>17: Google
        google (GoogleOAuthSettingOpenApiVO | Unset): Google OAuth setting, required when [authType] is 16 and social
            auth [enabledTypes] contains 17.
        sms (SmsSetting | Unset): Sms Portal Setting.
        portal_form_id (str | Unset): Portal form ID, required when [authType] is 11 and hotspot [enabledTypes] contains
            12.
        hotspot_radius (HotspotRadiusSetting | Unset): Hotspot RADIUS Portal Setting.
        external_portal (ExternalServerPortalSetting | Unset): External Server Portal Setting.
        external_radius (ExternalRadiusSetting | Unset): External RADIUS Portal Setting.
        ldap (LdapSetting | Unset): Ldap Portal Setting.
        page_type (int | Unset): Page type, should be a value as follows: 1: Use default page, 2: use uploaded page.
            When [pageType] is null, it defaults to 1
        imported_portal_page (ImportedPortalPageOpenApiVO | Unset): Imported portal page, required when parameter
            [pageType] is 2
        portal_customize (PortalCustomizeOpenApiVO | Unset): Portal Customize, required when parameter [pageType] is 1
            or null
    """

    name: str
    enable: bool
    auth_type: int
    auth_timeout: AuthTimeoutSetting
    https_redirect_enable: bool
    landing_page: int
    ssid_list: list[str] | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    landing_url_scheme: str | Unset = UNSET
    landing_url: str | Unset = UNSET
    no_auth: NoAuthSetting | Unset = UNSET
    simple_password: SimplePasswordSetting | Unset = UNSET
    hotspot: HotspotSetting | Unset = UNSET
    social_login: SocialLoginSettingOpenApiVO | Unset = UNSET
    google: GoogleOAuthSettingOpenApiVO | Unset = UNSET
    sms: SmsSetting | Unset = UNSET
    portal_form_id: str | Unset = UNSET
    hotspot_radius: HotspotRadiusSetting | Unset = UNSET
    external_portal: ExternalServerPortalSetting | Unset = UNSET
    external_radius: ExternalRadiusSetting | Unset = UNSET
    ldap: LdapSetting | Unset = UNSET
    page_type: int | Unset = UNSET
    imported_portal_page: ImportedPortalPageOpenApiVO | Unset = UNSET
    portal_customize: PortalCustomizeOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enable = self.enable

        auth_type = self.auth_type

        auth_timeout = self.auth_timeout.to_dict()

        https_redirect_enable = self.https_redirect_enable

        landing_page = self.landing_page

        ssid_list: list[str] | Unset = UNSET
        if not isinstance(self.ssid_list, Unset):
            ssid_list = self.ssid_list

        network_list: list[str] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        landing_url_scheme = self.landing_url_scheme

        landing_url = self.landing_url

        no_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_auth, Unset):
            no_auth = self.no_auth.to_dict()

        simple_password: dict[str, Any] | Unset = UNSET
        if not isinstance(self.simple_password, Unset):
            simple_password = self.simple_password.to_dict()

        hotspot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hotspot, Unset):
            hotspot = self.hotspot.to_dict()

        social_login: dict[str, Any] | Unset = UNSET
        if not isinstance(self.social_login, Unset):
            social_login = self.social_login.to_dict()

        google: dict[str, Any] | Unset = UNSET
        if not isinstance(self.google, Unset):
            google = self.google.to_dict()

        sms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sms, Unset):
            sms = self.sms.to_dict()

        portal_form_id = self.portal_form_id

        hotspot_radius: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hotspot_radius, Unset):
            hotspot_radius = self.hotspot_radius.to_dict()

        external_portal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_portal, Unset):
            external_portal = self.external_portal.to_dict()

        external_radius: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_radius, Unset):
            external_radius = self.external_radius.to_dict()

        ldap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap, Unset):
            ldap = self.ldap.to_dict()

        page_type = self.page_type

        imported_portal_page: dict[str, Any] | Unset = UNSET
        if not isinstance(self.imported_portal_page, Unset):
            imported_portal_page = self.imported_portal_page.to_dict()

        portal_customize: dict[str, Any] | Unset = UNSET
        if not isinstance(self.portal_customize, Unset):
            portal_customize = self.portal_customize.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "enable": enable,
                "authType": auth_type,
                "authTimeout": auth_timeout,
                "httpsRedirectEnable": https_redirect_enable,
                "landingPage": landing_page,
            }
        )
        if ssid_list is not UNSET:
            field_dict["ssidList"] = ssid_list
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if landing_url_scheme is not UNSET:
            field_dict["landingUrlScheme"] = landing_url_scheme
        if landing_url is not UNSET:
            field_dict["landingUrl"] = landing_url
        if no_auth is not UNSET:
            field_dict["noAuth"] = no_auth
        if simple_password is not UNSET:
            field_dict["simplePassword"] = simple_password
        if hotspot is not UNSET:
            field_dict["hotspot"] = hotspot
        if social_login is not UNSET:
            field_dict["socialLogin"] = social_login
        if google is not UNSET:
            field_dict["google"] = google
        if sms is not UNSET:
            field_dict["sms"] = sms
        if portal_form_id is not UNSET:
            field_dict["portalFormId"] = portal_form_id
        if hotspot_radius is not UNSET:
            field_dict["hotspotRadius"] = hotspot_radius
        if external_portal is not UNSET:
            field_dict["externalPortal"] = external_portal
        if external_radius is not UNSET:
            field_dict["externalRadius"] = external_radius
        if ldap is not UNSET:
            field_dict["ldap"] = ldap
        if page_type is not UNSET:
            field_dict["pageType"] = page_type
        if imported_portal_page is not UNSET:
            field_dict["importedPortalPage"] = imported_portal_page
        if portal_customize is not UNSET:
            field_dict["portalCustomize"] = portal_customize

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_timeout_setting import AuthTimeoutSetting
        from ..models.external_radius_setting import (
            ExternalRadiusSetting,
        )
        from ..models.external_server_portal_setting import (
            ExternalServerPortalSetting,
        )
        from ..models.google_o_auth_setting_open_api_vo import (
            GoogleOAuthSettingOpenApiVO,
        )
        from ..models.hotspot_radius_setting import (
            HotspotRadiusSetting,
        )
        from ..models.hotspot_setting import HotspotSetting
        from ..models.imported_portal_page_open_api_vo import (
            ImportedPortalPageOpenApiVO,
        )
        from ..models.ldap_setting import LdapSetting
        from ..models.no_auth_setting import NoAuthSetting
        from ..models.portal_customize_open_api_vo import (
            PortalCustomizeOpenApiVO,
        )
        from ..models.simple_password_setting import (
            SimplePasswordSetting,
        )
        from ..models.sms_setting import SmsSetting
        from ..models.social_login_setting_open_api_vo import (
            SocialLoginSettingOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        enable = d.pop("enable")

        auth_type = d.pop("authType")

        auth_timeout = AuthTimeoutSetting.from_dict(d.pop("authTimeout"))

        https_redirect_enable = d.pop("httpsRedirectEnable")

        landing_page = d.pop("landingPage")

        ssid_list = cast(list[str], d.pop("ssidList", UNSET))

        network_list = cast(list[str], d.pop("networkList", UNSET))

        landing_url_scheme = d.pop("landingUrlScheme", UNSET)

        landing_url = d.pop("landingUrl", UNSET)

        _no_auth = d.pop("noAuth", UNSET)
        no_auth: NoAuthSetting | Unset
        if isinstance(_no_auth, Unset):
            no_auth = UNSET
        else:
            no_auth = NoAuthSetting.from_dict(_no_auth)

        _simple_password = d.pop("simplePassword", UNSET)
        simple_password: SimplePasswordSetting | Unset
        if isinstance(_simple_password, Unset):
            simple_password = UNSET
        else:
            simple_password = SimplePasswordSetting.from_dict(_simple_password)

        _hotspot = d.pop("hotspot", UNSET)
        hotspot: HotspotSetting | Unset
        if isinstance(_hotspot, Unset):
            hotspot = UNSET
        else:
            hotspot = HotspotSetting.from_dict(_hotspot)

        _social_login = d.pop("socialLogin", UNSET)
        social_login: SocialLoginSettingOpenApiVO | Unset
        if isinstance(_social_login, Unset):
            social_login = UNSET
        else:
            social_login = SocialLoginSettingOpenApiVO.from_dict(_social_login)

        _google = d.pop("google", UNSET)
        google: GoogleOAuthSettingOpenApiVO | Unset
        if isinstance(_google, Unset):
            google = UNSET
        else:
            google = GoogleOAuthSettingOpenApiVO.from_dict(_google)

        _sms = d.pop("sms", UNSET)
        sms: SmsSetting | Unset
        if isinstance(_sms, Unset):
            sms = UNSET
        else:
            sms = SmsSetting.from_dict(_sms)

        portal_form_id = d.pop("portalFormId", UNSET)

        _hotspot_radius = d.pop("hotspotRadius", UNSET)
        hotspot_radius: HotspotRadiusSetting | Unset
        if isinstance(_hotspot_radius, Unset):
            hotspot_radius = UNSET
        else:
            hotspot_radius = HotspotRadiusSetting.from_dict(_hotspot_radius)

        _external_portal = d.pop("externalPortal", UNSET)
        external_portal: ExternalServerPortalSetting | Unset
        if isinstance(_external_portal, Unset):
            external_portal = UNSET
        else:
            external_portal = ExternalServerPortalSetting.from_dict(_external_portal)

        _external_radius = d.pop("externalRadius", UNSET)
        external_radius: ExternalRadiusSetting | Unset
        if isinstance(_external_radius, Unset):
            external_radius = UNSET
        else:
            external_radius = ExternalRadiusSetting.from_dict(_external_radius)

        _ldap = d.pop("ldap", UNSET)
        ldap: LdapSetting | Unset
        if isinstance(_ldap, Unset):
            ldap = UNSET
        else:
            ldap = LdapSetting.from_dict(_ldap)

        page_type = d.pop("pageType", UNSET)

        _imported_portal_page = d.pop("importedPortalPage", UNSET)
        imported_portal_page: ImportedPortalPageOpenApiVO | Unset
        if isinstance(_imported_portal_page, Unset):
            imported_portal_page = UNSET
        else:
            imported_portal_page = ImportedPortalPageOpenApiVO.from_dict(
                _imported_portal_page
            )

        _portal_customize = d.pop("portalCustomize", UNSET)
        portal_customize: PortalCustomizeOpenApiVO | Unset
        if isinstance(_portal_customize, Unset):
            portal_customize = UNSET
        else:
            portal_customize = PortalCustomizeOpenApiVO.from_dict(_portal_customize)

        portal_setting = cls(
            name=name,
            enable=enable,
            auth_type=auth_type,
            auth_timeout=auth_timeout,
            https_redirect_enable=https_redirect_enable,
            landing_page=landing_page,
            ssid_list=ssid_list,
            network_list=network_list,
            landing_url_scheme=landing_url_scheme,
            landing_url=landing_url,
            no_auth=no_auth,
            simple_password=simple_password,
            hotspot=hotspot,
            social_login=social_login,
            google=google,
            sms=sms,
            portal_form_id=portal_form_id,
            hotspot_radius=hotspot_radius,
            external_portal=external_portal,
            external_radius=external_radius,
            ldap=ldap,
            page_type=page_type,
            imported_portal_page=imported_portal_page,
            portal_customize=portal_customize,
        )

        portal_setting.additional_properties = d
        return portal_setting

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
