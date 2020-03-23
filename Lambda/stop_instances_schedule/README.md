### Lambda functions to automatically stop EC2 instances to cut costs
For example, say you have a developer account where the Dev's work from 9am-5pm.
There is no reason for instances to be running after 6pm, you can schedule Cloudwatch rule via cron
to automatically run and shutdown instances in that account for all regions.

`iam.json` will show the permissions needed for the execution role

`lambda_function.py` will show the lambda function code to get this job done

#### Cloudwatch Event Rule
Cron expression = `0 23 ? * MON-FRI *`

- Notice its set for 11:00pm, why? because these are done with UTC, so EST is UTC - 5hours
- Hence, 11:00pm UTC (subtract 5 hrs) will equal 6:00pm EST
