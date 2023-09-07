from subprocess import call


class Traws(object):
    import requests
    def __init__(self, path = r'C:\Users\athar\OneDrive\Documents\Atharva Purdue\First Year\Spring 22\TRAWS\Weather.py'):
        import requests
        self.path = path
    
    def call_Weather(self):
        import requests
        call(["Python3", "{}".format(self.path)])


if __name__ == '__main__':
    import requests
    c = Traws()
    c.call_Weather()
