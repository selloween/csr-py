#!/usr/bin/python
from OpenSSL.SSL import FILETYPE_PEM
from OpenSSL.crypto import (dump_certificate_request, dump_privatekey, PKey, TYPE_RSA, X509Req, X509Extension)
import re
import sys
import os
from config import config

def create_csr(domain, csr_file_path, key_file_path):
    private_key_path = re.sub(r".(pem|crt)$", ".key", key_file_path, flags=re.IGNORECASE)

    if not domain:
        print("Please set a domain!")
        sys.exit(1)

    if not csr_file_path:
        print("Please set the CSR file path!")
        sys.exit(1)

    if not key_file_path:
        print("Please set key file path!")    
        sys.exit(1)

 
    # Create public/private key
    key = PKey()
    key.generate_key(TYPE_RSA, 2048)
 
    # Generate CSR
    req = X509Req()
    san = ("DNS:" + domain).encode('ascii')
    req.add_extensions([
        X509Extension(b"subjectAltName", False, san)
    ])

    req.get_subject().CN = domain
    req.get_subject().O = config['subject_o']
    req.get_subject().OU = config['subject_ou']
    req.get_subject().L = config['subject_l']
    req.get_subject().ST = config['subject_st']
    req.get_subject().C = config['subject_c']
    req.get_subject().emailAddress = config['subject_email']
    req.set_pubkey(key)
    req.sign(key, 'sha256')
 
    csr_dump = dump_certificate_request(FILETYPE_PEM, req)

    # Write CSR and Key
    with open(csr_file_path, 'wb+') as f:
        f.write(csr_dump)
    with open(private_key_path, 'wb+') as f:
        f.write(dump_privatekey(FILETYPE_PEM, key))
        

def main():
    os.chdir(sys.path[0])
    print("Please input domain (subject common name):")
    domain = input() 
    csr_file_path  = config['csr_file_path'] + domain + ".csr"
    key_file_path =  config['key_file_path'] + domain + ".key"
    create_csr(domain, csr_file_path, key_file_path)

main()
