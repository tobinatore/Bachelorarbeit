import pyion

# Create a proxy to node 2 and attach to it
proxy = pyion.get_bp_proxy(8)
proxy.bp_attach()



# Listen to 'ipn:8.1' for incoming data
with proxy.bp_open('ipn:8.1') as eid:
    while eid.is_open:
        try:
            # This is a blocking call.
            data = eid.bp_receive()
            data = data.decode('utf-8')
            source, msg = data.split('--')
            print("Message from node "+source+": " +msg)
        
        except InterruptedError:
            # User has triggered interruption with Ctrl+C
            break
