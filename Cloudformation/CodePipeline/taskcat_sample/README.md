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
