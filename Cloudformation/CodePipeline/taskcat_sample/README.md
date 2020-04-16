# Taskcat Sample Project
Taskcat is a tool that lets you automate the testing of your Infrastructure as Code (Cloudformation) templates.
This is a basic project that we'll incorporate into a Codepipeline, but first lets dive into the various parts of Taskcat.

First, we'll install Taskcat and then take a look at the various configuration files required for it to test our templates.

#### Installation
Since I'm a little crazy about keeping my laptop cruft free, I like to use one of two methods:
1. Docker
  - AWS Quickstart team has made this very easy on us, they have a script that wraps the Docker run command so that it has access to our `~/.aws` directory where our credentials are typically found
  ```
  curl -s https://raw.githubusercontent.com/aws-quickstart/taskcat/master/installer/docker-installer.sh | sh
  ```

2. Python virtual environment 
  - I use `virtualenvwrapper`, so if you use a different wrapper then create a new environment according to your tool of choice and `pip install taskcat` after activating.
```
mkvirtualenv -i taskcat taskcat

```

#### Project Structure
Now that we have Taskcat installed, we need to setup the configuration files for our project with a specific structure so Taskcat can find them.
Within our projects base folder, in the below examples we'll refer to it as `taskcat-sample/`, we need a `ci/` and `templates/` folders:
```
taskcat-sample/
    ci/
        input.json
        taskcat.yml
    templates/
        sample.yml
```
- `input.json`
  - This file will contain a list of key:value pairs that will provide values for any Parameters you have in your template

- `taskcat.yml`
  - This file defines our configuration which tells taskcat what, where, and how

#### Taskcat Useful Features
One of the best features of **Taskcat** that you should get familiar with lies in the `input.json` file. This is where you handle the parameter definitions for the template(s) you are testing. Similar to launching a **Cloudformation** stack from the command line, you have to handle any input parameters at launch. **Taskcat** has a clever approach of auto-generating parameters such as UUIDs, regions, strings and numbers at launch via *Tokens*. Below is a table outlining the available *Tokens* you can use in your `input.json` file:

| **To** | **Use Token** | **Generates** | **Example** |
| ------ | ------------- | ------------- | ----------- |
| Generate AZs | `$[taskcat_genaz_<n>`] | *n* AZs | For **us-east-1** `$[taskcat_genaz_2]` generates *us-east-1a, us-east-2b |
| Create S3 Bucket Name | `$[taskcat_autobucket]` | Auto-generated bucket name | taskcat-tag-sample-taskcat-project-6ji6342 |
| Generate UUID | `$[taskcat_genuuid]` | Auto-generated identifier | 1c2e3483-2c99-45bb-801d-8af68a3b907b |
| Generate random string | `$[taskcat_random-string]` | Random sequence of 20 alphabet characters | qwerasdftyuighjkoplm |
| Generate random numbers | `$[taskcat_random-numbers]` | Random sequence of 20 numbers | 83726549387625142351 |
| Generate a password | `$[taskcat_genpass_<n><A|S>]` | Alphanumeric (A) or with Special Characters (S) of length *n* | `$[taskcat_genpass_8A]` might generate tI8zN3iX8 and `$[taskcat_genpass_8S]` might generate mA5@cB5! |
| Confirm the password | `$[taskcat_getval_<parameter_key>]` | Previously generated password for specified parameter key | If you used the parameter key Pwd for `$[taskcat_genpass_8A]` and it generated tI8zN3iX8, `$[taskcat_getval_Pwd]` will generate that same value |
