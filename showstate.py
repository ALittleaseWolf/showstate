from pynvml import nvmlInit,nvmlDeviceGetCount,\
    nvmlDeviceGetHandleByIndex,nvmlDeviceGetName,\
    nvmlDeviceGetMemoryInfo,nvmlDeviceGetUtilizationRates,nvmlShutdown
def getGpu():
    nvmlInit()     #初始化
    # print("Driver: ",nvmlSystemGetDriverVersion())  #显示驱动信息

    deviceCount = nvmlDeviceGetCount()
    for i in range(deviceCount):
        print("-------------------------")
        handle = nvmlDeviceGetHandleByIndex(i)
        print("GPU", i, ":", nvmlDeviceGetName(handle))
        info = nvmlDeviceGetMemoryInfo(handle)
        used = nvmlDeviceGetUtilizationRates(handle)
        print("GPU Memory Total: {0}M ".format((info.total)//1048576))
        print("GPU Memory Free: {0}M ".format((info.free)//1048576))
        print("GPU used: "+str(used.gpu)+"%")

    nvmlShutdown()

from psutil import virtual_memory,cpu_percent
def getCpu():
    data = virtual_memory()
    total = data.total//1048576  # 总内存
    free = data.available//1048576  # 可用内存
    print('Memory Total: {0}M'.format(total))
    print('Memory Free: {0}M'.format(free))
    CPU = "CPU:%0.2f" %cpu_percent(interval=1)
    print(CPU + '%')

if __name__ == "__main__":
    getGpu()
    getCpu()
