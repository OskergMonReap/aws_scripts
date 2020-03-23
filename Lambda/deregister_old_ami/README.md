### Deregister Old AMI's
General lambda function that will parse through our account, all regions,
and deregister any AMI's that are older than **X** days

To change the number of days, the cutoff for deregistering AMI's,
simply adjust the below line within our lambda code:
```
if age_days >= 2:
```
