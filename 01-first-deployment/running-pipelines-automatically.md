```bash
azureuser@agent-vm:~/aks-storage-demo$ cd ~/myagent/

azureuser@agent-vm:~/myagent$ sudo ./svc.sh install
Creating launch agent in /etc/systemd/system/vsts.agent.anuroop\x2dfirst\x2dorg.self\x2dhosted\x2dagents.agent\x2dvm.service
Run as user: azureuser
Run as uid: 1000
gid: 1000
Created symlink /etc/systemd/system/multi-user.target.wants/vsts.agent.anuroop\x2dfirst\x2dorg.self\x2dhosted\x2dagents.agent\x2dvm.service → /etc/systemd/system/vsts.agent.anuroop\x2dfirst\x2dorg.self\x2dhosted\x2dagents.agent\x2dvm.service.

azureuser@agent-vm:~/myagent$ sudo ./svc.sh start

/etc/systemd/system/vsts.agent.anuroop\x2dfirst\x2dorg.self\x2dhosted\x2dagents.agent\x2dvm.service
● vsts.agent.anuroop\x2dfirst\x2dorg.self\x2dhosted\x2dagents.agent\x2dvm.service - Azure Pipelines Agent (anuroop-first-org.self-hosted-agents.agent-vm)
     Loaded: loaded (/etc/systemd/system/vsts.agent.anuroop\x2dfirst\x2dorg.self\x2dhosted\x2dagents.agent\x2dvm.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2026-05-01 07:34:05 UTC; 6ms ago
   Main PID: 6208 (runsvc.sh)
      Tasks: 2 (limit: 50543)
     Memory: 1.0M
        CPU: 3ms
     CGroup: /system.slice/vsts.agent.anuroop\x2dfirst\x2dorg.self\x2dhosted\x2dagents.agent\x2dvm.service
             ├─6208 /bin/bash /home/azureuser/myagent/runsvc.sh
             └─6211 ./externals/node20_1/bin/node --version

May 01 07:34:05 agent-vm systemd[1]: Started Azure Pipelines Agent (anuroop-first-org.self-hosted-agents.agent-vm).
May 01 07:34:05 agent-vm runsvc.sh[6208]: .path=/home/azureuser/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/gam…s:/snap/bin
May 01 07:34:05 agent-vm runsvc.sh[6211]: v20.20.0
May 01 07:34:05 agent-vm runsvc.sh[6212]: Starting Agent listener with startup type: service
May 01 07:34:05 agent-vm runsvc.sh[6212]: Started listener process
May 01 07:34:05 agent-vm runsvc.sh[6212]: Started running service
Hint: Some lines were ellipsized, use -l to show in full.

azureuser@agent-vm:~/myagent$ ps -ef | grep Agent
root         544     456  0 03:46 ?        00:00:08 python3 -u bin/WALinuxAgent-2.15.1.3-py3.12.egg -run-exthandlers
azureus+    6212    6208  0 07:34 ?        00:00:00 ./externals/node20_1/bin/node ./bin/AgentService.js
azureus+    6219    6212 27 07:34 ?        00:00:01 /home/azureuser/myagent/bin/Agent.Listener run --startuptype service
azureus+    6234    5354  0 07:34 pts/0    00:00:00 grep --color=auto Agent
azureuser@agent-vm:~/myagent$
```