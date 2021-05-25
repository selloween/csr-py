# csr-py

This is a simple Python script that generates a CSR (Certificate Signing Request) together with it's Private Key.

## Config

Copy `config-sample.py` to `config.py` and adjust the values.

```python
# config.py

config = {
          'subject_o': 'Organization',
          'subject_ou': 'Organization unit',
          'subject_l': 'Locality',
          'subject_st': 'state or province',
          'subject_c': 'AT',
          'subject_email': 'foo@bar.com'   
          'csr_file_path': './',
          'key_file_path': './'
         }
```

## Run the script

```bash
# In project directory
python3 main.py
```
The script will prompt you for the `Subject Common Name` (your domain)
After input it will generate `{yourdomain}.csr` and `{yourdomain}.key` files in the local directory. You can change the path of the csr and key files in `config.py`.

```bash
# Example
Please input Domain for CSR request:
www.mysite.local

# list current directory
ls -la 
-rw-r--r-- 1 xxxxxx xxxxxx 1.2K May 25 10:23 www.mysite.local.csr
-rw-r--r-- 1 xxxxxx xxxxxx 1.7K May 25 10:23 www.mysite.local.key
```
