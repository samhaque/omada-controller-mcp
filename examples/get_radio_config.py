"""Fetch an AP's radio config. Usage: uv run python examples/get_radio_config.py <site_id> <ap_mac>"""

import sys

from omada_auth.auth import OmadaSession
from omada_client.api.ap import get_radios_config


def main() -> None:
    site_id, ap_mac = sys.argv[1], sys.argv[2]
    session = OmadaSession()
    with session.client() as client:
        response = get_radios_config.sync_detailed(
            omadac_id=session.omadac_id, site_id=site_id, ap_mac=ap_mac, client=client
        )
    print(response.status_code, response.content.decode())


if __name__ == "__main__":
    main()
