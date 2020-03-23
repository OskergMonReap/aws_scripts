### Automating EC2 Backup strategy
Now, AWS does offer EBS snapshot lifecycle management, however it is very limited (12hr or 24hr schedule)
and also has less than ideal handling of certain snapshots when it comes to pruning

To work around this, we'll create a custom snapshot Lambda function
and then a custom prune Lambda function (to clean up how we want)
