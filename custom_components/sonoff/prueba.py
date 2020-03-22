import sonoff
import config

s = sonoff.Sonoff(config.username, config.password, config.api_region)
devices = s.get_devices()
if devices:
    # We found a device, lets turn something on
    device_id = devices[0]['deviceid']
    s.switch('on', device_id, None)

# update config
config.api_region = s.get_api_region
config.user_apikey = s.get_user_apikey
config.bearer_token = s.get_bearer_token
