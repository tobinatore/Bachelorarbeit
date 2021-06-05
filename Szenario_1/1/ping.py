import pyion

proxy = pyion.get_bp_proxy(1)
proxy.bp_attach()

with proxy.bp_open('ipn:1.2') as eid:
    eid.bp_send('ipn:8.1', b'1--Important')
