# United-Domains unofficial api

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/flowluap/united-domains)
![GitHub Hacktoberfest combined status (suggestion label override)](https://img.shields.io/github/hacktoberfest/2020/flowluap/united-domains?label=status&suggestion_label=status)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/flowluap/united-domains)

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
  - key | permission | ratelimit - Management
- [ ] create a Docker capable Micro-service-wrapper for fast deployment
- [ ] CLI
- [ ] create DNS profiles
- [ ] check if DNS change is available 
- [ ] buy/list domains and prices
