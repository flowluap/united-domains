# Here are the kind of possible record-types

### Notes

- ```id``` and ```formId``` seem to be the same
- when creating the record, leave ```id:null``` and set ```formId``` to ```AAAA0``` in case of a first *AAAA*-record

## MX
```json 
"record":{
        "prio":10,
        "mail_server":"mail.mailserver.de",
        "id":12345678,
        "filter_value":"uu.de",
        "ttl":3600,
        "type":"MX",
        "standard_value":false,
        "sub_domain":"",
        "domain":"domainname.de",
        "webspace":false,
        "udag_record_type":5,
        "formId":12345678
},
"domain_lock_state":{
        "domain_locked":false,
        "email_locked":false
}
```
## CNAME 
```json
"record":{
        "target":"mail.mailserver.de",
        "id":23456789,
        "filter_value":"autoconfig.domainname.de",
        "ttl":600,
        "type":"CNAME",
        "standard_value":false,
        "sub_domain":"autoconfig",
        "domain":"domainname.de",
        "webspace":false,
        "udag_record_type":5,
        "formId":23456789
},
"domain_lock_state":{
        "domain_locked":false,
        "domain_locked":false,
}
```
## TXT
```json
"record":{
        "text":"LONGTEXTSTRING",
        "id":34567890,
        "filter_value":"dkim._domainkey.domainname.de",
        "ttl":"600",
        "type":"TXT",
        "standard_value":false,
        "sub_domain":"dkim._domainkey",
        "domain":"domainname.de",
        "webspace":false,
        "udag_record_type":5,
        "formId":34567890
},
"domain_lock_state":{
        "domain_locked":false,
        "email_locked":false
}
```
## SRV
```json
"record":{
        "service":"_autodiscover._tcp",
        "prio":100,
        "weight":1,
        "port":"443",
        "target":"mail.mailserver.de",
        "id":12345678,
        "filter_value":"_autodiscover._tcp.domainname.de",
        "ttl":600,
        "type":"SRV",
        "standard_value":false,
        "sub_domain":"_autodiscover._tcp",
        "domain":"domainname.de",
        "webspace":false,
        "udag_record_type":5,
        "formId":12345678
},
"domain_lock_state":{
        "domain_locked":false,
        "email_locked":false
}
        
```
# A
```json
"record":{
        "address":"65.57.209.100",
        "id":12345678,
        "filter_value":"domainname.de",
        "ttl":600,
        "type":"A",
        "standard_value":false,
        "sub_domain":"",
        "domain":"domainname.de",
        "webspace":false,
        "udag_record_type":5,
        "formId":12345678
},
"domain_lock_state":{
        "domain_locked":false,
        "email_locked":false
}
```

        



        
