# def sum_2(a, b):
#     return a+b
#
#
# sum_2(5, 6)

import logging
import os
import pyqrcode
import requests
import traceback
import asyncio
from asyncio.base_events import Server
from aiohttp import web
from aiohttp.web_routedef import RouteTableDef
from verity_sdk.handlers import Handlers
from verity_sdk.protocols.v0_6.IssuerSetup import IssuerSetup
from verity_sdk.protocols.v0_6.UpdateConfigs import UpdateConfigs
from verity_sdk.protocols.v0_6.UpdateEndpoint import UpdateEndpoint
from verity_sdk.protocols.v0_6.WriteCredentialDefinition import WriteCredentialDefinition
from verity_sdk.protocols.v0_6.WriteSchema import WriteSchema
from verity_sdk.protocols.v0_7.Provision import Provision
from verity_sdk.protocols.v1_0.Connecting import Connecting
from verity_sdk.protocols.v1_0.IssueCredential import IssueCredential
from verity_sdk.protocols.v1_0.PresentProof import PresentProof
from verity_sdk.protocols.v1_0.Relationship import Relationship
from verity_sdk.protocols.v1_0.CommittedAnswer import CommittedAnswer
from verity_sdk.utils.Context import Context
from indy.wallet import delete_wallet
from indy.error import WalletNotFoundError

from helper import *


INSTITUTION_NAME: str = 'NHS'
LOGO_URL: str = 'https://www.u-print.org/wp-content/uploads/2018/12/NHS-Logo.png'
CONFIG_PATH: str = 'verity-context.json'
WALLET_NAME: str = 'examplewallet1'
WALLET_KEY: str = 'examplewallet1'

context: Context
issuer_did: str = ''
issuer_verkey: str = ''

server: Server
port: int = 4000
handlers: Handlers = Handlers()
handlers.set_default_handler(default_handler)
handlers.add_handler('trust_ping', '1.0', noop)

routes: RouteTableDef = web.RouteTableDef()