#!/usr/bin/python3
# encoding:utf-8
from django.db import models


class auth_user(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'