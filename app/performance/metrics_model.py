from prometheus_client import Counter, Histogram, Gauge
import tracemalloc
import time
import psutil

class Metrics:
    
    couter = Counter('python_request_operations_total', 
                      'The total number of processed requests')

    histogram = Histogram('python_request_duration_seconds', 
                            'Histogram for the duration in seconds', 
                            buckets = (1, 2, 5, 6, 10, float('inf')))

    gauge = Gauge('system_usage', 'Hold current system resource usage',
                        ['resource_type'])

    
    def __init__(self):
        self.starts = []
    
    def tracing_start(self):
        tracemalloc.stop()
        print("nTracing Status : ", tracemalloc.is_tracing())
        tracemalloc.start()
        print("Tracing Status : ", tracemalloc.is_tracing())
        self.starts.append(time.time())
    
    def tracing_mem(self):
        _, first_peak = tracemalloc.get_traced_memory()
        peak = first_peak/(1024*1024)
        time_seconds = time.time()-self.starts.pop()
        return peak, time_seconds
    
    def calculate_metrics(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory()[2]
        self.gauge.labels('CPU').set(cpu)
        self.gauge.labels('Memory').set(memory)
        self.couter.inc()
        peak, time_spent = self.tracing_mem()
        self.histogram.observe(time_spent)
        
        return cpu, memory, peak, time_spent