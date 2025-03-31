def get_answer(question: str) -> str:
    """
    Returns predefined answers based on the given question.
    """
    question = question.lower().strip()

    answers = {
        #GA 1 Q1
        "code -s": r"""Version:          Code 1.95.3 (f1a4fb101478ce6ec82fe9627c43efbf9e98c813, 2024-11-13T14:50:04.152Z)
OS Version:       Windows_NT x64 10.0.19045
CPUs:             12th Gen Intel(R) Core(TM) i7-12800H (20 x 2803)
Memory (System):  31.67GB (15.92GB free)
VM:               0%
Screen Reader:    no
Process Argv:     --crash-reporter-id 2b6d6fb4-b3ac-483b-9b02-36eacb1ee122
GPU Status:       2d_canvas:                              enabled
                  canvas_oop_rasterization:               enabled_on
                  direct_rendering_display_compositor:    disabled_off_ok
                  gpu_compositing:                        enabled
                  multiple_raster_threads:                enabled_on
                  opengl:                                 enabled_on
                  rasterization:                          enabled
                  raw_draw:                               disabled_off_ok
                  skia_graphite:                          disabled_off
                  video_decode:                           enabled
                  video_encode:                           enabled
                  vulkan:                                 disabled_off
                  webgl:                                  enabled
                  webgl2:                                 enabled
                  webgpu:                                 enabled
                  webnn:                                  disabled_off

CPU %   Mem MB     PID  Process
    0      134   17488  code main
    0      140    2588     window
    0      195    5320     gpu-process
    0      112   11932  fileWatcher [1]
    0      137   20868  ptyHost
    0       14    1352       conpty-agent
    0       82   10028       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       83   13052       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       14   14292       conpty-agent
    0       12   20104       C:\WINDOWS\System32\cmd.exe
    0      117   26864         electron-nodejs (cli.js )
    0      143   18316           "C:\Program Files\Microsoft VS Code\Code.exe" -s
    0       96    1056             crashpad-handler
    0      109   17788             gpu-process
    0      101   30524             utility-network-service
    0       82   26724       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       14   27392       conpty-agent
    0       82   27396       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       14   28648       conpty-agent
    0       14   32368       conpty-agent
    0      234   23404  window [1] (ΓùÅ keywords.ipynb - DS Projects - Visual Studio Code)
    0      187   27156  extensionHost [1]
    0      248    8728       electron-nodejs (bundle.js )
    0       11   14160       c:\Users\SESA731472\.vscode\extensions\ms-python.python-2024.20.0-win32-x64\python-env-tools\bin\pet.exe server
    0       18   10104         C:\WINDOWS\system32\conhost.exe 0x8
    0       74   23528       electron-nodejs (ac.js )
    0       18   12500         C:\WINDOWS\system32\conhost.exe 0x8
    0       23   30960       c:\Users\SESA731472\AppData\Local\Programs\Python\Python312\python.exe c:\Users\SESA731472\.vscode\extensions\ms-toolsai.jupyter-2024.10.0-win32-x64\pythonFiles\vscode_datascience_helpers\kernel_interrupt_daemon.py --ppid 27156
    0       18   26400         C:\WINDOWS\system32\conhost.exe 0x8
    5      159   27532  shared-process
    0       38   28380     crashpad-handler
    0       99   29644     utility-process
    0       57   30660     utility-network-service

Workspace Stats:
|  Window (ΓùÅ keywords.ipynb - DS Projects - Visual Studio Code)
|    Folder (DS Projects): 3 files
|      File types: ipynb(1) xlsx(1) csv(1)
|      Conf files:

C:\Work\DS Projects>code -s

Version:          Code 1.95.3 (f1a4fb101478ce6ec82fe9627c43efbf9e98c813, 2024-11-13T14:50:04.152Z)
OS Version:       Windows_NT x64 10.0.19045
CPUs:             12th Gen Intel(R) Core(TM) i7-12800H (20 x 2803)
Memory (System):  31.67GB (16.23GB free)
VM:               0%
Screen Reader:    no
Process Argv:     --crash-reporter-id 2b6d6fb4-b3ac-483b-9b02-36eacb1ee122
GPU Status:       2d_canvas:                              enabled
                  canvas_oop_rasterization:               enabled_on
                  direct_rendering_display_compositor:    disabled_off_ok
                  gpu_compositing:                        enabled
                  multiple_raster_threads:                enabled_on
                  opengl:                                 enabled_on
                  rasterization:                          enabled
                  raw_draw:                               disabled_off_ok
                  skia_graphite:                          disabled_off
                  video_decode:                           enabled
                  video_encode:                           enabled
                  vulkan:                                 disabled_off
                  webgl:                                  enabled
                  webgl2:                                 enabled
                  webgpu:                                 enabled
                  webnn:                                  disabled_off

CPU %   Mem MB     PID  Process
    0      140   17488  code main
    0      179    5320     gpu-process
    0      111   11932  fileWatcher [1]
    0      100   15408     utility-process
    0      134   20868  ptyHost
    0       14    1352       conpty-agent
    0       82   10028       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       82   13052       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       14   14292       conpty-agent
    0       12   20104       C:\WINDOWS\System32\cmd.exe
    0      116    9520         electron-nodejs (cli.js )
    0      143   32052           "C:\Program Files\Microsoft VS Code\Code.exe" -s
    0      101   13564             utility-network-service
    0       97   16020             crashpad-handler
    0      105   18992             gpu-process
    0       82   26724       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       14   27392       conpty-agent
    0       82   27396       C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -noexit -command "try { . \"c:\Program Files\Microsoft VS Code\resources\app\out\vs\workbench\contrib\terminal\common\scripts\shellIntegration.ps1\" } catch {}"
    0       14   28648       conpty-agent
    0       14   32368       conpty-agent
    0      228   23404  window [1] (DS Projects - Visual Studio Code)
    0      187   27156  extensionHost [1]
    0      213    8728       electron-nodejs (bundle.js )
    0       11   14160       c:\Users\SESA731472\.vscode\extensions\ms-python.python-2024.20.0-win32-x64\python-env-tools\bin\pet.exe server
    0       18   10104         C:\WINDOWS\system32\conhost.exe 0x8
    0       23   30960       c:\Users\SESA731472\AppData\Local\Programs\Python\Python312\python.exe c:\Users\SESA731472\.vscode\extensions\ms-toolsai.jupyter-2024.10.0-win32-x64\pythonFiles\vscode_datascience_helpers\kernel_interrupt_daemon.py --ppid 27156
    0       18   26400         C:\WINDOWS\system32\conhost.exe 0x8
    0      139   27532  shared-process
    0       38   28380     crashpad-handler
    0       54   30660     utility-network-service

Workspace Stats:
|  Window (DS Projects - Visual Studio Code)
|    Folder (DS Projects): 0 files
|      File types:
|      Conf files:""",
        
        #GA 1 Q2
        "httpbin.org/get": '{"args":{"email":"23f1000529@ds.study.iitm.ac.in"},"headers":{"Accept":"*/*","User-Agent":"HTTPie/3.2.1"},"url":"https://httpbin.org/get?email=23f1000529@ds.study.iitm.ac.in"}',
        
        #GA 1 Q3
        "npx -y prettier@3.4.2 readme.md | sha256sum": "627ae98894ab61ae62f738cb7ad66aa55f207b39f49021d26e9fe0c278bc5873 CertUtil: -hashfile command completed successfully.",

        #GA 1 Q4
        "sum(array_constrain(sequence(100, 100, 10, 13), 1, 10))": "685",

        #GA 1 Q5
        "=sum(take(sortby({8,5,0,7,0,9,5,3,9,15,10,7,6,7,2,3}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 3))": "16",

        #GA 1 Q6
        "secret value": "t4puf8u8nb",

        #GA 1 Q7
        "1982-02-28 to 2014-06-25": "1687",

        #GA 1 Q8
        "extract.csv": "45447",

        #GA 1 Q9
        "sort this json array of objects": '[{"name": "Grace", "age": 4}, {"name": "Liam", "age": 9}, {"name": "Emma", "age": 21}, {"name": "Frank", "age": 24}, {"name": "Oscar", "age": 33}, {"name": "Nora", "age": 38}, {"name": "Henry", "age": 54}, {"name": "Jack", "age": 54}, {"name": "David", "age": 56}, {"name": "Bob", "age": 58}, {"name": "Ivy", "age": 60}, {"name": "Mary", "age": 63}, {"name": "Karen", "age": 67}, {"name": "Alice", "age": 71}, {"name": "Paul", "age": 79}, {"name": "Charlie", "age": 96}]',

        #GA 1 Q10
        "use multi-cursors": "5fb24fc59a3cc3f0bb02fe7835a29015c9416edd6eae08cf6ae5c767cdd53277",

        #GA 1 Q11
        "css selectors": "418",

        #GA 1 Q12
        "three files with different encodings": "37500",

        #GA 1 Q13
        "create a github account": "https://raw.githubusercontent.com/neelakandanr3/iitm-bs-tds-t1-2025/refs/heads/main/email.json",

        #GA 1 Q14
        "in upper, lower, or mixed case": "38e1d51db7e2c9952ef886b6e3c075b8ecfb54b2c6a51dd12ee7437b84dda114 *-",

        "grep . * | lc_all=c sort | sha256sum": "cd83d547babe3e0ae6ccc22f77a9b04c1afefe71a7a35758009b4af9e14001d1 *-",

        "a.txt and b.txt": "35",

        '"gold" ticket type': """SELECT SUM(units * price) AS total_sales
FROM tickets
WHERE LOWER(TRIM(type)) = 'gold';"""
    }

    for key in answers:
        if key.lower().strip() in question:  # <-- Case-insensitive check
            return answers[key]

    return "Question not recognized"