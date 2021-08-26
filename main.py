#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
import imports.cloudposse.elastic_beanstalk_application.aws as elbsk

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here


app = App()
MyStack(app, "test-module-python-cloudposse")

app.synth()
