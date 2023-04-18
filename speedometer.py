import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    report = session.next()
    if report['class'] == 'TPV':
        if hasattr(report, 'speed'):
            print("Текущая скорость: ", round(report.speed * 1.852, 2), "километров в час.")
