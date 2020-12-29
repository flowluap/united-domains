# United-Domains unofficial api

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/flowluap/united-domains)

- LogIn with and without 2FA
- List Domains
- List SubDomains
- List Records
- Edit Records (Not fully working yet)

# Install

```python
pip3 install virtualenv
```
```python
virtualenv united-domains
```
```python
source myproject/venv/bin/activate
```

### Starting

Move the *example.env* to *.env* and modify email and username.

### Run via (in src folder)
```python
python3 main.py
```



# Features:

- [ ] validate Records
- [ ] translate minimal record entry to ud-record
- [ ] create a rest API
- [ ] create a Docker capable Micro-service-wrapper for fast deployment
- [ ] create DNS profiles
