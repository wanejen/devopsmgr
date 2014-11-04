from django.db import models

class Machine_Lab(models.Model):
    name = models.CharField(max_length=100, blank=False)
    l_status = models.PositiveSmallIntegerField(default=0)  ## status值为0(正常)、1(异常)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

class Machine(models.Model):
    hostname = models.CharField(max_length=100, blank=False)
    telecom_ip = models.IPAddressField(blank=False)
    unicom_ip = models.IPAddressField(blank=False)
    mobile_ip = models.IPAddressField(blank=False)
    machine_lab = models.ForeignKey('Machine_Lab', related_name="machines")
    m_status = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

class Platform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=10, blank=False)
    p_status = models.PositiveSmallIntegerField(default=0)
    remarks = models.CharField(max_length=500, blank=True)      ## 备注,记录该渠道的使用,如youai代表国内混服
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

class Serverlist(models.Model):
    name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=10, blank=False)
    open_time = models.DateTimeField(blank=False)   #开服时间
    type = models.PositiveSmallIntegerField(default=0)   ##默认blank=False；服务器类型(正常、合服 ...)
    platform = models.ForeignKey("Platform", related_name="p_servers")
    domain_name = models.CharField(max_length=30, blank=False)
    login_port = models.PositiveSmallIntegerField(blank=False)
    backend_url = models.SlugField(max_length=30, blank=False)
    backend_http_port = models.PositiveSmallIntegerField(default=80)
    backend_https_port = models.PositiveSmallIntegerField(default=443)
    center_url = models.SlugField(max_length=30, blank=False)
    center_http_port = models.PositiveSmallIntegerField(default=80)
    center_https_port = models.PositiveSmallIntegerField(default=443)
    server_machine = models.ForeignKey("Machine", related_name="games")
    master_port = models.PositiveSmallIntegerField(blank=False)
    slave_machine = models.ForeignKey("Machine", related_name="slaves")
    slave_port = models.PositiveSmallIntegerField(blank=False)
    db_name = models.CharField(max_length=10, blank=False)
    server_path = models.CharField(max_length=50, blank=False)
    s_status = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

class UpdateList(models.Model):
    onlycode = models.CharField(max_length=30, blank=False)
    version = models.CharField(max_length=30, blank=False)
    update_time = models.DateTimeField(blank=False)
    update_servers = models.CommaSeparatedIntegerField(max_length=10000)
    location = models.CharField(max_length=10, blank=False)
    u_status = models.PositiveSmallIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)