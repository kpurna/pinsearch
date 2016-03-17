# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AdminUser(models.Model):
    username = models.IntegerField(primary_key=True)
    client_id = models.IntegerField()
    client_user_id = models.IntegerField()
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=240)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    last_login_time = models.IntegerField(null=True, blank=True)
    created_time = models.IntegerField(null=True, blank=True)
    status = models.IntegerField()
    parent_user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'admin_user'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    parent_admin_user_id = models.IntegerField(null=True, blank=True)
    client_name = models.CharField(max_length=600, blank=True)
    client_full_name = models.CharField(max_length=600, blank=True)
    description = models.TextField(blank=True)
    website = models.CharField(max_length=192, blank=True)
    profile_image_path = models.CharField(max_length=300, blank=True)
    created_time = models.IntegerField(null=True, blank=True)
    last_updated_time = models.IntegerField(null=True, blank=True)
    last_updated_id = models.IntegerField()
    client_address = models.CharField(max_length=768)
    client_pincode = models.IntegerField()
    client_city_id = models.IntegerField()
    client_email = models.CharField(max_length=768)
    client_mobile = models.CharField(max_length=30)
    client_contact_no = models.CharField(max_length=48)
    last_activity_date = models.IntegerField(null=True, blank=True)
    last_activity_fw_emp_id = models.IntegerField(null=True, blank=True)
    last_activity_id = models.IntegerField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'client'

class ClientUsers(models.Model):
    client_user_id = models.IntegerField(primary_key=True)
    client_id = models.IntegerField(null=True, blank=True)
    parent_admin_user_id = models.IntegerField(null=True, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    state_id = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=192, blank=True)
    personal_email = models.CharField(max_length=192, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    additional_mobile = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=240, blank=True)
    contact_person_name = models.CharField(max_length=225, blank=True)
    contact_person_designation = models.IntegerField(null=True, blank=True)
    contact_no = models.CharField(max_length=48, blank=True)
    address = models.CharField(max_length=768, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    created_time = models.IntegerField(null=True, blank=True)
    last_updated_time = models.IntegerField(null=True, blank=True)
    last_updated_id = models.IntegerField()
    last_login_time = models.IntegerField(null=True, blank=True)
    email_confirmed = models.IntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    class Meta:
        db_table = u'client_users'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(max_length=300, unique=True)
    model = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class SchoolproUsers(models.Model):
    uid = models.IntegerField(primary_key=True)
    inst_id = models.IntegerField(null=True, blank=True)
    roll_no = models.CharField(max_length=90)
    email = models.CharField(max_length=192, blank=True)
    picture = models.CharField(max_length=765)
    first_name = models.CharField(max_length=192)
    last_name = models.CharField(max_length=192)
    dob = models.DateField()
    gender = models.CharField(max_length=24)
    mobile_no = models.CharField(max_length=48)
    contact_no = models.CharField(max_length=48)
    additional_no = models.CharField(max_length=48, blank=True)
    extension = models.CharField(max_length=48)
    address = models.TextField()
    pincode = models.IntegerField()
    city_id = models.IntegerField()
    state_id = models.IntegerField()
    class_field = models.IntegerField(db_column='class') # Field renamed because it was a Python reserved word.
    division = models.IntegerField()
    created_time = models.IntegerField()
    class Meta:
        db_table = u'schoolpro_users'

class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=765)
    country_id = models.IntegerField()
    state_flag = models.IntegerField()
    display_order = models.IntegerField()
    class Meta:
        db_table = u'state'

