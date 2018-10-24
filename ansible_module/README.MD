#Ansible模块编写 


    
##模块编写经常用到的变量模型
- 必填项：name=dict(required=True)
- 默认项：default=dict(default='preset')
- 选填项：choices=dict(default='present',choices=['present','absent'])
- 布尔值：bools=dict(type='bool')
- 字符型：str=dict=(type='str')
- 任选变量型：name1=dict(aliases=['name2','name3'])

`modules目录设置ansible.cfg library = /etc/ansible/modules/`        