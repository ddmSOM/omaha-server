#   Copyright (C) 2011 Crystalnix <vgachkaylo@crystalnix.com>

#   This file is part of omaha-server.

#   omaha-server is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   omaha-server is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with omaha-server.  If not, see <http://www.gnu.org/licenses/>.

import pwd, os

class Config:
    # SSL config
    useCertificateChain = True
    certificateChainFile = 'cert/server_chain.pem'
    certificateFile = 'cert/server_cert.pem'
    privateKeyFile = 'cert/privkey.pem'
    
    # Network config
    httpPort = 80
    httpsPort = 443
    domainName = 'localhost'
    secureDomain = 'https://' + domainName
    insecureDomain = 'http://' + domainName
    
    # Application config
    bitpopDirectory = 'bitpop'
    installerName = 'bitpopinstall.exe'
    bitpopUpdateInfoFile = 'bitpop.json'
    bitpopNewUpdateInfoFile = 'bitpop_new.json'
  
    userName = 'nobody'
    uid = pwd.getpwnam(userName).pw_uid if os.name == 'posix' else 0
    gid = pwd.getpwnam(userName).pw_gid if os.name == 'posix' else 0