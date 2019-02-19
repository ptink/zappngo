Zappngo
=======
An entire django application deployment in one command. Uses [pico_django.py](https://github.com/readevalprint/mini-django/blob/master/pico_django.py) for the tiniest Django project and [zappa](https://github.com/Miserlou/Zappa) to harness the power of serverless python on AWS Lambda

Dependencies
============
* python ^3.6
* django
* zappa

Prerequisites
=============
You will need an AWS account and your [AWS credentials file](https://aws.amazon.com/blogs/security/a-new-and-standardized-way-to-manage-credentials-in-the-aws-sdks/) must be properly installed

Install
=======
1. Clone this repo
2. `pip install django zappa`
3. Run `zappa deploy dev`

You may wish to change `aws_region` and `profile_name` in `zappa_settings.json` from their defaults of `eu-west-2` / `default`

**Note: This is not production ready! Please do not run anything critical off this without considering the security implications**
