# -*- coding: utf-8 -*-
"""
Python 3.6.8
requires: dnspython

The script is meant to test options provided by python to verify whether
an email address is valid and if it does exist. Email address is tested
against syntax, dns server (domain) existence and existence of the email
address itself. The last check is performed initialising a 'conversation'
with the mailbox; it may return false if the access to the server is denied
resulting in 'False' flag.

Author: Patryk Jesionka
Copyright: Copyright 2020, Email Verifier
License: MIT
Version: 1.0
Mmaintainer: Patryk Jesionka
Status: Maintenance
"""

import re
import dns.resolver
import socket
import smtplib


def check_email(address_to_verify):
    # Simple Regex for syntax checking
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

    # Error flags
    valid_syntax = None
    valid_domain = None
    email_exists = None  # I bumped into 'access denied', which will also cause 'False' flag

    # Syntax check
    match = re.match(regex, address_to_verify)
    if match is None:
        valid_syntax = False
    else:
        valid_syntax = True

        # Get domain for DNS lookup
        split_address = address_to_verify.split('@')
        domain = str(split_address[1])

        # MX record lookup
        try:
            records = dns.resolver.query(domain, 'MX')
        except:
            valid_domain = False
        else:
            valid_domain = True

            mx_record = records[0].exchange
            mx_record = str(mx_record)

            # Get local server hostname
            host = socket.gethostname()

            # SMTP lib setup (use debug level for full output)
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            # SMTP Conversation
            server.connect(mx_record)
            server.helo(host)
            server.mail('contact@jpatryk.com')
            code, message = server.rcpt(str(address_to_verify))
            server.quit()

            # Assume 250 as Success
            if code == 250:
                email_exists = True
            else:
                email_exists = False

    if valid_syntax and valid_domain and email_exists:
        return True
    else:
        return False
