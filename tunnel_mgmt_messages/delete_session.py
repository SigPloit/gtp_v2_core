#       create_bearer.py
#       
#       Copyright 2018 LOAY
#

#       Redistribution and use in source and binary forms, with or without
#       modification, are permitted provided that the following conditions are
#       met:
#       
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above
#         copyright notice, this list of conditions and the following disclaimer
#         in the documentation and/or other materials provided with the
#         distribution.
#       * Neither the name of the  nor the names of its
#         contributors may be used to endorse or promote products derived from
#         this software without specific prior written permission.
#       
#       THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#       "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#       LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#       A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#       OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#       SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#       LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#       DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#       THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#       (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#       OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#!/usr/bin/env  python
# -*- coding: utf-8 -*-
from gtp_v2_core.commons.gtp_v2_msg_base import GTPV2MessageBase

from gtp_v2_core.commons.gtp_v2_commons import GTPmessageTypeDigit
from gtp_v2_core.commons.gtp_v2_information_element_base import *


##
## @brief  Class implementing a Delete Session Request message
##
class DeleteSessionRequest(GTPV2MessageBase):
    ##
    ## @brief      Init method
    ##
    ## @param      self  refers to the class itself
    ## @param      teid  GTP V2 Tunnel Endpoint Identifier 
    ## @param      mcc  mobile country code
    ## @param      mcc  mobile network code    
    ## @param      lac  location area code
    ## @param      rac  routing area code         
    ## @param      tac  Type allocation Code       
    ## @param      ecgi Eutran Cell Global Identifier 
    ## @param      sac  Service Area Code     
    ## @param      cgi Cell Global Identifier  
    ## @param      ebi  refers to EPSBearerID. Default 5
    ## 
    def __init__(self, teid, source_ip = "127.0.0.1", ebi=5, mcc="222", 
                 interface = 7, mnc="88", lac=2788, rac=1, tac=0, ecgi=0, sac=0, 
                 cgi=0):
        '''
        Constructor
        '''

        GTPV2MessageBase.__init__(self, t=0x01,
            msg_type=GTPmessageTypeDigit['delete-session-request'])
        self.set_teid(teid)
        self.add_ie(EPSBearerID(ebi))
        if interface == 10 or interface == 11:
            self.add_ie(UserLocationInformation(mcc=mcc, mnc=mnc, lac=lac,
                                                rac=rac, tac=tac, ecgi=ecgi,
                                                sac=sac, cgi=cgi))
            #This is not exactly correct. Here MME/SGSN IP should be set within 
            #their TEID associated to the teid of the tunnel that will be deleted
            fteid = FTeid(source_ip, interface)
            self.add_ie(fteid)


##
## @brief  Class implementing a Delete Session Response message
##
class DeleteSessionResponse(GTPV2MessageBase):
    ##
    ## @brief      Init method
    ##
    ## @param      self  refers to the class itself
    ## @param      teid Tunnel Endpoint Identifier to set
    ## @param      source_ip  source ip to set into information elements 
    ## @param      sqn  GTP header sequence number to set       
    ##
    def __init__(self, teid, sqn = 0x00):
        '''
        Constructor
        '''
        GTPV2MessageBase.__init__(self, t = 0x01, sequence = sqn,
            msg_type = GTPmessageTypeDigit['delete-session-response'])
        self.set_teid(teid)
        self.add_ie(Cause())
