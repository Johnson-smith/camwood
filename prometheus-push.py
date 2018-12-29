from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_client.exposition import basic_auth_handler

def my_auth_handler(url, method, timeout, headers, data):
    return basic_auth_handler(url, method, timeout, headers, data)
registry = CollectorRegistry()
lst=['key', 'error', 'hello']
env=['ulipay','dyb','nfoooo']
key = {'key' : 'ulipay','error':'dyb','hello':'nfoooo'}
for k ,v in key.items():
    print(k, v)
    g = Gauge('{}'.format(k), ['mylabelname']'{}'.format(v), registry=registry)
    g.set_to_current_time()
    push_to_gateway('47.101.165.17:9091', job='aly', registry=registry, handler=my_auth_handler)





