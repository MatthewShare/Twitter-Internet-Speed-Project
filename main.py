from TwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10

test = InternetSpeedTwitterBot()
internet_speeds = test.get_internet_speed()
if internet_speeds[0] < PROMISED_DOWN or internet_speeds[1] < PROMISED_UP:
    test.tweet_at_provider(internet_speeds)
